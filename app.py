from flask import Flask
from routes.upload import upload_bp
from routes.query import query_bp

app = Flask(__name__)

app.register_blueprint(upload_bp, url_prefix='/upload')
app.register_blueprint(query_bp, url_prefix='/query')

@app.route('/')
def index():
    return "The application is deployed and it is running."

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000, debug=False)
    app.run()
