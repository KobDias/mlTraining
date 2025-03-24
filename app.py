from funcao import prediz
from flask import Flask, request, jsonify
from waitress import serve

app = Flask(__name__)

# routes
@app.route('/api/classify/iris', methods=['POST'])
def iris_classifier_api():
    return jsonify({
        "species": prediz(request.json['sepal_length'], request.json['sepal_width'], request.json['petal_length'], request.json['petal_width'])
        })

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8080)