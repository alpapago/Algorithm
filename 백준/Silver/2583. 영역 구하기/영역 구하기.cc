#include <bits/stdc++.h>

using namespace std;

int R, C, k ;
int board[101][101];
int vis[101][101];

vector<pair<int,int>> direction = {{1,0},{0,1},{-1,0},{0,-1}};

int bfs(int r, int c){
  int ans = 1;
  queue<pair<int,int>> q;
  vis[r][c] = 1;
  q.push({r,c});

  while(!q.empty()){
    int nr,nc;
    tie(nr,nc) = q.front();
    q.pop();
    for(auto d : direction){
      int dr = nr + d.first;
      int dc = nc + d.second;
      if(dr < 0 || dr >= R || dc < 0 || dc >= C) continue;
      if(vis[dr][dc] == 1) continue;
      if(board[dr][dc] == 1) continue;
      vis[dr][dc] = 1;
      ans++;
      q.push({dr,dc});
    }
  }
  return ans;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  cin >> R >> C >> k;
  fill(&board[0][0], &board[0][0] + 101*101, 0);
  fill(&vis[0][0], &vis[0][0] + 101*101, 0);

  while(k--){
    int lc, lr, rc, rr;
    cin >> lc >> lr >> rc >> rr;
    for(int i = lc; i < rc; i++){
      for(int j = lr; j < rr; j++){
        board[j][i] = 1; // 1은 불가능하다는 뜻
      }
    }
  }
  // 오름차순 출력
  priority_queue<int,vector<int>,greater<int>> pq;
  int tot = 0;
  
  for(int i = 0; i < R; i++){
    for(int j = 0; j < C; j++){
      if (vis[i][j] == 1 || board[i][j] == 1) continue;
      int k = 0;
      k = bfs(i,j);
      pq.push(k);
      tot++ ;
    }
  }
  cout << tot<< "\n";
  while(tot--){
    cout << pq.top()<< " ";
    pq.pop();
  }
  
  return 0;
}
