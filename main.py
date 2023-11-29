from network import Network
from communication_manager import CommunicationManager as CM


if __name__ == "__main__":
    # 10000回の通信を実行
    network = Network()
    network.show()
    network.show_current()
    # TODO: アルゴリズムとパラメタnを変化させる
    cm = CM(algorithm=4, communication_time=1)
    cm.run()
