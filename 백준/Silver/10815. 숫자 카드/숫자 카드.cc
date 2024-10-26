#include <iostream>
#include <algorithm>

using namespace std;

int n, m;
int arr[500001];
int exam[500001];

int bisec(int x){
  int l = 0, r = n-1;
  int mid;
  while(l<=r){
    mid = (l+r)/2;
    if (arr[mid] == x){
      return 1;
    }else if(arr[mid] > x){
      r = mid-1;
    }else if(arr[mid] < x){
      l = mid+1;
    }
  }
  return 0;
}

int main() { 
  cin >> n;
  for(int i = 0; i < n; i++){
    cin >> arr[i];
  }
  sort(arr, arr+n);

  cin >> m;
  for (int i=0;i<m; i++){
    cin >> exam[i];
  }
  for (int i=0;i<m; i++){
    int k = bisec(exam[i]);
    cout << k << " ";
  }
}