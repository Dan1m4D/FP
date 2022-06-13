import bisect

def extract ():
    word = line.strip()
    return word

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i

with open ("wordlist.txt", "r") as fin:
    fin.readline()
    wordLst = []
    for line in fin:
        word = extract()
        wordLst.append(word)
    print (wordLst)
#prefix = "ea"