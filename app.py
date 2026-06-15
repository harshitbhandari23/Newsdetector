
import nltk
import joblib
import spacy
nlp=spacy.load('en_core_web_lg')
import re
from flask import Flask,render_template,request,url_for,redirect
model=joblib.load('news.pkl')
from nltk.corpus import stopwords
nltk.download('stopwords')
stop=set(stopwords.words('english'))
app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def home():
    if request.method=='POST':
        text=request.form['news']
        words=re.findall(r'\w+',text)
        words=' '.join(i.lower() for i in words if i not in stop)
        vect = nlp(words).vector.reshape(1, -1)

        pred=model.predict(vect)
        ans=""
        if(pred[0]==0):
            ans="TrueNews"
        else:
            ans="Fake news"
        return redirect(url_for("display",predict=ans))
         
    return render_template("home.html")
@app.route("/about")
def about():
    return render_template("about.html")
@ app.route("/result/<predict>")
def display(predict):
    return render_template("result.html",predict=predict)
if __name__=="__main__":
    app.run()