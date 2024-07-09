package whattotrack;

public class RansomNote {
    /**
     * Check if ransom note can be constructed using magazine
     * 
     * COMPLEXITY
     * Time: O(N * 26) =~ O(N)
     * Space: O(26) =~ O(1)
     * 
     * @param ransomNote
     * @param magazine
     * @return Flag indicating ransom note can be constructed using magazine
     */
    public static boolean ransomNote(String ransomNote, String magazine) {
        int[] count = new int[26];

        for (int i = 0; i < magazine.length(); i++) {
            count[magazine.charAt(i) - 'a']++;
        }

        for (int i = 0; i < ransomNote.length(); i++) {
            if (--count[ransomNote.charAt(i) - 'a'] < 0) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        System.out.println(ransomNote("a", "b")); // false
        System.out.println(ransomNote("aa", "aab")); // true
    }
}
