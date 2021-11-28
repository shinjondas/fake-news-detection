import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__,template_folder='.')

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/data/', methods = ['POST'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        prediction=True
        return render_template('data.html',form_data = form_data,prediction=prediction)





# def predict():
#     # if request.method == 'POST':
#     #     message = request.form['name']
#     #     pred = fake_news_det(message)
#     #     print(pred)
#     #     return render_template('data.html', prediction=pred)
#     # else:
#     #     return render_template('data.html', prediction="Something went wrong")


#     # message = request.form['name']
#     # # final_features = [np.array(int_features)]
#     # prediction = model.predict(message)

#     # output = round(prediction[0], 2)
#     prediction=True
#     return render_template('data.html', prediction=prediction)





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000,debug=True)