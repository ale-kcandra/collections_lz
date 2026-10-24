import matplotlib.pyplot as plt # подключаем библиотеку для графиков

x = [-2 + i*0.1 for i in range(41)] # создаем список точек по оси X (от -2 до 2 с шагом 0.1 для плавности линий)

x_int = [-2, -1, 0, 1, 2] # создаем списки для целых значений X (чтобы ставить на них маркеры) 

# создаем списки значений Y для каждой функции
y_x2 = [i**2 for i in x] # значения для x^2
y_ex = [2.718**i for i in x] # значения для e^x 
y_x3 = [i**3 for i in x] # значения для x^3

# для логарифма берем только положительные X, так как логарифм от 0 и -1 не существует
x_log = [0.1, 1, 2] 
y_log = [__import__('math').log(i) for i in x_log] # считаем ln(x)

# рисуем графики или линии
plt.plot(x, y_x2, color='red', label='x²') # красная линия x^2
plt.plot(x, y_ex, color='green', label='e^x') # зеленая линия e^x
plt.plot(x_log, y_log, color='blue', label='ln(x)') # синяя линия ln(x)
plt.plot(x, y_x3, color='yellow', label='x³') # желтая линия x^3

# ставим маркеры (точки и кресты) только на целых значениях X
plt.plot(x_int, [i**2 for i in x_int], 'ro') # красные точки для x^2
plt.plot(x_int, [2.718**i for i in x_int], 'gx') # зеленые кресты для e^x
plt.plot([1, 2], [0, 0.693], 'bo') # синие точки для ln(x) (в точках 1 и 2)
plt.plot(x_int, [i**3 for i in x_int], 'yellow', marker='x', linestyle='') # желтые кресты для x^3

plt.grid(True) # включаем сетку
plt.show() # показываем график