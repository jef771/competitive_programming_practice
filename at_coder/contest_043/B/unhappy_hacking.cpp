#include <bits/stdc++.h>

using namespace std;

int main() {
	string s;
	cin>>s;

	int size=s.size();
	string ans;

	for(int i=0;i<size;i++) {
		if(s[i]!='B') {
			ans+=s[i];
		} else if(s[i]=='B') {
			if(ans.size()>0){
				ans.pop_back();
			}
		}
	}

	size=ans.size();

	for(int i=0;i<size;i++)
		cout<<ans[i];

	return 0;
}