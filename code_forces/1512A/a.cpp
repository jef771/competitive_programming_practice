#include <bits/stdc++.h>

using namespace std;

int main() {
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int t,n,x,temp;
    bool flag;

    cin >> t;

    for(int i=0;i<t;i++) {
        cin >> n;
        flag = false;
        cin >> temp;
        for(int j=1;j<n;j++) {
            cin >> x;
            if(x!=temp && !flag) {
                if(j==1)
                cout << (j+1) << '\n';
                flag = true;
            }
        }
    }
    return 0;
}
