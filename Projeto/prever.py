import joblib
import warnings
warnings.filterwarnings("ignore")
modelo = joblib.load("modelo.pkl")
tfidf = joblib.load("tfidf.pkl")

def analisar(noticia):

    noticia_transformada = tfidf.transform([noticia])

    resultado = modelo.predict(noticia_transformada)

    return resultado[0]