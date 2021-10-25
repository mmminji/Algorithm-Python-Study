# 2021-10-19
# - 문제 설명
# 트리의 일부를 서브 트리라고 한다. 주어진 이진 트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내는 프로그램을 만드시오.

# 주어지는 트리는 부모와 자식 노드 번호 사이에 특별한 규칙이 없고, 부모가 없는 노드가 전체의 루트 노드가 된다.

# 이런 경우의 트리는 부모 노드를 인덱스로 다음과 같은 방법으로 나타낼 수 있다. 자식 노드가 0인 경우는 노드가 자식이 없는 경우이다.


# [입력]

# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50

# 다음 줄부터 테스트 케이스의 별로 첫 줄에 간선의 개수 E와 N이 주어지고, 다음 줄에 E개의 부모 자식 노드 번호 쌍이 주어진다.

# 노드 번호는 1번부터 E+1번까지 존재한다. 1<=E<=1000, 1<=N<=E+1

# [출력]

# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


# 입력
# 3
# 5 1
# 2 1 2 5 1 6 5 3 6 4
# 5 1
# 2 6 6 4 6 5 4 1 5 3
# 10 5
# 7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10

# 출력
# #1 3
# #2 1
# #3 3


# == 나의 풀이 == 
T = int(input())
def dfs(n):
    ans.append(n)
    if len(edge_lst[n]) == 0:
        return
    else:
        for a in edge_lst[n]:
            dfs(a)

    
for test_case in range(1, T + 1):
    e,sn = map(int, input().split())
    lst = list(map(int, input().split()))
    edge_lst = [[]*max(lst) for _ in range(max(lst)+1)]
    
    for k in range(len(lst)//2):
        edge_lst[lst[k*2]].append(lst[k*2+1])
    
    ans = []    
    dfs(sn)
    print('#{} {}'.format(test_case, len(ans)))
      