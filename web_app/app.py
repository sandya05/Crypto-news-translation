# app.py
from flask import Flask, render_template, request
from googletrans import Translator



app = Flask(__name__)
app.secret_key = 'Translator'

@app.route("/translate_lang", methods=["post"])
def translate_lang():
    if request.method == "POST":
        sentence = str(request.form["sentence"])
        code = str(request.form["code"])

        print(sentence)
        translator = Translator()

        translated_sentence = translator.translate(sentence, src="en",dest=code)
        translated=translated_sentence.text

    return render_template("index2.html", language_selected=code, sentence = sentence, translated_res=translated)


@app.route("/")
def index():
    lang = [{"name":"Telugu","code":"te"}, {"name":"Tamil","code":"ta"}, {"name":"Marathi","code":"mr"}, {"name":"Kannada","code":"kn"}, {"name":"Malayalam","code":"ml"}, {"name":"Gujarati","code":"gu"}, {"name":"Hindi","code":"hi"},{"name":"English","code":"en"}, {"name":"Bengali","code":"bn"}, {"name":"Arabic","code":"ar"}, {"name":"Odia","code":"or"}, {"name":"Urdu","code":"ur"}]

    return render_template("index2.html", languages=lang)

   



if __name__ == '__main__':
	app.run(debug=True)