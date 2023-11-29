import heapq
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
        self.current_networks[s_node][e_node] -= 1

    def end(self, s_node: int, e_node: int) -> None:
        """
        ネットワークの終了. 容量を増やす.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        # TODO: current_networksの容量がnetworksの容量を超えていないか確認
        self.current_networks[s_node][e_node] += 1
        if self.current_networks[s_node][e_node] > self.networks[s_node][e_node]:
            raise Exception("current_networksの容量がnetworksの容量を超えています。")

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

    # s_nodeからe_nodeへの経路があるか確認する
    def is_path(self, s_node: int, e_node: int, networks: list = None) -> bool:
        """
        ノード間に経路があるか確認する.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        # s_nodeとつながっているノードを取得し、再帰的に探索. e_nodeが見つかればTrueを返す
        return False

    def shortest_path_between(self, networks: list, s_node: int, e_node: int) -> list:
        """
        ノード間の最短路(ノード数が一番少ない経路)を返す.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        return []

    def widest_path_between(self, s_node: int, e_node: int, networks: list = None) -> list:
        """
        ノード間の最大路(一番通信容量を大きくできる経路)を返す.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        print(f"start: {s_node}, end: {e_node}")
        if networks is None:
            # 0で初期化
            networks = [[0 for _ in range(len(self.networks))]
                        for _ in range(len(self.networks))]
        
        for i in range(len(networks)):
            print(networks[i])

        # リンクを重みの大きい順にソート
        links = []
        for i in range(len(self.networks)):
            for j in range(len(self.networks[i])):
                if self.is_capacity(i, j) and i < j:
                    heapq.heappush(links, (-self.networks[i][j], i, j))

        print(links)

        # リンクを大きい順に取り出し、経路を作成
        while links:
            # リンクを取り出す
            link = heapq.heappop(links)
            print(link)

            # 経路にリンクを追加
            networks[link[1]][link[2]] = 1

            # 経路があるか確認
            if self.is_path(s_node, e_node, networks):
                # 経路があれば、経路を返す
                return networks

            # 経路がなければ、リンクを削除
            networks[link[1]][link[2]] = 0

        # 経路がなければ、Noneを返す
        raise None


if __name__ == "__main__":
    # ネットワークのインスタンスを作成
    network = Network()

    # 開始ノードと終了ノードを取得
    start_node, end_node = network.get_random_nodes()

    # 最大路を求める
    widest_path = network.widest_path_between(start_node, end_node)

    # 結果を表示
    print(f"Widest Path from Node {start_node} to Node {end_node}: {widest_path}")
