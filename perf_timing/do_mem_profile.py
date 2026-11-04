# here we carry out a profile of to_mem_profile
from to_mem_profile import CompareTechniques
import profiling.tracing # new in 3.15 recommended, improvements over cProfile

# we may also use a sampling profile (less interfering)
# python -m profiling.sampling run <filename>


if __name__ == '__main__':
    with profiling.tracing.Profile() as pr:
        words = ['one', 'two', 'three', 'four', 'five'] # a list is an ordinal mutable collection of any data type
        compare = CompareTechniques()
        compare.parse_list(words)
        url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
        compare.parse_url(url)
        # read the results and look for large time and memory usage
        # these are targets for optimization
        pr.print_stats()