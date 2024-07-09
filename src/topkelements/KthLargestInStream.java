package topkelements;

import java.util.PriorityQueue;

public class KthLargestInStream {
    
    /**
     * Find kth largest element in the stream
     * 
     * COMPLEXITY
     * Time: O(N * log(K))
     * Space: O(K)
     * 
     * @param nums
     * @param k
     * @return
     */
    public int kthLargestInStream(int[] nums, int k) {
        PriorityQueue<Integer> topK = new PriorityQueue<>();

        for (int num : nums) {
            if (topK.size() < k) {
                topK.offer(num);
            } else if (num > topK.peek()) {
                topK.poll();
                topK.offer(num);
            }
        }

        return topK.peek();
    }
}