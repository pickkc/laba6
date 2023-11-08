
import random

size1 = int(input("Введите размер матрицы M1: "))
size2 = int(input("Введите размер матрицы M2: "))

M1 = []

for i in range(size1):
    row = []
    for j in range(size1):
        row.append(0)
    M1.append(row)

for i in range(size1):
    for j in range(i + 1, size1):
        M1[i][j] = M1[j][i] = random.randint(0, 1)

lists = [[] for _ in range(size1)]
for i in range(size1):
    for j in range(size1):
        if M1[i][j] == 1:
            lists[i].append(j)
M2 = []
for i in range(size2):
    row = []
    for j in range(size2):
        row.append(0)
    M2.append(row)

for i in range(size2):
    for j in range(i + 1, size2):
        M2[i][j] = M2[j][i] = random.randint(0, 1)

print("Матрица смежности для G1: ")
for row in M1:
    print(row)

print("\nСписок смежности для M1: ")
for i, verticles in enumerate(lists):
    print(f"Вершина {i}: {verticles}")

print("\nМатрица смежности для G2: ")
for row in M2:
    print(row)

G_union = []
size_union = max(size1, size2)

for i in range(size_union):
    row = []
    for j in range(size_union):
        val1 = M1[i][j] if i < size1 and j < size1 else 0
        val2 = M2[i][j] if i < size2 and j < size2 else 0
        row.append(val1 or val2)
    G_union.append(row)

print("\nМатрица смежности для объединения графов G (G1 U G2): ")
for row in G_union:
    print(row)

G_intersection = []
size_intersection = min(size1, size2)

for i in range(size_intersection):
    row = []
    for j in range(size_intersection):
        row.append(M1[i][j] and M2[i][j])
    G_intersection.append(row)

print("\nМатрица смежности для пересечения графов G (G1 ? G2): ")
for row in G_intersection:
    print(row)

G_ring_sum = []
size_ring_sum = max(size1, size2)

for i in range(size_ring_sum):
    row = []
    for j in range(size_ring_sum):
        if i < size1 and j < size1:
            val1 = M1[i][j]
        else:
            val1 = 0

        if i < size2 and j < size2:
            val2 = M2[i][j]
        else:
            val2 = 0

        row.append(val1 ^ val2)
    G_ring_sum.append(row)

print("\nМатрица смежности для кольцевой суммы графов G (G1 ? G2): ")
for row in G_ring_sum:
    print(row)

dekart = []
size_product = size1 * size2

for i in range(size1 * size2):
    row = []
    for j in range(size1 * size2):
        row.append(0)
    dekart.append(row)

for i in range(size1):
    for j in range(size1):
        for k in range(size2):
            for l in range(size2):
                if M1[i][j] == 1 and M2[k][l] == 1:
                    dekart[i * size2 + k][j * size2 + l] = 1

print("\nМатрица смежности для декартова произведения графов G1 и G2:")
for row in dekart:
    print(row)

