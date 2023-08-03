from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def root():
    return 'App Started'


@app.route('/test')
@app.route('/test/hello')
def test_hello():
    return 'Hello World'


@app.route('/greet')
@app.route('/greet/<string:user>')
@app.route('/greet/<string:user>/<string:lang>')
def greet(user='user', lang='es'):
    return f'Hello {user} {lang}'


@app.route('/html')
@app.route('/html/<string:user>')
def html(user='user'):
    return '''
        <html>
            <body>
                <h1>Hola Flask</h1>
                <p>Hola %s</p>
                <ul>
                    <li>Item 1</li>
                    <li>Item 2</li>
                </ul>
            </body>
        </html>
    ''' % user


@app.route('/static-file')
def static_file():
    return "<img src='/static/img/flask-logo.png'/>"


@app.route('/static-file/url-for')
def static_file_url_for():
    return "<img src='"+url_for("static", filename="img/flask-logo.png")+"'>"


@app.route('/template')
@app.route('/template/<string:user>')
def template(user='user'):
    return render_template('view.html', name=user)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
