def mod_exp(x, y, N):
    if y == 0:      # Base Case! If y is 0...
        return 1    # return 1
    z = mod_exp(x, (y // 2), N)     # Recursively call mod_exp with half the exponent O(n)
    if y % 2 == 0:      # If the exponent is even...
        return (z ** 2) % N     # Return z^2 % N
    else:   # Otherwise the exponent is odd and...
        return (x * (z**2)) % N     # ... We return x * z^2 % N


def fprobability(k):
    return 1 - (1 / (2 ** k))


def mprobability(k):
    return 1 - (1 / (4 ** k))


def fermat(N, k):
    for i in range(k):      # Runs through k trial runs O(k)
        a = random.randint(1, N - 1)    # Generate a random integer within 1 <= a < N. A new integer is generated every trial
        if mod_exp(a, N - 1, N) != 1:   # If mod_exp doesn't evaluate to 1... O(n)
            return 'composite'      # ... Then it has to be composite
        return 'prime'      # Otherwise it's prime


def miller_rabin(N, k):
    for i in range(k):  # Runs through k trial runs
        exp = N - 1     # A variable to hold and keep track of the exponent. It resets with every trial
        a = random.randint(1, N - 1)    # Generate a random integer within 1 <= a < N. A new integer is generated every trial
        if N % 2 == 0 and N > 2:    # If even and greater than 2 (since 2 is prime), automatic composite
            return 'composite'
        while exp % 2 == 0:     # While loop to run through all the possible even square roots
            result = mod_exp(a, exp, N)     # Gets a result from mod_exp using a, exp, and N
            if result == 1:     # If result ends up being 1, then we still test
                exp = exp // 2  # Since it passed (for now), divide the exponent by 2 and run again
            elif result == N-1:     # Otherwise if result is -1, still technically valid, but its gets weird, so break
                break   # break from the while and get a new random.
            else:   # Otherwise it's something super totally wrong and isn't prime
                return 'composite'  # It's composite!
    return 'prime'  # If it reaches here, the number passed all the prime tests and must therefore be prime
