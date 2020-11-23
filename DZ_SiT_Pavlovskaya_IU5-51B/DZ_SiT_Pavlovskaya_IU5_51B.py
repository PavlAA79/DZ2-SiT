from math import factorial
from prettytable import PrettyTable
from sympy.utilities.iterables import multiset_permutations

#Функция, реализующая наложение вектора ошибки
def ErrorOverlay(v1, e):
    res = [0]*15
    for i in range(0,15):
        res[i]=e[i]^v1[i]
    return res

#Функция, реализующая вычисление синдрома ошибки
def ErrorSyndrom(v2):
    h = [0]*4
    h[0] = v2[7]^v2[6]^v2[5]^v2[4]^v2[3]^v2[2]^v2[1]^v2[0] 
    h[1] = v2[11]^v2[10]^v2[9]^v2[8]^v2[3]^v2[2]^v2[1]^v2[0]
    h[2] = v2[13]^v2[12]^v2[9]^v2[8]^v2[5]^v2[4]^v2[1]^v2[0]
    h[3] = v2[14]^v2[12]^v2[10]^v2[8]^v2[6]^v2[4]^v2[2]^v2[0]
    return h

#Функция, реализующая кодирование исходной кодовой последовательности
def Coding(v):
    v1 = [0]*15
    v1[0]=v[0]
    v1[1]=v[1]
    v1[2]=v[2]
    v1[3]=v[3]
    v1[4]=v[4]
    v1[5]=v[5]
    v1[6]=v[6]
    v1[8]=v[7]
    v1[9]=v[8]
    v1[10]=v[9]
    v1[12]=v[10]
    #Определение значений проверочных разрядов:
    v1[14]=v1[12]^v1[10]^v1[8]^v1[6]^v1[4]^v1[2]^v1[0]
    v1[13]=v1[12]^v1[9]^v1[8]^v1[5]^v1[4]^v1[1]^v1[0]
    v1[11]=v1[10]^v1[9]^v1[8]^v1[3]^v1[2]^v1[1]^v1[0]
    v1[7]=v1[6]^v1[5]^v1[4]^v1[3]^v1[2]^v1[1]^v1[0]
    return v1

#Функция, реализующая декодирование полученной кодовой последовательности
def Decoding(v2):
    v2.pop(14)
    v2.pop(13)
    v2.pop(11)
    v2.pop(7)
    return v2

#Функция, реализующая исправление ошибки
def ErrorFix(v2,h):
    er_index = ((h[3]*1 + h[2]*2 + h[1]*4 + h[0]*8) - 1)
    v2[14-er_index] = v2[14-er_index]^1
    return v2


def CreateTable(v1):
    e1 = [0]*15
    h = [0]*4
    C0 = [0]*15
    n0 = [0]*15
    Combinations = [0]*15
    all_errors = []
    for i in range (0,14):
        e1[i] = 1
        all_errors = list(multiset_permutations(e1))
        for j in range (len(all_errors)):
            #Наложение вектора ошибки
            v2 = ErrorOverlay(v1, all_errors[j])
            #Вычисление синдрома ошибки
            h = ErrorSyndrom(v2)
            if (h != [0,0,0,0]):
                n0[i] = n0[i] + 1
        #Определение обнаруживающей способности     
        Combinations[i]=int(factorial(15)/(factorial(i+1)*factorial(15-(i+1))))
        C0[i] = n0[i]/Combinations[i]
        C0[i] =float('{:.7f}'.format(C0[i]))
    Combinations[14]=int(factorial(15)/(factorial(15)*factorial(0)))
    i1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    table = PrettyTable()

    table.add_column("i", i1)
    table.add_column("n0", n0)  
    table.add_column("Сочетания", Combinations)  
    table.add_column("C0", C0)  

    return table

def main():
    print("ИУ5-51Б Павловская А.А. Вариант 15")

    #Решение задачи варианта 15
    print("Исходный вектор:")
    v = [1,0,1,0,1,0,1,0,1,0,0]
    print("v =",v)
    print("Вектор в коде Хэмиинга:")
    v1 = Coding(v)
    print("v1 =",v1)
    #Наложение вектора ошибки кратности 1
    e = [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
    print("Результат воздействия однократной ошибки:")
    v2 = ErrorOverlay(v1,e)
    print("v2 =",v2)
    #Вычисление синдрома ошибки
    h = ErrorSyndrom(v2)
    print("Синдром ошибки:")
    print("h =",h)

    print("Исправление ошибки")
    v2 = ErrorFix(v2,h)
    print("v2 =",v2)

    print("Декодирование кодового вектора")
    v2 = Decoding(v2)
    print("v2 =",v2)
    
    print("Итоговая таблица:")
    #Создание итоговой таблицы вычисления обнаруживающей способности кода для ошибок всех кратностей
    table = CreateTable(v1)
    print(table)
    
if __name__ == "__main__":
    main()
