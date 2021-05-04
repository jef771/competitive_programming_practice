#include <bits/stdc++.h>

using namespace std;




int main() {
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int n, x, y, z;
    cin >> n;

    for(int i=0;i<n;i++) {
            
            cin >> x >> y >> z;
            if(max(x,y) - min(x,y) >= z ) {
                cout << "YES" << '\n';
            } else {
                cout<< "NO" << '\n';
            }
    }

    return 0;
}
