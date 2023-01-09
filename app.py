import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from sklearn import preprocessing
import pickle

app = Flask(__name__)
model = pickle.load(open('stacked_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    feature_list = request.form.to_dict()
    feature_list = list(feature_list.values())
    feature_list = list(map(int, feature_list))
    final_features = np.array(feature_list).reshape(1, 45) 
    
    prediction = model.predict(final_features)
    output = int(prediction[0])
    if output == 1:
        text = "Bad loan"
    else:
        text = "Good loan"

    return render_template('index.html', prediction_text='Loan outcome is {}'.format(text))


if __name__ == "__main__":
    app.run(debug=True)
