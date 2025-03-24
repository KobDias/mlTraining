from funcao import prediz
from flask import Flask, request, jsonify, render_template
from waitress import serve

app = Flask(__name__)

# routes

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/api/classify/iris', methods=['POST'])
def iris_classifier_api():
    return jsonify({
        "species": prediz(request.json['sepal_length'], request.json['sepal_width'], request.json['petal_length'], request.json['petal_width'])
        })

@app.route('/api/classify/iris', methods=['GET'])
def iris_classifier_get():
    return render_template('index.html')

@app.route('/api/classify/iris', methods=['POST'])
def iris_classifier():
    return render_template('index.html', especie=species, )
    

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8080)