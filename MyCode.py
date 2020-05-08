pos = -1

def search(list,n):
    i = 0
    while i < len(list):
        if list [i] == n:
            globals() ['pos'] = i
            return True
        i += 1
    return False

list = [5,8,6,4,2,9]

n = 9
if search(list,n):
    print("Found and Position is: ",pos)
else:
    print("Not Found")