# ft_linear_regression

走行距離(mileage)から車の価格(price)を予測する、単回帰モデルを勾配降下法で実装した課題。

## 使い方

### 学習

`data.csv`(`km,price`の2列)を読み込み、勾配降下法で`theta0`, `theta1`を求めて`theta.txt`に保存する。

```bash
uv run train.py
```

### 予測

走行距離を入力すると、学習済みの`theta.txt`(なければ`theta0=theta1=0`)を使って価格を推定する。

```bash
uv run predict.py
```

### グラフ表示

データの散布図と回帰直線を表示する。

```bash
uv run plot.py
```

### 精度評価

RMSEとR2を計算して表示する。

```bash
uv run evaluate.py
```
