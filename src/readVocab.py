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
            # print (key)
            value = splitted[1]
            # print(value)
            dict [key] = value
    
    print (dict)

fileToMap('../vocab/sunda.txt')


