def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage


def load_theta(path):
    try:
        with open(path) as f:
            theta0, theta1 = f.read().split(",")
            return float(theta0), float(theta1)
    except FileNotFoundError:
        return 0.0, 0.0


def main():
    theta0, theta1 = load_theta("theta.txt")

    mileage = float(input("走行距離を入力してください: "))
    price = estimate_price(mileage, theta0, theta1)
    print(price)


if __name__ == "__main__":
    main()
