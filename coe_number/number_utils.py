def is_prime_list(numbers):
    for num in numbers:
        if num < 2:
            return False
        elif num == 2:
            return True
        for n in range(3, num):
            if num % n == 0:
                return False
    return True