from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

reviews = [
    (' This product is absolatelty amzing! highly recommanded',1),
    ('Great quality and fast deleviery',1),
    ('loved it!',1),
    ('super satisfied with the purcase',1),
    ('five stars! outstanding product',1),
    ('Wrost purchase ever. complete waste of money',0),
    ('poor quality and very late deleivery',0),
    ('total scam. do not buy',0),
]

texts, labels = zip(*reviews)

vectorizer = TfidfVectorizer(ngram_range=(1,2), max_features=500)
X = vectorizer.fit_transform(texts)
y = list(labels)

X_traiin,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=42)

clf = LogisticRegression()
clf.fit(X_traiin, y_train)
print(f'accuracy: {accuracy_score(y_test,clf.predict(X_test))*100:.0f}')

new = [
    '   This is a wonderful product! Totally worth it!'
       'very bad experience, quality is avful',
       'Average product . Nothing special',
       ]


X_new = vectorizer.transform(new)
for review, pred, prob in zip(new, clf.predict(X_new), clf.predict_proba(X_new)):
    sentiment = 'Positive' if pred==1 else 'Negative'
    confidence = max(prob)*100
    print(f'[{sentiment} {confidence:.0f}%] {review[:45]}...')

