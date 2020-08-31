#include <bits/stdc++.h>

using namespace std;

int main() {
    
    freopen("input.txt", "r", stdin);

    int n, ans = 1;

    cin>>n;

    vector<int> numbers;
    vector<int> ans_v;

    for(int i=0; i<n; i++){
        int temp;
        cin>>temp;
        numbers.push_back(temp);
    }

    for(int i=1; i<n; i++) {
        if(numbers[i] > numbers[i-1]) {
            ans++;
        } else {
            ans_v.push_back(ans);
            ans = 1;
        }
    }
    ans_v.push_back(ans);
    
    int ans2 = *max_element(ans_v.begin(), ans_v.end());

    cout<<ans2;
}