from flask import Flask, url_for, render_template, request
from utils.downloadXvideos import download_xvideos

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    equals = []
    return render_template('index.html', equals=equals)


@app.route('/check', methods=['POST'])
def check():
    if request.method == 'POST':
        link = request.form['url']
        if 'xvideo' not in link:
            return render_template('index.html', fail='Not Found')
        equals = download_xvideos(link)
        return render_template('index.html', equals=equals, link=link)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
