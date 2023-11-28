import os
import random


class Network():
    def __init__(self) -> None:
        self.networks = [
            [0, 3, 0, 3, 0, 0, 0, 0, 0, 0],  # 0
            [3, 0, 3, 4, 0, 0, 0, 0, 0, 0],  # 1
            [0, 3, 0, 0, 4, 3, 0, 0, 0, 0],  # 2
            [3, 4, 0, 0, 5, 0, 0, 3, 0, 0],  # 3
            [0, 0, 4, 5, 0, 5, 0, 4, 0, 0],  # 4
            [0, 0, 3, 0, 5, 0, 3, 0, 4, 0],  # 5
            [0, 0, 0, 0, 0, 3, 0, 0, 3, 0],  # 6
            [0, 0, 0, 3, 4, 0, 0, 0, 4, 3],  # 7
            [0, 0, 0, 0, 0, 4, 3, 4, 0, 3],  # 8
            [0, 0, 0, 0, 0, 0, 0, 3, 3, 0],  # 9
        ]
        self.current_networks = [
            [0, 3, 0, 3, 0, 0, 0, 0, 0, 0],  # 0
            [3, 0, 3, 4, 0, 0, 0, 0, 0, 0],  # 1
            [0, 3, 0, 0, 4, 3, 0, 0, 0, 0],  # 2
            [3, 4, 0, 0, 5, 0, 0, 3, 0, 0],  # 3
            [0, 0, 4, 5, 0, 5, 0, 4, 0, 0],  # 4
            [0, 0, 3, 0, 5, 0, 3, 0, 4, 0],  # 5
            [0, 0, 0, 0, 0, 3, 0, 0, 3, 0],  # 6
            [0, 0, 0, 3, 4, 0, 0, 0, 4, 3],  # 7
            [0, 0, 0, 0, 0, 4, 3, 4, 0, 3],  # 8
            [0, 0, 0, 0, 0, 0, 0, 3, 3, 0],  # 9
        ]

    def get(self) -> list:
        return self.networks

    def show(self) -> None:
        print("===networks===")
        for i in range(len(self.networks)):
            print(self.networks[i])

    def get_current(self) -> list:
        return self.current_networks

    def show_current(self) -> None:
        print("===current_networks===")
        for i in range(len(self.current_networks)):
            print(self.current_networks[i])

    def get_random_nodes(self) -> tuple[int, int]:
        """
        ランダムなノードを2つ返す.
        """
        node_num = len(self.networks)
        nodes = list(range(node_num))
        s_node, e_node = random.sample(nodes, 2)
        return s_node, e_node

    def start(self, s_node: int, e_node: int) -> None:
        """
        ネットワークの開始. 容量を減らす.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        pass

    def end(self, s_node: int, e_node: int) -> None:
        """
        ネットワークの終了. 容量を増やす.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        # TODO: current_networksの容量がnetworksの容量を超えていないか確認
        pass

    def capacity_between(self, s_node: int, e_node: int) -> int:
        """
        ノード間の容量を返す.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        return self.networks[s_node][e_node]

    def current_capacity_between(self, s_node: int, e_node: int) -> int:
        """
        ノード間の現在の容量を返す.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        return self.current_networks[s_node][e_node]

    def is_capacity(self, s_node: int, e_node: int) -> bool:
        """
        ノード間に容量があるか確認する.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        return self.networks[s_node][e_node] > 0

    def is_current_capacity(self, s_node: int, e_node: int) -> bool:
        """
        現在、ノード間に容量があるか確認する.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        return self.current_networks[s_node][e_node] > 0

    def shortest_path_between(self, s_node: int, e_node: int) -> list:
        """
        ノード間の最短路(ノード数が一番少ない経路)を返す.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        return []

    def widest_path_between(self, s_node: int, e_node: int) -> list:
        """
        ノード間の最大路(一番通信容量を大きくできる経路)を返す.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        return []


