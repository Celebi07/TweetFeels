import re
import pickle
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from nltk.tokenize import RegexpTokenizer

# Load the saved model from the file
with open('LRmodel.pkl', 'rb') as file:
    model = pickle.load(file)

with open('vectoriser.pkl', 'rb') as file:
    vectoriser = pickle.load(file)

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(content_length))

        received_message = data['message'].lower()
        text = received_message
        # Process the data using your ML model and generate the output
        stopwordlist = ['a', 'about', 'above', 'after', 'again', 'ain', 'all', 'am', 'an',
                    'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'before',
                    'being', 'below', 'between', 'both', 'by', 'can', 'd', 'did', 'do',
                    'does', 'doing', 'down', 'during', 'each', 'few', 'for', 'from',
                    'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here',
                    'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in',
                    'into', 'is', 'it', 'its', 'itself', 'just', 'll', 'm', 'ma',
                    'me', 'more', 'most', 'my', 'myself', 'now', 'o', 'of', 'on', 'once',
                    'only', 'or', 'other', 'our', 'ours', 'ourselves', 'out', 'own', 're',
                    's', 'same', 'she', "shes", 'should', "shouldve", 'so', 'some', 'such',
                    't', 'than', 'that', "thatll", 'the', 'their', 'theirs', 'them',
                    'themselves', 'then', 'there', 'these', 'they', 'this', 'those',
                    'through', 'to', 'too', 'under', 'until', 'up', 've', 'very', 'was',
                    'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom',
                    'why', 'will', 'with', 'won', 'y', 'you', "youd", "youll", "youre",
                    "youve", 'your', 'yours', 'yourself', 'yourselves']

        STOPWORDS = set(stopwordlist)

        def cleaning_stopwords(text):
            return " ".join([word for word in str(text).split() if word not in STOPWORDS])

        import string

        english_punctuations = string.punctuation
        punctuations_list = english_punctuations

        def cleaning_punctuations(text):
            translator = str.maketrans('', '', punctuations_list)
            return text.translate(translator)

        def cleaning_repeating_char(text):
            return re.sub(r'(.)1+', r'1', text)

        def cleaning_URLs(data):
            return re.sub('((www.[^s]+)|(https?://[^s]+))', ' ', data)

        def cleaning_numbers(data):
            return re.sub('[0-9]+', '', data)

        text = cleaning_stopwords(text)
        text = cleaning_punctuations(text)
        text = cleaning_repeating_char(text)
        text = cleaning_URLs(text)
        text = cleaning_numbers(text)

        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(text)
        print(tokens)

        import nltk

        st = nltk.PorterStemmer()

        def stemming_on_text(text):
            stemmed_text = [st.stem(word) for word in text]
            return stemmed_text

        stemmed_tokens = stemming_on_text(tokens)
        stemmed_text = ' '.join(stemmed_tokens)

        text = vectoriser.transform([stemmed_text])
        y_pred44 = model.predict(text)

        sentiment_label = "Neutral"
        if y_pred44[0] == 0:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Positive"
            # Replace this with your own code
        output = {
            'output': sentiment_label
        }

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers() 
        self.wfile.write(json.dumps(output).encode('utf-8'))

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Server running on http://localhost:8000')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()