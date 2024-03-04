#include <iostream>
using namespace std;

int main(void) {
  int arr[9];
  int price = 0;
  cin >> price;
  for (int i = 0; i < 9; i++) {
    cin >> arr[i];
    price -= arr[i];
  }
  cout << price << '\n';
  return 0;
}