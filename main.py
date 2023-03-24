from timeit import default_timer as timer
import random
import BinaryTree as BT
import ListSort as LS
import RBtree as RB
import pickle

testList=[]
tree=BT.BinaryTree()
size=0

n_struct_data=10  # creo 15 istanze per ogni struct data   #15
n_times_plus=15 # numero di volte che aumento la dim di plus_dim  #20
plus_dim=100 # di quanto aumento la dimensione       #300
n_mis=10  # misuro 10 volte il tempo di os_select/rank per poi farne la media #30
n_test=3

#dati per numero di esecuzione/dimensione
def test_OS_Select(_list,_tree,_RBTree,i):
    times=[]
    #LIST
    start=timer()
    LS.OS_Select_list(_list,i)
    end=timer()
    times.append(end-start)
    #TREE
    start=timer()
    BT.OS_Select(_tree.elements[0],i)
    end=timer()
    times.append(end-start)
    #RB
    start=timer()
    RB.OS_SelectRB(_RBTree.elements[0],i+1) #sennò andrebbe alla foglia che è None
    end=timer()
    times.append(end-start)

    return times

def test_OS_Rank(_list,_tree,_RBTree,rL,RT,_RB):
    times=[]
    #LIST
    start=timer()
    LS.OS_Rank_list(_list,rL)
    end=timer()
    times.append(end-start)
    #TREE
    start=timer()
    BT.OS_Rank(_tree.elements[0],RT.key)
    end=timer()
    times.append(end-start)
    #RB
    start=timer()
    RB.OS_RankRB(_RBTree,_RB)
    end=timer()
    times.append(end-start)

    return times



def main():

    

    dim=[[] for i in range(n_times_plus)]
    listRes=[]#da togliere tanto faccio l'append in fondo
    treeRes=[]
    RB_Res=[]

    

    current_dim=0


    for i in range(n_times_plus): # ciclo per ogni dimensione
        current_dim+=plus_dim
        print(current_dim)
        #current_dim=10
        dim[i]=current_dim

        listRes_per_dim=[]
        treeRes_per_dim=[]
        RBRes_per_dim=[]

        for j in range(n_struct_data):  # ciclo per ogni struttura creata con la stessa dim
            
            tree=BT.BinaryTree()
            RBtree=RB.RBtree()
            myList=[]


            for new_el in range(current_dim):  #inzializzo e riempio le struct dati con un valore random
                val=random.randint(-5000,5000)
                #val=random.randint(0,10)
                tree.insert(val)
                RBtree.insert(val)
                myList.append(val)
            LS.list_merge_sorting(myList) #ordino la lista dopo che è piena
            
            ridx=random.randint(0,current_dim-1)
            randomTreeNode=tree.nodes[ridx]
            randomRBNode=RBtree.nodes[ridx]
            randomList=myList[ridx]
            
            Min_randomTreeNode=tree.Min(tree.elements[0])
            Min_randomRBNode=RBtree.Min(RBtree.elements[0])
            Min_randomList=myList[0]
            
            Max_randomTreeNode=tree.Max(tree.elements[0])
            Max_randomRBNode=RBtree.Max(RBtree.elements[0])
            Max_randomList=myList[len(myList)-1]  # ultimo elemento della lista
            
            misList=[]   #salvo i risultati di ogni misurazione cosi' ne faccio la media 
            misTree=[]
            misRB=[]

            # tree.showTreeInorder(tree.elements[0])
            # print(tree.Min(tree.elements[0]).key)
            # print(RBtree.Min(RBtree.elements[0]).key)
            # print(myList[0])

            for k in range(n_mis):
                
                # Test Standard
                #print('\n\nstd_test')
                #print('SEL')
                Select_res=test_OS_Select(myList,tree,RBtree,ridx)
                #print('Rank')
                Rank_res=test_OS_Rank(myList,tree,RBtree,randomList,randomTreeNode,randomRBNode)

                misList.append(Select_res[0])
                misList.append(Rank_res[0])
                misTree.append(Select_res[1])
                misTree.append(Rank_res[1])
                misRB.append(Select_res[2])
                misRB.append(Rank_res[2])

                # Test col Minimo
                #print('\nMin_test')
                
                #print('SEL')
                Select_res=test_OS_Select(myList,tree,RBtree,0) #inserisco il primo indice
                #print('Rank')
                Rank_res=test_OS_Rank(myList,tree,RBtree,Min_randomList,Min_randomTreeNode,Min_randomRBNode)

                misList.append(Select_res[0])
                misList.append(Rank_res[0])
                misTree.append(Select_res[1])
                misTree.append(Rank_res[1])
                misRB.append(Select_res[2])
                misRB.append(Rank_res[2])

                # Test col Max
                #print('\nMax_test')
                
                #print('SEL')
                Select_res=test_OS_Select(myList,tree,RBtree,len(myList)-1) #ultimo indice
                #print('Rank')
                Rank_res=test_OS_Rank(myList,tree,RBtree,Max_randomList,Max_randomTreeNode,Max_randomRBNode)
                

                misList.append(Select_res[0])
                misList.append(Rank_res[0])
                misTree.append(Select_res[1])
                misTree.append(Rank_res[1])
                misRB.append(Select_res[2])
                misRB.append(Rank_res[2])


            #finito questo ciclo avrò i n_mis tentativi dei risultati dai quali otterrò la media
            midList=get_mid_result(misList,n_mis,n_test)
            midTree=get_mid_result(misTree,n_mis,n_test)
            midRB=get_mid_result(misRB,n_mis,n_test)

            #aggiungo per ogni 'copia' di struttura dati la media dei n_mis tentativi sullo stesso oggetto
            for l in midList:listRes_per_dim.append(l)  
            for l in midTree:treeRes_per_dim.append(l)
            for l in midRB:RBRes_per_dim.append(l)
        # faccio la media delle medie per n_struct_data
        listRes_per=get_mid_result(listRes_per_dim,n_struct_data,n_test)
        treeRes_per=get_mid_result(treeRes_per_dim,n_struct_data,n_test)
        RBRes_per_=get_mid_result(RBRes_per_dim,n_struct_data,n_test)

        listRes.append(listRes_per)
        treeRes.append(treeRes_per)
        RB_Res.append(RBRes_per_)
        # print(listRes)
        # print(len(listRes))

    with open('list.pkl','wb') as ListRes_file:
        pickle.dump(listRes,ListRes_file)
    with open('tree.pkl','wb') as TreeRes_file:
        pickle.dump(treeRes,TreeRes_file)
    with open('RB.pkl','wb') as RBres_file:
        pickle.dump(RB_Res,RBres_file)

    

def get_mid_result(arr,n,n_test):
    _sum=[0 for j in range(2*n_test)]
    for i in range(0,n,2*n_test):
        for j in range(2*n_test):
            _sum[j]+=arr[i+j]
    
    for j in range(2*n_test):
            _sum[j]=_sum[j]/n
    return _sum











#RANDOM TREE
# for i in range(6):
#     num=random.randint(0,10)
#     tree.insert(num)

if __name__ == "__main__":
     main()