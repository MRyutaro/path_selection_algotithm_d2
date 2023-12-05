from collections import deque
import numpy as np
import random


class Network():
    """
    ネットワークを表すオブジェクト。
    """
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
        self.current_networks = self.networks.copy()

    def get(self) -> list:
        return self.networks

    def show(self) -> None:
        print("networks")
        for i in range(len(self.networks)):
            print(self.networks[i])

    def get_current(self) -> list:
        return self.current_networks

    def show_current(self) -> None:
        print("current_networks")
        for i in range(len(self.current_networks)):
            print(self.current_networks[i])

    def random_two_nodes(self) -> tuple[int, int]:
        """
        ランダムなノードを2つ返す.
        """
        node_num = len(self.networks)
        nodes = list(range(node_num))
        s_node, e_node = random.sample(nodes, 2)
        return s_node, e_node

    def adjacent_nodes(self, node: int, networks: list = []) -> list:
        """
        ノードに隣接するノードを取得する.

        引数
        - node: ノード
        """
        if networks == []:
            networks = self.current_networks

        # 隣接しているノードのインデックスを取得
        adjacent_nodes = [i for i, weight in enumerate(networks[node]) if weight > 0]
        # ランダムに並び替え
        random.shuffle(adjacent_nodes)
        return adjacent_nodes

    def start(self, path: list) -> bool:
        """
        ネットワークの開始. 容量を減らす.

        引数
        - path: 経路
        """
        # パスが空、すなわち経路がない場合は通信は失敗
        if len(path) == 0:
            return False

        # path上のすべてのリンクの容量が1以上あるか確認したあと、容量を1減らす
        for i in range(len(path) - 1):
            if self.current_networks[path[i]][path[i + 1]] < 1:
                return False

        # networkの総和を計算
        # sum_network = sum([sum(row) for row in self.current_networks])
        # print(f"sum_network: {sum_network/2}")

        # 容量を1減らす
        for i in range(len(path) - 1):
            self.current_networks[path[i]][path[i + 1]] -= 1
            self.current_networks[path[i + 1]][path[i]] -= 1
            if self.current_networks[path[i]][path[i + 1]] < 0:
                raise Exception("current_networksの容量が0以下です。")


        return True

    def end(self, path: list) -> None:
        """
        ネットワークの終了. 容量を増やす.

        引数
        - path: 経路
        """
        # パスの容量を1増やす
        for i in range(len(path) - 1):
            self.current_networks[path[i]][path[i + 1]] += 1
            self.current_networks[path[i + 1]][path[i]] += 1
            if self.current_networks[path[i + 1]][path[i]] > self.networks[path[i + 1]][path[i]]:
                raise Exception("current_networksの容量がnetworksの容量を超えています。")

    def capacity_between(self, s_node: int, e_node: int, networks: list = []) -> int:
        """
        ノード間の現在の容量を返す.

        引数
        - s_node: 開始ノード
        - e_node: 終了ノード
        - networks: ネットワーク (デフォルトは現在のネットワーク)
        """
        if networks == []:
            networks = self.current_networks

        return networks[s_node][e_node]

    def is_capable(self, networks: list = []) -> bool:
        """
        ネットワークの容量があるか確認する.
        """
        if networks == []:
            networks = self.current_networks

        # networksの中身がすべて0なら容量がない
        return not np.all(np.array(networks) == 0)

    def is_capable_between(self, s_node: int, e_node: int, networks: list = []) -> bool:
        """
        ノード間に容量があるか確認する。

        引数
        - s_node: 開始ノード
        - e_node: 終了ノード
        - networks: ネットワーク (デフォルトは現在のネットワーク)
        """
        if networks == []:
            networks = self.current_networks

        return self.capacity_between(s_node, e_node, networks) > 0

    def path_between(self, s_node: int, e_node: int, networks: list) -> list:
        """
        s_nodeとe_nodeの間の経路を返す。深さ優先探索を使用。スタックを用いる。

        引数
        - s_node: 開始ノード
        - e_node: 終了ノード
        - networks: ネットワーク
        """
        # 空き容量がなければ、空リストを返す
        if not self.is_capable(networks):
            return []

        # スタックの初期化
        stack = deque([(s_node, [s_node])])

        while stack:
            current_node, path = stack.pop()

            # 終了ノードに到達したら経路を返す
            if current_node == e_node:
                return path

            # 隣接ノードを探索
            neighbors = self.adjacent_nodes(current_node, networks)
            for neighbor in neighbors:
                if neighbor not in path:
                    stack.append((neighbor, path + [neighbor]))

        # 終了ノードに到達できなかった場合は空のリストを返す
        return []

    def shortest_path_between(self, s_node: int, e_node: int, networks: list) -> list:
        """
        ノード間の最小ホップ経路を返す。幅優先探索を使用。キューを用いる。

        引数
        - s_node: 開始ノード
        - e_node: 終了ノード
        - networks: ネットワーク
        """
        # 空き容量がなければ、空リストを返す
        if not self.is_capable(networks):
            return []

        # キューの初期化
        queue = deque([(s_node, [s_node])])

        while queue:
            current_node, path = queue.popleft()

            # 終了ノードに到達したら経路を返す
            if current_node == e_node:
                return path

            # 隣接ノードを探索
            neighbors = self.adjacent_nodes(current_node, networks)
            for neighbor in neighbors:
                if neighbor not in path:
                    queue.append((neighbor, path + [neighbor]))

        # 終了ノードに到達できなかった場合は空のリストを返す
        return []

    def widest_path_between(self, s_node: int, e_node: int, networks: list) -> list:
        """
        ノード間の最大路を返す。

        引数
        - s_node: 開始ノード
        - e_node: 終了ノード
        - networks: ネットワーク
        """
        # 空き容量がなければ、空リストを返す
        if not self.is_capable(networks):
            return []

        # G'を初期化
        more_than_max_networks = [
            [0 for _ in range(len(self.networks))] for _ in range(len(self.networks))
        ]

        # リンクを重みの大きい順にソート。ネットワーク容量がキー、(開始ノード、終了ノード)が値の辞書型にする
        weight_sorted_links = {}
        for i, row in enumerate(networks):
            for j in range(i + 1, len(networks)):
                    if row[j] > 0:
                        weight = row[j]
                        if weight not in weight_sorted_links:
                            weight_sorted_links[weight] = [(i, j)]
                        else:
                            weight_sorted_links[weight].append((i, j))

        # リンクを大きい順に取り出し、経路を作成
        for weight in sorted(weight_sorted_links.keys(), reverse=True):
            # 最大容量のリンクをすべて取り出す
            links = weight_sorted_links[weight]
            # G'にリンクを追加
            for link in links:
                s_node, e_node = link
                more_than_max_networks[s_node][e_node] = weight
                more_than_max_networks[e_node][s_node] = weight
            # 経路を作成
            path = self.path_between(s_node, e_node, more_than_max_networks)
            # 経路があれば、経路を返す
            if path:
                return path

        # 経路がなければ、空リストを返す
        return []

    def shortest_widest_path_between(self, s_node: int, e_node: int, networks: list) -> list:
        """
        ノード間の最短最大路を返す。
        
        引数
        - s_node: 開始ノード
        - e_node: 終了ノード
        - networks: ネットワーク
        """
        # 空き容量がなければ、空リストを返す
        if not self.is_capable(networks):
            return []

        # G'を初期化
        more_than_max_networks = [
            [0 for _ in range(len(self.networks))] for _ in range(len(self.networks))
        ]

        # リンクを重みの大きい順にソート。ネットワーク容量がキー、(開始ノード、終了ノード)が値の辞書型にする
        weight_sorted_links = {}
        for i, row in enumerate(networks):
            for j in range(i + 1, len(networks)):
                    if row[j] > 0:
                        weight = row[j]
                        if weight not in weight_sorted_links:
                            weight_sorted_links[weight] = [(i, j)]
                        else:
                            weight_sorted_links[weight].append((i, j))

        # リンクを大きい順に取り出し、経路を作成
        for weight in sorted(weight_sorted_links.keys(), reverse=True):
            # 最大容量のリンクをすべて取り出す
            links = weight_sorted_links[weight]
            # G'にリンクを追加
            for link in links:
                s_node, e_node = link
                more_than_max_networks[s_node][e_node] = weight
                more_than_max_networks[e_node][s_node] = weight
            # 最小ホップ経路を作成
            shortest_path = self.shortest_path_between(s_node, e_node, more_than_max_networks)
            # 経路があれば、経路を返す
            if shortest_path:
                return shortest_path

        # 経路がなければ、空リストを返す
        return []


