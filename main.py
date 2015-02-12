from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello(path):
    return 'Gone', 410


@app.errorhandler(404)
def page_not_found(e):
    return 'Sorry, nothing at this URL.', 404
