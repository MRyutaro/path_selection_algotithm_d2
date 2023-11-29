import heapq
import random
from collections import deque

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

    def random_two_nodes(self) -> tuple[int, int]:
        """
        ランダムなノードを2つ返す.
        """
        node_num = len(self.networks)
        nodes = list(range(node_num))
        s_node, e_node = random.sample(nodes, 2)
        return s_node, e_node
    
    def adjacent_nodes(self, node: int, networks: list = None) -> list:
        """
        ノードに隣接するノードを取得する.

        node: ノード
        """
        if networks is None:
            networks = self.current_networks

        return [i for i, x in enumerate(networks[node]) if x > 0]

    def start(self, path: list) -> bool:
        """
        ネットワークの開始. 容量を減らす.

        path: 経路
        """
        # パスが空、すなわち経路がない場合は通信は失敗
        if len(path) == 0:
            return False

        # path上のすべてのリンクの容量が1以上あるか確認したあと、容量を1減らす
        for i in range(len(path)-1):
            if self.current_networks[path[i]][path[i+1]] < 1:
                return False

        # 容量を1減らす
        for i in range(len(path)-1):
            self.current_networks[path[i]][path[i+1]] -= 1
            self.current_networks[path[i+1]][path[i]] -= 1
            if self.current_networks[path[i]][path[i+1]] < 0:
                raise Exception("current_networksの容量が0以下です。")

        return True

    def end(self, path: list) -> None:
        """
        ネットワークの終了. 容量を増やす.

        path: 経路
        """
        # パスの容量を1増やす
        for i in range(len(path)-1):
            self.current_networks[path[i]][path[i+1]] += 1
            self.current_networks[path[i+1]][path[i]] += 1
            if self.current_networks[path[i+1]][path[i]] > self.networks[path[i+1]][path[i]]:
                raise Exception("current_networksの容量がnetworksの容量を超えています。")

    def capacity_between(self, s_node: int, e_node: int, networks: list = None) -> int:
        """
        ノード間の現在の容量を返す.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        if networks is None:
            networks = self.current_networks

        return networks[s_node][e_node]

    def is_capable(self, networks: list = None) -> bool:
        """
        ネットワークの容量があるか確認する.
        """
        if networks is None:
            networks = self.current_networks

        for i in range(len(networks)):
            for j in range(len(networks[i])):
                if i < j:
                    if self.is_capable_between(i, j, networks):
                        return True
        return False

    def is_capable_between(self, s_node: int, e_node: int, networks: list = None) -> bool:
        """
        ノード間に容量があるか確認する.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        if networks is None:
            networks = self.current_networks

        return self.capacity_between(s_node, e_node, networks) > 0

    def _path_between(self, s_node: int, e_node: int, networks: list, path: list = []) -> list:
        """
        s_nodeとつながっているノードを取得し、再帰的に探索. e_nodeが見つかれば経路を返す. 最短かどうかは保障しない.

        s_node: 開始ノード
        e_node: 終了ノード
        """
        if len(path) == 0:
            path.append(s_node)

        # 終了ノードに到達した場合は経路を返す
        if s_node == e_node:
            return path

        # s_nodeとつながっているノードを探索
        # TODO: adjacent_nodesを使えないか
        for node in range(len(networks[s_node])):
            if (node not in path) and (networks[s_node][node] > 0):
                # 再帰的に探索
                result = self._path_between(node, e_node, networks, path + [node])
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
            for neighbor in self.adjacent_nodes(current_node, networks):
                if neighbor not in path:
                    queue.append((neighbor, path + [neighbor]))

        # 終了ノードに到達できなかった場合は空のリストを返す
        return []

    def widest_path_between(self, s_node: int, e_node: int, networks: list) -> list:
        """
        ノード間の最大路(一番通信容量を大きくできる経路)を返す.

        s_node: 開始ノード
        e_node: 終了ノード
        networks: ネットワーク
        """
        # 空き容量がなければ、空リストを返す
        if not self.is_capable(networks):
            return []

        # G'を初期化
        more_than_max_networks = [[0 for _ in range(len(self.networks))]
                                    for _ in range(len(self.networks))]

        # リンクを重みの大きい順にソート
        links = []
        for i in range(len(networks)):
            for j in range(len(networks[i])):
                if i < j:
                    if self.is_capable_between(i, j, networks):
                        heapq.heappush(links, (-networks[i][j], i, j))

        # リンクを大きい順に取り出し、経路を作成
        while links:
            # リンクを取り出す
            link = heapq.heappop(links)

            # 経路にリンクを追加
            more_than_max_networks[link[1]][link[2]] = -link[0]
            more_than_max_networks[link[2]][link[1]] = -link[0]

            path = self._path_between(s_node, e_node, more_than_max_networks)
            if path:
                # 経路があれば、経路を返す
                return path

        # 経路がなければ、空リストを返す
        return []


if __name__ == "__main__":
    # ネットワークのインスタンスを作成
    network = Network()

    # 開始ノードと終了ノードを取得
    start_node, end_node = network.random_two_nodes()

    # 最大路を求める
    widest_path = network.widest_path_between(start_node, end_node, network.get())
    # 結果を表示
    print(f"Widest Path from Node {start_node} to Node {end_node}: {widest_path}")

    # 最短路を求める
    shortest_path = network.shortest_path_between(start_node, end_node, network.get())
    # 結果を表示
    print(f"Shortest Path from Node {start_node} to Node {end_node}: {shortest_path}")
