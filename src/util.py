def ignoreStopWords(sentence):
    newSentence = ''
    if(word.lower() != 'teh' and word.lower() != 'mah'):
        newSentence.append(word)
    
    return (newSentence)


def addStopWords(sentence):
    newSentence = []
    for word in sentence :
        if(word.lower() == 'siapa'):
            newSentence.append('teh')
            newSentence.append(word)
        else :
            newSentence.append(word)




