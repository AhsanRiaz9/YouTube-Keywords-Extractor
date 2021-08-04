from flask import Flask, render_template, jsonify,request, make_response
from Scrapping import getKeywords
from flask_ngrok import run_with_ngrok
app = Flask(__name__)
run_with_ngrok(app)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/getYoutubeVideoTags',methods=['POST'])
def getYoutubeTags():
    obj = eval(request.get_data())
    tagsList = getKeywords(obj['url'])
    print(tagsList)
    obj = {'tagList': tagsList}
    return jsonify(obj)


@app.route('/howToUse')
def howToUsePage():
    return render_template('How to Use.html')


@app.route('/About')
def aboutPage():
    return render_template('About.html')

@app.route('/Contact')
def contactUsPage():
    return render_template('Contact.html')


if __name__ == '__main__':
    app.run(debug=True)