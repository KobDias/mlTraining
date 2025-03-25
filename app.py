from funcao import prediz, get_prediction
from flask import Flask, request, jsonify, render_template
from waitress import serve

app = Flask(__name__)

# routes

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/classify/iris', methods=['POST'])
def iris_classifier_api():
    species = get_prediction(request.json)
    return jsonify({"species": species})

# @app.route('/api/classify/iris', methods=['GET'])
# def iris_classifier_get():
#     return render_template('index.html')

@app.route('/predict', methods=['POST'])
def iris_classifier():
    species = get_prediction(request.form)
    return render_template('index.html', especie=species)
    

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8080)
    app.run(debug=True)