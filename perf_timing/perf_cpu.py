from time import sleep, perf_counter, process_time

# compare 'wall time' with actual 'CPU time'
wall0, cpu0 = perf_counter(), process_time() # assignment of more than one member

# we will use time just to sleep
sleep(5) # sleep for 5 seconds
print(  f'Wall time: {perf_counter()-wall0}' )
print(  f'CPU time: {process_time()-cpu0}' ) # often appear to be 0.0, below any chance of optimizing

