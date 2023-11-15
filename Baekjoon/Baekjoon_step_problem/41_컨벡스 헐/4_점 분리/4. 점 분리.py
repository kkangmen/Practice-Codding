'''
문제
 -평면 위에 여러 개의 검정 점과 흰 점이 있다. 이때, 길이가 무한대인 직선을 그어 흰 점과 검은 점을 분리하려고 한다. 직선은 어떤 점과도 만나면 안 된다. 직선으로 인해서 나누어지는 두 그룹 중 한 그룹에는 흰 점만 있어야 하고, 다른 그룹에는 검은 점만 있어야 한다.
아래 그림에서 제일 왼쪽 예제는 점선으로 표시된 직선으로 두 점을 나눌 수 있다. 하지만 나머지 예제는 직선으로 점을 분리할 수 없다.

흰 점과 검은 점의 좌표가 주어졌을 때, 직선으로 점을 분리할 수 있는지 없는지를 알아내는 프로그램을 작성하시오.
입력
 -첫째 줄에는 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에 검정 점의 개수 n과 흰 점의 개수 m이 공백으로 구분되어 주어진다. n과 m은 100보다 작거나 같다. 다음 줄부터 n개의 줄에는 검정 점의 좌표가 공백으로 구분되어 주어진다. 그 다음 m개의 줄에는 흰 점의 좌표가 주어진다.
모든 점의 x, y좌표는 0보다 크거나 같고, 10000보다 작거나 같은 정수이다. 또한, 같은 위치에 점이 2개 이상 있는 경우는 없다.
출력
 -각각의 테스트 케이스에 대해서, 점을 문제의 설명대로 분리할 수 있으면 YES를, 아니면 NO를 출력한다.
예제 입력 1
 -10
3 3
100 700
200 200
600 600
500 100
500 300
800 500
3 3
100 300
400 600
400 100
600 400
500 900
300 300
3 4
300 300
500 300
400 600
100 100
200 900
500 900
800 100
1 2
300 300
100 100
500 500
1 1
100 100
200 100
2 2
0 0
500 700
1000 1400
1500 2100
2 2
0 0
1000 1000
1000 0
0 1000
3 3
0 100
4999 102
10000 103
5001 102
10000 102
0 101
3 3
100 100
200 100
100 200
0 0
400 0
0 400
3 3
2813 1640
2583 2892
2967 1916
541 3562
9298 3686
7443 7921

예제 출력 1
 -YES
NO
NO
NO
YES
YES
NO
NO
NO
YES

https://www.acmicpc.net//problem/3878
'''