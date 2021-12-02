from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def test():
    return render_template('index.html')

@app.route('/progress', methods=['GET', 'POST'])
def progress():
    if request.method == 'POST':
        pass

    return render_template('progress.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)