def binary_search(arr, l, r, value):
    while (l <= r):
        mid = l + (r-l) // 2
        if arr[mid] == value:
            return mid

        if arr[mid] < value:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def binary_search_recur(arr, l, r, value):
    mid = l + (r - l) // 2

    if arr[mid] == value:
        return mid
    
    if l == r: 
        return -1

    if arr[mid] < value:
        return binary_search_recur(arr, mid+1, r, value)

    else:
        return binary_search_recur(arr, l, mid-1, value)

if __name__ == "__main__":

    array = [10, 20, 30, 48, 53, 13, 589]
    array.sort()
    print("here is the array: ", array)

       
    print(binary_search(array, 0, len(array)-1, 20))
    print(binary_search(array, 0, len(array)-1, 589))
    print(binary_search(array, 0, len(array)-1, 100))
    print(binary_search(array, 0, len(array)-1, 13))
    print(binary_search(array, 0, len(array)-1, 48))

    print("now lets do it recursively")
    print(binary_search_recur(array, 0, len(array)-1, 20))
    print(binary_search_recur(array, 0, len(array)-1, 589))
    print(binary_search_recur(array, 0, len(array)-1, 100))
    print(binary_search_recur(array, 0, len(array)-1, 13))
    print(binary_search_recur(array, 0, len(array)-1, 48))
    
