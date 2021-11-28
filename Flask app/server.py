import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

model = pickle.load(open('detector_model.pkl', 'rb'))

vectorizer = pickle.load(open('vectorizer1.pkl','rb'))
tfvect = TfidfVectorizer(stop_words='english', max_df=0.7)

@app.route('/')
def form():
    return render_template('form1.html')

@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
    	if request.form['action'] == 'Check':
    		form_data = request.form
    		prediction = model.predict([form_data['name']])
    		print(form_data['name'])
    		return render_template('form1.html', form_data = form_data, prediction=prediction)
    	elif request.form['action'] == 'Fake':
	        form_data = request.form
	        # prediction=True
	        # vectorized_input_data = vectorizer.transform(form_data['name'])
	        prediction = model.predict([form_data['name']])
	        prediction = ['fake']
	        print(form_data['name'])
	        return render_template('form1.html', form_data = form_data, prediction=prediction)
        
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000,debug=True)