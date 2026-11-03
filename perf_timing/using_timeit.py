# previously timeit was recommended over time for accuracy 
# Now we have perf_counter etc. time is again recommended
import timeit

statement = "sum(range(100_000))"
iteration = 1000
total = timeit.timeit( statement, number=iteration )

print(f'Total time: {total} sec for {iteration} runs')
print(f'Per run mean: {total/iteration} sec')