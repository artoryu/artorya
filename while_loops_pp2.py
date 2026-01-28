i = int(input())
while i < 6:
    print(i)
    i += 1

n = int(input("enter the number:"))
while n != 0:
    print(f"You entered {n}")
n = int(input('enter a number'))

print("The end")

x = int(input("enter ur age"))
while x >= 18:
    print('u can vote')

    y = int(input('enter the number'))
    while y < 6:
        print(y)
        if y == 3:
            break
        i += 1

        i = 0
        while i < 10:
            i += 1
            if i == 3:
                continue
            print(i)

            i = 1
            while i < 6:
               print(i)
            i += 1
        else:
            print('i is no longer more than 6')