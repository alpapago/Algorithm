#include <bits/stdc++.h>

using namespace std;
vector<string> v;
vector<string> res;
map<string,int> m;

bool bi_search(string& s){

    int left =0, right = (int)v.size()-1, mid;
    while(left <= right)
    {
        mid = left + (right-left)/2;
        if(s.compare(v[mid])==0) return true;
        else if(s.compare(v[mid]) <0) {
            right = mid-1;
        }
        else if(s.compare(v[mid]) >0){
            left = mid+1;
        }
    }
    return false;
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int N, M;
    cin >> N >> M;
    for(int i = 0 ; i< N; i++)
    {
        string s;
        cin >> s;
        v.push_back(s);
    }
    sort(v.begin(), v.end());
    for(int i = 0 ; i< M; i++)
    {
        string s;
        cin >> s;
        if(bi_search(s)) res.push_back(s);
    }
    sort(res.begin(), res.end());
    cout << res.size() << endl;
    for(int i = 0 ; i< (int)res.size(); i++)
    {
        cout << res[i] << '\n';
    }
}