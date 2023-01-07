import os
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import string 
import sys
fileLoc = 'data/names/test.txt'
fileLoc1= 'data/TrainEval/filterBD.txt'
fileFiltered = open(fileLoc1, "a")
special_characters = "!@#$%^&*()-+?_=,<>/"
f = open('data/names/test.txt', 'r+')
data = f.readlines()
Nb_password=len(data)
password_length=[]
for f in data:
    password_length.append(len(f)-1)
    #print(stringPassword(f))
#print(password_length)
avg = np.mean(password_length)
#print("moyenne = ",avg)
print("max=",max(password_length))
max_length=max(password_length)
axis=[]
ordo=[]
for i in range(1,max(password_length)):
    axis.append(i)
    ordo.append(password_length.count(i))
    print(i,password_length.count(i))
plt.xlabel('Taille des mot de passe.')
plt.ylabel('Nombre d\'occurance')
plt.bar(axis, ordo)
plt.show()

longueur_totale=max_length

def only_digits(file):
    count = 0
    global longueur_totale
    file = open(file, 'r')
    lines = file.readlines()
    data=[]
    print("password with Number :\n")
    for line in lines:
        line2 = line.strip()
        x = line2.isdigit()
        if (x == True):
            #print(line2)
            if len(line2) < 9:
                fileFiltered.write(line2+"\n")
            count = count + 1
            data.append(line2)
    return count,data   
only_digits(fileLoc)
def only_letters(file):
    count = 0
    global longueur_totale
    file = open(file, 'r')
    lines = file.readlines()
    data=[]
    print("password with Letters only  :\n")
    for line in lines:
        line2 = line.strip()
        x = line2.isalpha()
        if (x == True):
            #print(line2)
            if len(line2) < 9:
                fileFiltered.write(line2+"\n")
            count = count + 1
            data.append(line)
    return count,data
 
only_letters(fileLoc)

def onlyNumletter(file):
    count = 0
    global longueur_totale
    file = open(file, 'r')
    lines = file.readlines()
    data=[]
    print("password with Number and Letter only :\n")
    for line in lines:
        line2 = line.strip()
        x = line2.isalnum()
        if (x == True):
            if len(line2) < 9:
                fileFiltered.write(line2+"\n")
            #print(line2)
            count = count + 1
            data.append(line)
    return count,data
onlyNumletter(fileLoc)
def only_specchar(file):
    file = open(file, 'r')
    lines = file.readlines()
    invalidcharacters= set(string.punctuation)
    count=0
    data=[]
    print("password with spec char :\n")
    for line in lines:
        line2 = line.strip()
        if any(char in invalidcharacters for char in line2):
            #print(line2)
            count = count + 1
            data.append(line)
    return count,data
print(only_specchar(fileLoc))
#
Number=only_digits(fileLoc)[0]
Letters=only_letters(fileLoc)[0]
NumberAndLetter=onlyNumletter(fileLoc)[0]
SpecialsChars=only_specchar(fileLoc)[0]
print("Nb_pwd =",Nb_password,"\n")
print("% Number =",(Number / Nb_password)*100,"% .Letter" ,(Letters/Nb_password)*100,"% Num Letter",(NumberAndLetter/Nb_password)*100,"%Spec_char",(SpecialsChars/Nb_password)*100)
sys.exit()
labels = 'Number', 'Letters', 'NumberAndLetter', 'SpecialsChars'

sizes = [Number, Letters, NumberAndLetter, SpecialsChars]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
#Fonction de répartition 
max_length=max(password_length)
axis=[]
ordo=[]
somme=0
for i in range(1,max(password_length)):
    axis.append(i)
    somme=somme+password_length.count(i)
    ordo.append(somme)
print(max(password_length))
#print(ordo)
plt.xlabel('Taille des mot de passe.')
plt.ylabel('Nombre d\'occurance')
plt.bar(axis, ordo)
plt.show()

"""
def filterDatabase(path):    
    with open(path, 'r') as file:
        data = only_digits(path)[1]
    with open(path, 'w') as file:
        for pwd in data:
            file.write(pwd)
filterDatabase(fileLoc)
"""