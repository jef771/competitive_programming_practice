#include <bits/stdc++.h>

using namespace std;

int main() {
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int t, n;
    char c;
    bool flag = false;

    cin >> t;
    for(int i=0;i<t;i++) {
        cin >> n;
        char a[n][n];
        pair<int, int> pi1;
        pair<int, int> pi2;
        for(int j=0;j<n;j++) {
            for(int k=0;k<n;k++) {
                cin>>c;
                a[j][k] = c;
                if(c == '*' && !flag) {
                    pi1 = make_pair(j,k);
                    flag = true;
                } else if(c=='*' && flag) {
                    pi2 = make_pair(j,k);
                    flag = false;
                }
            }
            

        }

        if(pi1.second != pi2.second && pi1.first != pi2.first) {
            swap(pi1.second, pi2.second);
            a[pi1.first][pi1.second] = '*';
            a[pi2.first][pi2.second] = '*';
        } else if(pi1.second == pi2.second && pi1.first != pi2.first) {
            if(pi1.second < n-1) {
                a[pi1.first][pi1.second+1] = '*';
                a[pi2.first][pi2.second+1] = '*';
            } else {
                a[pi1.first][pi1.second-1] = '*';
                a[pi2.first][pi2.second-1] = '*';
            }
            
        } else if(pi1.second != pi2.second && pi1.first == pi2.first) {
            if(pi1.first < n-1) {
                a[pi1.first+1][pi1.second] = '*';
                a[pi2.first+1][pi2.second] = '*';
            } else {
                a[pi1.first-1][pi1.second] = '*';
                a[pi2.first-1][pi2.second] = '*';
            }
        }
        for(int l=0;l<n;l++) {
            for(int m=0;m<n; m++) {
                cout << a[l][m];
            }
            cout << '\n';
        }
    }
}
