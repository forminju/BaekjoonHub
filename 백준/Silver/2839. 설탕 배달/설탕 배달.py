N = int(input())
count = 0
while True: ## 조건 : 5의 배수로 나누어 떨어질 때까지
    if(N%5)==0: 
        count +=(N//5) 
        print(count)
        break
    N-=3 ## 과정 : 3씩 빼주기
    count+=1 # 봉지 개수 추가
    if(N<0):
        print("-1")
        break