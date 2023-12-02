import pandas as pd
import matplotlib.pyplot as plt

file_path = [
    'data/confirm/algorithm_1_out.csv',
    'data/confirm/algorithm_2_out.csv',
    'data/confirm/algorithm_3_out.csv',
    'data/confirm/algorithm_4_out.csv',
    'data/confirm/algorithm_5_out.csv',
    'data/confirm/algorithm_6_out.csv'
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
