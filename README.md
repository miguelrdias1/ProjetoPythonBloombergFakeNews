# Detector de Fake News

Projeto em Python que classifica notícias em português como verdadeiras ou falsas. Fiz na faculdade para praticar NLP e machine learning na prática.

Você cola o texto de uma notícia e o programa diz se ela parece verdadeira ou falsa.

## Como funciona

O modelo foi treinado com o [Fake.br Corpus](https://github.com/roneysco/Fake.br-Corpus), um conjunto de notícias em português brasileiro criado pela USP, dividido em duas classes: `fake` e `true`.

No notebook `treinamento_do_modelo.ipynb` eu limpo os textos, transformo em números com TF-IDF e treino o classificador ([algoritmo usado]). O modelo e o vetorizador ficam salvos em `modelo.pkl` e `tfidf.pkl`, e o `main.py` carrega os dois para classificar textos novos.

## Arquivos

```
Projeto/
├── main.py                       # programa principal, é este que você roda
├── prever.py                     # função que faz a previsão
├── modelo.pkl                    # modelo treinado
├── tfidf.pkl                     # vetorizador TF-IDF
└── treinamento_do_modelo.ipynb   # treino do modelo
```

## Como rodar

```bash
git clone https://github.com/miguelrdias1/ProjetoPythonBloombergFakeNews.git
cd ProjetoPythonBloombergFakeNews/Projeto
pip install scikit-learn pandas
python main.py
```

Depois é só colar o texto da notícia.

## Resultados

- Acurácia: [preencher]
- F1-score: [preencher]

## Limitações

O modelo só conhece o que viu no Fake.br, então pode errar em notícias de outros temas ou de outra época. Também não é um substituto para checar a informação em fontes confiáveis, é só um projeto de estudo.

## Autor

Miguel Ribeiro Dias, estudante de Ciência da Computação no Instituto Mauá de Tecnologia.

[LinkedIn](https://www.linkedin.com/in/miguel-ribeiro-dias-184819402) | [GitHub](https://github.com/miguelrdias1)
