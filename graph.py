from main import n_struct_data,n_times_plus,n_test,n_mis,plus_dim
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pickle

ResList=pickle.load(open("list.pkl", "rb"))
ResTree=pickle.load(open("tree.pkl", "rb"))
ResRB=pickle.load(open("RB.pkl", "rb"))

fileRes=[ResList,ResTree,ResRB]

legend=["standard","Min","Max"]

for l in range(0,3):
    fig=plt.figure(l+1)
    if l==0:
        currentFile=ResList
        name='List'
    if l==1:
        currentFile=ResTree
        name='Tree'
    if l==2:
        currentFile=ResRB
        name='RBTree'

    plt.style.use('ggplot')

    x_ax=[]
    current=0
    for i in range(n_times_plus):
        current=current+plus_dim
        x_ax.append(current)

    axes=x_ax
    plt.subplot(221)
    plt.title( name+' OS-Select')
    plt.xlabel('dimension')
    plt.ylabel('time')

    for k in range(0,n_test):
        plt.plot(axes,[val[2*k] for val in currentFile])

    plt.legend(legend)


    plt.subplot(222)
    plt.title( name+' OS-Rank')
    plt.xlabel('dimension')
    plt.ylabel('time')

    for k in range(0,n_test):
        plt.plot(axes,[val[(2*k)+1] for val in currentFile])

    plt.legend(legend)

    plt.savefig(f'GRAPHS/{name}.png')
    plt.clf()
# PER OGNI TEST FACCIO DELLE FIGURE IN CUI CONFRONTO LE DUE FUNZIONI SULLE STRUCT DIVERSE


legend=["List","Tree","RBTree"]

for i in range(0,n_test):
    fig=plt.figure(i+1)
    fig.tight_layout(pad=0.05)
    x_ax=[]
    current=0
    for j in range(n_times_plus):
        current=current+plus_dim
        x_ax.append(current)

    axes=x_ax
    plt.subplot(221)
    plt.title(f'OS-Select test-{i+1}')
    plt.xlabel('dimension')
    plt.ylabel('time')

    for res in fileRes: #scorre per i risultati
        plt.plot(axes,[val[i*2] for val in res])
        
    plt.legend(legend)

    

    plt.subplot(222)
    plt.title(f'OS-Rank test-{i+1}')
    plt.xlabel('dimension')
    plt.ylabel('time')

    for res in fileRes: #scorre per i risultati
        plt.plot(axes,[val[(i*2)+1] for val in res])
        
    plt.legend(legend)
    plt.savefig(f'GRAPHS/test-{i+1}.png')
    plt.clf()


for i in range(0,n_test):
    fig=plt.figure(i+1)
    #fig.suptitle(f'OS-Select:  test{i+1}', fontsize=16)
    fig.tight_layout(pad=0.1)
    x_ax=[]
    current=0
    for j in range(n_times_plus):
        current=current+plus_dim
        x_ax.append(current)

    axes=x_ax
    
    #plt.subplot(131)
    plt.style.use('ggplot')
    plt.title(f'OS-Select List')
    plt.xlabel('dimension')
    plt.ylabel('time')
    
        #scorre per i risultati
    plt.plot(axes,[val[i*2] for val in ResList])
    plt.savefig(f'GRAPHS/SelectList-test-{i+1}.png')
    plt.clf()




    #plt.subplot(132)
    plt.style.use('ggplot')
    plt.title(f'OS-Select Tree')
    plt.xlabel('dimension')
    plt.ylabel('time')

        #scorre per i risultati
    plt.plot(axes,[val[i*2] for val in ResTree])
    plt.savefig(f'GRAPHS/SelectTree-test-{i+1}.png')
    plt.clf()



   # plt.subplot(133)
    plt.style.use('ggplot')
    plt.title(f'OS-Select RBTree')
    plt.xlabel('dimension')
    plt.ylabel('time')

        #scorre per i risultati
    plt.plot(axes,[val[i*2] for val in ResRB])
    plt.savefig(f'GRAPHS/SelectRB-test-{i+1}.png')
    plt.clf()

    #plt.subplot(131)
    plt.style.use('ggplot')
    plt.title(f'OS-Rank List')
    plt.xlabel('dimension')
    plt.ylabel('time')

        #scorre per i risultati
    plt.plot(axes,[val[(i*2)+1] for val in ResList])
    plt.savefig(f'GRAPHS/RankList-test-{i+1}.png')
    plt.clf()



    #plt.subplot(132)
    plt.style.use('ggplot')
    plt.title(f'OS-Rank Tree')
    plt.xlabel('dimension')
    plt.ylabel('time')

        #scorre per i risultati
    plt.plot(axes,[val[(i*2+1)] for val in ResTree])
    plt.savefig(f'GRAPHS/RankTree-test-{i+1}.png')
    plt.clf()


    #plt.subplot(133)
    plt.style.use('ggplot')
    plt.title(f'OS-Rank RBTree')
    plt.xlabel('dimension')
    plt.ylabel('time')

        #scorre per i risultati
    plt.plot(axes,[val[(i*2+1)] for val in ResRB])
    #plt.clf()
    plt.savefig(f'GRAPHS/RankRB-test-{i+1}.png')
    plt.clf()
    
#plt.show()
