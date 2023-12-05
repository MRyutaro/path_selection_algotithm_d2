import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

experiment = 1

file_path = [
    f'data/ex1/{experiment}/algorithm_1_out.csv',
    f'data/ex1/{experiment}/algorithm_2_out.csv',
    f'data/ex1/{experiment}/algorithm_3_out.csv',
    f'data/ex1/{experiment}/algorithm_4_out.csv',
    f'data/ex1/{experiment}/algorithm_5_out.csv',
    f'data/ex1/{experiment}/algorithm_6_out.csv'
]

algorithms = [
    '1: static shortest path',
    '2: static widest path',
    '3: dynamic shortest path',
    '4: dynamic widest path',
    '5: static shortest widest path',
    '6: dynamic shortest widest path'
]

plt.xlabel('Service Time')
plt.ylabel('Average Loss')
plt.grid(True)

for i, path in enumerate(file_path):
    df = pd.read_csv(path, encoding='utf-8')
    # lossの平均値を計算
    average_loss = df.groupby('service_time')['loss'].mean().reset_index()
    # グラフの描画
    plt.plot(average_loss['service_time'], average_loss['loss'], label=algorithms[i])

plt.legend()
plt.show()
