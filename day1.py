# day1.py
# Dylan Palmieri
# 12/04/19
# Catching up on Advent of Code 2019 day 1


def main():
    sum = 0
    with open('./input/day1.txt', 'r') as fp:
        for fuel in fp:
            round = int(fuel)
            while True:
                round = int(round/3) - 2
                if round < 0:
                    break
                sum += round
    print(sum)


main()
