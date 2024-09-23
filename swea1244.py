## 내 처음 접근 ## (X)
from tabnanny import check

# 계수정렬을 통해서 정렬하고, 그 갯수를 알아냄
# 갯수를 알면, 그걸 가지고 숫자를 재배치함
# 원래의 수와 비교해서 몇번 최소로 바꿔야 결과와 같아지는지 확인하고, 그 수를 전체 교환해야하는 횟수에서 차감
# 만약 짝수번이 남았다면 그냥 무시해줘도 됌
# 홀수번이 남고, 2개 이상인 수가 없으면, 1의자리와 10의 자리 수를 한 번 바꾼 것이 결과
# 그렇다면, 최대값을 만들기 위해 최소 몇번 교환해야하는지는 어떻게 알지?



## 너비우선탐색을 이용한 풀이 ##
T = int(input())

for test_case in range(1, T+1) :
    board, n = input().split()
    n = int(n)
    now = set([board])
    next = set()

    for _ in range(n) :
        while now :
            s = now.pop()
            s = list(s)

            for i in range(len(board) - 1) :
                for j in range(i+1, len(board)) :
                    s[i], s[j] = s[j], s[i]
                    next.add(''.join(s))
                    s[i], s[j] = s[j], s[i]

        # 이제 while을 다 돌고, 하나의 깊이에 대해서 모든 경우를 set에 추가했다. 그 결과는 next에 있고, 이젠 그 경우 하나하나를 또 now에 놓고 돌려야한다. -> 너비우선탐색 = 얼음얼리는 문제와 유사한 방식

        next, now = now, next

    # 이제 모든 경우의 수 값들이 now에 담겨있다. 이제 max()를 이용해서 큰 값 하나를 뽑아주면 된다.
    anser = max(map(int, now))




## 깊이우선탐색을 이용한 풀이 ##

def dfs(depth):
    global ans

    # 재귀적으로 사용하려면 이와같이 종료조건을 정의해 줘야함
    if depth == M:
        ans = max(ans, int(''.join(arr)))
        return


    # 모든 교환 경우의 수를 시행
    for i in range(len(arr)-1):
        for j in range(i + 1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]

            # check 변수에 값을 넣고 해당 깊이의 해당 값이 방문한 적이 있는지 확인
            check = int(''.join(arr))
            # 방문한 적이 없다면 방문 배열에 넣은 후 깊이를 1 증가시켜서 그 방문한 적 없는 수를 깊이우선탐색함
            if (depth, check) not in visited:
                visited.append((depth, check))
                dfs(depth + 1)
                # 위 과정이 특정깊이 M까지 도달하면 함수를 종료하고, 그 값을 기존 ans값과 비교해서 큰 값을 ans에 넣음 -> 이 과정은 dfs함수 내에서 발생 = 깊이가 M일 때의 값만 ans에 기록됨

            # 이렇게 for문을 한 번 다 돌면 다음 경우의 수를 알아보기 위해 수를 처음 상태로 원상복구시킴
            arr[i], arr[j] = arr[j], arr[i]


result = []
T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(str(N))
    visited = []
    ans = 0
    dfs(0)

    result.append(f"#{case} {ans}")
for i in result:
    print(i)











