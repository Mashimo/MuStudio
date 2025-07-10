from MuNLP import MuNLP

# run pytest

     # 1 paragraph, 6 lines, 4 sentences, 74 words (54 unique), 401 chars, 479 chars with spaces, punctuation and newlines
sample = """Processing raw text intelligently is difficult: most words are rare, 
and it’s common for words that look completely different to mean almost the same thing. 
The same words in a different order can mean something completely different. 
Even splitting text into useful word-like units can be difficult in many languages. 
While it’s possible to solve some problems starting from only the raw characters, 
it’s usually better to use linguistic knowledge to add useful information."""

line =  "Hello, world!"  # 13 chars


def test_getLength():
    nlp = MuNLP(line)
    assert nlp.getLength() == 13

def test_getNumWords():
    nlp = MuNLP(line)
    assert nlp.getNumWords() == 2
    
def test_getNumSentences():
    nlp = MuNLP(line)
    assert nlp.getNumSentences() == 1

def test_getStats():
    nlp = MuNLP(sample)
    assert(nlp.getStats() == (74, 54, 4, 479))

def test_numTopWords():
    nlp = MuNLP(sample)
    assert(len(nlp.getMostCommonWords()) == 9)
    
def test_getTopBigrams():
    nlp = MuNLP(sample)
    bigrams = nlp.getTopBigrams()
    assert(len(bigrams) == 1)
    assert(bigrams[0][1] == 2)
    