import random
import copy
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_grid(size):
  """Создает пустую сетку заданного размера."""
  grid = []
  for _ in range(size):
    row = [0] * size
    grid.append(row)
  return grid

def initialize_grid(grid, density):
  """Инициализирует сетку случайными живыми клетками с заданной плотностью."""
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if random.random() < density:
        grid[i][j] = 1

def count_neighbors(grid, row, col):
  """Подсчитывает количество живых соседей для клетки."""
  size = len(grid)
  count = 0
  for i in range(row - 1, row + 2):
    for j in range(col - 1, col + 2):
      if 0 <= i < size and 0 <= j < size and (i != row or j != col):
        count += grid[i][j]
  return count

def update_grid(grid):
  """Обновляет сетку по правилам игры "Жизнь"."""
  new_grid = copy.deepcopy(grid)
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      neighbors = count_neighbors(grid, i, j)
      if grid[i][j] == 0:  # Проверяем, является ли клетка мертвой
        if neighbors in [3, 4]:  # Рождение при 3 или 4 соседях
          new_grid[i][j] = 1
      else:  # Правила для живых клеток остаются прежними
        if neighbors < 1 or neighbors > 7:
          new_grid[i][j] = 0
  return new_grid

def animate(frame_num, img, grid):
  """Функция для анимации, которая обновляет изображение в каждом кадре."""
  global global_grid  # Объявляем, что мы будем использовать глобальную переменную 'global_grid'
  global_grid = update_grid(global_grid)  # Обновляем глобальную сетку
  img.set_data(global_grid)  # Используем глобальную сетку для обновления изображения
  return img,

def main():
  """Основная функция."""
  size = 50
  density = 0.2
  global global_grid  # Объявляем глобальную переменную 'global_grid'
  global_grid = create_grid(size)  # Создаем глобальную сетку
  initialize_grid(global_grid, density)  # Инициализируем глобальную сетку

  fig, ax = plt.subplots()
  img = ax.imshow(global_grid, cmap='binary', interpolation='nearest')
  ani = animation.FuncAnimation(fig, animate, fargs=(img, global_grid), interval=100, blit=True)

  plt.show()

if __name__ == "__main__":
  main()