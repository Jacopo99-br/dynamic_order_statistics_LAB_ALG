import csv 
import pickle
from main import n_times_plus,plus_dim

ResList=pickle.load(open("list.pkl", "rb"))
ResTree=pickle.load(open("tree.pkl", "rb"))
ResRB=pickle.load(open("RB.pkl", "rb"))

header=['dim','List','Tree','RBTree']

# per ogni test salvo i risultati di ogni struct data

def save_in_csv(filename):
    
    test=int(filename.split('_')[1])  ## prendo il numero del test
    test=test-1

    with open(f'{filename}_Select.csv','w') as file:
        writer = csv.writer(file)

        # write the header
        writer.writerow(header)

        current=0

        for i in range(n_times_plus):
            data=[]
            current=current+plus_dim
            data.append(current)
            data.append(ResList[i][test*2])
            data.append(ResTree[i][test*2])
            data.append(ResRB[i][test*2])

            writer.writerow(data)

    with open(f'{filename}_Rank.csv','w') as file:
        writer = csv.writer(file)

        # write the header
        writer.writerow(header)

        current=0

        for i in range(n_times_plus):
            data=[]
            current=current+plus_dim
            data.append(current)
            data.append(ResList[i][(test*2)+1])
            data.append(ResTree[i][(test*2)+1])
            data.append(ResRB[i][(test*2)+1])

            writer.writerow(data)



save_in_csv('test_1')
save_in_csv('test_2')
save_in_csv('test_3')