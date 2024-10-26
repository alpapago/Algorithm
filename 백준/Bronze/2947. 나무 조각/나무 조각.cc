#include <iostream>

using namespace std;

int arr[5];
void tmpOut(int tmp_arr[]){
  for (int i=0;i<5;i++){
    cout << tmp_arr[i]<< " ";
  }
  cout<< "\n";
};

int main() { 
  for(int i = 0; i < 5; i++){
    cin >> arr[i];
  }
  int flag = 1;
  while(flag){
    int small_flag = 0;
    for(int j=0; j<4; j++){
      if(arr[j] > arr[j+1]){
        int temp = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = temp;
        tmpOut(arr);
        small_flag = 1;
      }
    }
    if (small_flag == 0){
      flag = 0;
    }
  }
}