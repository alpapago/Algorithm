#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int n,answer;
int arr[8];
bool visit[8] = {false,};
vector<int> v;

void dfs(int k){
  
  if (k == n) {
    int tmp = 0;
    for (int i = 0; i<n-1; i++){
      tmp += abs(v[i]- v[i+1]);
    }
    if (tmp>answer){
      answer = tmp;
    }
    return;
  }
  for(int i=0; i<n; i++){
    if (visit[i] == true){
      continue;
    }
    visit[i] = true;
    v.push_back(arr[i]);
    dfs(k+1);
    visit[i] = false;
    v.pop_back();
  }
}

int main() {
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }
  dfs(0);
  cout << answer;
}