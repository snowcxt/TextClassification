from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = joblib.load('./vectorizer.pkl')
clf = joblib.load('./MultinomialNB.pkl')
categories = joblib.load('./categories.pkl')

def predict(text):  
    pred = clf.predict(vectorizer.transform([text]))
    return categories[pred[0]]
