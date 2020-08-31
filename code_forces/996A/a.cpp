#include <iostream>
     
using namespace std;
     
int main() {
    unsigned int n, x=0;
    cin>>n;
     
    while(n!=0) {
        while(n>=100) {
            n-=100;
            x++;
        } while(n>=20) {
            n-=20;
            x++;
        } while(n>=10) {
            n-=10;
            x++;
        } while(n>=5) {
            n-=5;
            x++;
        } while(n>=1) {
            n-=1;
            x++;
        }
    }
    cout<<x<<endl;
}