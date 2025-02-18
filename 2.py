import math
import sys

class Fraction:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю.")
        
        # Находим наибольший общий делитель (НОД) для сокращения дроби
        common_divisor = math.gcd(numerator, denominator)
        
        # Сокращаем дробь
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor
        
        # Если знаменатель отрицательный, делаем числитель отрицательным
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def __str__(self):
        if self.numerator % self.denominator == 0:
            return f"{self.numerator // self.denominator}"
        return f"{self.numerator}/{self.denominator}"
    
    def __abs__(self):
        return Fraction(abs(self.numerator), abs(self.denominator))
        
    def __repr__(self):
        if self.numerator % self.denominator == 0:
            return f"{self.numerator // self.denominator}"
        return f"{self.numerator}/{self.denominator}"
    
    def __neg__(self):
        cnt = 0
        if self.numerator < 0:
            cnt += 1
        if self.denominator < 0:
            cnt += 1
        if cnt % 2 == 0:
            return Fraction(-abs(self.numerator), abs(self.denominator))
        else:
            return Fraction(abs(self.numerator), abs(self.denominator))

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError("Нельзя делить на ноль.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        return self.numerator * other.denominator >= other.numerator * self.denominator

def my_print(t, par, matrixs):
    print(t)
    for i in range(t):
        print(par[i])
        for j in range(par[i][0]):
            print(matrixs[i][j])
    print()

def my_read(filename: str) -> list:
    data = []
    with open(filename, 'r') as file:
        lines = file.readlines()  # Вызываем метод readlines()
        for line in lines:
            # Обработка каждой строки (например, преобразование в числа)
            data.append(line.strip())  # Добавляем строку в список, убирая лишние пробелы и симв
        t = int(data[0])
        par = [] 
        matrixs = []
        accum = 0
        for i in range(t):
            m, n = map(int, data[i+1+accum].split())
            accum += m
            par.append((m, n))
            matrix = []
            for j in range(m):
                matrix.append([Fraction(int(x)) for x in data[j+2+i*(par[i][0]+1)].split()])
            matrixs.append(matrix)
    return t, par, matrixs

def swap(matrix, x, y):
    if x == y:
        return matrix
    t = matrix[x]
    matrix[x] = matrix[y]
    matrix[y] = t
    return matrix

def div(matrix, k, s, n):
    t = matrix[k][s]
    for i in range(s, n):
        matrix[k][i] /= t
    return matrix
    
def mx_idx(matrix, k, s, m):
    mx = 0
    idx = -1
    for i in range(k, m):
        t = abs(matrix[i][s])
        if mx < t:
            mx = t
            idx = i
    return idx

def null(matrix, idx, n):
    for i in range(n):
        if matrix[idx][i] != 0:
            return False
    return True

def f(matrix, k, s, m, n):
    for j in range(s+1, n):
        for i in range(m):
            if i == k: continue
            matrix[i][j] -= matrix[k][j]*matrix[i][s]
    return matrix

def print_answer(matrix, m, n):
    for i in range(m):
        print(f"x_{i+1} =", end=' ')
        print(f"{matrix[i][n-1]}", end=' ')
        for j in range(i):
            if matrix[i][j] > 0:
                print(f"- {matrix[i][j]}*x_{j+1}", end=' ')
            elif matrix[i][j] < 0:
                print(f"+ {-matrix[i][j]}*x_{j+1}", end=' ')
        for j in range(i+1, n-1):
            if matrix[i][j] > 0:
                print(f"- {matrix[i][j]}*x_{j+1}", end=' ')
            elif matrix[i][j] < 0:
                print(f"+ {-matrix[i][j]}*x_{j+1}", end=' ')
        print()
    print()

def print_matrix(matrix, m, n, i):
    print(f"Шаг номер {i}:")
    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()
    print()

def none(matrix, m, n):
    for i in range(m):
        flag = True
        for j in range(n-1):
            if matrix[i][j] != 0:
                flag = False
        if flag and matrix[i][n-1] != 0:
            return True
    return False

def PositiveRight(matrix, m, n):
    for i in range(m):
        if matrix[i][n-1] < 0
            matrix[i][n-1] *= -1
    return matrix

def SelectingAResolutionElement(matrix, m, n, s):
    idx = -1
    mn = max([max(x) for x in matrix])
    for i in range(m):
        t = matrix[i][s]/matrix[i][n-1]
        if t > 0 :
            if mn > t:
                mn = t
                idx = i
    return idx

def factorial(x):
    ret = 1
    for i in range(2, x+1):
        ret *= i
    return ret
   
def CombinationsWithoutRepetitions(r, n):
    ret = []
    start = [0]*r
    for i in range(r):
        start[i] = i
    ret.append(start)
    print(start)
    r-=1
    n-=1
    k = r
    p = k
    while start[0] != n-r:
        if start[r] != n:
            p = k
            start[r] += 1
        else:
            p -= 1
            start[p] += 1 
            for i in range(p+1, r+1):
                start[i] = start[i-1] + 1
        ret.append(start)
        print(start)
    return ret
      
def solve(m, n, matrix):
    r, s, k = m, 0, 0
    flag = False
    matrix = PositiveRight(matrix, m, n)
    while k < r:
        idx = SelectingAResolutionElement(matrix, m, n, s)
        if idx != -1:
            matrix = swap(matrix, idx, k)
            matrix = div(matrix, k, s, n)
            matrix = f(matrix, k, s, r, n)
            for i in range(r):
                if i == k: continue
                matrix[i][s] = Fraction(0)
            i = k+1
            while i < r:
                if null(matrix, i, n):
                    matrix.pop(i)
                    r-=1
                i += 1
            if k < r:
                k += 1
                s += 1
        else:
            s += 1
        # print_matrix(matrix, m, n, k)
        if none(matrix, r, n):
                flag = True
                break
    
    c = factorial(n-1)/(factorial(n-1-r)*factorial(r))
    combs = CombinationsWithoutRepetitions(r, n-1)
    idxs = [-1]*r
    answer = []
    
    for comb in combs:
        mns = []
        for x in comb:
            msn.append(SelectingAResolutionElement(matrix, m, n, x))
            flag = False
            for mn in mns:
                if mn == -1 or mns.count(mn) > 1:
                    flag = True
                    break
                else:
                    matrix = div(matrix, mn, x, n)
                    matrix = f(matrix, mn, x, r, n)
                    for i in range(r):
                        if i == mn: continue
                        matrix[i][s] = Fraction(0)
        if flag:
            print("решения нет")
        else:
            print(f"решение{comb}:")
        for x in comb:
            print(f"x{x} = {matrix[n-1]}")
        print()
    print()
        
    
    # if flag:
    #     print("Система не имеет решений:")
    # else:
    #     if m == r:
    #         print("Система имеет единственное решение:")
    #     elif r < m:
    #         print("Система имеет бесконечное множество решений:")
    #     print_answer(matrix, r, n)
    


def main():
    filename = 'input.txt'
    if len(sys.argv) == 2:
        filename = sys.argv[1]


    try:
        t, par, matrixs = my_read(filename)
        for i in range(t):
            print(f"Номер примера - {i+1}:")
            solve(par[i][0], par[i][1], matrixs[i])
            print()
        # my_print(t, par, matrixs)

    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден.")

if __name__ == "__main__":
    main()
