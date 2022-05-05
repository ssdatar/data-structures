
def is_unique(s):
    lookup = {}
    
    for char in s:
        if not lookup.get(char):
            lookup[char] = 1
        else:
            return False

    return True


def is_unique_2(s):
    return len(s) == len(set(s))


def main():
    # print(is_unique('hello'))
    # print(is_unique('hello'))
    print(is_unique_2('mask'))

if __name__ == '__main__':
    main()