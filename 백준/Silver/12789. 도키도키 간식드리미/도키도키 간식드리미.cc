#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    int n;
    cin >> n;
    
    queue<int> arr;
    for(int i = 1; i <= n; i++) {
        int tmp;
        cin >> tmp;
        arr.push(tmp);
    }
    
    vector<int> stk;
    int current = 1;
    
    while(current <= n) {
        if(!stk.empty() && stk.back() == current) {
            stk.pop_back();
            current++;
        }
        else if(!arr.empty() && arr.front() == current) {
            arr.pop();
            current++;
        }
        else if(!arr.empty()) {
            stk.push_back(arr.front());
            arr.pop();
        }
        else {
            cout << "Sad";
            return 0;
        }
    }
    
    cout << "Nice";
    return 0;
}