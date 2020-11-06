# Group Member: Sivananda Rajananda, Xin Zeng

class Sentence:
    def __init__(self, text): 
        self.words = text.split() 

    def __iter__(self):
        for word in self.words:
            yield word


if __name__ == "__main__":
    text = "Hi Sandraw"
    si = Sentence(text)
    
    it = iter(si)
    print(next(it))
    print(next(it))

    for word in si:
        print(word)
