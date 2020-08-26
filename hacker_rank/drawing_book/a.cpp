#include <bits/stdc++.h>

using namespace std;

int turn_2(vector<pair<int,int>>book_pages, int p) {
    int size = book_pages.size(), ans=0;
    for(int i=size-1; i>=0; i--) {
        if(p == book_pages[i].first || p == book_pages[i].second){
            break;
        } else {
            ans++;
        }
    }

    return ans;
}


int turn_1(vector<pair<int,int>>book_pages, int p) {
    int size = book_pages.size(), ans=0;
    for(int i=0; i<size; i++) {
        if(p == book_pages[i].first || p == book_pages[i].second){
            break;
        } else {
            ans++;
        }
    }

    return ans;
}


int main() {
    
    // #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    // #endif

    int n, p;
    vector<int>n_pages;
    cin>>n>>p;

    for(int i=0; i<=n; i++){
        n_pages.push_back(i);
    }
    /*n_pages.push_back(0);*/

    pair<int,int>pages;
    vector<pair<int,int>>book_pages;

    int size = n_pages.size();

    for(int i=0; i<size; i+=2) {
        pages.first = n_pages[i];
        pages.second = n_pages[i+1];
        book_pages.push_back(pages);
    }

/*    for(int i=0; i<size/2; i++) {
        cout<<book_pages[i].first<<" "<<book_pages[i].second<<'\n';
    }*/

    vector<int> ans = {turn_1(book_pages, p), turn_2(book_pages,p )};

    auto min_value = *min_element(ans.begin(),ans.end());

    cout<<min_value<<'\n';
    /*for(int x: ans) {
        cout<<x<<" ";
    }*/

    /*cout<<final_ans<<'\n';*/

    return 0;
    
}