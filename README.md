# Crochet Reviews Classification Using Hugging Face

the deployed app: [https://customercrochetreviews.streamlit.app/]

## 1. Project Overview

This project uses pretrained Hugging Face models to classify customer reviews about crochet products.

The project includes two tasks:
- Task A: Sentiment Analysis
- Task B: Zero-Shot Classification

## 2. Dataset Collection

I collected customer reviews from my own crochet business, @fluffy.bh, and other shops that sell crochet products.

All reviews from my business were positive, so I collected reviews from other crochet shops to include different opinions and make the dataset more balanced.

The dataset contains 62 reviews.

## 3. Task A: Sentiment Analysis

The goal of this task is to classify reviews into three sentiments:

- Positive
- Neutral
- Negative

I tested three pretrained Hugging Face models and compared their performance.

## 4. Sentiment Models

### Model 1
cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual

### Model 2
lxyuan/distilbert-base-multilingual-cased-sentiments-student

### Model 3
cardiffnlp/twitter-roberta-base-sentiment-latest

## 5. Sentiment Analysis Results

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---|---|---|---|
| Model 1 | 80.65% | 72.43% | 67.01% | 69.23% |
| Model 2 | 74.19% | 57.72% | 56.01% | 56.30% |
| Model 3 | 69.35% | 68.95% | 64.21% | 64.80% |

## 6. Best Sentiment Model

Model 1 achieved the highest accuracy of 80.65%.

It correctly classified 50 out of 62 reviews and made 12 incorrect predictions.

This model performed best overall based on accuracy and F1 score.

## 7. Sentiment Error Analysis

I used a confusion matrix to understand the predictions.

I also compared the actual sentiments with the predicted sentiments to identify mistakes.

Some possible reasons for incorrect predictions include:
- Reviews containing mixed opinions
- Unclear wording
- Different writing styles
- Difficulty understanding the context

## 8. Task B: Zero-Shot Classification

In this task, I used zero-shot classification to predict the topic of customer reviews.

Unlike sentiment analysis, zero-shot classification allows me to provide categories without training the model on examples of those categories.

The model compares each review with the candidate categories and predicts the best match.

## 9. Zero-Shot Results

| Metric | Result |
|---|---|
| Accuracy | 38.71% |
| Macro F1 Score | 31.66% |

The zero-shot model achieved lower performance than the sentiment models.

This suggests that identifying the topic of a review was more difficult for the model.

Some reviews may discuss more than one topic, making classification harder.

## 10. Tools and Libraries

The project uses:

- Python
- Google Colab
- Hugging Face Transformers
- Pandas
- Scikit-learn
- Matplotlib

## 11. Challenges and Limitations

One challenge was collecting reviews with different sentiments because all reviews from my business were positive.

To solve this, I collected additional reviews from other crochet shops.

Another challenge was comparing the models because their predicted labels sometimes had different formats.

The zero-shot model also achieved lower accuracy than expected, likely because there wasnt any clear classes for each review.

The dataset is relatively small, so the results may change with a larger dataset.

## 12. Conclusion

In this project, I learned how to use pretrained Hugging Face models for sentiment analysis and zero-shot classification.

The best sentiment model achieved 80.65% accuracy, while zero-shot classification achieved 38.71% accuracy.

I also learned how to calculate evaluation metrics, compare models, and analyze incorrect predictions.

Overall, sentiment analysis performed better than zero-shot classification on my dataset.
