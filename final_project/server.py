from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def renderIndexPage():
    """
    Function that renders index page
    """
    return render_template("index.html")

@app.route("/englishToFrench")
def englishToFrench():
    """
    function to translate English to French
    """
    textToTranslate = request.args.get('textToTranslate')
    return translator.english_to_french(textToTranslate)
    
@app.route("/frenchToEnglish")
def frenchToEnglish():
    """
    Function to translate French to Enlish
    """
    textToTranslate = request.args.get('textToTranslate')
    return translator.french_to_english(textToTranslate)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    
