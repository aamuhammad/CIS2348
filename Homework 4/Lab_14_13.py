#Amaan Muhammad
#PSID: 1607608


num_calls = 0

def partition(user_ids, i, k):
    pivot = (i + k) // 2
    partition_index = i
    while(partition_index <= k):
        while(user_ids[partition_index] < user_ids[pivot]):
            partition_index = partition_index + 1
        while(user_ids[k] > user_ids[pivot]):
            k = k - 1
        if(partition_index <= k):
            t = user_ids[partition_index]
            user_ids[partition_index] = user_ids[k]
            user_ids[k] = t
            partition_index = partition_index + 1
            k = k - 1
    return partition_index

def quicksort(user_ids, i, k):
    global num_calls
    num_calls = num_calls + 1
    if(i >= k):
        return
    partition_index = partition(user_ids, i, k)
    quicksort(user_ids, i, partition_index - 1)
    quicksort(user_ids, partition_index, k)

if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()
    quicksort(user_ids, 0, len(user_ids) - 1)
    print(num_calls)
    for user_id in user_ids:
        print(user_id)
