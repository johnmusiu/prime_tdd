# def prime(num):
#     if num < 0:
#         return "error negative num given"
#     results = []
#     for i in range (2, num+1):
#         if isPrime(i):
#             results.append(i)
    
#     return results

def isPrime(number):
    # if number in 
    for i in range(2, number):
        if number % i == 0:
            return False
    return True 

def prime_tdd(number):
    """
    input 
        number(int) -> this is a positive number

    outputs:
        results(list) -> list of numbers
    """
    if not isinstance(number, int):
        return "Unexpected non integer input"

    if number < 0:
        return "error"

    results = []
    for i in range(2, number+1):
        if isPrime(i):
            results.append(i)
    
    return results
