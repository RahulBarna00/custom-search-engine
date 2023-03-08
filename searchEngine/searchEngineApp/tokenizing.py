# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords

def tokenization(text):
    text = text.lower()
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    
    tokens = [word for word in tokens if word not in stop_words]
    
    if (tokens == []):
        tokens = word_tokenize(text)

    listn = []

    for x in tokens:
        listn.append(x)
        
    return listn
