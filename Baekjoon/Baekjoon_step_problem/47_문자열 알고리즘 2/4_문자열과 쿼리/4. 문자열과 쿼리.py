'''
문제
 -문자열 S = S1S2...SN이 주어진다. 함수 F(i)는 S와 S1S2...Si의 가장 긴 공통 접미사의 길이로 정의된다.
예를 들어, S = "zaaxbaacbaa"인 경우에, F(1) = 0, F(2) = 1, F(3) = 2이다.
문자열 S와 쿼리 M개가 주어졌을 때, 각각의 쿼리에 대해서, F(i)를 구하는 프로그램을 작성하시오.
입력
 -첫째 줄에 문자열 S가 주어진다. (1 ≤ N ≤ 1,000,000)
둘째 줄에 쿼리의 개수 M이 주어진다. (1 ≤ M ≤ 100,000)
셋째 줄부터 M개의 줄에 각각의 쿼리 i가 주어진다. (1 ≤ i ≤ n)
출력
 -각각의 쿼리 i에 대해서, F(i)를 출력한다.
예제 입력 1
 -zaaxbaacbaa
11
1
2
3
4
5
6
7
8
9
10
11

예제 출력 1
 -0
1
2
0
0
1
3
0
0
1
11

https://www.acmicpc.net//problem/13713
'''