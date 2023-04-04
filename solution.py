import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 544835691 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    y = x[:, 0]
    x_squared = x[:, 1]
    x_mean = np.mean(x_squared)
    y_mean = np.mean(y)
    beta_1 = np.sum((x_squared - x_mean) * (y - y_mean)) / np.sum((x_squared - x_mean) ** 2)
    beta_0 = y_mean - beta_1 * x_mean
    n = len(y)
    residuals = y - beta_0 - beta_1 * x_squared
    sigma_hat = np.sqrt(np.sum(residuals ** 2) / (n - 2))
    t_alpha_2 = t.ppf(1 - alpha / 2, n - 2)
    se_beta_1 = sigma_hat / np.sqrt(np.sum((x_squared - x_mean) ** 2))
    lower_bound = beta_1 - t_alpha_2 * se_beta_1
    upper_bound = beta_1 + t_alpha_2 * se_beta_1
    
    return lower_bound, upper_bound
