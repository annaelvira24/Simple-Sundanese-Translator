from flask import Flask, redirect, url_for, render_template, request
import webFunctions
app = Flask(__name__)

'''
File ini berisi fungsi untuk back-end dari website
'''

@app.route("/", methods=["POST", "GET", "SWAP"])
def home():
    if request.method == "POST":
        
        inputSentence = request.form["inputText"]
        method = request.form["algorithm"]
        language = request.form["language"]
        translation = webFunctions.translate(inputSentence, method, language)

        return render_template("homePage.html", inputText = inputSentence, translatedText = translation )
    else:
        return render_template("homePage.html", inputText = '', translatedText = '')

if __name__ == "__main__":
    app.static_folder = 'static'
    app.run(debug=True)

