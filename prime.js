const primes = [2, 3, 5, 7];
let numPrime = 100000000;
let x = 0;

while (x < numPrime) {
  let current = primes[primes.length - 1] + 1;

  for (let i = 0; i < primes.length; i++) {
    if (current % primes[i] === 0) {
      current++;
      i = -1;
    }
  }
  primes.push(current);
  x++;
}

console.log(primes);
