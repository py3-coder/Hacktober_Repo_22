import numpy as np
import torch
import random
from RBM import RBM

class DBN:
    def __init__(self, input_size, layers, mode='bernoulli', k=5, savefile=None):
        self.layers = layers
        self.input_size = input_size
        self.layer_parameters = [{'W':None, 'hb':None, 'vb':None} for _ in range(len(layers))]
        self.k = k
        self.mode = mode
        self.savefile = savefile

    def sample_v(self, y, W, vb):
        wy = torch.mm(y, W)
        activation = wy + vb
        p_v_given_h = torch.sigmoid(activation)
        if self.mode == 'bernoulli':
            return p_v_given_h, torch.bernoulli(p_v_given_h)
        else:
            return p_v_given_h, torch.add(p_v_given_h, torch.normal(mean=0, std=1, size=p_v_given_h.shape))

    def sample_h(self, x, W, hb):
        wx = torch.mm(x, W.t())
        activation = wx + hb
        p_h_given_v = torch.sigmoid(activation)
        if self.mode == 'bernoulli':
            return p_h_given_v, torch.bernoulli(p_h_given_v)
        else:
            return p_h_given_v, torch.add(p_h_given_v, torch.normal(mean=0, std=1, size=p_h_given_v.shape))

    def generate_input_for_layer(self, index, x):
        if index>0:
            x_gen = []
            for _ in range(self.k):
                x_dash = x.clone()
                for i in range(index):
                    _, x_dash = self.sample_h(x_dash, self.layer_parameters[i]['W'], self.layer_parameters[i]['hb'])
                x_gen.append(x_dash)

            x_dash = torch.stack(x_gen)
            x_dash = torch.mean(x_dash, dim=0)
        else:
            x_dash = x.clone()

        return x_dash

    def train(self, x, epochs, batch_size):
        for index, layer in enumerate(self.layers):
            if index == 0:
                vn = self.input_size
            else:
                vn = self.layers[index-1]
            hn = self.layers[index]

            rbm = RBM(vn, hn, mode='bernoulli', lr=0.0005, k=10, optimizer='adam')
            x_dash = self.generate_input_for_layer(index, x)
            rbm.train(x_dash, epochs=epochs, batch_size=batch_size, early_stopping_patience=10)
            self.layer_parameters[index]['W'] = rbm.W.cpu()
            self.layer_parameters[index]['hb'] = rbm.hb.cpu()
            self.layer_parameters[index]['vb'] = rbm.vb.cpu()
            print('Finished Training Layer:', index, 'to', index+1)

        if self.savefile is not None:
            torch.save(self.layer_parameters, self.savefile)

    def reconstructor(self, x):
        '''
        dbn.train(dataset)
        y = dbn.reconstructor(dataset)
        print('MAE of an all 0 reconstructor:', torch.mean(dataset).item())
        print('MAE between reconstructed and original sample:', torch.mean(torch.abs(y - dataset)).item())
        '''
        x_gen = []
        for _ in range(self.k):
            x_dash = x.clone()
            for i in range(len(self.layer_parameters)):
                _, x_dash = self.sample_h(x_dash, self.layer_parameters[i]['W'], self.layer_parameters[i]['hb'])
            x_gen.append(x_dash)
        x_dash = torch.stack(x_gen)
        x_dash = torch.mean(x_dash, dim=0)

        y = x_dash

        y_gen = []
        for _ in range(self.k):
            y_dash = y.clone()
            for i in range(len(self.layer_parameters)):
                i = len(self.layer_parameters)-1-i
                _, y_dash = self.sample_v(y_dash, self.layer_parameters[i]['W'], self.layer_parameters[i]['vb'])
            y_gen.append(y_dash)
        y_dash = torch.stack(y_gen)
        y_dash = torch.mean(y_dash, dim=0)

        return y_dash, x_dash

    def net(self):
        print('The Last layer will not be activated. The rest are activated using the Sigoid Function')
        modules = []
        for index, layer in enumerate(self.layer_parameters):
            modules.append(torch.nn.Linear(layer['W'].shape[1], layer['W'].shape[0]))
            if index < len(self.layer_parameters) - 1:
                modules.append(torch.nn.Sigmoid())
        model = torch.nn.Sequential(*modules)

        for layer_no, layer in enumerate(model):
            if layer_no // 2 == len(self.layer_parameters)-1:
                break
            if layer_no % 2 == 0:
                model[layer_no].weight = torch.nn.Parameter(self.layer_parameters[layer_no // 2]['W'])
                model[layer_no].bias = torch.nn.Parameter(self.layer_parameters[layer_no // 2]['hb'])

        return model