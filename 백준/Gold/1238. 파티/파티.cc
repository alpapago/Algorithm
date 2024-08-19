#include <iostream>
#include <vector>
#include <queue>
#include <climits>
using namespace std;

int n, m, x;
vector<vector<pair<int, int>>> graph;
vector<int> dijkstra(int start) {
    vector<int> dist(n + 1, INT_MAX);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    
    dist[start] = 0;
    pq.push({0, start});
    
    while (!pq.empty()) {
        int cur_dist = pq.top().first;
        int cur = pq.top().second;
        pq.pop();
        
        if (dist[cur] < cur_dist) continue;
        
        for (auto &edge : graph[cur]) {
            int next = edge.first;
            int next_dist = cur_dist + edge.second;
            
            if (next_dist < dist[next]) {
                dist[next] = next_dist;
                pq.push({next_dist, next});
            }
        }
    }
    return dist;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> n >> m >> x;
    graph.resize(n + 1);
    
    for (int i = 0; i < m; i++) {
        int s, d, w;
        cin >> s >> d >> w;
        graph[s].push_back({d, w});
    }
    
    vector<int> to_x = dijkstra(x);
    int ans = 0;
    
    for (int i = 1; i <= n; i++) {
        if (i == x) continue;
        vector<int> from_i = dijkstra(i);
        ans = max(ans, from_i[x] + to_x[i]);
    }
    
    cout << ans << endl;
    return 0;
}