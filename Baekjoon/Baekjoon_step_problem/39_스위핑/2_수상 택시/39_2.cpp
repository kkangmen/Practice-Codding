/*
문제
 -상근이가 살고 있는 도시에는 큰 강이 흐르고 있고, 모든 사람의 집은 이 강 근처에 있다. 집은 0번부터 M번까지 강을 따라서 번호가 매겨져 있고, 인접한 집 사이의 거리는 모두 1 킬로미터이다.
상근이는 0번 집에 살고 있고, 보트를 이용해서 사람들을 운송하는 일을 하고 있다.
오늘은 저녁때까지 M번 집으로 가야한다. 상근이는 M번 집으로 가는 길에 사람들을 태워주려고 한다.
오늘 상근이의 수상 택시를 타려고 하는 사람은 총 N명이다. 상근이는 각 사람들이 탑승할 위치와 목적지를 알고 있다. 상근이의 보트는 매우 커서 N명 모두 보트에 태울 수 있다.
예를 들어, 사람 A가 2번 집에서 8번으로 가려고 하고, B가 6에서 4로 가려고 하는 경우를 생각해보자. 상근이는 0번 집에서 시작해서, 2번에서 A를 태우고, 6번에서 B를 태울 것이다. 그 다음 4로 돌아가 B를 내려주고, 8번에서 A를 내려다준다. 그 다음에 원래 상근이가 가려고 했던 M번 집으로 가면 된다.
상근이가 모든 사람을 데려다주고, M번 집으로 가기 위해서 이동해야 하는 거리의 최솟값을 구하는 프로그램을 작성하시오.
입력
 -첫째 줄에 N과 M이 주어진다. (N ≤ 300,000, 3 ≤ M ≤ 109)
다음 N개 줄에는 각 사람이 상근이의 수상 택시를 타는 위치와 목적지가 주어진다. 모든 숫자는 0과 M 사이이다.
출력
 -첫째 줄에 상근이의 이동 거리의 최솟값을 출력한다.
예제 입력 1
 -2 10
2 8
6 4

예제 출력 1
 -14

예제 입력 2
 -8 15
1 12
3 1
3 9
4 2
7 13
12 11
14 11
14 13

예제 출력 2
 -27

https://www.acmicpc.net//problem/2836
*/