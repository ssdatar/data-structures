def permute(s, prefix = ''):
    if len(s) == 0:
        print(prefix)
    else:
        for i in range(len(s)):
            # print('Now on:', s[i])
            this = s[i]
            rest = s[0:i] + s[i+1: ]
            permute(rest, prefix + this)


answer = set()

def combine(s, k, prefix = ''):
    if len(s) == 0:
        answer.add(prefix)  
        print(answer)
        
    else:
        for i in range(len(s)):
            print(i)
            this = s[i]
            rest = s[0:i] + s[i+1:]
            print(rest, prefix+this)
            # combine(rest, k, (prefix + this))


combine('GOOGLE', 3)

# print('GOOGLE'[0:0], 'GOOGLE'[1:3])

# combine('OO', 'G')
#     combine('O', 'GO')
#         combine('O', 'GO')