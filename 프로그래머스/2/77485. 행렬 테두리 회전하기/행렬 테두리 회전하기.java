import java.util.*;

class Solution {
    
    int[][] board;
    
    public int rotate(int[] query){
        int x1 = query[0];
        int y1 = query[1];
        int x2 = query[2];
        int y2 = query[3];
        
        int temp = board[x1][y1];
        int min = temp;
        
        // 아래 -> 위 (좌)
        for (int r = x1; r < x2; r++){
            board[r][y1] = board[r+1][y1];
            min = Math.min(min, board[r][y1]);
        }
        
        // 오 -> 왼 (아래)
        for (int c = y1; c < y2; c++){
            board[x2][c] = board[x2][c+1];
            min = Math.min(min, board[x2][c]);
        }
        
        // 위 -> 아래 (우)
        for (int r = x2; r > x1; r--){
            board[r][y2] = board[r-1][y2];
            min = Math.min(min, board[r][y2]);
        }
        
        // 왼 -> 오 (위)
        for (int c = y2; c > y1; c--){
            board[x1][c] = board[x1][c-1];
            min = Math.min(min, board[x1][c]);
        }
        
        board[x1][y1+1] = temp;
        
        return min;
    }
    
    public int[] solution(int rows, int columns, int[][] queries) {
        board = new int[rows+1][columns+1];
        int num = 1;
        
        // 행렬 초기화
        for (int i = 1; i <= rows; i++){
            for (int j = 1; j <= columns; j++){
                board[i][j] = num++;
            }
        }
        
        int[] answer = new int[queries.length];
        
        for (int i = 0; i < queries.length; i++){
            answer[i] = rotate(queries[i]);
        }
        return answer;
    }
}