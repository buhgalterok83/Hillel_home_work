from typing import List

# Абстрактний клас стратегії сортування
class SortStrategy:
    def sort(self, data: List[int]) -> List[int]:
        raise NotImplementedError()

# Конкретна стратегія сортування "Сортування бульбашкою"
class BubbleSortStrategy(SortStrategy):
    def sort(self, data: List[int]) -> List[int]:
        # Реалізація сортування бульбашкою
        sorted_data = data.copy()
        n = len(sorted_data)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if sorted_data[j] > sorted_data[j + 1]:
                    sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]
        return sorted_data

# Конкретна стратегія сортування "Сортування вибором"
class SelectionSortStrategy(SortStrategy):
    def sort(self, data: List[int]) -> List[int]:
        # Реалізація сортування вибором
        sorted_data = data.copy()
        n = len(sorted_data)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if sorted_data[j] < sorted_data[min_idx]:
                    min_idx = j
            sorted_data[i], sorted_data[min_idx] = sorted_data[min_idx], sorted_data[i]
        return sorted_data

# Клієнтський клас, що використовує стратегію сортування
class SortClient:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self.strategy = strategy

    def sort_data(self, data: List[int]) -> List[int]:
        return self.strategy.sort(data)

# Приклад використання
data = [5, 2, 8, 1, 9]

# Створення клієнтського об'єкта з початковою стратегією сортування бульбашкою
client = SortClient(BubbleSortStrategy())

# Сортування даних з поточною стратегією
sorted_data = client.sort_data(data)
print("Сортування бульбашкою:", sorted_data)

# Зміна стратегії на сортування вибором
client.set_strategy(SelectionSortStrategy())

# Повторне сортування даних з новою стратегією
sorted_data = client.sort_data(data)
print("Сортування вибором:", sorted_data)
