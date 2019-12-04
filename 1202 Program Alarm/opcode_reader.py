#!/bin/python

# Open a file in read mode
def read_file(file: str) -> []:
    f = open(file, "r")
    list = f.read().split(',')
    f.close()

    # Convert to list of ints
    for nr in range(0, len(list)):
        list[nr] = int(list[nr])
    
    return list

def read_four(list: list) -> []:
    i = 0
    nr_opcodes = (len(list) // 4)

    while(i<=nr_opcodes*4):
        if(list[i] == 99):
            return list
        elif(list[i] == 1):
            index1 = list[i+1]
            index2 = list[i+2]
            index3 = list[i+3]
            list[index3] = list[index1] + list[index2]
        
        elif(list[i] == 2):
            index1 = list[i+1]
            index2 = list[i+2]
            index3 = list[i+3]
            list[index3] = list[index1] * list[index2]

        else:
            print("Unknown opcode, exiting")
            exit()
        i += 4
    return list

def main():
    # File to read
    file = "opcode.txt"
    list_from_file = read_file(file)
    print("Correct value is: ", read_four(list_from_file)[0])



if __name__== "__main__":
    main() 
