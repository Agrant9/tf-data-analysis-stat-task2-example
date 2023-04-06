import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 544835691 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    t = 2  # время измерения
    eps_var = 1/2  # дисперсия ошибки измерения пути
    sigma_eps = np.sqrt(eps_var)  # стандартное отклонение ошибки измерения пути
    sigma_x = np.sqrt(2 * eps_var)  # стандартное отклонение случайной величины X
    X = np.sum(S) / n  # выборочное среднее значений пути
    z = norm.ppf(1 - alpha/2)  # квантиль стандартного нормального распределения
    a_left = (X - z * sigma_x / np.sqrt(n)) / 2  
    b_right = (X + z * sigma_x / np.sqrt(n)) / 2 
    
    return a_left, b_right
