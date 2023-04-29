import random
f = open("input/in5.txt", "w")
n = int(input("input a number"))
f.write(str(n) + "\n")
for _ in range(n):
    string = str(random.randint(0, 30)) + " " + str(random.randint(0, 30)) + "\n"
    f.write(string)