from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = joblib.load('./vectorizer.pkl')
clf = joblib.load('./MultinomialNB.pkl')
categories = [
    'alt.atheism',
    'comp.graphics',
    'comp.os.ms-windows.misc',
    'comp.sys.ibm.pc.hardware',
    'comp.sys.mac.hardware',
    'comp.windows.x',
    'misc.forsale',
    'rec.autos',
    'rec.motorcycles',
    'rec.sport.baseball',
    'rec.sport.hockey',
    'sci.crypt',
    'sci.electronics',
    'sci.med',
    'sci.space',
    'soc.religion.christian',
    'talk.politics.guns',
    'talk.politics.mideast',
    'talk.politics.misc',
    'talk.religion.misc']

def predict(text):  
    pred = clf.predict(vectorizer.transform([text]))
    return categories[pred[0]]
