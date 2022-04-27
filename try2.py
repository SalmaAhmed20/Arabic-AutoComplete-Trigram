# -*- coding: utf-8 -*-
import os
# GUI
import tkinter
from tkinter import FLAT

import nltk
from nltk.corpus import stopwords


class LanguageModel:
    def __init__(self):
        # يعرض فيها الباحثون :عدد مرات انها جت بالشكل ده
        # فيها الباحثون ثمرات :عدد مرات انها جت بالشكل ده
        self.TrigramsDic = {}  # key :value
        self.probabilitiesDic = {}

    def ReadData(self, dir):
        datasetTxt = ""
        for filename in os.listdir(dir):
            f = os.path.join(dir, filename)
            # checking if it is a file
            if os.path.isfile(f):
                file = open(f, "r", encoding='utf-8')
                datasetTxt = datasetTxt + ".\n" + file.read().strip()
                file.close()
        return datasetTxt

    def Tokenization(self, text):
        sw = stopwords.words('arabic')
        tokens = nltk.word_tokenize(text)
        return tokens

    def calcProb(self, sentence):
        counter = 0
        # sentence not exist add new key to dic
        if sentence not in self.TrigramsDic.keys():
            # no.occurrence = 1
            self.TrigramsDic[sentence] = 1
        else:
            # increase number of occurrence
            self.TrigramsDic[sentence] += 1
        counter += 1
        self.probabilitiesDic[sentence] = self.TrigramsDic[sentence] / counter

    # make list of sentence of 3 words from tokens  and calculate probability
    def generate3Grams(self, words_list):
        for num in range(0, len(words_list)):
            sentence = ' '.join(words_list[num:num + 3])
            self.calcProb(sentence)

    def PredictNext(self, inputsentence):
        FoundedSequence = []
        options = []
        predicted = []
        inputSequence = inputsentence.split(" ")
        # search in dictionary
        for sentence in self.probabilitiesDic.keys():
            if inputsentence in sentence:
                FoundedSequence = sentence.split(" ")
                # print(FoundedSequence)
                cont = False
                for i in range(0, len(inputSequence)):
                    if FoundedSequence[i] != inputSequence[i]:
                        cont = True
                        break
                if cont:
                    continue
                predicted.append((sentence, self.probabilitiesDic[sentence]))
        predicted.sort(key=lambda x: x[1], reverse=True)
        if (len(predicted) == 0):
            return []
        else:
            options.append(FoundedSequence[len(inputSequence)])
        return options


# top = tkinter.Tk()
#
# top.title("Arabic Auto fill")
# canvas1 = tkinter.Canvas(top, width=400, height=300,background='#EFFFFD')
# canvas1.pack()
# label1 = tkinter.Label(top, text='Enter your phrase',background='#EFFFFD')
# label1.config(font=('helvetica', 16))
# canvas1.create_window(200, 25, window=label1)
# entry1 = tkinter.Entry(top, width=20,font=('Arial 14'),borderwidth=2)
#
#
# def getNextword():
#     seq = entry1.get()
#     words1 = seq.split(" ")
#     # print(len(words1))
#     if len(words1) <= 2:
#         Lm = LanguageModel()
#         dataset = Lm.ReadData('Khaleej-2004/Economy')
#         words = Lm.Tokenization(dataset)
#         Lm.generate3Grams(words)
#         nxtwords = Lm.PredictNext(seq)
#         # print(nxtwords)
#     else:
#         seq2 = words1[len(words1) - 2] + " " + words1[len(words1) - 1]
#         Lm = LanguageModel()
#         dataset = Lm.ReadData('Khaleej-2004/Economy')
#         words = Lm.Tokenization(dataset)
#         Lm.generate3Grams(words)
#         nxtwords = Lm.PredictNext(seq2)
#     if len(nxtwords) != 0:
#         label3 = tkinter.Label(top, text=seq + " " + nxtwords[0],font=('helvetica', 16),background="lightblue")
#     else:
#         label3 = tkinter.Label(top, text="No expected",font=('helvetica', 16),background='red')
#     canvas1.create_window(200, 230, window=label3)
#
#
# button1 = tkinter.Button(text='submit', command=getNextword,height=1,background="lightblue",font=('helvetica', 12))
# button1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT)
# canvas1.create_window(200, 100, window=button1)
# canvas1.create_window(200, 60, window=entry1)
# top.mainloop()
if __name__ == '__main__':
    Lm = LanguageModel()
    dataset = Lm.ReadData('Khaleej-2004/Economy')
    # print(dataset)
    words = Lm.Tokenization(dataset)
    seq = input("Enter search words: ")
    Lm.generate3Grams(words)
    nxtwords = Lm.PredictNext(seq)
    if len(nxtwords) != 0:
        print(nxtwords)
    else:
        print("No expected")
