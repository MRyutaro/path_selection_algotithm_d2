import datetime

from communication_manager import CommunicationManager as CM

if __name__ == "__main__":
    # ==========
    # 実験1（サービス時間、到着間隔を固定する場合）
    # ==========
    # 実験回数。初期値は10
    experiment_num = 10

    # アルゴリズム。初期値は[1, 2, 3, 4, 5, 6]
    # 1: static shortest path
    # 2: static widest path
    # 3: dynamic shortest path
    # 4: dynamic widest path
    # 5: static shortest widest path
    # 6: dynamic shortest widest path
    algorithms = [1, 2, 3, 4, 5, 6]

    # サービス時間。初期値は1から100までの整数
    service_times = [i for i in range(1, 501)]

    for algorithm in algorithms:
        print(f"algorithm: {algorithm}")
        for service_time in service_times:
            print(f"service_time: {service_time}", end=", ")
            now = datetime.datetime.now()
            for _ in range(experiment_num):
                cm = CM(algorithm=algorithm, service_time=service_time)
                cm.run()
            print(f"time: {datetime.datetime.now() - now}")
