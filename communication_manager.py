import os

from communication import Communication
from network import Network


class CommunicationManager():
    def __init__(self, algorithm: int = 1, service_time: int = 1, arrival_interval: int = 1) -> None:
        """
        algorithm: 通信のアルゴリズム
        1 => 最小ホップ経路を用いた固定経路
        2 => 最大路を用いた固定経路
        3 => 最小ホップ経路を用いた要求時経路
        4 => 最大路を用いた要求時経路
        service_time: 通信時間
        arrival_interval: 通信の到着間隔
        """
        self.network = Network()
        self.ALGORITHM = algorithm
        self.communication_start_num = 0
        self.communication_end_num = 0
        self.try_start_num = 0
        self.MAX_TRY_START_NUM = 10000

        # サービス時間と到着間隔は固定値
        self.service_time = service_time
        self.arrival_interval = arrival_interval
        if self.service_time < 0:
            raise Exception("通信時間は0以上である必要があります。")
        if self.arrival_interval < 0:
            raise Exception("通信の到着間隔は0以上である必要があります。")
        # サービス時間と到着間隔は指数分布に従う. 0で初期化
        self.avarage_service_time = 0
        self.avarage_arrival_interval = 0

        self.communication_start_schedule = {}
        self.communicaton_end_schedule = {}

        self.out_file = f"data/algorithm_{self.ALGORITHM}_out.csv"
        self.setup()

    def setup(self) -> None:
        """
        出力ファイルの作成.
        """
        if not os.path.isdir("data"):
            os.mkdir("data")
        if not os.path.isfile(self.out_file):
            with open(self.out_file, "w") as f:
                f.write("service_time, loss\n")

    def save(self) -> None:
        """
        通信を保存する.
        """
        with open(self.out_file, "a") as f:
            f.write(f"{self.service_time}, {self.loss()}\n")

    def loss(self) -> float:
        """
        通信のロス率を返す.
        """
        return (self.MAX_TRY_START_NUM - self.communication_start_num) / self.MAX_TRY_START_NUM
    
    def set_service_time_by_expovariate(self, average_service_time: int = 1) -> None:
        """
        指数分布に従う通信時間を設定する.

        average: 平均 = 1
        """
        self.avarage_service_time = average_service_time

    def set_arrival_interval_by_expovariate(self, average_arrival_interval: int = 1) -> None:
        """
        指数分布に従う通信の到着間隔を設定する.

        average: 平均 = 1
        """
        self.avarage_arrival_interval = average_arrival_interval

    def __print_result(self) -> None:
        """
        実験結果を表示する.
        """
        print(f"アルゴリズム: {self.ALGORITHM}", end=", ")
        print(f"サービス時間: {self.service_time}", end=", ")
        print(f"到着間隔: {self.arrival_interval}", end=", ")
        print(f"通信開始回数: {self.communication_start_num}", end=", ")
        print(f"通信開始試行回数: {self.try_start_num}", end=", ")
        print(f"呼損率: {self.loss()}")

    def __print_status(self) -> None:
        """
        現在の通信の状況を出力する.
        """
        print(f"通信時間: {self.service_time}, 通信開始回数: {self.communication_start_num}, 通信開始試行回数: {self.try_start_num}, 呼損率: {self.loss()}")
        print(f"通信開始スケジュール: {self.communication_start_schedule}")
        print(f"通信終了スケジュール: {self.communicaton_end_schedule}")

    def run(self) -> None:
        """
        通信を実行する.
        """
        time = 0
        while True:
            # 現在の通信の状況を出力
            # self.__print_status()

            # 通信試行回数がMAX_TRY_START_NUMを超えた以降は通信を開始しない
            if self.try_start_num < self.MAX_TRY_START_NUM:
                self.try_start_num += 1

                # 通信の到着
                s_node, e_node = self.network.random_two_nodes()
                communication = Communication(self.network, s_node, e_node, self.ALGORITHM, self.service_time, self.arrival_interval)

                # サービス時間と到着間隔を設定
                if self.avarage_service_time > 0:
                    communication.set_service_time_by_expovariate(self.avarage_service_time)
                if self.avarage_arrival_interval > 0:
                    communication.set_arrival_interval_by_expovariate(self.avarage_arrival_interval)

                arrival_interval = communication.get_arrival_interval()
                if time + arrival_interval in self.communication_start_schedule:
                    # arrivalじゃなくてservice_time?
                    self.communication_start_schedule[time + arrival_interval].append(communication)
                else:
                    self.communication_start_schedule[time + arrival_interval] = [communication]

                # 通信の開始
                if time in self.communication_start_schedule:
                    for communication in self.communication_start_schedule[time]:
                        if communication.start():
                            self.communication_start_num += 1
                            service_time = communication.get_service_time()
                            if time + service_time in self.communicaton_end_schedule:
                                self.communicaton_end_schedule[time + service_time].append(communication)
                            else:
                                self.communicaton_end_schedule[time + service_time] = [communication]

                    # 通信が始まっても始まらなくてもスケジュールから削除
                    self.communication_start_schedule.pop(time)

            else:
                # 終了
                if len(self.communicaton_end_schedule) == 0:
                    break

            # 通信の終了
            if time in self.communicaton_end_schedule:
                for communication in self.communicaton_end_schedule[time]:
                    self.communication_end_num += 1
                    communication.end()
                self.communicaton_end_schedule.pop(time)

            time += 1

        # networkとcurrent_networkが一致していなければエラー
        if self.network.get() != self.network.get_current():
            raise Exception("networkとcurrent_networkが一致しません。")

        # 実験の結果を表示
        self.__print_result()
        # 通信の保存
        self.save()
