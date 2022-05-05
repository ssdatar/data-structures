def reverse(lst):
    if not len(lst):
        return []
    else:
        return reverse(lst[1:]) + lst[0:1]

def revString(s):
    if not len(s):
        return ''
    else:
        return revString(s[1:]) + s[0:1]

# [1, 2, 3, 4, 5, 6]
def nested_add(lst):
    total = 0

    # # base case
    # for n in lst:
    #     if type(n) == list:
    #         total += nested_add(n)
    #     else:
    #         total += n

    # return total

    if type(lst) != list:
        return lst

    elif not len(lst):
        return 0
    else:
        return nested_add(lst[0]) + nested_add(lst[1:])

    # if len(lst) == 1:
    #     return lst[0]

    # else:
    #     # recursive case
    #     return nested_add(lst[0:1]) + nested_add(lst[1:])


cache = {}

def factorial(n):
    if n in cache:
        return n

    elif n == 0 or n == 1:
        return 1
    else:
        x = n * factorial(n - 1)
        cache[n] = x
        return x


def main():
    # print(reverse([1, 2, 3, 4]))
    # print(revString("hello"))
    # print(factorial(5))
    # print(nested_add([1, 2, 3, 4, 5, 6]))
    print(nested_add([[[[[[[[[5]]]]]]]]]))
    print(nested_add([1, 2, 3, 4, 5, [6, 7, 8], 9, [[10, 11], 13, [14]]]))

if __name__ == '__main__':
    main()