#include <bits/stdc++.h>

using namespace std;

int get_div(int a, int b) {
    int count = 0;
    while(a%b != 0) {
        a++;
        count++;
    }

    return count;
}


int main() {
    
    int n;
    cin >> n;

    for(int i=0; i<n; i++) {
        int a, b;
        cin >> a >> b;
        cout << get_div(a,b) << "\n";
    }
    
}