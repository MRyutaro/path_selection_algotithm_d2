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
        ノード間に現在の容量があるか確認する.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        return self.current_networks[s_node][e_node] > 0

    def shortest_path_between(self, s_node: int, e_node: int) -> list:
        """
        ノード間の最短路を返す.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        return []

    def widest_path_between(self, s_node: int, e_node: int) -> list:
        """
        ノード間の最大路を返す.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        return []


class Communication():
    def __init__(self, network: Network) -> None:
        self.network = network

    def start(self, s_node: int, e_node: int) -> bool:
        """
        通信の開始. もし容量があれば容量を1減らし、Trueを返す.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        return False

    def end(self, s_node: int, e_node: int) -> None:
        """
        通信の終了. 容量を増やす.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        pass


class CommunicationManager():
    def __init__(self, time: int) -> None:
        self.network = Network()
        self.time = time
        # 1: 最小ホップ経路を用いた固定経路
        # 2: 最大路を用いた固定経路
        # 3: 最小ホップ経路を用いた要求時経路
        # 4: 最大路を用いた要求時経路
        self.ALGORITHM = 1
        self.start_num = 0
        self.end_num = 0
        self.MAX_START_NUM = 10000
        self.communication = []

    def run(self) -> None:
        """
        通信を実行する.
        """
        pass

    def save(self) -> None:
        """
        通信を保存する.
        """
        # TODO: data/{ALGORITHM}_out.csvに追記
        # TODO: time, 1-(start_num/MAX_START_NUM)
        pass


if __name__ == "__main__":
    network = Network()
    network.show()
    network.show_current()
