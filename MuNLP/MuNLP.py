##  Module muNLP.py
##
##  Created by Mashimo on 17/5/25.
##  Copyright © 2025 OffMu. All rights reserved.
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##  http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.
"""
Basic NLP module for text analysis and generation
"""

from pypdf import PdfReader
from collections import Counter
import re



class MuNLP:
    'Text object, with analysis methods' 
    
     # standard initialisation, from a string
    def __init__(self, inputText, language = "EN"):
        self.text = inputText  # raw input text
        self.cleanText = ""    # without punctuation
        self.words = []
        self.tokens = []
        self.sentences = []
        self.language = language
        
        self._preprocessText()  # remove puntuaction from text and store cleaned text in cleanText
        

        
    @classmethod
    def fromPDF(cls, inputFile, language = "EN"):
        """alternative initialisation, from a PDF file"""

        reader = PdfReader(inputFile)
        
        nPages = len(reader.pages)

        content = ""

        for p in range(nPages):
            page = reader.pages[p]
            text = page.extract_text()
    
            content += text

        print("Total read pages: ", nPages)

        return cls(content, language)

    @classmethod
    def fromText(cls, inputFile, language = "EN"):
        """alternative initialisation, from a text file"""

        f = open(inputFile)
        try:
            content = f.read()  # this is a giant String
        finally:
            f.close()  # we should always close the file once finished      

        return cls(content, language)
    
    #
    # Internal functions
    #
    def _cleanTheText(self):
        """ remove punctuation from text"""
        import re

        self.cleanText = re.sub(r"([^\s\w'’])+", '', self.text.strip()) # remove punctuation & trailing spaces

        self.cleanText = self.cleanText.replace('\n', ' ')  # replace newlines with space

        self.cleanText = self.cleanText.lower() # replace capital letters
        
        
    def _removeStopwords(self):
        
        f = open("stopwords.txt")
        stopWordsText = f.read().splitlines()  # splitlines is used to remove newlines
        f.close()
        stopWords = set(stopWordsText)
        self.tokens = [token for token in self.words if token not in stopWords]
        
        
    def _preprocessText(self):
        self._cleanTheText()  # remove puntuaction from text and store cleaned text in cleanText
        self.words = self.cleanText.split() 
        
        self.sentences = re.split(r'(?<=[.!?])\s+', self.text)  # a very simple split into sentences
        
        self._removeStopwords()
        
        
        
    #
    # Set information methods
    #
    def updateText(self, newText):
        """ replace the existing text with new one + clean the new text
        Arguments:
            newText : string
        """
        self.text = newText
        
        self._preprocessText()  # remove puntuaction from text and store cleaned text in cleanText

    #
    # Retrieve information methods
    #
    def getLength(self, verbose = 0):
        """
        total number of characters in the raw text
        Arguments:
            verbose: level of verbosity: 0 = no prints, 1 = summary, 2 = per page (default=0)

        Returns:
            int = total characters
        """

        totalChars = len(self.text)

        if (verbose != 0):
            print("Total chars: ", totalChars)
        
        return totalChars
    
    
    def getNumWords(self, verbose = 0):
        """
        total number of words in the text
        Arguments:
            verbose: level of verbosity: 0 = no prints, 1 = summary, 2 = per page (default=0)

        Returns:
            int = total words
        """
        
        totalWords = len(self.words)

        if (verbose != 0):
            print("Total words: ", totalWords)
        
        return totalWords

    def getNumSentences(self, verbose = 0):
        
        totalSentences = len(self.sentences)
        
        if (verbose != 0):
            print("Approximate total number of sentences: ", totalSentences)
         
        return totalSentences
    
    def getStats(self, verbose = 0):
        """
        Basic text statistics: total words and characters
        Arguments:
            verbose: level of verbosity: 0 = no prints, 1 = summary, 2 = per page (default=0)

        Returns:
            tuple = (total words, total characters)
        """

        totalChars = len(self.text)
        totalWords = len(self.words)
        totalSentences = len(self.sentences)

        wordsCount = len(Counter(self.words)) # count the occurrences

        if (verbose != 0):
            print("Total words: ", totalWords)
            print("Unique words: ", wordsCount)
            print("Approximate total number of sentences: ", totalSentences)
            print("Total chars: ", totalChars)
        
        return totalWords, wordsCount, totalSentences, totalChars
    
    
    def getMostCommonWords(self, n=10):
        """
        the most used words and their occurence
        Arguments: 
            n: top words to return
        Returns:
            n top words and their occurence
        """
        wordsCount = Counter(self.tokens) # count the occurrences
    
        return wordsCount.most_common()[:n]
    
