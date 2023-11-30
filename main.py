from communication_manager import CommunicationManager as CM
from network import Network

if __name__ == "__main__":
    # 10000回の通信を実行
    network = Network()
    # TODO: アルゴリズムとパラメタnを変化させる
    cm = CM(algorithm=1, service_time=20)
    cm.run()
