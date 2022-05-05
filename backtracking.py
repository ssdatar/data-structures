chosen = []

def sublists(arr, rem = []):
    if len(arr) == 0:
        print(rem)
    else:
        current = arr[0]
        arr.pop(0)

        # Include tree with this person
        chosen.append(current)
        sublists(arr, chosen)

        # Exclude this person in choices
        chosen.remove(current)
        sublists(arr, chosen)


sublists(['jane', 'bob', 'matt', 'sara'])

