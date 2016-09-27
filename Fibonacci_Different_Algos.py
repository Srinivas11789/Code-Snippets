# Fibonacci Series
# 0 1 1 2 3 5


# Iteration Method
def iteration(number):
 first = 0
 second = 1 
 print "%d %d" % (int(first),int(second)),
 for i in range(1,int(number)):
    next = int(first) + int(second)
    print "%d" % (int(next)),
    swap = first
    first = second
    second = next

# Recursion Method
def recursion(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return recursion(number - 1) + recursion(number - 2)

# Memoized Version of the Recursion Function

def memo(n):
   if n in range(len(series)):
     return series[n]
   else:
     element = memo(n-1) + memo(n-2)
     series.append(element)
     return element
           
    
# MAIN

number = int(raw_input("Enter the total number: "))

#### Iteration Call
#iteration(number)

#### Recursion Call
#for i in range(1,number):
#    c = recursion(i)
#    print c,

#### Memoized Call
series = [0,1]
memo(number)
print(series)
    
