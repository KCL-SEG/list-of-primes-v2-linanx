"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError(f"Number of primes {number_of_primes}: should have been greater than 0.")

    list = []
    index = 2
    while len(list) < number_of_primes:
        if len(list) == 0:
            list.append(index)
        else:
            for p in list:
                if index % p == 0:
                    break
            else:
                list.append(index)
        index += 1
    return list
