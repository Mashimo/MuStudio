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




class MuNLP:
    'Text object, with analysis methods' 
    
     # standard initialisation, from a string
    def __init__(self, inputText, language = "EN"):
        self.text = inputText
        self.cleanText = ""
        self.tokens = []
        self.sentences = []
        self.language = language
        
        self.removePunctuation()
        
        
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

    def getLength(self, verbose = 0):
        """
        Basic text statistics
        Arguments:
            text: string
            verbose: level of verbosity: 0 = no prints, 1 = summary, 2 = per page (default=0)

        Returns:
            int = total characters
        """

        text = self.text.replace('\n', '')

        totalChars = len(text)

        if (verbose != 0):
            print("Total chars: ", totalChars)
        
        return totalChars
    
    def getNumWords(self, verbose = 0):
        """
        Basic text statistics
        Arguments:
            text: string
            verbose: level of verbosity: 0 = no prints, 1 = summary, 2 = per page (default=0)

        Returns:
            int = total words
        """

        text = self.text.replace('\n', '')

        totalWords = len(text.split())

        if (verbose != 0):
            print("Total words: ", totalWords)
        
        return totalWords

    def getStats(self, verbose = 0):
        """
        Basic text statistics
        Arguments:
            text: string
            verbose: level of verbosity: 0 = no prints, 1 = summary, 2 = per page (default=0)

        Returns:
            tuple = (total words, total characters)
        """

        text = self.text.replace('\n', '')

        totalChars = len(text)
        totalWords = len(text.split())

        if (verbose != 0):
            print("Total words: ", totalWords)
            print("Total chars: ", totalChars)
        
        return totalWords, totalChars
    
    def removePunctuation(self):
        """ remove punctuation from text"""
        import re

        self.cleanText = re.sub(r'([^\s\w_]|_)+', '', self.text.strip()) # remove punctuation


