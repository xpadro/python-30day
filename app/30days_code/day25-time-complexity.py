def find_prime(data):
    is_prime = True

    if data != 2 and data % 2 == 0 or data < 2:
        is_prime = False
    elif data != 2:
        current = 0

        for current in range(3, data, 2):
            if current*current > data:
                break
            
            if data % current == 0:
                is_prime = False
        
    if is_prime:
        print("Prime")
    else:
        print("Not prime")


T=int(input())

for i in range(T):
    data=int(input())
    find_prime(data)


