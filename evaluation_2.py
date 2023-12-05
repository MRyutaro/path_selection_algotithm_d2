import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

experiment = 3

file_path = [
    f'data/ex2/{experiment}/algorithm_1_out.csv',
    f'data/ex2/{experiment}/algorithm_2_out.csv',
    f'data/ex2/{experiment}/algorithm_3_out.csv',
    f'data/ex2/{experiment}/algorithm_4_out.csv',
    f'data/ex2/{experiment}/algorithm_5_out.csv',
    f'data/ex2/{experiment}/algorithm_6_out.csv'
]

algorithms = [
    '1: static shortest path',
    '2: static widest path',
    '3: dynamic shortest path',
    '4: dynamic widest path',
    '5: static shortest widest path',
    '6: dynamic shortest widest path'
]

plt.xlabel('Average Service Time / Average Arrival Interval')
plt.ylabel('Average Loss')
plt.grid(True)

for i, path in enumerate(file_path):
    df = pd.read_csv(path, encoding='utf-8')
    # サーバ稼働率の平均値を計算
    # サーバ稼働率 = 平均サービス時間 / 平均到着間隔
    df['server_usage'] = df['average_service_time'] / df['average_arrival_interval']
    # lossの平均値を計算
    average_loss = df.groupby('server_usage')['loss'].mean().reset_index()
    # グラフの描画
    plt.plot(average_loss['server_usage'], average_loss['loss'], label=algorithms[i])

plt.legend()
plt.show()
