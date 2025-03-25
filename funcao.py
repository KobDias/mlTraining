import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def create_model():
    iris = pd.read_csv('iris.csv')

    X_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    y_columns = ['species']
    X = iris[X_columns]
    y = iris[y_columns].values.ravel()


    
    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=101)
    X_train.shape
    X_test.shape



    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    preds = knn.predict(X_test)
    preds

    
    joblib.dump(knn, 'knn.pkl')

def prediz(sepal_length, sepal_width, petal_length, petal_width):
    if not os.path.isfile('knn.pkl'):
        create_model() # Certifica que o arquivo pkl existe
    modelo = joblib.load('knn.pkl') # Carregando o modelo
    especie = modelo.prediz([[sepal_length, sepal_width, petal_length, petal_width]]) # Predizendo a espécie
    return especie[0]

def get_prediction(data):
    return prediz(
        data['sepal_length'],
        data['sepal_width'],
        data['petal_length'],
        data['petal_width']
    )

    