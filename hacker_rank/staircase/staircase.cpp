#include <bits/stdc++.h>

using namespace std;

int main() {
	int N = 4, x=1, y=N;

	for(int i=0;i<N;i++,x++,y--) {
		cout<<setw(y);
		for(int j=0;j<x;j++) {
			cout<<'#';
		}
		cout<<endl;
	}
}