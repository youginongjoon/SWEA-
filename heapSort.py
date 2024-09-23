def heapify(arr, n, i):
    while True:
        largest = i  # 루트를 최대값으로 가정
        l = 2 * i + 1  # 왼쪽 자식
        r = 2 * i + 2  # 오른쪽 자식

        # 왼쪽 자식이 루트보다 크다면
        if l < n and arr[l] > arr[largest]:
            largest = l

        # 오른쪽 자식이 현재 최대값보다 크다면
        if r < n and arr[r] > arr[largest]:
            largest = r

        # 최대값이 루트가 아니라면 교환
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # 교환
            i = largest  # 교환 후 힙을 다시 정렬
        else:
            break

def heap_sort(arr):
    n = len(arr)

    # 최대 힙을 구축
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 하나씩 요소를 추출하여 정렬 배열의 마지막 요소와 루트를 교환하고 힙의 크기를 줄여가며 heapify를 호출하여 정렬
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

# 예제 사용법
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("정렬된 배열:", arr)
