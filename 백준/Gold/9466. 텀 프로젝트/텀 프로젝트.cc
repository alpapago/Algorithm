#include <bits/stdc++.h>

using namespace std;

int arr[100005];
int state[100005];
const int IN_CYCLE = -1;
const int NOT_VISITED = 0;

void cycle(int x){
    int cur = x;
  
    while(true){
      // 부모 노드 작성
      state[cur] = x;
      // 자식 노드 탐색
      cur = arr[cur];
      
      // 사이클 발견
      if(state[cur] == x){
        // 방문한 적 있다면
        while(state[cur] == x){
          state[cur] = IN_CYCLE;
          cur = arr[cur];
        }
        return ;
      }
      else if (state[cur] != NOT_VISITED) return ;
    }
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int t;
  cin >> t;

  while(t--){
    int n;
    cin >> n;
    
    // 초기화
    fill(&arr[0], &arr[100005], 0);
    fill(&state[0], &state[100005], 0);

    
    for(int i = 1; i <= n; i++){
      cin >> arr[i];
    }
    
    for(int i = 1; i <= n; i++){
      if(state[i] == NOT_VISITED){
        cycle(i);
      }
    }

    int ans = 0;
    for(int i = 1; i <= n; i++){
      if( state[i] != IN_CYCLE){
        ans++;
      }
    }
    cout << ans << "\n";
  }
  return 0;
}
