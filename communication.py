import numpy.random as random

from network import Network


class Communication():
    """
    1回の通信を管理するオブジェクト。
    """
    def __init__(self, network: Network, s_node: int, e_node: int, algorithm: int, service_time: int = 1, arrival_interval: int = 1) -> None:
        """
        コンストラクタ。

        引数
        - network: ネットワーク
        - s_node: 開始ノード
        - e_node: 終了ノード
        - algorithm: 経路の決定方法
            - 1: 最小ホップ経路を用いた固定経路
            - 2: 最大路を用いた固定経路
            - 3: 最小ホップ経路を用いた要求時経路
            - 4: 最大路を用いた要求時経路
            - 5: 最短最大路を用いた固定経路
            - 6: 最短最大路を用いた要求時経路
        - service_time: 通信時間（初期値は1）
        - arrival_interval: 通信の到着間隔（初期値は1）
        """
        self.network = network
        self.path = self.decide_path(s_node, e_node, algorithm)
        self.service_time = service_time
        self.arrival_interval = arrival_interval
        self.is_communicating = False

    def __getmetric_distribution(self, average: int) -> int:
        return random.geometric(1 / average)

    def set_service_time_by_geometric_distribution(self, average: int = 1) -> None:
        """
        幾何分布に従う通信時間を設定する。

        引数
        - average: 平均（初期値は1）
        """
        self.service_time = self.__getmetric_distribution(average)

    def set_arrival_interval_by_geometric_distribution(self, average: int = 1) -> None:
        """
        幾何分布に従う通信の到着間隔を設定する。

        引数
        - average: 平均（初期値は1）
        """
        self.arrival_interval = self.__getmetric_distribution(average)

    def get_service_time(self) -> int:
        """
        通信時間を返す。
        """
        return self.service_time

    def get_arrival_interval(self) -> int:
        """
        通信の到着間隔を返す。
        """
        return self.arrival_interval
    
    def get_path(self) -> list:
        """
        経路を返す。
        """
        return self.path

    def decide_path(self, s_node: int, e_node: int, algorithm: int) -> list:
        """
        経路を決定する。

        引数
        - s_node: 開始ノード
        - e_node: 終了ノード
        - algorithm: 経路の決定方法
            - 1: 最小ホップ経路を用いた固定経路
            - 2: 最大路を用いた固定経路
            - 3: 最小ホップ経路を用いた要求時経路
            - 4: 最大路を用いた要求時経路
            - 5: 最短最大路を用いた固定経路
            - 6: 最短最大路を用いた要求時経路
        """
        if algorithm == 1:
            return self.network.shortest_path_between(s_node, e_node, self.network.get())
        elif algorithm == 2:
            return self.network.widest_path_between(s_node, e_node, self.network.get())
        elif algorithm == 3:
            return self.network.shortest_path_between(s_node, e_node, self.network.get_current())
        elif algorithm == 4:
            return self.network.widest_path_between(s_node, e_node, self.network.get_current())
        elif algorithm == 5:
            return self.network.shortest_widest_path_between(s_node, e_node, self.network.get())
        elif algorithm == 6:
            return self.network.shortest_widest_path_between(s_node, e_node, self.network.get_current())
        else:
            raise Exception("algorithmの値が不正です。")

    def start(self) -> bool:
        """
        通信の開始。もし容量があれば容量を1減らし、Trueを返す。
        """
        if self.is_communicating:
            raise Exception("通信中です。")

        if self.network.start(self.path):
            self.is_communicating = True
            return True
        else:
            return False

    def end(self) -> None:
        """
        通信の終了。容量を増やす。
        """
        if not self.is_communicating:
            raise Exception("通信が開始されていません。")

        self.is_communicating = False
        self.network.end(self.path)


if __name__ == "__main__":
    network = Network()
    s_node, e_node = network.random_two_nodes()
    communication = Communication(network, s_node, e_node, 3)
    print(f"path: {communication.get_path()}")
    communication.start()
    communication.end()