if __name__ == "__main__":
    import datetime

    # ネットワークのインスタンスを作成
    network = Network()

    now = datetime.datetime.now()

    for _ in range(10000):
        # 開始ノードと終了ノードを取得
        start_node, end_node = network.random_two_nodes()

        # ==========
        # 深さ優先探索で経路を求める
        path = network.path_between(start_node, end_node, network.get())
        # 結果を表示
        # print(f"Path from Node {start_node} to Node {end_node}: {path}")
        # ==========

        # ==========
        # # 幅優先探索で最小ホップ経路を求める
        # shortest_path = network.shortest_path_between(start_node, end_node, network.get())
        # # 結果を表示
        # print(f"Shortest Path from Node {start_node} to Node {end_node}: {shortest_path}")
        # ==========

        # ==========
        # # 最大路を求める
        # widest_path = network.widest_path_between(start_node, end_node, network.get())
        # # 結果を表示
        # print(f"Widest Path from Node {start_node} to Node {end_node}: {widest_path}")
        # ==========

    print(f"time: {datetime.datetime.now() - now}")


if __name__ == "__main__":
    network = Network()
    s_node, e_node = network.random_two_nodes()
    print(f"start_node: {s_node}, end_node: {e_node}")

    widest_path_between = network.widest_path_between(s_node, e_node, network.get())
