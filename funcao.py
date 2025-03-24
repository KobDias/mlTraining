import pandas as pd
import joblib
import os

def create_model():
    iris = pd.read_csv('iris.csv')

    X_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    y_columns = ['species']
    X = iris[X_columns]
    y = iris[y_columns].values.ravel()


    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=101)
    X_train.shape
    X_test.shape

    from sklearn.neighbors import KNeighborsClassifier

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    preds = knn.predict(X_test)
    preds

    from sklearn.metrics import accuracy_score
    joblib.dump(knn, 'knn.pkl')
def prediz(sep_l, sep_w, pet_l, pet_w):
    if not os.path.isfile('knn.pkl'):
        create_model() # Certifica que o arquivo pkl existe

    modelo = joblib.load('knn.pkl') # Carregando o modelo
    especie = modelo.predict([[sep_l, sep_w, pet_l, pet_w]]) # Predizendo a espécie
    return especie[0]