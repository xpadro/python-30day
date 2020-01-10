'''
    Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
    You will then be given an unknown number of names to query your phone book for. For each name queried, 
    print the associated entry from your phone book on a new line in the form name=phoneNumber; 
    if an entry for name is not found, print Not found instead.

    Input

    - The first line contains an integer, n, denoting the number of entries in the phone book.
    - Each of the n subsequent lines describes an entry in the form of 2 space-separated values on a single line (name phone)
    - After the n lines, there are an unknown number of lines of queries. Each line contains a name to look up
'''

phones = {}

def addToDictionary(name, phone):
    phones[name] = phone


def getFromDictionary(name):
    return phones.get(name, "Not found")


n = int(input())

for i in range(int(n)):
    name, phone = input().split()
    addToDictionary(name, phone)

    
x = input()
while (len(x) > 0):
    result = getFromDictionary(x)
    if (result == "Not found"):
        print(result)
    else:
        print(x + "=" + result)
    
    x = input()
