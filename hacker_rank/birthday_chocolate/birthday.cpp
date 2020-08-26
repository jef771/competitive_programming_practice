#include <bits/stdc++.h>

using namespace std;


int get_cake(vector<int>s2, int d, int m, int x) {
    int ans=0;
    for(int i=x;i<=m;i++){
        ans+=s2[i];
    }

    if(ans==d) {
        return 1;
    } else {
        return 0;
    }
}


int birthday(vector<int> s, int d, int m) {
    int size=s.size(), ans=0;
    for(int i=0;i<size;i++) {
        ans+=get_cake(s, d, m, i);
    }

    return ans;
}


int main() {
    vector<int> v={1,2,1,6,1,2};
    int x=birthday();
    cout<<x;
}