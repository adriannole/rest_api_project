from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/api/v1/hello', methods=['GET'])
    def hello_world():
        return {"message": "Hola Mundo!"}, 200

    return app