while True:
    print("1. Отождествление вершин")
    print("2. Стягивание ребра")
    print("3. Расщепление вершины")
    print("4. Завершить")
    choice = int(input("\nВыберите операцию для матрицы M1: "))

    if choice == 4:
        break
    elif choice == 1:
        v1 = int(input("Введите номер первой вершины для отождествления: "))
        v2 = int(input("Введите номер второй вершины для отождествления: "))
        if v1 < size1 and v2 < size1:
            size = len(M1)
            if v1 < size and v2 < size:
                for i in range(size):
                    if i != v2:
                        M1[v1][i] = M1[v1][i] or M1[v2][i]
                        M1[i][v1] = M1[i][v1] or M1[i][v2]

                M1[v1][v1] = 1

                new_size = size - 1
                new_matrix = [[0] * new_size for _ in range(new_size)]

                for i in range(size):
                    if i != v2:
                        for j in range(size):
                            if j != v2:
                                new_i = i if i < v2 else i - 1
                                new_j = j if j < v2 else j - 1
                                new_matrix[new_i][new_j] = M1[i][j]

                M1 = new_matrix
    elif choice == 2:
        v1 = int(input("Введите номер первой вершины: "))
        v2 = int(input("Введите номер второй вершины: "))
        if v1 < size1 and v2 < size1:
            size = len(M1)
            if v1 < size and v2 < size and M1[v1][v2] == 1:
                for i in range(size):
                    if i != v2:
                        M1[v1][i] = M1[v1][i] or M1[v2][i]
                        M1[i][v1] = M1[i][v1] or M1[i][v2]
                new_size = size - 1
                new_matrix = [[0] * new_size for _ in range(new_size)]

                for i in range(size):
                    if i != v2:
                        for j in range(size):
                            if j != v2:
                                new_i = i if i < v2 else i - 1
                                new_j = j if j < v2 else j - 1
                                new_matrix[new_i][new_j] = M1[i][j]

                for i in range(new_size):
                    new_matrix[i][i] = 0

                M1 = new_matrix
            else:
                print("Такого ребра не существует")
                continue
    elif choice == 3:
        v1 = int(input("Введите номер вершины для расщепления: "))
        if v1 < size1:
            size = len(M1)
            size += 1
            new_matrix = [[0] * size for _ in range(size)]

            for i in range(size - 1):
                for j in range(size - 1):
                    new_matrix[i][j] = M1[i][j]

            for i in range(size - 1):
                if M1[i][v1] == 1:
                    new_matrix[i][size - 1] = 1
                    new_matrix[size - 1][i] = 1

            M1 = new_matrix

print("Итоговая матрица M1: ")
for row in M1:
    print(row)

while True:
    print("1. Отождествление вершин")
    print("2. Стягивание ребра")
    print("3. Расщепление вершин")
    print("4. Завершить")
    choice = int(input("\nВыберите операцию для списка смежности M1:"))

    if choice == 4:
        break
    elif choice == 1:
        v1 = int(input("Введите номер первой вершины для отождествления: "))
        v2 = int(input("Введите номер второй вершины для отождествления: "))
        if v1 < size1 and v2 < size1:
            new_adj_list = list(set(lists[v1] + lists[v2]))
            if v2 not in lists[v1]:
                new_adj_list.append(v1)
            if M1[v1][v2] != 1:
                new_adj_list = [x for x in new_adj_list if x != v1]
            lists[v1] = new_adj_list
            for vertex in lists:
                if v2 in vertex:
                    vertex.remove(v2)
                for index, item in enumerate(vertex):
                    if item == v2:
                        vertex[index] = v1
            lists.pop(v2)
            size1 -= 1
    elif choice == 2:
        v1 = int(input("Введите номер первой вершины, соединенной ребром: "))
        v2 = int(input("Введите номер второй вершины, соединенной ребром: "))
        if v1 < size1 and v2 < size1:
            new_adj_list = list(set(lists[v1] + lists[v2]))
            if M1[v1][v2] == 1:
                new_adj_list = [x for x in new_adj_list if x != v1]
            lists[v1] = new_adj_list
            for vertex in lists:
                if v2 in vertex:
                    vertex.remove(v2)
                for index, item in enumerate(vertex):
                    if item == v2:
                        vertex[index] = v1
            lists.pop(v2)
            size1 -= 1

    elif choice == 3:
        v1 = int(input("Введите номер вершины для расщепления: "))
        if v1 < size1:
            new_vertex = size1
            lists.append([v1])
            for vertex in lists[v1]:
                lists[new_vertex].append(vertex)
                lists[vertex].append(new_vertex)
                lists[vertex].remove(v1)
            lists[v1].append(new_vertex)
            size1 += 1

print("Итоговый список смежности для M1:")
for i, vertices in enumerate(lists):
    print(f"Вершина {i}: {vertices}")
