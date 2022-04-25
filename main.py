import os

import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

if __name__ == '__main__':
    # Your directory to the folder with scraped websites
    scraped_dir = 'Khaleej-2004/Economy'
    dataset=""
    x=0
    for filename in os.listdir(scraped_dir):
        f = os.path.join(scraped_dir, filename)
        # checking if it is a file
        if os.path.isfile(f):
            page = open(f, encoding='utf-8')
            dataset=dataset+page.read()
    sw = stopwords.words('arabic')
    tokens = nltk.word_tokenize(dataset)
    stopped_tokens = [i for i in tokens if not i in sw]
    print(stopped_tokens)
    x=x+len(stopped_tokens)

    print(x)
        # for item in stopped_tokens:
        #     print(item)

