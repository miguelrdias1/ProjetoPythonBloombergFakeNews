import joblib
import warnings
import os
warnings.filterwarnings("ignore")
BASE_DIR = os.path.dirname(__file__)
modelo_path = os.path.join(BASE_DIR, "modelo.pkl")
tfidf_path = os.path.join(BASE_DIR, "tfidf.pkl")
modelo = joblib.load(modelo_path)

tfidf = joblib.load(tfidf_path)


def analisar(noticia):

    noticia_transformada = tfidf.transform([noticia])

    resultado = modelo.predict(noticia_transformada)

    return resultado[0]