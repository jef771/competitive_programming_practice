#include <bits/stdc++.h>

using namespace std;

int main() {
    
    /*freopen("input.txt", "r", stdin);*/

    map<string, int> anton_p{ {("Tetrahedron"), 4},
                            {("Cube"), 6},
                            {("Octahedron"), 8},
                            {("Dodecahedron"), 12},
                            {("Icosahedron"), 20}
                        };

    int n, ans=0;

    cin>>n;

    for(int i=0; i<n; i++) {
        string s;
        cin>>s;
        ans += anton_p[s];
    }

    cout<<ans<<'\n';

    return 0;
}