import os
import re

import nltk
from nltk.corpus import stopwords


class languageModel:
    def __init__(self):
        self.trigramList = {}
        self.probabilities = {}

    # read data from specific directory into one string
    def ReadData(self,scraped_dir):
        datasetTxt = ""
        for filename in os.listdir(scraped_dir):
            f = os.path.join(scraped_dir, filename)
            # checking if it is a file
            if os.path.isfile(f):
                file = open(f, "r", encoding='utf-8')
                datasetTxt = datasetTxt +".\n"+ file.read().strip()
                file.close()
        return datasetTxt
    # if we don't have probability to one word for given statement
    def CalcProb(self,phrase, counter=0):
        if phrase not in self.trigramList.keys():
            self.trigramList[phrase] = 1
        else:
            self.trigramList[phrase] += 1
        counter += 1
        self.probabilities[phrase] = self.trigramList[phrase] / counter
        # print(self.probabilities[phrase])
        # print("innnn")
        # print(self.trigramList)

    def generateNGrams(self,words_list, counter=0):
        triGrams = []
        for num in range(0, len(words_list)):
            sentence = ' '.join(words_list[num:num + 3])
            self.CalcProb(sentence, counter)

    def splitSequence(self,seq):
        return seq.split(" ")
    def getPredictions(self,sequence):
        count = 0
        nPredictions = 5
        options = []
        predicted = []
        nPred = nPredictions
        inputSequence = self.splitSequence(sequence)
        for sentence in self.probabilities.keys():
            if sequence in sentence:
                outputSequence = self.splitSequence(sentence)
                cont = False
                for i in range(0, len(inputSequence)):
                    if outputSequence[i] != inputSequence[i]:
                        cont = True
                        break
                if cont:
                    continue
                predicted.append((sentence, self.probabilities[sentence]))
        predicted.sort(key=lambda x: x[1], reverse=True)

        noPrediction = False
        if len(predicted) == 0:
            print("No predicted words")
            noPrediction = True
        else:
            if len(predicted) < nPredictions:
                nPred = len(predicted)

            for i in range(0, nPred):
                outputSequence = predicted[i][0].split(" ")
                print(outputSequence[len(inputSequence)])
                options.append(outputSequence[len(inputSequence)])
        return options, noPrediction, nPred

    # preparing data for generating ngrams
    def tokenizeText(self,text):
        text = text.lower()
        # tokenizing text to work on arabic and english words and numbers
        text = re.sub('[^\sa-zA-Z0-9ء-ي]', '', text)
        return text.split()

if __name__ == '__main__':
    # # Your directory to the folder with scraped websites
    # scraped_dir = 'Khaleej-2004/Economy'
    # dataset = ""
    # x = 0
    # for filename in os.listdir(scraped_dir):
    #     f = os.path.join(scraped_dir, filename)
    #     # checking if it is a file
    #     if os.path.isfile(f):
    #         page = open(f, "r", encoding='utf-8')
    #         dataset = dataset + page.read().strip()
    # sw = stopwords.words('arabic')
    # tokens = nltk.word_tokenize(dataset)
    # stopped_tokens = [i for i in tokens if not i in sw]
    # print(tokens)
    # # stopped_tokens = list(dict.fromkeys(stopped_tokens))
    # x = x + len(stopped_tokens)
    #
    # print(x)
    # for item in stopped_tokens:
    #     print(item)
    l=languageModel()
    dataset = l.ReadData('Khaleej-2004/Economy')
    words = l.tokenizeText(dataset)

    seq = input("Enter search words: ")
    l.generateNGrams(words, len(seq.split()) + 1)
    l.getPredictions(seq)
