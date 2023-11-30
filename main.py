from communication_manager import CommunicationManager as CM
from network import Network

if __name__ == "__main__":
    # 10000回の通信を実行
    network = Network()
    # TODO: アルゴリズムとパラメタnを変化させる
    cm = CM(algorithm=3, communication_time=10)
    cm.run()
