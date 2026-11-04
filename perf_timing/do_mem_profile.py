# here we carry out a profile of to_mem_profile
from to_mem_profile import CompareTechniques
import profiling # new in 3.15

if __name__ == '__main__':
    with profiling.sampling.Profile() as pr:
        words = ['one', 'two', 'three', 'four', 'five'] # a list is an ordinal mutable collection of any data type
        compare = CompareTechniques()
        compare.parse_list(words)
        url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
        compare.parse_url(url)
        pr.print_stats()
