def make_counter(start=0, step=1):
    count = start
    def counter():

        nonlocal count
        count += step
        return count 
    
    return counter

def make_accumulator(initial=0):
    count = initial 
    def accumulator(n):
        nonlocal count
        count += n 
        return count 
    
    return accumulator

def make_history_counter():
    
    count = 0
    lst = [] 

    def take():
        nonlocal count
        count += 1
        lst.append(count) 
       
    def history():
        return lst.copy()
    
    return take, history 

def make_adder():
    count = 0
    def adder(n):
        nonlocal count 
        count += n 
        return count
    
    def reset():
        nonlocal count 
        count = 0 
        return count
    return adder, reset 



def make_minmax_tracker():
    min_sum = None
    max_sum = None

    def tracer(n=None):
        nonlocal min_sum, max_sum

        if n is None:
            return min_sum, max_sum

        if min_sum is None: 
            min_sum = n
            max_sum = n
        else:
            if n < min_sum:
                min_sum = n
            if n > max_sum:
                max_sum = n

        return min_sum, max_sum

    return tracer

def make_two_way_counter():
    count = 0
    def up():
        nonlocal count
        count += 1
    def down():
        nonlocal count
        count -= 1
    def value():
        return count 
    
    return up, down, value 

    