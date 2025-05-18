from MuNLP import MuNLP

def test_getLength():
    text = "Hello, world!"
    nlp = MuNLP(text)
    assert nlp.getLength() == 13

def test_getNumWords():
    text = "Hello, world!"
    nlp = MuNLP(text)
    assert nlp.getNumWords() == 2

