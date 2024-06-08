package whattotrack;

import java.util.*;

public class PalindromePermutation {

    /**
     * Is a valid palindrome permutation possible
     * 
     * @param str
     * @return Boolean flag
     */
    public static boolean palindromePermutation(String str) {
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
        System.err.println(palindromePermutation(strArray.get(1)));
    }
}