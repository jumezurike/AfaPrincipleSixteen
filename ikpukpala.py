# Principle of 16 project. This is a harbinger of a powerful autonomy for users bringing in web3.
import random
from random import randint
from time import sleep

print("\nWelcome to Afa Oracle casting program:");

ikpukpala = ["ogbi", "akwu", "ogheli", "odii", "ululu", "aghali", "obala", "okala",
             "ijite", "ora", "aka", "atulukpa", "otule", "ete", "ose", "ovu"];
print ("\nShow the ikpukpala list:\n")
print(ikpukpala);


numbers = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
print ("\nShow the assigned numbers to the list:\n")
print(numbers);

print ("\nShow the truth table for 4 stringed nodes flips:\n")
H = int;
T = int;
H == 0;
T == 1;

combination = [
                ('H', 'H', 'H', 'H'),
                ('H', 'H', 'H', 'T'),
                ('H', 'H', 'T', 'T'),
                ('H', 'H', 'T', 'T'),
                ('H', 'T', 'H', 'H'),
                ('H', 'T', 'H', 'T'),
                ('H', 'T', 'T', 'H'),
                ('H', 'T', 'T', 'T'),
                ('T', 'H', 'H', 'H'),
                ('T', 'H', 'H', 'T'),
                ('T', 'H', 'T', 'H'),
                ('T', 'H', 'T', 'T'),
                ('T', 'T', 'H', 'H'),
                ('T', 'T', 'H', 'T'),
                ('T', 'T', 'T', 'H'),
                ('T', 'T', 'T', 'T')
              ];
print(combination);

print("\n");

print(combination[8]);

h_counts = 0;
t_counts = 0;
#def h_t(num_of_flips):
num_of_flips = int(input("\nPlease enter the number of flips:"))

for i in range(num_of_flips):
    rand = randint(0,1)
    sleep(1)
    if rand == 0:
            h_counts +=1;
            print("H");
    else:
            print("T")
            t_counts +=1;

print("\nThe result are:")
print("T", t_counts)
print("H", h_counts)
#Will have to create a list of the recorded cast outcomes
