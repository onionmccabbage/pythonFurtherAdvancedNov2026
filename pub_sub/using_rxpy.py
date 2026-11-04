# may need to pip isntall reacticex (RxPY)
from reactivex import of, operators as op

# we can make ANY sequence into an asynch stream od data points 
source = of ('alpha', 'beta', 'gamma', 'delta', 'epsilon') # a tuple

source.subscribe( lambda value: print(f'Received: {value}') )
