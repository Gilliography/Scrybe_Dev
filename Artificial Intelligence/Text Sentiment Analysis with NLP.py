from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Sample text data and labels (1=Positive, 0=Negative)
text_data = ["I love this product", "This is terrible", "Best purchase ever", "Not worth the money", "Awesome!", "I hate this item"]
labels = [1, 0, 1, 0, 1, 0]

# Convert text to numeric data (Bag-of-Words model)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(text_data)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Train a Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train, y_train)

# Predict on test set and evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