class Communication():
    def __init__(self, network: Network, s_node: int, e_node: int, algorithm: int) -> None:
        self.network = network
        # 1: 最小ホップ経路を用いた固定経路
        # 2: 最大路を用いた固定経路
        # 3: 最小ホップ経路を用いた要求時経路
        # 4: 最大路を用いた要求時経路
        self.path = self.set_path(s_node, e_node, algorithm)
        # 指数分布に従う通信時間
        self.communication_time = 0
        self.set_communication_time_by_expovariate()

    def set_communication_time_by_expovariate(self, average: int = 10) -> None:
        """
        指数分布に従う通信時間を返す.

        average: 平均
        """
        self.communication_time = round(random.expovariate(1/average))

    def set_communication_time_by_int(self, communication_time: int) -> None:
        """
        通信時間を設定する.

        communication_time: 通信時間
        """
        self.communication_time = communication_time

    def get_communication_time(self) -> int:
        """
        通信時間を返す.
        """
        return self.communication_time

    def set_path(self, s_node: int, e_node: int, algorithm: int) -> list:
        """
        経路の決定.

        s_node: 開始ノード
        e_node: 終了ノード
        algorithm: 経路の決定方法
        1 => 最小ホップ経路を用いた固定経路
        2 => 最大路を用いた固定経路
        3 => 最小ホップ経路を用いた要求時経路
        4 => 最大路を用いた要求時経路
        """
        return []

    def start(self) -> bool:
        """
        通信の開始. もし容量があれば容量を1減らし、Trueを返す.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        return False

    def end(self) -> None:
        """
        通信の終了. 容量を増やす.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        pass


class CommunicationManager():
    def __init__(self, communication_time: int = 0) -> None:
        self.network = Network()
        # 1: 最小ホップ経路を用いた固定経路
        # 2: 最大路を用いた固定経路
        # 3: 最小ホップ経路を用いた要求時経路
        # 4: 最大路を用いた要求時経路
        self.ALGORITHM = 1
        self.start_num = 0
        self.end_num = 0
        self.MAX_START_NUM = 10000
        self.communication = []
        self.communication_time = communication_time
        if self.communication_time < 0:
            raise Exception("通信時間は0以上である必要があります。")
        self.communicaton_end_schedule = {}
        self.out_file = f"data/{self.ALGORITHM}_out.csv"
        self.setup()

    def setup(self) -> None:
        """
        出力ファイルの作成.
        """
        # dataフォルダがなければ作成
        if not os.path.isdir("data"):
            os.mkdir("data")
        # data/{ALGORITHM}_out.csvがなければ作成
        if not os.path.isfile(self.out_file):
            with open(self.out_file, "w") as f:
                f.write("communication_time, loss\n")

    def save(self) -> None:
        """
        通信を保存する.
        """
        # data/{ALGORITHM}_out.csvに追記
        with open(self.out_file, "a") as f:
            f.write(f"{self.communication_time}, {self.loss()}\n")

    def loss(self) -> float:
        """
        通信のロス率を返す.
        """
        return (self.MAX_START_NUM - self.start_num) / self.MAX_START_NUM

    def run(self) -> None:
        """
        通信を実行する.
        """
        # TODO: while文を回すように変更
        # TODO: で、MAX_START_NUM回通信を開始する。
        # TODO: そして通信がすべて終了したらwhile文を抜ける。
        for i in range(self.MAX_START_NUM):
            print(f"==={i}回目の通信===")

            s_node, e_node = self.network.get_random_nodes()
            communication = Communication(self.network, s_node, e_node, self.ALGORITHM)
            if self.communication_time > 0:
                communication.set_communication_time_by_int(self.communication_time)

            # 通信の開始
            if communication.start():
                self.start_num += 1
                self.communication.append(communication)
                communication_time = communication.get_communication_time()
                if i+communication_time in self.communicaton_end_schedule:
                    self.communicaton_end_schedule[i+communication_time].append(communication)
                else:
                    self.communicaton_end_schedule[i+communication_time] = [communication]
            else:
               self.communication.append(None)

            # 通信の終了
            if i in self.communicaton_end_schedule:
                for communication in self.communicaton_end_schedule[i]:
                    communication.end()
                    self.end_num += 1
                self.communicaton_end_schedule.pop(i)

        # networkとcurrent_networkが一致していなければエラー
        if self.network.get() != self.network.get_current():
            raise Exception("networkとcurrent_networkが一致しません。")

        # 通信の保存
        self.save()

if __name__ == "__main__":
    network = Network()
    network.show()
    network.show_current()
    cm = CommunicationManager()
    cm.run()
