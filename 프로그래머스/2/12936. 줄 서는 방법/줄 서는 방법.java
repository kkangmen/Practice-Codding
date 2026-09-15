import java.util.*;

class Solution {
    public int[] solution(int n, long k) {
        int[] answer = new int[n];
         // 숫자 배열
        List<Integer> list = new ArrayList<>();
        
        long nFact = 1L;
        for (int i = 1; i <= n; i++){
            nFact *= i;
            list.add(i);
        }
        
        k--;
        for (int i = n; i > 0; i--){
            
            nFact /= i;
            int index = (int)(k / nFact);
            
            answer[n-i] = list.remove(index);
            k %= nFact;
        }
        return answer;
    }
}