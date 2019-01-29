#include<iostream>
#include<cstdio>
#include<string.h>
#include<limits.h>
#include<vector>
#include<queue>
#include<functional>

#define MAX_NODE 1002

using namespace std;

typedef pair<int, int> pii;

vector<pair<int, int>> adj[MAX_NODE];
priority_queue<int> dist[MAX_NODE];

void dijkstra(int start, int V, int E,int K)
{
    dist[start].push(0);
    
    priority_queue<pii, vector<pii>, greater<pii> > pq;

    pq.push({0, start});
    
    while(!pq.empty())
    {
        int cost = pq.top().first;
        int here = pq.top().second;
        
        pq.pop();
        
        for(int i=0; i<adj[here].size(); i++)
        {
            int thereCost = adj[here][i].second;
            int there = adj[here][i].first;
            
            if(dist[there].size() < K)
            {
                dist[there].push(cost+thereCost);
                pq.push({(cost+thereCost), there});
            }else if(dist[there].top() > cost + thereCost)
            {
                dist[there].pop();
                dist[there].push(cost + thereCost);
                
                pq.push({(cost+thereCost), there});
            }
        }
    }
}

int main()
{
    int N, M, K;
    
    scanf("%d %d %d", &N, &M ,&K);

    for(int i=0; i< M; i++)
    {
        int f, t, w;
        scanf("%d %d %d", &f, &t ,&w);
        
        adj[f].push_back({t, w});
    }
    
    dijkstra(1, N, M, K);
    
    for(int i=1; i<=N; i++)
    {
        if(dist[i].size() == K)
            printf("%d\n", dist[i].top());
        else
            printf("-1\n");
            
    }
}