#!/bin/python

# Open a file in read mode
def read_file(file: str) -> []:
    f = open(file, "r")
    list = f.read().splitlines()
    f.close()
    return list

def calc_req(mass_list: str) -> int:
    sum_fuel = 0
    for mass in mass_list:
        fuel = (int(mass) // 3) - 2    
        sum_fuel += fuel
    
    # return the sum of fuel
    return sum_fuel

def main():
    # File to read
    file = "mass.txt"
    list_from_file = read_file(file)

    # Print sum of fuel
    print(calc_req(list_from_file))


if __name__== "__main__":
    main() 