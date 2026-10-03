import sys


def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage


def load_theta(path):
    try:
        with open(path) as f:
            content = f.read().strip()
    except FileNotFoundError:
        return 0.0, 0.0

    parts = content.split(",")
    if len(parts) != 2:
        raise ValueError(
            f"{path} の形式が不正です(theta0,theta1 の形式で保存されている必要があります)"
        )

    try:
        return float(parts[0]), float(parts[1])
    except ValueError:
        raise ValueError(f"{path} の内容が数値ではありません")


def parse_mileage(raw_input):
    try:
        mileage = float(raw_input)
    except ValueError:
        raise ValueError("走行距離は数値で入力してください")

    if mileage < 0:
        raise ValueError("走行距離は0以上の値を入力してください")

    return mileage


def main():
    try:
        theta0, theta1 = load_theta("theta.txt")
    except ValueError as e:
        print(f"エラー: {e}")
        sys.exit(1)

    raw_input = input("走行距離を入力してください: ")
    try:
        mileage = parse_mileage(raw_input)
    except ValueError as e:
        print(f"エラー: {e}")
        sys.exit(1)

    price = estimate_price(mileage, theta0, theta1)
    print(price)


if __name__ == "__main__":
    main()
