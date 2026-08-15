def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage


def main():
    theta0 = 0
    theta1 = 0

    mileage = float(input("走行距離を入力してください: "))
    price = estimate_price(mileage, theta0, theta1)
    print(price)


if __name__ == "__main__":
    main()
