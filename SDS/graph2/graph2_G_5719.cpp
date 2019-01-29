#include<iostream>
#include<vector>
#include<limits.h>
#include<string.h>
#include<queue>

using namespace std;

vector<pair<int, int>> adj[20001];

vector<int> dijkstra(vector<int> trace[501], int start, int V, int E)
{
    vector<int> dist(V, INT_MAX);
    dist[start] = 0;
    priority_queue<pair<int, int>> pq;
    
    pq.push(make_pair(0, start));
    
    while(!pq.empty())
    {
        int cost = -pq.top().first;
        int here = pq.top().second;
        
        pq.pop();

        if(dist[here] < cost)
            continue;
            
        for(int i=0; i<adj[here].size(); i++)
        {
            int there = adj[here][i].first;
            int nd = cost + adj[here][i].second;
            
            if(adj[here][i].second == -1)
                continue;
                
            if(dist[there] > nd)
            {
                dist[there] = nd;
                pq.push(make_pair(-nd, there));
                
                trace[there].clear();
                trace[there].push_back(here);
            }else if(dist[there] == nd)
                trace[there].push_back(here);
        }
    }
    
    return dist;
}

int main()
{
    while(1)
    {
        int V, E, start, end;
        
        scanf("%d %d", &V, &E);
        
        if(V == 0 && E == 0)
            break;
        
        scanf("%d %d", &start, &end);
        
        memset(adj, 0, sizeof(adj));
        
        for(int i=0; i<E; i++)
        {
            int from, to, val;
            scanf("%d %d %d", &from, &to, &val);
            
            adj[from].push_back({to, val});
        }
        
        vector<int> trace[501];
        memset(trace, 0, sizeof(trace));
        
        dijkstra(trace, start, V, E);
        
        queue<int> q;
        q.push(end);
        
        while(!q.empty())
        {
            int here = q.front();
            q.pop();
            
            for(int i=0; i < trace[here].size(); i++)
            {
                int there = trace[here][i];
                
                for(int j=0; j < adj[there].size(); j++)
                    if(adj[there][j].first == here)
                        adj[there][j].second =-1;
                        
                q.push(there);
            }
        }
        
        vector<int> result;
        result = dijkstra(trace, start, V, E);
    
        if(result[end] == INT_MAX)
            printf("-1\n");
        else
            printf("%d\n", result[end]);    
    }
    
}