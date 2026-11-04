# here we carry out similar operations 
# elsewhere we examine a memory profile of these ops

import requests

class CompareTechniques:
    def parse_list(self, word_list):
        '''open a text file and write a list into it'''
        # 'a' will append to a file 'w' will (over)write a file
        with open('word_list.txt', 'wt') as fout:
            for word in word_list:
                fout.writelines(f'{word}\n') # we choose to add a new line character

    def parse_url(self, word_url):
        '''access a remote API, retrieve the contents and write to a text file'''
        response = requests.get(word_url) # this returns text
        words = response.text  # read the retrieved text
        with open('url_list.txt', 'wt') as fout:
            # the URL returns a list of words, so no need ot add new line characters'
            fout.writelines(words)

def main():
    ''''''
    words = ['one', 'two', 'three', 'four', 'five'] # a list is an ordinal mutable collection of any data type
    compare = CompareTechniques()
    compare.parse_list(words)
    url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
    compare.parse_url(url)

if __name__ == '__main__':
    '''exercise the module'''
    main()