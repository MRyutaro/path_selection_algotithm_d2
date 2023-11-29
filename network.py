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

    def is_capacity(self, s_node: int, e_node: int, networks: list = None) -> bool:
        """
        現在、ノード間に容量があるか確認する.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        if networks is None:
            networks = self.current_networks

        return networks[s_node][e_node] > 0

    def get_path(self, s_node: int, e_node: int, networks: list, path: list = []) -> list:
        """
        s_nodeとつながっているノードを取得し、再帰的に探索. e_nodeが見つかれば経路を返す

        s_node: 開始ノード
        e_node: 終了ノード
        """
        if len(path) == 0:
            path.append(s_node)

        # 終了ノードに到達した場合は経路を返す
        if s_node == e_node:
            return path

        # s_nodeとつながっているノードを探索
        for node in range(len(networks[s_node])):
            if (node not in path) and (networks[s_node][node] > 0):
                # 再帰的に探索
                result = self.get_path(node, e_node, networks, path + [node])
                if result:
                    return result

        # 経路が見つからない場合は空リストを返す
        return []

    def shortest_path_between(self, s_node: int, e_node: int, networks: list) -> list:
        """
        ノード間の最短路(ノード数が一番少ない経路)を返す.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        return []

    def widest_path_between(self, s_node: int, e_node: int, networks: list, more_than_max_networks: list = None) -> list:
        """
        ノード間の最大路(一番通信容量を大きくできる経路)を返す.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        if more_than_max_networks is None:
            # 0で初期化
            more_than_max_networks = [[0 for _ in range(len(self.networks))]
                                      for _ in range(len(self.networks))]

        # リンクを重みの大きい順にソート
        links = []
        for i in range(len(networks)):
            for j in range(len(networks[i])):
                if self.is_capacity(i, j, network) and i < j:
                    heapq.heappush(links, (-networks[i][j], i, j))

        # リンクを大きい順に取り出し、経路を作成
        while links:
            # リンクを取り出す
            link = heapq.heappop(links)
            print(f"s_node: {link[1]}, e_node: {link[2]}, capacity: {-link[0]}")

            # 経路にリンクを追加
            networks[link[1]][link[2]] = -link[0]

            path = self.get_path(s_node, e_node, networks)
            if path:
                # 経路があれば、経路を返す
                return path

        # 経路がなければ、空リストを返す
        return []


if __name__ == "__main__":
    # ネットワークのインスタンスを作成
    network = Network()

    # 開始ノードと終了ノードを取得
    start_node, end_node = network.get_random_nodes()
    print(f"start_node: {start_node}, end_node: {end_node}")

    # start_nodeとend_nodeの間のpathを求める
    path = network.get_path(start_node, end_node, network.get())
    print(f"path: {path}")

    # # 最大路を求める
    # widest_path = network.widest_path_between(start_node, end_node)

    # # 結果を表示
    # print(f"Widest Path from Node {start_node} to Node {end_node}: {widest_path}")
