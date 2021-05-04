#include <bits/stdc++.h>

using namespace std;

int main() {
    
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    string s, temp, temp2, temp3;

    cin >> s;
    int n = s.size()-1;

    for(int i=n;i>=0;i--){
        temp+=s[i];
    }
    int count = 0;
    if(temp!=s) {
        while(temp!=temp3) {
            temp+='0';
            temp2+='0';

            temp3 = temp2 + s;
            count++;
            if(count > n) {
                break;
            }
        }
        if(temp!=temp3) {
            cout << "No";
            return 0;
        } 
    }
    cout << "Yes";
    
    
    return 0;
}
