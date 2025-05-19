from MuNLP import MuNLP

     # 1 page, 6 paragraphes, 74 words, 401 chars, 474 chars with spaces
    # 69+88+77+84+82+74 = 474
sample = """Processing raw text intelligently is difficult: most words are rare, 
and it’s common for words that look completely different to mean almost the same thing. 
The same words in a different order can mean something completely different. 
Even splitting text into useful word-like units can be difficult in many languages. 
While it’s possible to solve some problems starting from only the raw characters, 
it’s usually better to use linguistic knowledge to add useful information."""

line =  "Hello, world!"


def test_getLength():
    nlp = MuNLP(line)
    assert nlp.getLength() == 13

def test_getNumWords():
    nlp = MuNLP(line)
    assert nlp.getNumWords() == 2

def test_getStats():
    nlp = MuNLP(sample)
    assert(nlp.getStats() == (74, 474))

