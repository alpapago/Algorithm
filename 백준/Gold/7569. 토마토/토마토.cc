#include <bits/stdc++.h>

using namespace std;

int n,m,h;
typedef struct Triple{
  int z;
  int y;
  int x;
} triple;
int check[100][100][100];
int snail[100][100][100];

vector<triple> direction = {{1,0,0},{0,1,0},{-1,0,0},{0,-1,0},{0,0,1},{0,0,-1}};

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  
  cin >> n >> m >> h;
  int ans = 0;
  int s = 0;
  
  queue<triple> q;
  
  for(int i = 0; i < h; i++){
    for(int j = 0; j < m; j++){
      for(int k = 0; k < n; k++){
        cin >> snail[i][j][k];
        if (snail[i][j][k] == 1){ // 1은 토마토 찾음
          q.push({i,j,k}); // 일단 삽입
          check[i][j][k] = 1;
        };
        // 토마토가 없어서 방문 처리
        if (snail[i][j][k] == -1){
          check[i][j][k] = 1;
        }
        if (snail[i][j][k] == 0){
          s ++;
        }
      }
    }  
  }

  if(!s){
    cout << 0;
    return 0;
  }
  
  while(!q.empty()){
    triple cur = q.front();
    q.pop();
    //cout << cur.z << ' ' << cur.y << ' ' << cur.x << '\n';
    int z = cur.z; int r = cur.y; int c = cur.x;
    for(int i = 0; i < 6; i++){
      int nh = z + direction[i].z; 
      int nr = r + direction[i].y;
      int nc = c + direction[i].x;
      if ( nh<0 || nr < 0 || nc < 0|| nh>=h || nr >= m  || nc >= n) continue;
      if ( check[nh][nr][nc] >=1 ) continue;
      q.push({nh,nr,nc});
      check[nh][nr][nc] = check[z][r][c] + 1;
    }
  }
  
  for (int i = 0; i < h; i++){
    for (int j = 0; j < m; j++){
      for(int k = 0; k < n; k++){
        if (check[i][j][k] == 0){
          ans = -1;
          cout << ans;
          return 0;
        }
        else{
          ans = max(ans, check[i][j][k]);
        }
      }
    }
  }
  cout << ans - 1;
  }