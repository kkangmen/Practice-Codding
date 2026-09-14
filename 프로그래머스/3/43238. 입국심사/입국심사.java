import java.util.*;

class Solution {
    
    public long countN(long mid, int[] times){
        long count = 0;
        for (int time : times){
            count += mid / time;
        }
        return count;
    }
    
    public long solution(int n, int[] times) {
        long answer = 0;
        
        long left = 1;
        Arrays.sort(times);
        long right = n * (long)times[times.length-1];
        
        while (left <= right){
            long mid = (left+right)/2;
            
            long count = countN(mid, times);
            // System.out.println("mid: " + mid + " count: " + count);
            if (count >= n){
                right = mid-1;
                answer = mid;
            } else {
                left = mid+1;
            }
        }
        return answer;
    }
}