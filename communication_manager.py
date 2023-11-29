import os

from network import Network
from communication import Communication


class CommunicationManager():
    def __init__(self, algorithm: int = 1, communication_time: int = 0) -> None:
        """
        algorithm: 通信のアルゴリズム
        1 => 最小ホップ経路を用いた固定経路
        2 => 最大路を用いた固定経路
        3 => 最小ホップ経路を用いた要求時経路
        4 => 最大路を用いた要求時経路
        communication_time: 通信時間
        """
        self.network = Network()
        self.ALGORITHM = algorithm
        self.communication_start_num = 0
        self.communication_end_num = 0
        self.try_start_num = 0
        self.MAX_TRY_START_NUM = 10000
        self.communication_time = communication_time
        if self.communication_time < 0:
            raise Exception("通信時間は0以上である必要があります。")
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
                f.write("communication_time, loss\n")

    def save(self) -> None:
        """
        通信を保存する.
        """
        with open(self.out_file, "a") as f:
            f.write(f"{self.communication_time}, {self.loss()}\n")

    def loss(self) -> float:
        """
        通信のロス率を返す.
        """
        return (self.MAX_TRY_START_NUM - self.communication_start_num) / self.MAX_TRY_START_NUM

    def run(self) -> None:
        """
        通信を実行する.
        """
        self.network.show()
        self.network.show_current()

        # TODO: 通信の開始間隔も指数分布に従うようにする。
        time = 0
        while True:
            print(f"time: {time}, is_capable: {self.network.is_capable()}, start: {self.communication_start_num}, end: {self.communication_end_num}")
            # 通信試行回数がMAX_TRY_START_NUMを超えた以降は通信を開始しない
            if self.try_start_num < self.MAX_TRY_START_NUM:
                self.try_start_num += 1
                s_node, e_node = self.network.random_two_nodes()
                communication = Communication(self.network, s_node, e_node, self.ALGORITHM)

                if self.communication_time > 0:
                    communication.set_communication_time_by_int(self.communication_time)

                # 通信の開始
                if communication.start():
                    self.communication_start_num += 1
                    communication_time = communication.get_communication_time()
                    if time + communication_time in self.communicaton_end_schedule:
                        self.communicaton_end_schedule[time + communication_time].append(communication)
                    else:
                        self.communicaton_end_schedule[time + communication_time] = [communication]
            else:
                # 終了
                if len(self.communicaton_end_schedule) == 0:
                    print("通信がすべて終了しました。")
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

        # 通信の保存
        self.save()
