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

def calc_true(mass_list: str) -> int:
    sum_fuel = 0
    for mass in mass_list:
        fuel = (int(mass) // 3) - 2
        if (fuel > 0):
            sum_fuel += fuel
            fuel_added = fuel
            #print("Fuel added: ", fuel_added)
            while (fuel_added>0):
                fuel_added = (fuel_added // 3) - 2
                if (fuel_added < 0):
                    fuel_added = 0
                #print("Fuel added: ", fuel_added)
                
                sum_fuel += fuel_added
    # return the sum of fuel
    return sum_fuel


def main():
    # File to read
    file = "mass.txt"
    list_from_file = read_file(file)

    # Print sum of fuel
    print(calc_req(list_from_file))
    print(calc_true(list_from_file))


if __name__== "__main__":
    main() 