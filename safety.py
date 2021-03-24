processes = 5

# processes all set to default false
finish = [False]*processes

capacity = [10, 5, 7]

max_array = [[7,5,3], [3,2,2], [9,0,2],[2,2,2],[4,3,3]]

allocation_array = [[0,1,0], [2,0,0], [3,0,2],[2,1,1], [0,0,2]]

need_array = [[7,4,3],[1,2,2],[6,0,0],[0,1,1],[4,3,1]]


# generate available resource units by comparing to allocated and capacity 
def generate_available(allocation_array, capacity_array):
    alArray = []
    available = []
    temp_sum = 0
    for j in range(len(allocation_array[0])):
        for i in range(len(allocation_array)):
            # print(i,j)
            temp_sum += allocation_array[i][j]
        
        alArray.append(temp_sum)
        temp_sum = 0
    # subtract from capacity
    for i in range(len(alArray)):
        available.append(capacity_array[i] - alArray[i])
    
    return available

# compare if the available is more or equal to need array
def compare_dif(a, b):
    sef = False
    for i in range(len(a)):
        if a[i] < b[i]:
            return False
        elif a[i] >= b[i]:
            pass
    return True
            

# create safety cycle
def safety_path(available, need):
    path = []
    available = generate_available(allocation_array, capacity)              # generate available resource units
    need = need_array
    
    counter = 0
    yallo = 0
    ballo = len(need)
    for j in range(len(need)):
        for i in range(yallo, ballo):
            if not finish[i] == True:                                       # only run for process with finish False
                if not(need[i] == [0]*len(need[i])):
                    if (compare_dif(available, need[i])) == True:
                        # add allocation to available
                        available = [available[t] + allocation_array[i][t] for t in range(len(available))]  # add the allocation to available once done
                        path.append("P" + str(i))
                        # set need[i] to 000
                        need[i] = [0]*len(need[i])
                        finish[i] = True
                        
                    if counter == len(need)-1:
                        break
                
        # if False in finish:
        #     break
    return path

def is_safe(path):
    if len(path) == processes:
        print("Yes, the system is safe, and the path is: ", path)
        return True
    print("No the system is unsafe.")
    return False
    
is_safe(safety_path(allocation_array, need_array))