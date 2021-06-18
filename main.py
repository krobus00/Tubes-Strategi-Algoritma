def SelectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx][1] > arr[j][1]:
                min_idx = j 
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def MaxActivities(arr):
    selected = []
    SelectionSort(arr)
    i = 0
    selected.append(arr[i]) 
    for j in range(1, len(arr)):
      if arr[j][0] >= arr[i][1]:
          selected.append(arr[j])
          i = j
    return selected
 

activity = [[5, 9], [1, 2], [3, 4], [0, 6],[5, 7], [8, 9]]
selected = MaxActivities(activity)
print("Following activities are selected :")
print(selected)