import matplotlib.pyplot as plt
import pandas as pd
import ast

list = []
with open("loss.txt", mode='r') as f:
    for a in f:
        list.append(ast.literal_eval(a))


f.close()

df = pd.DataFrame(list)

print(df)

fig = plt.figure()

ax = fig.add_subplot(111,xlim=(0,10),ylim=(0,7),xlabel='epoch',ylabel='loss')

ax.plot(df['epoch'], df['loss'])

plt.show()



