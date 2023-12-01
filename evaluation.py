import pandas as pd
import matplotlib.pyplot as plt

file_path = 'data/confirm/algorithm_1_out.csv'

# CSVファイルからデータを読み込む
df = pd.read_csv(file_path, encoding='utf-8')
print(df.head())

# lossの平均値を計算
average_loss = df.groupby('service_time')['loss'].mean().reset_index()
print(average_loss.head())

# グラフの作成
plt.plot(average_loss['service_time'], average_loss['loss'], marker='.')
plt.xlabel('Service Time')
plt.ylabel('Average Loss')
plt.grid(True)
plt.show()
