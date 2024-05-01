#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    
    if(n == 1)
        return 0;
    int i = 2;
    while (n > 1){
        if( n % i == 0){
            n /= i;
            cout << i << endl;
        }
        else
            i++;
    }
    return 0;
}
