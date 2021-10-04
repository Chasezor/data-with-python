#imports
import matplotlib.pyplot as plt
import numpy as np
from os import close

#File
file1 = open('Cupcakeinvoices.csv')

#Variables
total =0
typeArr = []
amountArr = []

#Logic
for invoice in file1:
    invoice = invoice.rstrip('\n').split(',')
    print(invoice[2])
    value = float(invoice[3])
    typeArr.append(invoice[2])
    value2= float(invoice[4])
    sum =value * value2   
    amountArr.append(sum)
    print(sum)
    total += sum

#Execution
print(round(total,2))
file1.close()
#plt.scatter(np.array(typeArr), np.array(amountArr))
plt.bar(np.array(typeArr), np.array(amountArr))
plt.show()





