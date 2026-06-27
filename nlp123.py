import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt');
nltk.download('stopwords');
nltk.download('wordnet')
nltk.download('punkt_tab')


text = 'students are learning python aiml in BHopal'

tokens = word_tokenize(text.lower())
print('Tokens:,tokens')

stop = set(stopwords.words('english'))

filtered = [w for w in tokens if w not in stop and w.isalpha] 
print('After stopward removal:',filtered)
lema = WordNetLemmatizer()
final = [lema.lemmatize(w) for w in filtered]
print('After lematisation:', final)
from sklearn.feature_extraction.text import TfidfVectorizer
docs = ['python is great for data science','Machine learning is amazing',' Ai is the future of technology']
tfidf = TfidfVectorizer()
matrix = tfidf.fit_transform(docs)
print('Tf-IDF shape:' , matrix.shape)
print('feature names:', tfidf.get_feature_names_out())