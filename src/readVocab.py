'''
membaca file eksternal vocab dan memasukkannya 
ke dalam dictionary
'''
def fileToMap(source):
    dict = {}

    f = open(source)
    text = f.read()
    lines = text.split('\n')
    # print (lines)
    for line in lines:
        splitted = line.split(' = ')
        # print (splitted)
        if(len(splitted) > 1):
            key = splitted[0]
            value = splitted[1]
            dict.setdefault(key, [])
            dict[key].append(value)
    
    return (dict)


