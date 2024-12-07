#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main(){
    int n = 5;
    vector<int> arr;
    while(n--){
        int tmp;
        cin >> tmp;
        arr.push_back(tmp);
    }
    int f = arr[0];
    int s = arr[1];
    int g = arr[2];
    
    vector<int> dir;
    dir.push_back(arr[3]);
    dir.push_back(-arr[4]);

    queue<pair<int, int>> q;
    vector<bool> visited(f + 1, false);

    int ans = 0;
    
    q.push(make_pair(s,0));
    visited[s] = true;  
    bool flag = false;
    while(!q.empty()){
        pair<int,int> now =q.front(); q.pop();
        int n_floor = now.first;
        int n_ans = now.second;

        if (n_floor == g){
            ans = n_ans;
            flag = true;
            break;
        }

        for (int i = 0; i < 2; i++){
            int new_floor = n_floor+dir[i];
            if (new_floor > f || new_floor <= 0){
                continue;
            }
            if (visited[new_floor]){
                continue;
            }
            visited[new_floor] = true;
            q.push(make_pair(new_floor, n_ans+1));
        }
    }
    if (flag){
        cout << ans;
    }
    else{
        cout << "use the stairs";
    }
    return 0;
}