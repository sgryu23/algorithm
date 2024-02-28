#include <iostream>
using namespace std;
int fact(int n){
    if(n>2)
        n *= fact(n-1);
    return n;
}
int main(void){
    int num, result = 1;
    cin>>num;
    if(num!=0)
        result = fact(num);
    cout<<result;
}