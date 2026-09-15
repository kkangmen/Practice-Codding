import java.util.*;

class Solution {
    
    int[][][] map;
    int[] dx = {0, 1, 0, -1};
    int[] dy = {1, 0, -1, 0};
    Queue<int[]> q = new LinkedList<>();
    int[][][] costMap;
    
    public void bfs(int row, int col, int[][] board){
        q.offer(new int[]{0, 0, 0});
        q.offer(new int[]{0, 0, 1});
        costMap[0][0][0] = 0;
        costMap[0][0][1] = 0;
        
        while (!q.isEmpty()){
            int[] curNode = q.poll();
            for (int i = 0; i < 4; i++){
                int nx = curNode[0] + dx[i];
                int ny = curNode[1] + dy[i];
                if (0 <= nx && nx < row && 0 <= ny && ny < col){
                    if (board[nx][ny] == 0){
                        // 이전과 방향이 같을 때
                        int extraCharge = 0;
                        if (curNode[2] == i){
                            extraCharge = 100;
                        } else {
                            extraCharge = 600;
                        }
                        
                        // 더 적은 값으로 갈 수 있다면, 갱신하고 추가
                        int newCost = costMap[curNode[0]][curNode[1]][curNode[2]] + extraCharge;
                        if (newCost <= costMap[nx][ny][i]){
                            costMap[nx][ny][i] = newCost;
                            q.offer(new int[]{nx, ny, i});
                        }
                    }
                }
            }
        }
    }
    
    public int solution(int[][] board) {
        int answer = Integer.MAX_VALUE;
        
        int row = board.length;
        int col = board[0].length;
        map = new int[row][col][4];
        costMap = new int[row][col][4];
        
        // costMap 최대값 채우기
        for (int i = 0; i < row; i++){
            for (int j = 0; j < col; j++){
                Arrays.fill(costMap[i][j], Integer.MAX_VALUE);                
            }
        }
        
        bfs(row, col, board);
        
        // for (int i = 0; i < row; i++){
        //     for (int j = 0; j < col; j++){
        //         System.out.print(costMap[i][j] + " ");
        //     }
        //     System.out.println();
        // }
        for (int i = 0; i < 4; i++){
            answer = Math.min(answer, costMap[row-1][col-1][i]);
        }
        return answer;
    }
}