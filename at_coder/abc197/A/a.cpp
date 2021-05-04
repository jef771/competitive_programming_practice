#include <bits/stdc++.h>

using namespace std;

int main() {
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    string s;

    cin >> s;

    for(int i=1;i<s.size();i++) {
        cout << s[i];
    }

    cout << s[0];



    return 0;
}
