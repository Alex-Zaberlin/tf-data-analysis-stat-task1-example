import pandas as pd
import numpy as np


chat_id = 282219367 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    n = 64
    return x.mean()/n
