/*
문제
 -크기가 N인 수열 A0, A1, ..., AN-1이 주어졌을 때, 다음 두 종류의 쿼리를 수행해보자.

1 i j k: Ai, Ai+1, ..., Aj에 k를 xor한다.
2 i j: Ai, Ai+1, ..., Aj를 모두 xor한 다음 출력한다.
입력
 -첫 번째 줄에 수열의 크기 N이 주어진다.
두 번째 줄에는 A0, A1, ..., AN-1이 차례대로 주어지며, 공백 한 칸으로 구분되어져 있다.
세 번째 줄에는 쿼리의 개수 M이 주어지고, 다음 M개의 줄에 쿼리가 한 줄에 하나씩 주어진다.
출력
 -2번 쿼리의 결과를 모두 출력한다.
예제 입력 1
 -5
1 2 3 4 5
3
2 0 4
1 2 4 9
2 0 4

예제 출력 1
 -1
8

https://www.acmicpc.net//problem/12844
*/