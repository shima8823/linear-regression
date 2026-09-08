import csv


def load_data(path):
    mileages, prices = [], []
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            mileages.append(float(row["km"]))
            prices.append(float(row["price"]))
    return mileages, prices


def main():
    mileages, prices = load_data("data.csv")
    print(f"{len(mileages)} rows loaded")


if __name__ == "__main__":
    main()
