# path_selection_algotithm_d2

## 概要
経路選択アルゴリズムの実験用プログラム。経路選択アルゴリズムの動作を理解するとともに、その有効性を評価する方法について学ぶ。

## 環境
- Python 3.12.0
- pip 23.2.1
- matplotlib 3.8.2
- numpy 1.26.2
- pandas 2.1.3

## ディレクトリ構造とファイルの説明
```
C:.
│  .gitignore ---------------> git管理対象外のファイルやフォルダを指定するファイル
│  communication.py ---------> Communicationクラスを定義するファイル
│  communication_manager.py -> CommunicationManagerクラスを定義するファイル
│  evaluation_1.py -----------> 実験1の評価用のグラフを描画するときに実行するファイル
│  evaluation_2.py -----------> 実験2の評価用のグラフを描画するときに実行するファイル
│  main_1.py ----------------> 実験1を行うときに実行するファイル
│  main_2.py ----------------> 実験2を行うときに実行するファイル
│  network.py ---------------> Networkクラスを定義するファイル
│  README.md ----------------> 説明用ファイル
│  requirements.txt ---------> ライブラリを管理するファイル
│
└─data ----------------------> 出力結果を保管するフォルダ
```

## 動作方法
### 1. 必要なライブラリのインストール
```
pip install -r requirements.txt
```

### 2-1. 実験1
```
python main_1.py
```

### 2-2. 実験2
```
python main_2.py
```

### 3-1. 実験1に対する評価用グラフの描画
```
python evaluation_1.py
```

### 3-2. 実験2に対する評価用グラフの描画
```
python evaluation_2.py
```
