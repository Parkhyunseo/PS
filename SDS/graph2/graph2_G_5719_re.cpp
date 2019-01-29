#include<iostream>
#include<limits.h>
#include<string.h>
#include<queue>
#include<vector>

#define MAX_NODE 501

using namespace std;

vector<pair<int, int>> graph[MAX_NODE];

vector<int> find(vector<int> trace[MAX_NODE], int start, int V, int E)
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
            
        for(int i=0; i < graph[here].size(); i++)
        {
            int there = graph[here][i].first;
            int nextCost = cost + graph[here][i].second;
            
            if(graph[here][i].second == -1)
                continue;
            
            if(dist[there] > nextCost)
            {
                dist[there] = nextCost;
                pq.push(make_pair(-nextCost, there));
                
                trace[there].clear();
                trace[there].push_back(here);
            }else if(dist[there] == nextCost) // 최단경로가 하나가 아닐 수 있으니
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
        
        memset(graph, 0, sizeof(graph));
        
        for(int i=0; i<E; i++)
        {
            int from, to, val;
            scanf("%d %d %d", &from, &to, &val);
            
            graph[from].push_back({to, val});
        }
        
        vector<int> trace[501];
        memset(trace, 0, sizeof(trace));
        
        find(trace, start, V, E);
        
        queue<int> q;
        q.push(end);
        
        while(!q.empty())
        {
            int here = q.front();
            q.pop();
            
            for(int i =0 ; i < trace[here].size(); i++)
            {
                int there = trace[here][i];
                
                for(int j=0; j < graph[there].size(); j++)
                    if(graph[there][j].first == here)
                        graph[there][j].second = -1;
                        
                q.push(there);
            }
        }
        
        vector<int> result;
        result = find(trace, start, V,E);
        
        if(result[end] == INT_MAX)
            printf("-1\n");
        else
            printf("%d\n", result[end]);
        
    }
}