'''
Write a recursive function that computes the length of a string. You cannot use
the len function while computing the length of the string.
'''

def rec_length(s):
    if s == '':
        return 0
    else:
        return 1 + rec_length(s[1:])  

'''
Write a recursive function that takes a string like abcdefgh and returns badcfehg.
Call this function swap since it swaps every two elements of the original string
'''
def swap(s):
    if not len(s):
        return ''
    elif len(s) == 2:
        return s[1] + s[0]
    else:
        n = len(s)
        return swap(s[0: n/2]) + swap(s[n/2: ])

def main():
    print(rec_length('hell'))
    print(swap('abcdefgh'))

if __name__ == '__main__':
    main()
