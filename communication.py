import random

from network import Network


class Communication():
    def __init__(self, network: Network, s_node: int, e_node: int, algorithm: int) -> None:
        """
        network: ネットワーク
        s_node: 開始ノード
        e_node: 終了ノード
        algorithm: 経路の決定方法
        1 => 最小ホップ経路を用いた固定経路
        2 => 最大路を用いた固定経路
        3 => 最小ホップ経路を用いた要求時経路
        4 => 最大路を用いた要求時経路
        """
        self.network = network
        self.path = self.get_path(s_node, e_node, algorithm)
        self.service_time = 0
        self.arrival_interval = 0
        # TODO: ここはなくす。
        self.set_service_time_by_expovariate()
        self.set_arrival_interval_by_expovariate()
        self.is_communicating = False

    # 指数分布を返すプライベートメソッド
    def __expovariate(self, average: int) -> int:
        return round(random.expovariate(1 / average))

    def set_service_time_by_expovariate(self, average: int = 10) -> None:
        """
        指数分布に従う通信時間を設定する.

        average: 平均
        """
        self.service_time = self.__expovariate(average)

    def set_arrival_interval_by_expovariate(self, average: int = 10) -> None:
        """
        指数分布に従う通信の到着間隔を設定する.

        average: 平均
        """
        self.arrival_interval = self.__expovariate(average)

    def set_service_time_by_int(self, service_time: int) -> None:
        """
        通信時間を設定する.

        service_time: 通信時間
        """
        self.service_time = service_time

    def set_arrival_interval_by_int(self, arrival_interval: int) -> None:
        """
        通信の到着間隔を設定する.

        arrival_interval: 通信の到着間隔
        """
        self.arrival_interval = arrival_interval

    def get_service_time(self) -> int:
        """
        通信時間を返す.
        """
        return self.service_time

    def get_arrival_interval(self) -> int:
        """
        通信の到着間隔を返す.
        """
        return self.arrival_interval

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
        5 => 空き容量の逆数を考慮した経路
        6 => 最短最大路
        """
        # TODO: 5と6を実装する
        if algorithm == 1:
            return self.network.shortest_path_between(s_node, e_node, self.network.get())
        elif algorithm == 2:
            return self.network.widest_path_between(s_node, e_node, self.network.get())
        elif algorithm == 3:
            return self.network.shortest_path_between(s_node, e_node, self.network.get_current())
        elif algorithm == 4:
            return self.network.widest_path_between(s_node, e_node, self.network.get_current())
        else:
            raise Exception("algorithmの値が不正です。")

    def start(self) -> bool:
        """
        通信の開始. もし容量があれば容量を1減らし、Trueを返す.

        s_node: 開始ノード
        e_node: 終了ノード
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
        通信の終了. 容量を増やす.
        """
        if not self.is_communicating:
            raise Exception("通信が開始されていません。")

        self.is_communicating = False
        self.network.end(self.path)


if __name__ == "__main__":
    network = Network()
    s_node, e_node = network.random_two_nodes()
    communication = Communication(network, s_node, e_node, 3)
    print(communication.path)
    network.show_current()
    communication.start()
    network.show_current()
    communication.end()
    network.show_current()
