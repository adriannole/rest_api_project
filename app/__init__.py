from flask import Flask, render_template, jsonify

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def home():
        # Sirve el archivo HTML
        return render_template('index.html')

    @app.route('/api/v1/hello', methods=['GET'])
    def hello_world():
        # Devuelve un mensaje JSON
        return jsonify({"message": "Hola Mundo!"}), 200

    return app
