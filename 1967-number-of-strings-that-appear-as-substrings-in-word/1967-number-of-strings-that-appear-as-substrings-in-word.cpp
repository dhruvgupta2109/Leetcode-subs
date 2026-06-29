class Solution {
public:
    int numOfStrings(vector<string>& patterns, string word) {
        int c=0;
        for(int i=0; i<size(patterns); i++){
            if(word.contains(patterns[i])){
                c++;
            }
        }
        return c;
    }
};