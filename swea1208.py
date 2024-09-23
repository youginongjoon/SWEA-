T = 10

for test_case in range(1, T + 1):
    dmp = int(input())
    # 배열에 입력된 높이값 담기 (100개가 담김)
    arr = list(map(int, input().split()))
    result = 0
    for _ in range(dmp):
        # 배열에서 가장 큰 값 (높은 곳) 을 max_height 변수에 넣기
        max_height = max(arr)
        # 가장 낮은 곳을 min_height 변수에 넣기
        min_height = min(arr)

        # 인덱스 찾기 해서 값이 max_height인 곳과 값이 min_height인 곳의 인덱스를 찾고, 큰값에서 -1 작은값에 +1
        max_index = arr.index(max_height)  # 최대값의 인덱스 찾기
        min_index = arr.index(min_height)  # 최소값의 인덱스 찾기
        arr[max_index] -= 1
        arr[min_index] += 1

    # 최종적으로 배열에서 가장 큰 값과 가장 작은 값의 차이를 계산
    max_height = max(arr)
    min_height = min(arr)
    result = max_height - min_height

    print(f"#{test_case} {result}")




## sort 사용으로 최댓값은 0인덱스, 최솟값은 -1 인덱스로 가는 성질을 이용한 풀이 ##

T = 10

for test_case in range(1, T + 1):
    dmp = int(input())
    nums = list(map(int, input().split()))

    for x in range(dmp):
        nums.sort()
        nums[0] += 1
        nums[-1] -= 1
    print(f"#{test_case} {max(nums)-min(nums)}")