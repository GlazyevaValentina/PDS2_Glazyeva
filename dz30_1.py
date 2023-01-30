
# Завдання1
# Написати клас для створення і роботи з хеш-таблицями.
# Клас повинен містити наступні функції:
# - створення хеш-таблиці заданої довжини;
# - пошук, додавання і видалення нових елементів;
# - друкування хеш-таблиці;
# - виправлення колізій;

class HashTable:

    def __init__(self, lenth : int):
        self.lenth = lenth
        self.hash_table = [None] * lenth

    def __str__(self):
        return ''.join(map(str, self.hash_table))

    def __hash_func(self, key):
        return key % self.lenth

# Searching element

    def search(self, key):
        index = self.__hash_func(key)
        if self.hash_table[index]:
            return self.hash_table[index][self.hash_table[index].index(key) + 1]
        else:
            return None

# Adding element

    def add(self, key : int, data):
        index = self.__hash_func(key)
        if not self.hash_table[index]:
            self.hash_table[index] = [key, data]
        else:
            self.hash_table[index].extend([key,data])

# Removing element

    def remove(self, key: int, data):
        index = self.__hash_func(key)
        result = self.search(key)
        if result:
            if data in self.hash_table[index]:
                self.hash_table[index].remove(key)
                self.hash_table[index].remove(data)
            else:
                error = ValueError(f"There is no \'{data}\' data with the key ({key}).")
                raise error
        else:
            error = KeyError(f"There is no key ({key}) in the hash table.")
            raise error


    def print(self):
         for i in self.hash_table:
            if i is not None:
                print(f'{i[0]} : {i[1]}')
            else:
                print(f'{None} : {None}')


table = HashTable(10)
table.print()
print("_______________")
table.add(1, "London")
table.add(5, "Dublin")
table.add(8, "Paris")
table.add(2, "Berlin")
table.add(7, "Rome")
table.add(6, "Kyiv")
table.print()
table.remove(2, "Berlin")
table.remove(7, "Rome")
print(table)
print("----------------")
print(table.search(3))
print(table.search(5))
print(table.search(6))