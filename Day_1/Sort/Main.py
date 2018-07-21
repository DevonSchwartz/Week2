import time
tic = time.time()



def srt(lst):

    for i in range(1,len(lst)):

        key = lst[i]

        j = i - 1

        while j >= 0 and lst[j] > key:
            lst[j+1] = lst[j]
            j -= 1

        lst[j+1] = key

    return lst

def search(lst, number):
    count = 0
    for i in lst:
        if int(i) == int(number):
            return (count + 1)
        elif i != number:
            count +=1
    return - 1

def factorial(n):
    total = 1
    for i in range(1,n+1):
        total = total * i
    return total





lst = input("Input a list (separate with a comma). If no list, press 'enter' to continue: ")
Choice = input("Press 's' to sort 'x' to search, or 'f' to factorial: ")
lst = lst.split(",")
if Choice == 's':
    print (srt(lst))
elif Choice == 'x':
    number = eval(input("What number would you like to find the position of?: "))
    print (search(lst, number))
elif Choice == 'f':
    n = eval(input("What number would you like to factorial?: "))
    print (factorial(n))
toc = time.time()
print (str((toc - tic)) + "miliseconds")
