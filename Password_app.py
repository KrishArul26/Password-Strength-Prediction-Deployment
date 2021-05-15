import pandas as pd
import pickle
from sklearn.svm import SVC
from pandas import Series
import flask
from flask import Flask, render_template, url_for, request
from flask_ngrok import run_with_ngrok

model = pickle.load(open("SVM_classifier.pkl", "rb"))
app = flask.Flask(__name__)
run_with_ngrok(app)


@app.route('/')
def home():
    return render_template('home.html')


def preprocessing(text):
    # Find the length of character presented in password
    char_count = len(text)
    text: Series = pd.Series(text)
    # Find the length of number presented in password
    numerics = text.apply(lambda x: len(
        [str(x) for x in list(x) if str(x).isdigit()]))
    # Find the length of Alphabets presented in password
    alpha = text.apply(lambda x: len([x for x in list(x) if x.isalpha()]))
    # Find the length of punctuation presented in password
    specialSymbols = '!?%&.:~/\|,;<>-_+@#$%^&*(){}[]'
    punc = text.apply(lambda x: len(
        [x for x in list(x) if x in specialSymbols]))
    # Find the length of vowels presented in password
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels = text.apply(lambda x: len([x for x in list(x) if x in vowels]))
    # Find the length of consonants presented in password
    consonants = text.apply(lambda x: len(
        [x for x in list(x) if x not in vowels and x.isalpha()]))
    return char_count, numerics[0], alpha[0], punc[0], vowels[0], consonants[0]


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['password']
        length = preprocessing(text)
        data = pd.DataFrame(
            {'char_count': [length[0]], 'numerics': [length[1]], 'alpha': [length[2]], 'punc': [length[3]],
             'vowels': [length[4]], 'consonants': [length[5]]})
    my_prediction = model.predict(data)

    return render_template('result.html', prediction=my_prediction)


if __name__ == '__main__':
    app.run()
