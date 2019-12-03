#!/bin/python

def read_file(file: str) -> []:
    f = open(file, "r")
    list = f.read().splitlines()
    f.close()
    return list

def calc_req(mass_list: str) -> int:
    sum_fuel = 0
    # Test
    test = 0
    for mass in mass_list:
        (int(mass) // 3)    
    

def main():
    file = "mass.txt"
    list_from_file = read_file(file)
    print(list_from_file)

if __name__== "__main__":
    main() 