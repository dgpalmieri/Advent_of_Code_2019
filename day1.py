# day1.py
# Dylan Palmieri
# 12/04/19
# Catching up on Advent of Code 2019 day 1


def main():
    sum = 0
    with open('./input/day1.txt', 'r') as fp:
        for fuel in fp:
            round = int(int(fuel)/3) - 2
            sum += round
    print(sum)


main()
