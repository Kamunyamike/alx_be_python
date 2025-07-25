import csv

def main():
    with open("items.csv", "r") as file:
        f = csv.reader(file)
        for row in f:
            # name, price, quantity = row
            print(row)


if __name__ == "__main__":
    main()