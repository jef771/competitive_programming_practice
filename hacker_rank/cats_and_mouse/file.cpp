#include <bits/stdc++.h>

using namespace std;

string cat_mouse(int x, int y, int z) {

	while(x!=y) {
		if(x==z) {
			return "Cat A";
		} else if(y==z) {
			return "Cat B";
		}
		
		if(x<z && y<z) {
			x++;
			y++;
		} else if(x<z && y>z) {
			y--;
			x++;
		} else if(y<z && x>z) {
			x--;
			y++;
		} else if(y>z && x>z) {
			y--;
			x--;
		}
	}

	return "Mouse C";
}


int main() {
	
	#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif

	int q, x, y, z;

	cin>>q;

	for(int i=0; i<q; i++) {
		cin>>x>>y>>z;
		string ans=cat_mouse(x,y,z);
		cout<<ans<<endl;
	}

	return 0;
}