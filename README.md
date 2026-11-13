# 🎯 Career FAQ Intelligence

A career FAQ recommendation system that retrieves relevant questions and answers using TF-IDF keyword search and Sentence-BERT semantic search.

## Features

- Search 24,724 career FAQs collected from three datasets.
- Choose between TF-IDF and Sentence-BERT retrieval.
- Compare both methods side by side using the same question and result limit.
- View search times, shared results, and whether the top-ranked questions agree.
- Explore the FAQ data and the project's evaluation results.
- Use the standalone Streamlit app or the Streamlit interface with a FastAPI backend.

Similarity scores describe how closely a result matches within each model. They are not confidence probabilities, and scores from different models should not be compared directly. The displayed search times exclude model startup; API search times include request overhead.

## Datasets

| Source | Records |
|---|---:|
| CareerVillage Q&A | 23,064 |
| Entry Level Career QA | 1,620 |
| HR Interview Questions | 40 |
| **Total** | **24,724** |

## Tech stack

Python, Streamlit, FastAPI, Sentence-Transformers, FAISS, scikit-learn, pandas, and NLTK.

## Project structure

```text
├── app.py                 # Standalone Streamlit app
├── streamlit_app.py       # Streamlit interface for the API
├── comparison_ui.py       # Side-by-side comparison view
├── api/
│   └── main.py            # FastAPI backend
├── src/
│   ├── data_pipeline.py
│   ├── preprocessing.py
│   ├── tfidf_retriever.py
│   └── sbert_retriever.py
├── data/
│   └── processed/
│       └── faq_corpus.csv
├── requirements.txt
└── config.py
```

## Run locally

Use Python 3.11. From the project folder, create an environment and install the dependencies:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Start the standalone app:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Open the local address shown in the terminal, usually `http://localhost:8501`. The first launch may take longer while the models load.

To use the API version, start the backend and interface in separate terminals:

```powershell
.\.venv\Scripts\python.exe -m uvicorn api.main:app --reload --port 8000
```

```powershell
.\.venv\Scripts\python.exe -m streamlit run streamlit_app.py
```

## Evaluation results

The project evaluation reported:

| Metric | TF-IDF | Sentence-BERT |
|---|---:|---:|
| Precision@1 | 0.77 | **0.79** |
| Mean Reciprocal Rank | **0.812** | 0.810 |
| Precision@5 | **0.87** | 0.84 |

These are results from the project's evaluation, not measurements from an individual search in the app.

## Authors

- Jaya Peda Vignesh Reddy Duggempudi
- Naga Dhanushya Ram Munnanuru

*COSC 757 — Data Mining, Towson University, Fall 2025*