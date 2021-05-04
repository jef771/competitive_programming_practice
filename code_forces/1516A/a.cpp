#include <bits/stdc++.h>

using namespace std;

int main() {
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    int t, n;

    cin >> t;
    for(int i=0;i<t;i++) {
        cin >> n;
        int a[n];
        vector <int> even;
        vector <int> odd;
        for(int j=0;j<n;j++) {
            int temp;
            cin >> temp;
            a[j]=temp;
        }
        for(int k=0;k<n;k++) {
            if((a[k]&1)==1) {
                odd.push_back(a[k]);
                
            } else {
                even.push_back(a[k]);
            }

        }
        for(int x: odd) {
            cout << x << ' ';
        }
        for(int y: even) {
            cout << y << ' ';
        }
        cout<< '\n';
    }

    return 0;
}



/*int A,B;
    cin >> A >> B;

    if(A+B >= 15) {
        if(B>=8) {
            cout << 1;
        } else if(B>=3) {
            cout << 2;
        } else if(B >=1) {
            cout << 3;
        } else {
            cout << 4;
        }
    } else if(A+B >=10) {
        if(B>=3) {
            cout << 2;
        } else if(B >=1) {
            cout << 3;
        } else {
            cout << 4;
        }
    } else if(A+B >= 3) {
        cout << 3;
    } else {
        cout << 4;
    }


    return 0;*/