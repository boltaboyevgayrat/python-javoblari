# from sklearn.linear_model import LinearRegression, Ridge, Lasso
# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.model_selection import train_test_split
# import numpy as np

# # Ma'lumotlar
# X = np.array([1, 2, 3, 4, 5]).reshape(-1,1)
# y = np.array([2, 5, 9, 15, 23])

# # Polinomial regressiya (2-daraja)
# poly = PolynomialFeatures(degree=2)
# X_poly = poly.fit_transform(X)

# # Model yaratish
# model = LinearRegression()
# model.fit(X_poly, y)

# # Prognoz
# y_pred = model.predict(X_poly)
# print("Koefitsiyentlar:", model.coef_)
# print("Intercept:", model.intercept_)

# # Regulyarizatsiya misoli
# ridge = Ridge(alpha=0.5)
# ridge.fit(X_poly, y)
# print("Ridge Coef:", ridge.coef_)



# # Kutubxonalarni chaqirish
# import numpy as np
# import matplotlib.pyplot as plt

# # 1. Ma'lumotlarni o'qish
# x = []
# y = []

# with open('salary_data.csv', 'r') as f:
#     for line in f:
#         a = line.strip().split(",")
#         x.append(float(a[0]))  # kiruvchi o'zgaruvchi (masalan, ish yillari)
#         y.append(float(a[1]))  # chiquvchi o'zgaruvchi (masalan, maosh)

# # 2. Min-max normalizatsiya
# x_min = min(x)
# x_max = max(x)
# y_min = min(y)
# y_max = max(y)

# z = []  # normalizatsiyalangan x
# k = []  # normalizatsiyalangan y

# for i in range(len(x)):
#     z.append((x[i] - x_min) / (x_max - x_min))
#     k.append((y[i] - y_min) / (y_max - y_min))

# # 3. Gradient descent boshlang'ich qiymatlari
# w = [0.8]  # slope
# b = [0.4]  # intercept
# learning_rate = 0.001
# iterations = 20

# # w va b summasi (o'rtachani hisoblash uchun)
# w_sum = 0
# b_sum = 0

# # 4. Gradient descent algoritmi
# for i in range(1, iterations):
#     # gradient descent formulasi
#     w.append(w[i-1] - learning_rate * ((w[i-1] * z[i-1] + b[i-1] - k[i-1]) * z[i-1]))
#     b.append(b[i-1] - learning_rate * (w[i-1] * z[i-1] + b[i-1] - k[i-1]))

#     # summaga qo'shish
#     w_sum += w[i-1]
#     b_sum += b[i-1]

# # 5. O'rtacha qiymatlarni olish
# new_w = w_sum / iterations
# new_b = b_sum / iterations

# print("Model parametrlar (normalizatsiyalangan):")
# print("new_w =", new_w)
# print("new_b =", new_b)

# # 6. Grafik uchun asl x o'lchamlariga o'tkazish
# # y = w*x + b --> y = w_norm * ((x - x_min)/(x_max-x_min)) + b_norm
# predicted_y = [new_w * ((xi - x_min)/(x_max - x_min)) + new_b for xi in x]

# # y ni asl o'lchamga o'tkazish
# predicted_y_actual = [yi*(y_max - y_min) + y_min for yi in predicted_y]

# # 7. Grafikni chizish
# plt.scatter(x, y, color='blue', label='Asl ma\'lumotlar')
# plt.plot(x, predicted_y_actual, color='red', label='Chiziqli regressiya')
# plt.xlabel('Ish yillari')
# plt.ylabel('Maosh')
# plt.title('Chiziqli regressiya (Gradient Descent)')
# plt.legend()
# plt.show()

from numpy import *
import matplotlib.pylab as plt
import numpy as np

n = int(input('n='))
f = open('salary_data.csv', 'r')

x = []

first = True

for i in f:
    if first:
        first = False
        continue

    a = i.strip().split(",")
    if a[5] != "":
        x.append(float(a[5]))

print(max(x))

x_min = min(x)
x_max = max(x)

z = []

for i in range(0, n):
    z.append((x[i] - x_min) / (x_max - x_min))

# print(z[i], k[i])

w = []
w.append(0.8)

w_sum = 0
b_sum = 0

b = []
b.append(0.4)

for i in range(1, n + 1):
    w.append(w[i-1] - 0.001 * (w[i-1] * z[i-1] + b[i-1]) * z[i-1])
    b.append(b[i-1] - 0.001 * (w[i-1] * z[i-1] + b[i-1]))

    w_sum += w[i-1]
    b_sum += b[i-1]

new_w = w_sum / 20
new_b = b_sum / 20

print(new_w, new_b)