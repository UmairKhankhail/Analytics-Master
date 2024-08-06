from flask import Flask
#from routes.upload import upload_bp
#from routes.query import query_bp
#from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

#app.register_blueprint(upload_bp, url_prefix='/upload')
#app.register_blueprint(query_bp, url_prefix='/query')
# # Set strict_slashes to False for all routes
#app.url_map.strict_slashes = False

@app.route('/')
def index():
    return "The application is deployed and it is running."

#if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000, debug=False)
    app.run()
