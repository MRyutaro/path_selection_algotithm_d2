from communication_manager import CommunicationManager as CM

if __name__ == "__main__":
    experiment_num = 10
    algorithms = [2]
    service_times = [i for i in range(1, 500)]
    for algorithm in algorithms:
        print(f"algorithm: {algorithm}")
        for service_time in service_times:
            for _ in range(experiment_num):
                cm = CM(algorithm=algorithm, service_time=service_time)
                cm.run()
