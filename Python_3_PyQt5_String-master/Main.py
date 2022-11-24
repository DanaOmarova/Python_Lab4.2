#!/usr/bin/env python3
# coding=utf-8

import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('Работа с текстом в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)

    def solve(self):
        self.textEdit_words.clear()
        text = self.textEdit_text.toPlainText()
        for words in re.findall(r'\w*', text):
            self.textEdit_words.insertPlainText(words + " ")
            print(words)

        # my_dict = dict()
        # my_text = open(u'D:/text.txt', 'r').read()
        # for c in my_text:
        #     if c in my_dict:
        #         my_dict[c] = my_dict[c] + 1
        #     else:
        #         my_dict.update({c: 1})
        # for w in sorted(my_dict, key=my_dict.get):
        #     print(w, my_dict[w])

        # for word in re.findall(r'\b[АВСТРХОНКМУЕ]+\b', word):
        #     self.textEdit_words.insertPlainText(word + " ")

        my_text = open('text.txt', 'r')
        # text_string = words.read().lower()
        frequency = {}
        match_pattern = re.findall(r'\b[a-z]{3,15}\b', text)
        # match_pattern = re.findall(r'\b[а-я]{3,15}\b', text)

        for word in match_pattern:
            count = frequency.get(word, 0)
            frequency[word] = count + 1
        frequency_list = frequency.keys()
        for word1 in frequency_list:
            print(word1, frequency[word1])

    def clear(self):
        self.textEdit_text.clear()
        self.textEdit_words.clear()

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
