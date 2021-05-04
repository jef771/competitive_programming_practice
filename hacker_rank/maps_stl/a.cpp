#include <bits/stdc++.h>

using namespace std;

int main() {
    
    freopen("input.txt", "r", stdin);

    map<string, int> students;

    int Q;

    cin >> Q;

    for(int i=0; i<Q; i++) {
        string student;
        int x, y;
        cin >> x;
        if(x == 1) {
            if(students[student] < 0) {
                cin >> student >> y;
                students.insert(make_pair(student, y));
            }
            else {
                cin >> student >> y;
                students[student] += y;
            }
        } 
        else {
            if(x == 2) {
                cin >> student;
                students[student] = 0;
            } else if(x == 3) {
                cin >> student;
                cout << students[student] << '\n';
            }
        }

    }

    return 0;
}