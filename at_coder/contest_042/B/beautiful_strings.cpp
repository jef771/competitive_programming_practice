#include <bits/stdc++.h>

using namespace std;

int main() {
	string S;

	cin>>S;

	int size=S.size(),count=0,ans=0,odd=0;

	for(int i=0;i<size;i++) {
		for(int j=0;j<size;j++) {
			if(S[i]==S[j]) {
				count++;
			}
		}
		if(count%2==0){
			ans+=count;
		} else {
			odd+=count;
		}
		count=0;
	}

	if(ans%2==0 && odd==0) {
		cout<<"Yes";
	} else {
		cout<<"No";
	}

	return 0;
}