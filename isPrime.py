value = 13

primes = [2, 3]
current = primes[len(primes)-1]
isPrime = 0

while (current <= value):
    current = primes[len(primes)-1]

    for i in primes:
        if (current % i == 0):
            current+=1
            i = primes[0]
    primes.append(current)
    if (current == value):
        isPrime = 1;
        break;

if (isPrime):
    print(value, ' is prime')
else:
    print(value, ' is not prime')
