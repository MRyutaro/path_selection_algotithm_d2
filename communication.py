import random

from network import Network


class Communication():
    def __init__(self, network: Network, s_node: int, e_node: int, algorithm: int) -> None:
        self.network = network
        # 1: 最小ホップ経路を用いた固定経路
        # 2: 最大路を用いた固定経路
        # 3: 最小ホップ経路を用いた要求時経路
        # 4: 最大路を用いた要求時経路
        self.path = self.get_path(s_node, e_node, algorithm)
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

    def get_path(self, s_node: int, e_node: int, algorithm: int) -> list:
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
        if algorithm == 1:
            return self.network.shortest_path_between(self.network.get(), s_node, e_node)
        elif algorithm == 2:
            return self.network.widest_path_between(self.network.get(), s_node, e_node)
        elif algorithm == 3:
            return self.network.shortest_path_between(self.network.get_current(), s_node, e_node)
        elif algorithm == 4:
            return self.network.widest_path_between(self.network.get_current(), s_node, e_node)
        else:
            raise Exception("algorithmの値が不正です。")

    def start(self) -> bool:
        """
        通信の開始. もし容量があれば容量を1減らし、Trueを返す.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        # self.pathが空なら経路がないので通信は失敗
        if self.path is None:
            return False

        # self.pathの容量があるか確認
        for link in range(len(self.path) - 1):
            if not self.network.is_capacity(self.path[link], self.path[link + 1]):
                # 1つでも容量がなければ通信は失敗
                return False

        # self.pathの容量を減らす
        for link in range(len(self.path) - 1):
            self.network.start(self.path[link], self.path[link + 1])

        return True

    def end(self) -> None:
        """
        通信の終了. 容量を増やす.
        """
        for link in range(len(self.path) - 1):
            self.network.end(self.path[link], self.path[link + 1])
