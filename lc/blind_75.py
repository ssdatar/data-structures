# O(N^2)
def longest_substring(s):
    answer = set()
    start = 0

    if not len(s):
        return ''

    if len(s) < 3:
        answer = s

    else:
        
        for i, c in enumerate(s):
            lookup = set()
            
            for j, l in enumerate(s[i:]):
                print('answer', answer)
                if l in lookup:
                    break
                else:
                    lookup.add(l)

            if len(answer) < len(lookup):
                answer = lookup

    return answer


# O(N)
def longest_substring(s):
    answer = ''
    start = 0
    max_length = 0

    if not len(s):
        return ''

    if len(s) < 3:
        answer = s

    lookup = {}

    for i, char in enumerate(s):
        if char in lookup and start <= lookup[char]:
            start = lookup[char] + 1
        else:
            max_length = max(max_length, i - start + 1)

        lookup[char] = 




def main():
    print(longest_substring('pwwkew'))


if __name__ == '__main__':
    main()