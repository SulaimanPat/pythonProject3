from random import randint, choice

list_number=[]
for i in range(10):
    list_number.append(randint(0,100))
def bubble_sort(list_number):
    n=len(list_number)
    for i in range(n-1):
        for a in range(0, n-i-1):
            if list_number[a]>list_number[a+1]:
                list_number[a],list_number[a+1]=list_number[a+1],list_number[a]
    return list_number


bubble_sort(list_number)
print(f'Отсортированный список: {list_number}')
searched_number=int(input("Введите число: "))
def binary_search(val, a):
    n=len(a)
    first=0
    last=n-1
    while True:
        if first<last:
            middle=(first+last)//2
            if val==a[middle]:
                first=middle
                last=first
                pos=middle
                print(f"Элемент найден, его индекс: {pos}")
                break
            elif val>a[middle]:
                first=middle
            else:
                last=middle-1
        else:
            print("Элемент не найден")
            break

binary_search(searched_number, list_number)