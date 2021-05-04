#include <bits/stdc++.h>

using namespace std;


int review_site(int a[], int n) {

    int s1 = 0, s2 = 0;

    for(int i=0;i<n;i++) {
        if(a[i] == 2) {
            if(s1 < s2) {
                s1--;
            } else if(s2 < s1) {
                s2--;
            } else {
                s1--;
            }
        } else {
            if(s1 > s2) {
                s1++;
            } else if(s2 > s1) {
                s2++;
            } else {
                s1++;
            }
        }
    }

    return max(s1,s2);

}


int main() {
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    int t, n, x;

    cin >> t;

    for(int i=0;i<t;i++) {
        cin >> n;
        int a[n];
        for(int j=0;j<n;j++) {
            cin >> x;
            a[j] = x;
        }
        int ans = review_site(a, n);
        cout << ans << '\n';
    }


    return 0;
}
