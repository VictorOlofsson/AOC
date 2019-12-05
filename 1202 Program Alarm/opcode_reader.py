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
            print(list)
            print("Unknown opcode, exiting")
            exit()
        i += 4
    return list

def find_noun_verb(list: list, file: str) -> int:
    list_cpy = list.copy()
    
    for i in range(0, len(list_cpy)):
        list_cpy[1] = i
        for y in range(0, len(list_cpy)):
            list_cpy[2] = y
            read_four(list_cpy)

            if(list_cpy[0] == 19690720):
                return list_cpy[1], list_cpy[2]
            else:
                list_cpy = list.copy()
                list_cpy[1] = i    

def main():
    # File to read
    file = "opcode.txt"
    list_from_file = read_file(file)
    # To find the correct answer part 1
    list_from_file[1] = 12
    list_from_file[2] = 2
    print("Correct value part1 is:", read_four(list_from_file)[0])

    # To find the correct answer part 2
    list_from_file = read_file(file)
    noun, verb = find_noun_verb(list_from_file,file)
    print("Noun:", noun)
    print("Verb:", verb)
    print("Correct value part2 is:", 100 * noun + verb)



    
    



if __name__== "__main__":
    main() 
