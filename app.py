from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/ml', methods = ['post', 'get'])
def ml():
    ml_url = request.form.get("ml_url")
    # 머신러닝 코드
    return render_template('ml.html', ml_result=ml_url)


if __name__ == '__main__':
    app.run(debug=True)
