import time

# compare techniwues to find most efficient

text = '''Aaronsburg
Aaronson
AARP
aarrgh
aarrghh
Aaru
AAS
A'asia
aasvogel
aasvogels
AAU
AAUP
AAUW
AAVSO
AAX
A-axes
A-axis
AB
ab-
ABA
Ababa
Ababdeh
Ababua
abac
abaca
abacay
abacas
abacate
abacaxi
abaci
abacinate
abacination
abacisci
abaciscus
abacist'''

def writeText():
    global text # we now have access to the long text string
    with open('words.txt', 'at') as fout:
        fout.write(text)

def readText():
    with open('words.txt', 'rt') as fin:
        # fin.read() # read all the text into one string (including newlines)
        words_list = fin.readlines() # read all the text into a list of strings (for each new line)
    return words_list

def fnA():
    '''this function takes each word and makes it uppercase in a loop'''
    s = readText() # we now have a long list of words
    Upper = []
    for _ in s:
        Upper.append( _.upper() )
    return Upper

def fnB():
    '''this function takes each word and makes it uppercase using map'''
    s = readText() # we now have a long list of words
    Upper = list( map( str.upper, s ) ) # map will apply a given function to each member of a collection
    return Upper


if __name__ == '__main__':
    '''measure both function times'''
    # writeText()
    start1 = time.perf_counter()
    start1_ns = time.perf_counter_ns() # nanoseconds
    fnA()
    elapsed1 = time.perf_counter()
    elapsed1_ns = time.perf_counter_ns()
    print(f'Operation A took {elapsed1-start1} sec, or {elapsed1_ns-start1_ns} nanosec')

    start2 = time.perf_counter()
    start2_ns = time.perf_counter_ns() # nanoseconds
    fnB()
    elapsed2 = time.perf_counter()
    elapsed2_ns = time.perf_counter_ns()
    print(f'Operation B took {elapsed2-start2} sec, or {elapsed2_ns-start2_ns} nanosec')