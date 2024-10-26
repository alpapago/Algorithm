#include <algorithm>
#include <iostream>

using namespace std;

int n;
int arr[8];

int main() {
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> arr[i];
  }
  sort(arr, arr + n);
  int answer = 0;

  // even
  
  if (n % 2 == 0) {

    for (int i = 0; i < n / 2 - 1; i++) {
      answer += 2 * arr[n - 1 - i];
      answer -= 2 * arr[i];
    }
    answer += (arr[n / 2] - arr[n / 2 - 1]);
  }
  // odd
  if (n>3){
  if (n % 2 == 1) {
    for (int i = 0; i < n / 2 - 1; i++) {
      answer += 2 * arr[n - 1 - i];
      answer -= 2 * arr[i];
    }
    answer += (arr[n / 2] + arr[n / 2 + 1]);
    answer -= 2*arr[n / 2 - 1];
  }
    }
  if(n == 3){
    answer = (2*arr[2] - arr[1]- arr[0]);
  }
  cout << answer;
}