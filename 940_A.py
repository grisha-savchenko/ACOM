import heapq

import bisect

# from collections import Counter
# import math


def find_k_smallest_elements(arr, k):
    heap = []
    
    for element in arr:
        if len(heap) < k:
            heapq.heappush(heap, element)
        else:
            if element < heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, element)
    
    return heap

def find_k_largest_elements(arr, k):
    heap = []
    
    for element in arr:
        if len(heap) < k:
            heapq.heappush(heap, -element)
        else:
            if element > -heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, -element)
    
    return [-x for x in heap]

def find_longest_sequences(arr):
    max_positive_sum = 0
    max_negative_sum = 0
    current_positive_sum = 0
    current_negative_sum = 0
    max_positive_length = 0
    max_negative_length = 0
    current_positive_length = 0
    current_negative_length = 0

    for num in arr:
        if num == 1:
            # Работаем с положительными числами (1)
            current_positive_sum += 1
            current_positive_length += 1

            # Сбрасываем отрицательную последовательность
            current_negative_sum = 0
            current_negative_length = 0

            # Обновляем максимальную положительную последовательность
            if current_positive_length > max_positive_length:
                max_positive_length = current_positive_length
                max_positive_sum = current_positive_sum
            elif current_positive_length == max_positive_length:
                max_positive_sum = max(max_positive_sum, current_positive_sum)

        elif num == -1:
            # Работаем с отрицательными числами (-1)
            current_negative_sum += -1
            current_negative_length += 1

            # Сбрасываем положительную последовательность
            current_positive_sum = 0
            current_positive_length = 0

            # Обновляем максимальную отрицательную последовательность
            if current_negative_length > max_negative_length:
                max_negative_length = current_negative_length
                max_negative_sum = current_negative_sum
            elif current_negative_length == max_negative_length:
                max_negative_sum = max(max_negative_sum, current_negative_sum)

        elif num == 0:
            continue
        else:
            # Если элемент отличается от 1 или -1, обнуляем текущие суммы
            current_positive_sum = 0
            current_positive_length = 0
            current_negative_sum = 0
            current_negative_length = 0

    return max_positive_sum, max_negative_sum


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Добавляет элемент в стек."""
        self.items.append(item)

    def pop(self):
        """Удаляет и возвращает верхний элемент стека."""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Попытка удалить элемент из пустого стека")

    def peek(self):
        """Возвращает верхний элемент стека без удаления."""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Попытка получить элемент из пустого стека")

    def is_empty(self):
        """Проверяет, пуст ли стек."""
        return len(self.items) == 0

    def size(self):
        """Возвращает количество элементов в стеке."""
        return len(self.items)

    def __str__(self):
        return str(self.items)

def solve():
    
    n = int(input())

    # n, l, r = map(int, input().split())

    w = list(map(int, input().split()))

    tree = {x+1:[] for x in range(n-1)}

    a = []

    for i in range(n-1):
        t1, t2 = map(int, input().split())
        a.append((t1, t2))
        tree[t1].append(t2)

    # print(tree)
    
    
    max_value = max(w)  
    max_indices = [index + 1 for index, value in enumerate(w) if value == max_value]
    print(max_indices)
    mxs = []
    for item in max_indices:
        chain = []
        for t1, t2 in a:
            if t2 == item:
                chain.append(t2)
                item = t1
        print(chain)
        mx = -1
        idx = -1
        for i in range(n):
            if not( i in chain):
                if mx < w[i]:
                    mx = w[i]
                    idx = i
        print(mx)
        return
        mxs.append(mx)
    



            


    



t = int(input())

for _ in range(t):
    solve()