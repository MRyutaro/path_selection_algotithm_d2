import os

from communication import Communication
from network import Network


class CommunicationManager():
    """
    通信を管理するオブジェクト。
    """
    def __init__(self, algorithm: int, service_time: int = 1, arrival_interval: int = 1, average_service_time: int = 0, average_arrival_interval: int = 0) -> None:
        """
        コンストラクタ。

        引数
        - algorithm: 通信のアルゴリズム
            - 1: 最小ホップ経路を用いた固定経路
            - 2: 最大路を用いた固定経路
            - 3: 最小ホップ経路を用いた要求時経路
            - 4: 最大路を用いた要求時経路
            - 5: 最短最大路を用いた固定経路
            - 6: 最短最大路を用いた要求時経路
        - service_time: 通信時間（初期値は1）
        - arrival_interval: 通信の到着間隔（初期値は1）
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
        # サービス時間と到着間隔は幾何分布に従う。0で初期化
        self.avarage_service_time = average_service_time
        self.avarage_arrival_interval = average_arrival_interval

        # 一定到着率の仮定より、単位時間あたりに到着する通信の数は1つとする
        self.communication_start_schedule: dict[int, Communication] = {}
        self.communicaton_end_schedule: dict[int, list[Communication]] = {}

        self.out_file = f"data/algorithm_{self.ALGORITHM}_out.csv"
        self.setup()

    def setup(self) -> None:
        """
        出力ファイルを作成する。
        """
        if not os.path.isdir("data"):
            os.mkdir("data")
        if not os.path.isfile(self.out_file):
            with open(self.out_file, "w") as f:
                if self.avarage_service_time > 0 and self.avarage_arrival_interval > 0:
                    f.write("average_service_time,average_arrival_interval,loss\n")
                else:
                    f.write("service_time,loss\n")

    def save(self) -> None:
        """
        通信を保存する。
        """
        with open(self.out_file, "a") as f:
            if self.avarage_service_time > 0 and self.avarage_arrival_interval > 0:
                f.write(f"{self.avarage_service_time},{self.avarage_arrival_interval},{self.loss()}\n")
            else:
                f.write(f"{self.service_time},{self.loss()}\n")

    def loss(self) -> float:
        """
        通信のロス率を返す。
        """
        return (self.MAX_TRY_START_NUM - self.communication_start_num) / self.MAX_TRY_START_NUM
    
    def set_service_time_by_geometric_distribution(self, average_service_time: int = 1) -> None:
        """
        幾何分布に従う通信時間を設定する。

        引数
        - average: 平均（初期値は1）
        """
        self.avarage_service_time = average_service_time

    def set_arrival_interval_by_geometric_distribution(self, average_arrival_interval: int = 1) -> None:
        """
        幾何分布に従う通信の到着間隔を設定する。

        引数
        - average: 平均（初期値は1）
        """
        self.avarage_arrival_interval = average_arrival_interval

    def print_result(self) -> None:
        """
        実験結果を表示する。
        """
        print(f"アルゴリズム: {self.ALGORITHM}", end=", ")
        if self.avarage_service_time > 0:
            print(f"サービス時間の平均: {self.avarage_service_time}", end=", ")
        else:
            print(f"サービス時間: {self.service_time}", end=", ")
        if self.avarage_arrival_interval > 0:
            print(f"到着間隔の平均: {self.avarage_arrival_interval}", end=", ")
        else:
            print(f"到着間隔: {self.arrival_interval}", end=", ")
        print(f"通信開始回数: {self.communication_start_num}", end=", ")
        print(f"通信開始試行回数: {self.try_start_num}", end=", ")
        print(f"呼損率: {self.loss()}")

    def print_status(self, time) -> None:
        """
        現在の通信の状況を出力する。
        """
        print(f"{time} -> 通信開始回数: {self.communication_start_num}, 通信開始試行回数: {self.try_start_num}", end=", ")
        print(f"現在のネットワークの総容量: {self.network.get_sum_current_networks()}", end=", ")
        print(f"通信開始スケジュールの長さ: {len(self.communication_start_schedule)}", end=", ")
        print(f"通信終了スケジュールの長さ: {len(self.communicaton_end_schedule)}")

    def run(self) -> None:
        """
        通信を実行する。
        """
        time = 0

        # 最初の通信を開始スケジュールに追加
        s_node, e_node = self.network.random_two_nodes()
        communication = Communication(self.network, s_node, e_node, self.ALGORITHM, self.service_time, self.arrival_interval)
        if self.avarage_service_time > 0:
            communication.set_service_time_by_geometric_distribution(self.avarage_service_time)
        if self.avarage_arrival_interval > 0:
            communication.set_arrival_interval_by_geometric_distribution(self.avarage_arrival_interval)
        arrival_interval = communication.get_arrival_interval()
        if arrival_interval <= 0:
            raise Exception("通信の到着間隔は0より大きい必要があります。")

        self.communication_start_schedule[time + arrival_interval] = communication

        while True:
            # 現在の通信の状況を出力
            self.print_status(time)

            # 通信の終了
            if time in self.communicaton_end_schedule:
                for communication in self.communicaton_end_schedule[time]:
                    self.communication_end_num += 1
                    communication.end()
                self.communicaton_end_schedule.pop(time)

            # 通信試行回数がMAX_TRY_START_NUMを超えた以降は通信を開始しない
            if self.try_start_num < self.MAX_TRY_START_NUM:
                # 通信の開始
                if time in self.communication_start_schedule:
                    communication = self.communication_start_schedule[time]
                    self.try_start_num += 1
                    if communication.start():
                        self.communication_start_num += 1
                        service_time = communication.get_service_time()
                        if service_time <= 0:
                            raise Exception("通信時間は0より大きい必要があります。")

                        if time + service_time in self.communicaton_end_schedule:
                            self.communicaton_end_schedule[time + service_time].append(communication)
                        else:
                            self.communicaton_end_schedule[time + service_time] = [communication]

                    # 通信が始まっても始まらなくても開始スケジュールから削除
                    self.communication_start_schedule.pop(time)

                    # communication_start_scheduleの管理
                    s_node, e_node = self.network.random_two_nodes()
                    communication = Communication(self.network, s_node, e_node, self.ALGORITHM, self.service_time, self.arrival_interval)
                    if self.avarage_service_time > 0:
                        communication.set_service_time_by_geometric_distribution(self.avarage_service_time)
                    if self.avarage_arrival_interval > 0:
                        communication.set_arrival_interval_by_geometric_distribution(self.avarage_arrival_interval)
                    arrival_interval = communication.get_arrival_interval()
                    if arrival_interval <= 0:
                        raise Exception("通信の到着間隔は0より大きい必要があります。")
                    # 次の通信の到着を開始スケジュールに追加
                    self.communication_start_schedule[time + arrival_interval] = communication

            else:
                # 終了
                if len(self.communicaton_end_schedule) == 0:
                    break

            time += 1

        # networkとcurrent_networkが一致していなければエラー
        if self.network.get() != self.network.get_current():
            raise Exception("networkとcurrent_networkが一致しません。")

        # 実験の結果を表示
        # self.print_result()
        # 通信の保存
        self.save()


if __name__ == "__main__":
    algorithm = 1
    service_time = 100
    average_service_time = 0
    average_arrival_interval = 0
    cm = CommunicationManager(
        algorithm=algorithm,
        service_time=service_time,
        average_service_time=average_service_time,
        average_arrival_interval=average_arrival_interval
    )
    cm.run()
    cm.print_result()
