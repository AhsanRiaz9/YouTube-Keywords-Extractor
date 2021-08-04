from flask import Flask, render_template, jsonify,request, make_response
from Scrapping import getKeywords
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("a.html")

@app.route('/getYoutubeVideoTags',methods=['POST'])
def getYoutubeTags():
    obj = eval(request.get_data())
    tagsList = getKeywords(obj['url'])
    print(tagsList)
    obj = {'tagList': tagsList}
    return jsonify(obj)

if __name__ == '__main__':
    app.run()