package whattotrack;

import java.util.*;

public class FirstUniqueCharacter {

    /**
     * Find the first unique character index
     * 
     * COMPLEXITY
     * Time: O(N * 26) =~ O(N)
     * Space: O(26) =~ O(1)
     * 
     * @param s
     * @return First unique character index
     */
    public static int firstUniqueCharacter(String s) {
        HashMap<Character, Integer> wordCount = new HashMap<>();

        for (Character ch : s.toCharArray()) {
            wordCount.compute(ch, (key, value) -> (value == null) ? 1 : value + 1);
        }

        for (int i = 0; i < s.length(); i++) {
            if (wordCount.get(s.charAt(i)) == 1) {
                return i;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        System.out.println(firstUniqueCharacter("ababccdeezee"));
    }
} 