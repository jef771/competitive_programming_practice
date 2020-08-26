#include <bits/stdc++.h>

using namespace std;

int main() {
    
    // #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    // #endif

    int n, j=0, m=0;

    cin>>n;

    vector<int>clouds;

    for(int i=0; i<n; i++) {
        int x;
        cin>>x;
        clouds.push_back(x);
    }

    while(j<n-1) {
        j++;
        j++;
        m++;
        if(clouds[j] == 1) {
            j--;
        }
    }

    cout<<m;
}