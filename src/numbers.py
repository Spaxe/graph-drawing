from math import sqrt
from collections import defaultdict

numbers = defaultdict(lambda x: factors(x))

def factors(n):    
    return set(reduce(list.__add__, 
                  ([i, n//i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0)))
