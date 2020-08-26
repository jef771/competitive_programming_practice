#include <bits/stdc++.h>

using namespace std;


int main() {

    int n;
    vector<int> sticks2;

    cin>>n;

    int ans = n;

    for(int i=0; i<n; i++) {
        int temp;
        cin>>temp;
        sticks2.push_back(temp);
    }

    while(ans!=0) {
        int temp = *min_element(sticks2.begin(), sticks2.end());
        cout<<ans<<'\n';
        sticks2.erase(remove(sticks2.begin(), sticks2.end(), temp), sticks2.end());
        ans = sticks2.size();
    }
    
    return 0;
}