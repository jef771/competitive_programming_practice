#include <bits/stdc++.h>

using namespace std;

int main() {
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int H, W, X, Y, ans = 0;
    cin >> H >> W >> X >> Y;

    char s[H][W];

    for(int i=0;i<H;i++) {
        for(int j=0;j<W;j++) {
            char c;
            cin >> c;
            s[i][j] = c;
        }
    }
        for(int k=Y-1;k>=0;k--) {
            if(s[X-1][k]=='.') {
                ans++;
            } else {
                break;
            }
        }
        for(int v=Y;v<W;v++) {
            if(s[X-1][v]=='.') {
                ans++;
            } else {
                break;
            }
        }
        for(int l=X-1;l>=0;l--) {
            if(s[l][Y-1]=='.') {
                ans++;
            } else {
                break;
            }
        }
        for(int m=X;m<H;m++) {
            if(s[m][Y-1]=='.') {
                ans++;
            } else {
                break;
            }
        }

    cout << --ans;


    return 0;
}
