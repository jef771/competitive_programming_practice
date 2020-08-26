#include <bits/stdc++.h>

using namespace std;

int main() {
    
    freopen("input.txt", "r", stdin);

    map<char, int> steps{ {'U', 1}, {'D', -1}};

    int n, valleys = 0, ans = 0;
    bool flag = false;
    char temp;

    cin >> n;

    for(int i=0; i<=n; i++) {
        if(valleys < 0 && !flag) {
            cin >> temp;
            valleys += steps[temp];
            flag = true;
        }
        else if(valleys == 0 && flag) {
            ans++;
            cin >> temp;
            valleys += steps[temp];
            flag = false;
        }
        else {
            cin >> temp;
            valleys += steps[temp];
        }
    }

    cout << ans << '\n';
    
    return 0;
}