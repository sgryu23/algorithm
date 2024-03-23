#include<cstdio>
#include<vector>
using namespace std;


int main(){

	int n, q, tmp;
	vector<int> v;

	scanf("%d %d", &n, &q);

	for(int i = 0; i < n; i++){
		scanf("%d", &tmp);
		v.push_back(tmp);
	}

	int t, s, it = 0;

	for(int i = 0; i < q; i++){
		scanf("%d", &tmp);
		switch(tmp){
			case 1: {
				scanf("%d %d", &t, &s);
				if(it+t>n){
					v[it+t-n-1] += s;
				}
				else{
					v[it+t-1] += s;
				}
				break;
			}
			case 2:{
				scanf("%d", &s);
				if(it-s<0){
					it = it+n-s;
				}
				else{
					it = it-s;
				}
				break;
			}
			case 3:{
				scanf("%d", &s);
				if(it+s>=n){
					it = it-n+s;
				}
				else{
					it = it+s;
				}
				break;
			}
		}	
	}

	for(int i = 0; i<n; i++){
		if(it+i>=n){
			printf("%d ", v[it-n+i]);
		}
		else{
			printf("%d ", v[it+i]);
		}
	}
	printf("\n");

	return 0;
}