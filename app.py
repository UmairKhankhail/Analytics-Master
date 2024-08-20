from flask import Flask
from routes.upload import upload_bp
from routes.query import query_bp

app = Flask(__name__)

app.register_blueprint(upload_bp, url_prefix='/upload')
app.register_blueprint(query_bp, url_prefix='/query')
# # Set strict_slashes to False for all routes
#app.url_map.strict_slashes = False

@app.route('/connect')
def connect():
    return "The application is deployed and it is running."


@app.route('/is_dataset_clean')
def is_dataset_clean():
    # Simulate a POST request to the '/query/' route
    data = {'query': 'Is the dataset clean and ready for analysis?'}
    
    with app.test_request_context(method='POST', json=data):
        response = app.view_functions['query.query_data']()
        return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
    #app.run()
