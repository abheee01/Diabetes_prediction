from flask import Flask, render_template, request
import pickle
import numpy as np
filename="diabetes.pkl"
classifier=pickle.load(open(filename,'rb'))
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('inde.html')
@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        glucose=request.form('glucose')
        bp=request.form('bloodpressure')
        insulin=request.form('insulin')
        bmi=request.form('bmi')
        dpf=request.form('diabestespedigreefunction')
        age=request.form('age')
        data=np.array([[glucose,bp,insulin,bmi,dpf,age]])
        for i in range(data.shape[0]):
            if np.dot(data.to_numpy()[i], classifier)<1.5:
                predicted = 0
            else:
                predicted = 1
        return render_template('result.html',prediction=predicted)

if __name__=="__main__":
    app.run(debug=True)