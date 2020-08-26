#include <bits/stdc++.h>

using namespace std;

int main() {
    
    freopen("input.txt", "r", stdin);

    int N;

    cin>>N;

    vector<int> dollars;

    for(int i=0; i<N; i++) {
        int temp;
        cin>>temp;
        dollars.push_back(temp);
    }

    float y = 0.0; 
    int ans = 0;
    y = accumulate(dollars.begin(), dollars.end(), y) / dollars.size();
    y = round(y);

    for(int x: dollars) {
        ans += pow(x - y, 2);

    }

    cout<<ans<<'\n';

    return 0;
}