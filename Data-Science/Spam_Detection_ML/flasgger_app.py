from flask import Flask, request
import pickle
import string
from nltk.corpus import stopwords
from flasgger import Swagger


app = Flask(__name__)
Swagger(app)


def process_text(text):
  #1-remove puncuation
  #2-remove stopwords
  
  nopunc = [word for word in text if word not in string.punctuation]

  nopunc = ''.join(nopunc)

  clean_word = [word for word in nopunc.split() if word .lower() not in stopwords.words('english')]

  return clean_word

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def welcome():
    return "Welcome"


@app.route('/predict', methods=["GET"])
def prediction():

    """Check whether E-Mail is spam or not.
    This is using docstrings.
    ---
    parameters:
      - name: Mail
        in: query
        type: string
        required: true
    responses:
        200:
            description: The output value
    """

    mail = request.args.get('Mail')
    pred = model.predict([mail])

    if pred[0] == 0:
        return "This Mail is not Spam."
    else:
        return "This Mail is Spam."


if __name__ == '__main__':
    app.run(debug=True)
