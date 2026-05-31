# 📰 Detecção de Fake News — Bloomberg Style

> Classificação automática de notícias falsas em português com Python e Machine Learning.

---

## 📌 Sobre o Projeto

Este projeto aplica **Processamento de Linguagem Natural (NLP)** e **Machine Learning** para classificar notícias em português como verdadeiras ou falsas.

O modelo é treinado sobre o **Fake.br Corpus** (USP) e exposto via interface em `main.py`. O usuário insere o texto de uma notícia e recebe a classificação em tempo real.

---

## 🗂️ Dataset

**Fake.br Corpus** — desenvolvido pela Universidade de São Paulo (USP)  
🔗 https://github.com/roneysco/Fake.br-Corpus

- Notícias em **português brasileiro**
- Duas classes: `fake` e `true`

---

## 🛠️ Tecnologias

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.x |
| Treinamento | Jupyter Notebook |
| Vetorização | TF-IDF (`tfidf.pkl`) |
| Modelo | Classificador serializado (`modelo.pkl`) |

---

## 📁 Estrutura

```
Projeto/
├── main.py                    # Interface principal — execute este arquivo
├── prever.py                  # Lógica de predição
├── modelo.pkl                 # Modelo treinado
├── tfidf.pkl                  # Vetorizador TF-IDF
└── treinamento_do_modelo.ipynb # Notebook de treinamento do modelo
```

---

## 📊 Pipeline

```
Fake.br Corpus (USP)
        ↓
  treinamento_do_modelo.ipynb
  (pré-processamento + TF-IDF + treino)
        ↓
  modelo.pkl + tfidf.pkl
  (artefatos serializados)
        ↓
  main.py
  (interface de classificação)
```

---

## 👤 Autor

**Miguel Dias**  
Estudante de Tecnologia da Informação — Instituto Mauá de Tecnologia (IMT)  
🔗 [github.com/miguelrdias1](https://github.com/miguelrdias1)

---

## 📄 Licença

Projeto acadêmico. Dataset sujeito aos termos do [Fake.br Corpus](https://github.com/roneysco/Fake.br-Corpus).
