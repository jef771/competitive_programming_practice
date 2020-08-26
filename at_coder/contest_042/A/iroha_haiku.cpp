#include <iostream>

using namespace std;

int main() {
	int x,y,z,count=0;

	cin>>x>>y>>z;

	if(x==5) {
		count++;
	} else if(x==7) {
		count++;
	}

	if(y==5) {
		count++;
	} else if(y==7) {
		count++;
	}

	if(z==5) {
		count++;
	} else if(z==7) {
		count++;
	}

	if(count==3 && x+y+z==17) {
		cout<<"YES"<<endl;
	} else {
		cout<<"NO"<<endl;
	}

	return 0;
}