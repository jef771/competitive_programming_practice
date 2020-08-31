#include <bits/stdc++.h>

using namespace std;

int main() {
    
    freopen("input.txt", "r", stdin);
    int n, ans=0;

    vector<int> soldiers;

    cin>>n;

    for(int i=0; i<n; i++) {
        int temp;
        cin>>temp;
        soldiers.push_back(temp);
    }

    int x = *max_element(soldiers.begin(), soldiers.end());

    auto min_max = minmax_element(soldiers.begin(), soldiers.end());
    int min_ele = *min_max.first;
    int max_ele = *min_max.second;
    while(soldiers[0] != max_ele) {
        int max_index = max_element(soldiers.begin(), soldiers.end()) - soldiers.begin();
        swap(soldiers[max_index], soldiers[max_index-1]);
        ans++;
    }

    while(soldiers[n-1] != min_ele) {
        soldiers.pop_back();
        n--;
        ans++;
    }

    cout<<ans;
    return 0;
}