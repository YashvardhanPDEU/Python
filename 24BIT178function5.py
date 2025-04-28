sentence = input("enter sentence: ")

def ispangram(sentence):

    alphaset = set("abcdefghijklmnopqrstuvwxyz")
    sentenceset = set(sentence.lower())
    if alphaset <= sentenceset:
        print("is pangram")
    else:
        print("no")

ispangram(sentence)        
