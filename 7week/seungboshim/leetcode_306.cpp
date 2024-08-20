#include <string>

class Solution {
public:
    bool isAdditiveNumber(string num) { // 112358
        for (int i=num.length()-1; i>1; i--) {
            num[i] = num[i] - '0'; // 8
            for (int j=i-1; j>0; j--) {
                num[j] = num[j] - '0'; // 5
                
            }

        }
    }
};