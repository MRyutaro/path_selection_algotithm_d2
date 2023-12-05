import datetime

from communication_manager import CommunicationManager as CM

if __name__ == "__main__":
    # ==========
    # 実験2(指数分布に従うサービス時間、到着間隔を生成する場合)
    # ==========
    # 実験回数。初期値は10
    experiment_num = 10

    # アルゴリズム。初期値は[1, 2, 3, 4, 5]
    # 1: static shortest path
    # 2: static widest path
    # 3: dynamic shortest path
    # 4: dynamic widest path
    # 5: static shortest widest path
    # 6: dynamic shortest widest path
    algorithms = [1, 2, 3, 4, 5, 6]
    # algorithms = [1, 2]
    # algorithms = [3, 4]
    # algorithms = [5, 6]

    # 平均サービス時間。初期値は[i for i in range(1, 11)]
    average_service_times = [i for i in range(1, 101)]

    # 平均到着間隔。初期値は[i for i in range(1, 11)]
    average_arrival_intervals = [10,]

    for algorithm in algorithms:
        print(f"algorithm: {algorithm}")
        for average_service_time in average_service_times:
            for average_arrival_interval in average_arrival_intervals:
                print(f"average_service_time: {average_service_time}, average_arrival_interval: {average_arrival_interval}", end=", ")
                now = datetime.datetime.now()
                for _ in range(experiment_num):
                    cm = CM(algorithm=algorithm, average_service_time=average_service_time, average_arrival_interval=average_arrival_interval)
                    cm.run()
                print(f"time: {datetime.datetime.now() - now}")
