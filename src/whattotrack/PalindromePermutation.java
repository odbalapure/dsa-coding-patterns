package whattotrack;

import java.util.*;

public class PalindromePermutation {

    /**
     * Is a valid palindrome permutation possible
     * 
     * COMPLEXITY
     * Time: O(N * 26) =~ O(N)
     * Space: O(26) =~ O(1)
     * 
     * @param str
     * @return Boolean flag indicating valid palindrome permutation
     */
    public static boolean validPalindromePermutation(String str) {
        Map<Character, Integer> freq = new HashMap<>();

        for (Character ch : str.toCharArray()) {
            freq.compute(ch, (key, value) -> (value == null) ? 1 : value + 1);
        }

        int count = 0;
        for (Character ch : freq.keySet()) {
            if (freq.get(ch) % 2 != 0) {
                count += 1;
            }
        }

        return count <= 1;
    }

    public static void main(String[] args) {
        List<String> strArray = Arrays.asList("baefeab", "abc", "xzz", "jjadd", "kllk");
        System.err.println(validPalindromePermutation(strArray.get(1)));
    }
}