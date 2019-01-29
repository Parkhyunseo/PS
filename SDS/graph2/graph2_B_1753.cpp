#include<iostream>
#include<vector>
#include<limits.h>
#include<queue>

using namespace std;

vector<pair<int, int>> adj[20001];
int V;
int E;

vector<int> dijkstra(int start)
{
    vector<int> dist(V, INT_MAX);
    dist[start] = 0;
    priority_queue<pair<int, int>> pq;
    
    pq.push(make_pair(0, start));
    
    while(!pq.empty())
    {
        int cost = -pq.top().first;
        int index = pq.top().second;
        
        pq.pop();
        
        if(dist[index] < cost)
            continue;
            
        for(int i=0; i<adj[index].size(); i++)
        {
            int there = adj[index][i].first;
            int nd = cost + adj[index][i].second;
            
            if(dist[there] > nd)
            {
                dist[there] = nd;
                pq.push(make_pair(-nd, there));
            }
        }
    }
    
    return dist;
}

int main()
{
    int start;
    
    scanf("%d %d", &V, &E);
    scanf("%d", &start);
    
    V++;
    
    for(int i=0; i<E; i++)
    {
        int from, to, val;
        scanf("%d %d %d", &from, &to, &val);
        
        adj[from].push_back({to, val});
    }
    
    vector<int> result;
    
    result = dijkstra(start);
    
    for(int i =1 ; i< V; i++)
    {
        if(result[i] == INT_MAX)
            printf("INF\n");
        else
            printf("%d\n", result[i]);
    }
}