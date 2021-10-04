import matplotlib.pyplot as plt
import numpy as np
from os import close


file1 = open('Cupcakeinvoices.csv')

total =0
typeArr = []
amountArr = []
for invoice in file1:
    invoice = invoice.rstrip('\n').split(',')
    print(invoice[2])
    value = float(invoice[3])
    typeArr.append(invoice[2])
    amountArr.append(value)
    value2= float(invoice[4])
    sum =value * value2   
    print(sum)
    total += sum


print(round(total,2))
file1.close()
plt.scatter(amountArr, typeArr)
plt.bar(typeArr, amountArr)
plt.show()





