import numpy as np
#a = [111.87,  21.87, 31.82, 1.91, 1.90, 1.85]
#np_a = np.array(a)
#print(type(a))
#print(type(np_a))
#print(np_a.dtype)
#cc = 2*np_a/ (2+np_a)
#print(cc)
#print(np_a[np_a > 23])
#temperatures = np.array([23, 25, 28, 32, 35, 29])
#status = np.where(temperatures > 30, 'жарко', 'комфортно')
#print(status)  # ['комфортно' 'комфортно' 'комфортно' 'жарко' 'жарко' 'комфортно']
#data = np.array([1, np.nan, 3, np.nan, 5])
#cleaned_data = np.where(np.isnan(data), 0, data)
#print(cleaned_data)  # [1. 0. 3. 0. 5.]
#weight_kg = [500, 1100, 1800, 81.65, 97.52, 95.25, 92.98, 86.18, 88.45, 100., 120.,240.,]
## = np.array(weight_kg)
#np_tn = np_kg/1000
#less_100 = np_tn[np_tn < 0.1]
#more_100 = np_tn[np_tn >= 0.1]
#print(less_100)
#print(more_100)
#print(e)
#arr = np.array([1, 2, 3, 4, 5, 6])
#reshaped_arr = arr.reshape((2, 3))  # Результат: [[1 2 3], [4 5 6]]
#auto_reshaped = arr.reshape((-1, 3))  # Результат: [[1 2 3], [4 5 6]]  -1 - автоматическое вычисление размера
#print(auto_reshaped)
a = np.array([15,25,14,78,96])
a2 = a*2
print(a2)