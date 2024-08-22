#include <string>
#include <vector>
#include <string>
#include <set>

using namespace std;

int solution(int N, int number) {
    
    vector<set<int>> dp(9);
        
    // i개의 N을 걍 이어붙인거로 초기화
    for(int i = 1; i < 9; i++){
        dp[i].insert(stoi(string(i,'0' + N)));
        
        for(int j = 1; j < i; j++){
            for(int k: dp[j]){
                for(int l: dp[i-j]){
                    dp[i].insert(k+l);
                    dp[i].insert(k-l);
                    dp[i].insert(k*l);
                    if(l!=0) dp[i].insert(int(k/l));
                }
            }
        }
        if(dp[i].find(number) != dp[i].end()) return i;
    }
    
    return -1;
}