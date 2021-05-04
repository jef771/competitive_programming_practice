#include <bits/stdc++.h>

using namespace std;

int main() {
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    deque <int> cards;

    int n, t;

    cin >> n >> t;

    vector <int> ans;

    for(int i=0;i<n;i++) {
        int temp;
        cin >> temp;
        cards.push_back(temp);
    }
    
    for(int j=0;j<t;j++) {
        int temp;
        cin >> temp;
        for(int k=0;k<n;k++) {
            if(cards[k]==temp) {
                ans.push_back(k+1);
                cards.push_front(cards[k]);
                cards.erase(cards.begin()+k+1);
                break;
            }
        }
    }

    for(int x: ans) {
        cout << x << ' ';
    }



    return 0;
}
