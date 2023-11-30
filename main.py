from communication_manager import CommunicationManager as CM
from network import Network

if __name__ == "__main__":
    # 10000回の通信を実行
    network = Network()
    # TODO: アルゴリズムとパラメタnを変化させる
    cm = CM(algorithm=3, service_time=20, arrival_interval=1)
    # TODO: ここで指数分布に従う通信時間と通信の到着間隔をcmの外側から設定できるようにする
    # TODO: CMの引数としては固定の値、その中の初期値はそれぞれ1にする。
    cm.run()
