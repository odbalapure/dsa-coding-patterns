package whattotrack;

import java.util.HashMap;
import java.util.Map;

public class ValidAnagram {

    /**
     * Check for valid palindrome
     * 
     * COMPLEXITY
     * Time: O(N * 26) =~ O(N)
     * Space: O(26) =~ O(1)
     * 
     * @param str1
     * @param str2
     * @return Boolean flag indicating a stirng is anagram
     */
    public static boolean isAnagram(String str1, String str2) {
        if (str1.length() != str2.length()) {
            return false;
        }

        Map<Character, Integer> table = new HashMap<>();

        for (Character ch : str1.toCharArray()) {
            table.compute(ch, (key, value) -> value == null ? 1 : value + 1);
        }

        for (Character ch : str2.toCharArray()) {
            if (table.containsKey(ch)) {
                table.put(ch, table.get(ch) - 1);
            } else {
                return false;
            }
        }

        for (int count : table.values()) {
            if (count != 0) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        String[] str1List = { "listen", "race", "elbow", "cat", "inch" };
        String[] str2List = { "silent", "cares", "below", "act", "chin" };

        System.out.println(isAnagram(str1List[3], str2List[3]));
    }
}