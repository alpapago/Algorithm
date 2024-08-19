#include <bits/stdc++.h>

using namespace std;

int v,e,k;

vector<pair<int,int>> adj[20001];

vector<int> djk(int st){
    vector<int> d(v+1,INT_MAX);

    d[st] = 0;
    priority_queue<pair<int,int>,
    vector<pair<int,int>>,greater<pair<int,int>>> pq;

    pq.push({0,st});

    while(!pq.empty()){
        int w,u;
        tie(w,u) = pq.top(); pq.pop();
        if ( d[u] != w) continue;
        for (auto nxt: adj[u]){
            int v, dw;
            tie(dw,v) = nxt;
            if (d[v] > dw + w) {
                d[v] = dw + w;
                pq.push({d[v],v});
            }
        }
    }
    return d;
}

int main() {

    cin >> v >> e;
    cin >> k;
    while(e--){
        int a,b,c;
        cin >> a >> b >> c;
        adj[a].push_back({c,b});
    }
    
    vector<int> dist = djk(k);

    for(int i = 1; i <= v; i++){
        if(dist[i] == INT_MAX) cout << "INF\n";
        else{
            cout << dist[i] << "\n";
        }
    }

    return 0;
}