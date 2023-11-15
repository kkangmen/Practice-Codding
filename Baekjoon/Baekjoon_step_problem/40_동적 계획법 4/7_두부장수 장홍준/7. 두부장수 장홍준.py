'''
문제
 -장홍준은 참 특이한 두부장수이다. 세로크기 N, 가로크기 M인 두부판을 가지고 2x1짜리 두부로 잘라서 판다. 그런데, 두부판의 위치마다 등급이 다르다. 그리고 2x1짜리에 등급이 어떻게 매겨지느냐에 따라 두부의 값도 천차만별이 된다. 다음 등급표를 보자.

위의 표는 2x1짜리 두부의 등급에 따라 매겨지는 두부의 가격표다. 예를 들어 “AC" 두부의 가격은 7이고, ”DB" 두부의 가격은 3이다.
세로크기 M, 가로크기 N의 두부판이 주어진다. 각 칸마다 두부의 등급이 A, B, C, D, F로 매겨져 있다. 홍준이는 전체 두부가격의 합을 최대가 되게 두부를 자르려고 한다. 2x1짜리 두부로 잘라내고 남은 한 칸짜리 두부는 가격이 0이기 때문에 버린다. 홍준이를 도와 가격이 최대가 되게 두부판을 자르는 프로그램을 작성하시오.

위 그림은 N=4, M=4 인 두부판의 한 예이다. 오른쪽 그림이 잘라낸 두부가격의 합을 최대로 한 것이다. 한 칸짜리는 쓸모없으므로 버린다.
입력
 -첫째 줄에는 두부판의 세로크기 N, 가로크기 M이 주어진다. N, M은 1이상 14이하의 정수이다. 그 다음 N줄에 걸쳐 M개의 문자가 주어진다. 각 문자는 그 칸의 두부의 등급을 나타내며 A, B, C, D, F 중 하나로 주어진다.
출력
 -첫째 줄에 잘라낸 두부가격 합의 최댓값을 출력한다.
예제 입력 1
 -4 4
ACFC
FDAB
BACF
DBAC

예제 출력 1
 -37

https://www.acmicpc.net//problem/1657
'''