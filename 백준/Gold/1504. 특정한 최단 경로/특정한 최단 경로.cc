#include <bits/stdc++.h>

using namespace std;

const long long INF = LLONG_MAX;  // INF를 LLONG_MAX로 정의
vector<pair<int, int>> adj[802];
int n, e, v1, v2;

vector<long long> djk(int st) {
    vector<long long> d(n + 1, INF);
    d[st] = 0;
    priority_queue<pair<long long, int>,
                   vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    pq.push({0, st});

    while (!pq.empty()) {
        long long w;
        int u;
        tie(w, u) = pq.top(); pq.pop();
        if (d[u] != w) continue;
        for (auto nxt : adj[u]) {
            int v, dw;
            tie(dw, v) = nxt;
            if (d[v] > dw + w) {
                d[v] = dw + w;
                pq.push({d[v], v});
            }
        }
    }
    return d;
}

int main() {
    cin >> n >> e;
    
    for (int i = 0; i < e; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        adj[a].push_back({c, b});
        adj[b].push_back({c, a});
    }
    cin >> v1 >> v2;

    // Calculate shortest paths
    vector<long long> dist1 = djk(1);
    vector<long long> distV1 = djk(v1);
    vector<long long> distV2 = djk(v2);

    long long ans1 = INF;
    long long ans2 = INF;

    if (dist1[v1] < INF && distV1[v2] < INF && distV2[n] < INF) {
        ans1 = dist1[v1] + distV1[v2] + distV2[n];
    }

    if (dist1[v2] < INF && distV2[v1] < INF && distV1[n] < INF) {
        ans2 = dist1[v2] + distV2[v1] + distV1[n];
    }

    long long ans = min(ans1, ans2);

    if (ans >= INF) {
        cout << -1;
    } else {
        cout << ans;
    }

    return 0;
}
