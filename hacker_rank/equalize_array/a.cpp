#include <bits/stdc++.h>

using namespace std;

int main() {

    int n, index, ans=0;
    int max = INT_MIN;
    vector<int> numbers;

    cin>>n;

    for(int i=0; i<n; i++) {
        int temp;
        cin>>temp;
        numbers.push_back(temp);
    }

    map<int, int> numbers_map;

    for(int x: numbers) {
        int temp = count(numbers.begin(), numbers.end(), x);
        numbers_map[x] = temp;
        if(temp > max) {
            max = temp;
            index = x; 
        }
    }

    for(const auto& [number, count] : numbers_map) {
        if(number != index) {
            ans += count;
        }
    }

    cout<<ans;

    return 0;
}