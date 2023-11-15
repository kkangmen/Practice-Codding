/*
문제
 -자연수 \(n\)개로 이루어진 배열 \(a_1,a_2,a_3,\dots ,a_n\)이 있다.
\(l\)부터 \(r\)까지 부분 배열은 \(a_l,a_{l+1},\dots , a_r\) 이다.
\(K_s\)는 부분 배열 안에 있는 자연수 \(s\)의 개수이다.
부분 배열의 힘이란 모든 자연수 \(s\)에 대해서, \(K_s \cdot K_s \cdot s\)를 합한 값이다.
배열과 부분 배열의 범위가 주어졌을 때, 각 부분 배열의 힘을 구하는 프로그램을 작성하시오.
입력
 -첫째 줄에 배열의 크기 \(n\)과 부분 배열의 개수 \(t\)가 주어진다. (1 ≤ \(n\), \(t\) ≤ 105) 둘째 줄에는 \(n\)개의 자연수 \(a_i\) (1 ≤ \(a_i\) ≤ 106) 가 주어진다.
다음 \(t\)개 줄에는 부분 배열의 범위 \(l_i\)와 \(r_i\)가 주어진다. (1 ≤ \(l_i\) ≤ \(r_i\) ≤ \(n\))
출력
 -입력으로 주어지는 각 부분 배열의 힘을 출력한다.
예제 입력 1
 -8 3
4 3 1 1 1 3 1 2
2 7
1 6
3 8

예제 출력 1
 -28
25
21

https://www.acmicpc.net//problem/8462
*/