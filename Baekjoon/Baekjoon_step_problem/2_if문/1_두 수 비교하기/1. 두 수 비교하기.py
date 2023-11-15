'''
문제
 -두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
입력
 -첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.
출력
 -첫째 줄에 다음 세 가지 중 하나를 출력한다.

A가 B보다 큰 경우에는 '>'를 출력한다.
A가 B보다 작은 경우에는 '<'를 출력한다.
A와 B가 같은 경우에는 '=='를 출력한다.
예제 입력 1
 -1 2
예제 출력 1
 -<
예제 입력 2
 -10 2
예제 출력 2
 ->
예제 입력 3
 -5 5
예제 출력 3
 -==
https://www.acmicpc.net//problem/1330
'''
num_list=input().split()
for i in range(len(num_list)):
    num_list[i]=int(num_list[i])
if num_list[0]>num_list[1]:
    print(">")
elif num_list[0]<num_list[1]:
    print("<")
else :
    print("==")