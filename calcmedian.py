#CALC MEDIAN
import sys
import subprocess

def temptocelcius(temp):
    celcius = temp/10
    return celcius

def adjustscale(data):
    pass

def calcmed(name):
    med = 0
    count = 0
    total = []

    filename = "out"+name+".txt"
    with open(filename,"r") as file:
        for i in file:
            line = file.readline()
            if line == "":
                break
            if line == "\n":
                break
            else:
                total.append(line.strip())
                count += 1
    
    #IF EVEN
    if(count != 0):
        if((count%2) == 0):
            med = ((int(total[int(count/2)]) + int(total[int(count/2)+1]))/2)
        else:
            med = (int(total[int(count/2)])) 
    else:
        med = 0

if __name__ == "__main__":
    calcmed(sys.argv[1])

