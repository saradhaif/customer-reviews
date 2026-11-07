
import streamlit as st
from transformers import pipeline

st.title("Crochet Review Classifier")

@st.cache_resource
def load_models():
    sentiment_model = pipeline("sentiment-analysis", model="cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual")
    zero_shot_model = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")
    return sentiment_model, zero_shot_model

sentiment_model, zero_shot_model = load_models()

categories = [
    "overall satisfaction",
    "product quality",
    "packaging&delivery",
    "support",
    "general appreciation",
    "customer service",
    "product variaty",
    "website/online presence"
]

review = st.text_area("Enter a review")

if st.button("Analyze"):
    if review:
        sentiment = sentiment_model(review)[0]
        category = zero_shot_model(review, candidate_labels=categories)

        st.write("Sentiment:", sentiment["label"])
        st.write("Sentiment Score:", sentiment["score"])

        st.write("Category:", category["labels"][0])
        st.write("Category Score:", category["scores"][0])
