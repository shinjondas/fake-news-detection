# from flask import Flask,render_template,request


# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.linear_model import PassiveAggressiveClassifier
# import pickle
# import pandas as pd
# from sklearn.model_selection import train_test_split

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__,template_folder='.')


model = pickle.load(open('detector_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer1.pkl','rb'))

# tfvect = TfidfVectorizer(stop_words='english', max_df=0.7)
# loaded_model = pickle.load(open('detector_model.pkl', 'rb'))
# dataframe = pd.read_csv('train.csv')
# x = dataframe['text']
# y = dataframe['label']
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# def fake_news_det(news):
#     tfid_x_train = tfvect.fit_transform(x_train)
#     tfid_x_test = tfvect.transform(x_test)
#     input_data = [news]
#     vectorized_input_data = tfvect.transform(input_data)
#     prediction = loaded_model.predict(vectorized_input_data)
#     return prediction





@app.route('/')
def form():
    return render_template('form.html')

@app.route('/data/', methods = ['POST'])
# def data():
#     if request.method == 'GET':
#         return f"The URL /data is accessed directly. Try going to '/form' to submit form"
#     if request.method == 'POST':
#         form_data = request.form
#         return render_template('data.html',form_data = form_data)





def predict():
    if request.method == 'POST':
        message = request.form['name']
        pred = fake_news_det(message)
        print(pred)
        return render_template('data.html', prediction=pred)
    else:
        return render_template('data.html', prediction="Something went wrong")


    message = request.form['name']
    # final_features = [np.array(int_features)]
    prediction = model.predict(message)

    output = round(prediction[0], 2)
        prediction=True
        return render_template('data.html', prediction=prediction)





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000,debug=True)