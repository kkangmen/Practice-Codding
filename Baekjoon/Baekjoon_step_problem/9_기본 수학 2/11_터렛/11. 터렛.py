'''
문제
 -조규현과 백승환은 터렛에 근무하는 직원이다. 하지만 워낙 존재감이 없어서 인구수는 차지하지 않는다. 다음은 조규현과 백승환의 사진이다.
이석원은 조규현과 백승환에게 상대편 마린(류재명)의 위치를 계산하라는 명령을 내렸다. 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산했다.
조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때, 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.
입력
 -첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 이루어져 있다.
한 줄에 x1, y1, r1, x2, y2, r2가 주어진다. x1, y1, x2, y2는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이고, r1, r2는 10,000보다 작거나 같은 자연수이다.
출력
 -각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수를 출력한다. 만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1을 출력한다.
예제 입력 1
 -3
0 0 13 40 0 37
0 0 3 0 7 4
1 1 1 1 1 5
예제 출력 1
 -2
1
0
https://www.acmicpc.net//problem/1002
'''

import sys
input=sys.stdin.readline
input_data_num=int(input())
for _ in range(input_data_num):
    input_num_list=list(map(int,input().split()))
    radius_distance=input_num_list[2]+input_num_list[5]
    location_distance=((input_num_list[3]-input_num_list[0])**2+(input_num_list[4]-input_num_list[1])**2)**0.5
    down_radius_distance=min(input_num_list[2],input_num_list[5])
    up_radius_distance=max(input_num_list[2],input_num_list[5])
    if location_distance==0:
        if input_num_list[2]==input_num_list[5]: print(-1)
        else: print(0)
    elif location_distance==radius_distance: print(1)
    elif location_distance+down_radius_distance==up_radius_distance: print(1)
    elif location_distance>=radius_distance: print(0)
    elif location_distance<=radius_distance:
        if location_distance+down_radius_distance<up_radius_distance: print(0)
        else: print(2)