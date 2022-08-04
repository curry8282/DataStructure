from collections import deque

n,k=(map(int,input('숫자 입력').split(" ")))
N,K=map(int,input()).split(" ")
arr=[]
result=[]
for i in range(1, N+1):
    arr.append(i)

queue=deque(arr)

for i in range(N):
    for j in range(K-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())
print(result)

    
# 카드2
n=int(input())
from collections import deque
arr=[]
for i in range(1,n+1):
    arr.append(i)
queue=deque(arr)
for i in range(1,n):
    queue.popleft()
    queue.append(queue.popleft())
   
print(queue.pop())