from flask import Flask, render_template, jsonify,request, make_response,redirect
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
    return render_template('Contact.html',sendMessage=None)

@app.route('/sendMessage',methods=['GET','POST'])
def sendMessage():
    name = request.form['name']
    email = request.form['email']
    title = request.form['title']
    message = request.form['message']
    return render_template('Contact.html',message='Your message Sent Successfully! We will reach you within 24 hours.')

if __name__ == '__main__':
    app.run(debug=True)