#include<iostream>
#include<queue>
#include<vector>
#include<limits.h>

using namespace std;

int N, M;

vector<pair<int, int>> adj[1001];

int dijkstra(int src, int dst)
{
    vector<int> dist(N, INT_MAX);
    dist[src] = 0;
    
    priority_queue<pair<int, int>> pq;
    pq.push(make_pair(0, src));
    
    while(!pq.empty())
    {
        int cost = -pq.top().first;
        int here = pq.top().second;
        
        pq.pop();
        
        if(cost > dist[here])
            continue;
        
        for(int i=0; i < adj[here].size(); i++)
        {
            int there = adj[here][i].first;
            int nextCost = cost + adj[here][i].second;
            
            if(dist[there] > nextCost)
            {
                dist[there] = nextCost;
                pq.push({-nextCost, there});
            }
        }
    }
    
    return dist[dst];
}

int main()
{
    scanf("%d", &N);
    scanf("%d", &M);
    
    N++;
    
    for(int i=0; i<M ;i++)
    {
        int from, to, weight;
        scanf("%d %d %d",&from, &to, &weight);
        adj[from].push_back({to, weight});
    }
    
    int src, dst;
    scanf("%d %d",&src, &dst);
    
    printf("%d", dijkstra(src, dst));
    
    return 0;
}