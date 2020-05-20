import KMP
import BM
import regularExpression as regexp
import readVocab

dictSundaIndo = {}
dictIndoSunda = {}

'''
fungsi untuk menambahkan stopwords teh di dekat kata-kata
tertentu pada tranlation indonesia ke sunda
'''
def addStopWords(method, inputSentence):
    kataTanya = ['siapa', 'bagaimana', 'mengapa', 'sekarang']
    for word in kataTanya:
        found = (matchWithMethod(method, inputSentence, word))
        if(found != -1 and found != 0):
            inputSentence = (inputSentence[:found] + 'teh ' + inputSentence[found:])

    return inputSentence


'''
fungsi untuk mengabaikan stopword teh dan mah pada saat
translation sunda ke indonesia
'''
def ignoreStopWords(method, inputSentence):
    found = (matchWithMethod(method, inputSentence, ' teh '))
    if(found != -1):
        inputSentence = (inputSentence[:found] + inputSentence[(found + 4):])
    
    found = (matchWithMethod(method, inputSentence, ' mah'))
    if(found != -1):
        inputSentence = (inputSentence[:found] + inputSentence[(found + 4):])
    
    return inputSentence


def isOneWord(inputSentence):
    words = inputSentence.split(" ")
    if(len(words) == 1):
         return True
    else :
        return False

def sortByLen(e):
    return len(e)

'''
mencocokan string sesuai algoritma yang dipilih
'''
def matchWithMethod(method, text, pattern):
    if(method == 'bm'):
        return (BM.bmAlgorithm(text, pattern))
    elif(method == 'kmp'):
        return (KMP.kmpAlgorithm(text, pattern))
    else:
        return (regexp.regex(text, pattern))

'''
loading file vocab ke dictionary
'''
def loadFileVocab():
    global dictIndoSunda
    global dictSundaIndo

    dictSundaIndo = readVocab.fileToMap('../vocab/sunda.txt')
    dictIndoSunda = readVocab.fileToMap('../vocab/indonesia.txt')

loadFileVocab()

'''
melakukan translate kalimat dari input pengguna
'''
def translate(inputSentence, method, language):
    keys = []
    if(language == 'indotosunda'):
        dict = dictIndoSunda
        inputSentence = addStopWords(method, inputSentence)

    else:
        dict = dictSundaIndo
        inputSentence = ignoreStopWords(method, inputSentence)
    
    result = inputSentence

    keys = list(dict.keys())
    keys.sort(key = sortByLen, reverse = True)

    i = 0
    found = 1
    if(isOneWord(inputSentence)):
        for i in range (len(dict)):
            found = matchWithMethod(method, inputSentence, keys[i])

            if(found != -1):
                result = ''
                if(len(dict.get(keys[i]))>1):
                    for j in range(len(dict.get(keys[i]))-1):
                        result = result +  dict.get(keys[i])[j] + ' | '
                    result = result + dict.get(keys[i])[j+1]
                else:
                    result = dict.get(keys[i])[0]
                break
    else:
        while (found != -1):
            for i in range (len(dict)):
                found = matchWithMethod(method, inputSentence, keys[i])

                if(found != -1):
                    result = result[:found] + dict.get(keys[i])[0] + result[found + len(keys[i]):]
                                
                    dummyspace = ''
                    for j in range (len(dict.get(keys[i])[0])):
                        dummyspace = dummyspace + ' '
                    inputSentence = (inputSentence[:found] + dummyspace + inputSentence[found + len(keys[i]):])

            
    
    return result
    

            
