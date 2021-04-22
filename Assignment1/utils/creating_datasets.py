# imports random module
import random


# Opening a file
file = open("technical_domain_corpus.txt","rt")
counter = 0

f_train = open("train_technical.txt", "w")
f_test = open("test_technical.txt", "w")

for x in file:
    r1 = random.randint(1, 10)
    if(r1%2==0): f_train.write(x)
    elif(r1%2!=0 and counter<1000):
        f_test.write(x)
        counter+=1
    else: f_train.write(x)

print(counter)
