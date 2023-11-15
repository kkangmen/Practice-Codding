'''
문제
 -자연수를 저장하는 데이터베이스 S에 대해 다음의 쿼리를 처리합시다.
유형 1 : S에 자연수 X를 추가한다.
유형 2 : S에 포함된 숫자 중 X번째로 작은 수를 응답하고 그 수를 삭제한다.
입력
 -첫째 줄에 사전에 있는 쿼리의 수 N 이 주어집니다. (1 ≤ N ≤ 2,000,000)
둘째 줄부터 N개의 줄에 걸쳐 각 쿼리를 나타내는 2개의 정수 T X가 주어집니다.
T가 1이라면 S에 추가할 X가 주어지는 것입니다. (1 ≤ X ≤ 2,000,000)
T가 2라면 X는 S에서 삭제해야 할 몇 번째로 작은 수인지를 나타냅니다. S에 최소 X개의 원소가 있음이 보장됩니다.
출력
 -유형 2의 쿼리 개수만큼의 줄에 각 쿼리에 대한 답을 출력합니다.
예제 입력 1
 -5
1 11
1 29
1 89
2 2
2 2

예제 출력 1
 -29
89

https://www.acmicpc.net//problem/12899
'''