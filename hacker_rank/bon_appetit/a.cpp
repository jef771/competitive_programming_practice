#include <bits/stdc++.h>

using namespace std;

int main() {
    
    // #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    // #endif

    int n, k;
    vector<int> bill;

    cin>>n>>k;

    for(int i=0; i<n; i++){
        int temp;
        cin>>temp;
        bill.push_back(temp);
    }

    int b_charged, total=0;

    cin>>b_charged;

    for(int x: bill) {
        total+=x;
    }

    int b_actual = (total - bill[k]) / 2;

    if(b_actual == b_charged) {
        cout<<"Bon Appetit";
    } else {
        cout<<b_charged - b_actual;
    }
    
}