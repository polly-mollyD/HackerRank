# the first exercise

def print_hello(n):
    for _ in range(n):
        print("Hello World!")


print_hello(5)





# the second exercise

def sum_all_between(a, b):
    sum = 0
    for i in range(a, b+1):
        sum += i
    return sum


if sum_all_between(1, 2) == 3 and sum_all_between(4, 10) == 49 and sum_all_between(1, 100) == 5050:
    print("Correct!")
else:
    print("Incorrect!")






# the third exercise

def sum_squares_in_list(l):
    sum = 0
    for i in l:
        sum += i ** 2
    return sum


if sum_squares_in_list([1, 2]) == 5 and sum_squares_in_list([2, 4, 5, 6]) == 81 and sum_squares_in_list(
        [-2, -3, 10]) == 113:
    print("Correct!")
else:
    print("Incorrect!")






# the forth exercise

def max(l):
    a = l[0]
    for x in l:
        if x > a:
            a = x
    return a

if max([1, 2]) == 2 and max([2, 40, 5, 6]) == 40 and max([-2, -3, -10]) == -2:
    print("Correct!")
else:
    print("Incorrect!")






# the fifth exercise


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

if is_prime(3) and not is_prime(4) and is_prime(5) and not is_prime(6) and is_prime(7) and not is_prime(8) and not is_prime(9) and not is_prime(10) and is_prime(11) and not is_prime(12) and is_prime(13) and not is_prime(14):
    print("Correct!")
else:
    print("Incorrect!")






# the sixth exercise

def grade(n):
    if n >= 90:
        return 5
    elif 70 <= n:
        return 4
    elif 50 <= n:
        return 3
    else:
        return 2


if grade(91) == 5 and grade(90) == 5 and grade(80) == 4 and grade(70) == 4 and grade(60) == 3 and grade(
        50) == 3 and grade(49) == 2:
    print("Correct!")
else:
    print("Incorrect!")






# the seventh exercise

def is_even(n):
    return n % 2 == 0

if is_even(1234) and not is_even(12357):
    print("Correct!")
else:
    print("Incorrect")



# the eighth exercise

def is_odd(n):
    return not is_even(n)

if not is_odd(1234) and is_odd(12357):
    print("Correct!")
else:
    print("Incorrect")




#9


def is_rightangled(a, b, c):
    zero_val = c**2 - (a**2 + b**2)
    if -0.001 <= zero_val <= 0.001:
        return True
    else:
        return False

if is_rightangled(1.5, 2.0, 2.5) and not is_rightangled(4.0, 8.0, 16.0) and is_rightangled(4.1, 8.2, 9.167878707) and is_rightangled(4.1, 8.2, 9.16787) and not is_rightangled(4.1, 8.2, 9.168) and is_rightangled(0.5, 0.4, 0.64031):
    print("Correct!")
else:
    print("Incorrect!")



# 10


def is_rightangled_better(a, b, c):
    edges = [a, b, c]
    edges.sort()
    return is_rightangled(edges[0], edges[1], edges[2])

if is_rightangled_better(1.5, 2.5, 2.0) and not is_rightangled_better(16.0, 8.0, 4.0) and is_rightangled_better(9.167878707, 4.1, 8.2) and is_rightangled_better(4.1, 8.2, 9.16787) and not is_rightangled_better(4.1, 9.168, 8.2) and is_rightangled_better(0.4, 0.5, 0.64031):
    print("Correct!")
else:
    print("Incorrect!")


# 11

def my_sqrt(n, i):
    oldguess = n/2
    for j in range(i):
        new_guess = (1/2) * (oldguess + (n/oldguess))
    return new_guess

print("Sqrt of 2 is", my_sqrt(2, 100))
print("Sqrt of 3 is", my_sqrt(3, 100))