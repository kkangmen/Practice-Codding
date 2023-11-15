'''
문제
 -(연세대학교 도서관, 2016년 7월)
연세대학교에서는 매년 여름 깜짝 워터파크를 개장한다. 이 워터파크가 발생할 장소는 알 수 없지만, 보통 도서관이나 서문 쪽에 주로 개장한다는 사실만이 알려져 있다.
워터파크 개장을 막는 것이 힘들다고 판단한 학교에서는 차라리 학생들이 워터파크를 더 즐길 수 있도록 정수 Ki (-109 ≤ Ki ≤ 109)가 쓰여진 징검다리 N개를 놓아 두었다. 수업이 끝나고 친구들과 집에 가던 준호는 문득 이 징검다리를 이용해 여러 명이 즐길 수 있는 재미있는 게임을 하나 생각해냈다.

각 사람은 시작점으로 쓸 징검다리 하나를 아무 것이나 하나 고른다.
시작점에서 출발한 뒤 계속 점프하여 징검다리를 몇 개든 마음대로 밟은 뒤, 나오고 싶을 때 나온다. 시작점에서 바로 나오는 것도 가능하다.
시작점을 포함해, 밟은 모든 징검다리에 쓰여진 정수의 합이 가장 큰 사람이 이긴다.

이 규칙에 따라 게임을 하던 준호는, 제자리 점프를 이용해 10억점을 만드는 친구를 본 뒤 규칙을 좀 더 추가하기로 하였다. 추가된 규칙은 아래와 같다.

N개의 모든 징검다리에 순서대로 1 ~ N의 번호를 붙인다. U번 징검다리에서 V번 징검다리로 점프하기 위해서는, U와 V의 차이가 미리 정해진 값 D 이하여야 한다.
어떤 징검다리도 두 번 이상(한 번을 넘게) 밟을 수는 없다.

이제 다시 게임을 진행하려 한다. 이 게임에서 준호는 최대 몇 점을 얻을 수 있을까?
입력
 -첫 줄에 징검다리의 수 N과 문제에서 설명한 D가 주어진다. (2 ≤ N ≤ 105, 1 ≤ D ≤ N-1)
이어 N개의 정수로, 각 징검다리에 쓰인 수 Ki가 1번 징검다리부터 N번 징검다리까지 순서대로 주어진다. (-109 ≤ Ki ≤ 109)
출력
 -가능한 최대 점수를 출력한다.
예제 입력 1
 -10 2
2 7 -5 -4 10 -5 -5 -5 30 -10

예제 출력 1
 -40

예제 입력 2
 -3 2
-4 -2 -7

예제 출력 2
 --2

https://www.acmicpc.net//problem/15678
'''