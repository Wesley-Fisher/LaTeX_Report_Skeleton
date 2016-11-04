import os
import sys
import time

dir_path = os.path.dirname(os.path.realpath(__file__))

input = input("Enter Section Name: ")

new_dir = dir_path + "/" + input

if os.path.exists(new_dir):
    print("Section Found!")
    time.sleep(2)
    exit()


os.makedirs(new_dir)

file = open(new_dir + "/_" + input + ".tex", "a")
file.writelines("\section{" + input + "TODO}")
    