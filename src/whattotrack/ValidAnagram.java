package whattotrack;

import java.util.HashMap;
import java.util.Map;

public class ValidAnagram {

    /**
     * Check for valid palindromeß
     * 
     * @param str1
     * @param str2
     * @return
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
}