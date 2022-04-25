import codecs
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

if __name__ == '__main__':
    # Your directory to the folder with scraped websites
    scraped_dir = 'Khaleej-2004/Economy/arc_Articlesww0c5e.html'
    page=codecs.open(scraped_dir,encoding='utf-8')
    for line in page:
        print(line.strip())
        sw = stopwords.words('arabic')
        tokens = nltk.word_tokenize(line)
        stopped_tokens = [i for i in tokens if not i in sw]
        for item in stopped_tokens:
            print(item)


