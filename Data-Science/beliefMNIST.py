import pandas as pd
import numpy as np
import torch
from torchvision import datasets, transforms
import os

from DBN import DBN

def Net():
    net = torch.nn.Sequential(
            torch.nn.Linear(784, 512),
            torch.nn.Sigmoid(),
            torch.nn.Linear(512, 128),
            torch.nn.Sigmoid(),
            torch.nn.Linear(128, 64),
            torch.nn.Sigmoid(),
            torch.nn.Linear(64, 10),
            torch.nn.Softmax(dim=1),
            )

    return net

def train(net, epochs=5, batch_size=64):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'  
    device = torch.device(device)

    net = net.to(device)

    train_dataset = datasets.MNIST('dataset', download=True, train=True, transform=transforms.ToTensor())
    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

    test_dataset = datasets.MNIST('dataset', download=True, train=False, transform=transforms.ToTensor())
    test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=batch_size)

    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(net.parameters(), lr=0.001)
    progress = []

    for epoch in range(epochs):
        train_loss = 0
        train_acc = 0
        net.train()
        for train_x, train_y in train_loader:
            train_x = train_x.to(device)
            train_y = train_y.to(device)

            train_x = train_x.view(-1, 784)
            output = net(train_x)
            loss = criterion(output, train_y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            train_loss += loss.item()
            output = torch.argmax(output, dim=1)
            train_acc += torch.sum(output == train_y).item() / batch_size

        train_loss /= len(train_loader)
        train_acc /= len(train_loader)
        print('epoch %d train loss %5.3f train acc %5.3f' % (epoch+1, train_loss, train_acc))

        test_loss = 0
        test_acc = 0
        net.eval()
        for test_x, test_y in test_loader:
            test_x = test_x.to(device)
            test_y = test_y.to(device)
            test_x = test_x.view(-1, 784)

            with torch.no_grad():
                output_test = net(test_x)

            loss = criterion(output_test, test_y)
            test_loss += loss.item()
            output_test = torch.argmax(output_test, axis=1) 
            test_acc += torch.sum(output_test == test_y).item() / batch_size

        test_loss /= len(test_loader)
        test_acc /= len(test_loader)

        progress.append([epoch+1, test_loss, train_loss, test_acc, train_acc])

    return progress

if __name__ == '__main__':
    os.makedirs('./results', exist_ok=True)

    train_dataset = datasets.MNIST('./dataset', download=True, train=True, transform=transforms.ToTensor())
    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=len(train_dataset), shuffle=False)
    for train_x, train_y in train_loader:
        train_x = train_x.view(-1, 784)

    layers = [512, 128, 64, 10]

    print("fuck")
    dbn = DBN(train_x.shape[1], layers, savefile='./mnist_trained_dbn.pt')

    print('Unsupervised pre-training of DBN')
    dbn.train(train_x, epochs=100, batch_size=128)

    print('Without Pre-Training')
    net = Net()

    progress = train(net)
    progress = pd.DataFrame(np.array(progress))
    progress.columns = ['epochs', 'test loss', 'train loss', 'test acc', 'train acc']
    progress.to_csv('./results/DBN_without_pretraining_classifier.csv', index=False)

    print('With Pre-Training')
    dbn_net = torch.nn.Sequential(dbn.net(), torch.nn.Softmax(dim=1))
    progress = train(dbn_net)
    progress = pd.DataFrame(np.array(progress))
    progress.columns = ['epochs', 'test loss', 'train loss', 'test acc', 'train acc']
    progress.to_csv('./results/DBN_with_pretraining_classifier.csv', index=False)