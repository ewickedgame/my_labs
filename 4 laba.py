//////////////Задача1//////////
uslov1 = [12, 1, 4, 8, 554, 87, 12, 90]
print('Условие 1 задачи: ',uslov1)
res1 = []

def fun1 (list):
    k = len(list)
    for i in range(k):
        if i%2 == 0:
            res1.append( list[i] )
    print('Ответ ',res1)

fun1(uslov1)
print()


//////////////Задача1/////////
uslov2 = [1,5,2,7,9,1,2,4,6]
print('Условие 2 задачи: ',uslov2)
res2= []

def fun2 (list):
    k = len(list)
    for i in range(1,k):
        if list[i]>list[i-1]:
            res2.append( list[i])
    print('Ответ ',res2)

fun2(uslov2)
print()

//////////////Задача3///////////
uslov3 = [67,2,1,98,3,2,0]
print('Условие 3 задачи: ',uslov3)

def fun3 (list):
    maxel = list.index(max(list))
    minel = list.index(min(list))
    list[maxel],list[minel]=list[minel],list[maxel]
    print('Ответ ', uslov3)

fun3(uslov3)
print()



//////////////Задача4///////////
uslov4={1:"библиотека1",2:"библиотека2",3:"библиотека3"}
klch=int(input('Введите ключ(от 1 до 3): '))

def  fun4(dictionary):
    res4=dictionary.get(klch)
    print("Ответ ", res4)

fun4(uslov4)
print()
