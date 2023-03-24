import random
def list_merge_sorting(arr):
     if len(arr) > 1:
  
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        list_merge_sorting(L)
  
        # Sorting the second half
        list_merge_sorting(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# funzioni da eseguire dopo che ho ordinato la lista
def OS_Select_list(arr,i):
    idx=0
    for value in arr:
        if i==idx:
            #print('List: '+str(value))
            return
        idx+=1
        
def OS_Rank_list(arr,target):
    idx=0
    for value in arr:
        
        if target==value:
            #print('List: '+str(idx))
            return 
        idx+=1



# testList=[]
# testList.append(8)
# testList.append(4)
# testList.append(8)
# testList.append(6)
# testList.append(1)
# testList.append(6)

# # for i in range(6):
# #     num=random.randint(0,60)
# #     testList.append(num)

# print('before sorting:  '+str(testList))
# list_merge_sorting(testList)
# print('after merge sorting: '+str(testList))

# # print('\nOS_select res:  '+str(OS_Select_list(testList,9)))
# # print('\nOS_rank res:  '+str(OS_Rank_list(testList,1)))