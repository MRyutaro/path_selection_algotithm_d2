from communication_manager import CommunicationManager as CM

if __name__ == "__main__":
    # ==========
    # 実験1（サービス時間、到着間隔を固定する場合）
    # ==========
    experiment_num = 10
    algorithms = [3, 4]
    service_times = [i for i in range(1, 500)]

    for algorithm in algorithms:
        print(f"algorithm: {algorithm}")
        for service_time in service_times:
            for _ in range(experiment_num):
                cm = CM(algorithm=algorithm, service_time=service_time)
                cm.run()

    # ==========
    # 実験2(指数分布に従うサービス時間、到着間隔を生成する場合)
    # ==========
    # experiment_num = 10
    # algorithms = [2]
    # average_service_times = [0]
    # average_arrival_interval = [0]

    # for algorithm in algorithms:
    #     print(f"algorithm: {algorithm}")
    #     for average_service_time in average_service_times:
    #         for average_arrival_interval in average_arrival_interval:
    #             for _ in range(experiment_num):
    #                 cm = CM(algorithm=algorithm, average_service_time=average_service_time, average_arrival_interval=average_arrival_interval)
    #                 cm.run()
