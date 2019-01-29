#include<iostream>
#include<vector>
#include<algorithm>

#define MAX_V 100001

using namespace std;

int order[MAX_V];
vector<int> graph[MAX_V];
vector<pair<int, int>> iscut;

int number = 0;

int find(int here, int parent)
{
    ++number;
    order[here] = number;
    
    int minOrder = order[here];
    int childCount = 0;
    
    for(int i=0; i < graph[here].size(); i++)
    {
        int there = graph[here][i];
        
        if(there == parent)
            continue;
        
        if(order[there])
        {
            minOrder = min(minOrder, order[there]);
            continue;
        }
        
        childCount += 1;
        
        int prev = find(there, here);
        
        if(prev > order[here])
            iscut.push_back({min(here, there), max(here, there)});
            
        minOrder = min(minOrder, prev);
    }
    
    /*
    if(root && childCount >= 2)
    {
        for(int i=0; i < graph[here].size(); i++)
        {
            int there = graph[here][i];
            iscut.push_back({min(here, there), max(here, there)});
        }
    }*/
    return minOrder;
}

int main()
{
    int V, E;
    
    scanf("%d %d", &V, &E);
    
    for(int e=0; e < E; e++)
    {
        int f, t;
        scanf("%d %d", &f, &t);
        
        graph[f].push_back(t);
        graph[t].push_back(f);
    }
    
    for(int i=1; i <= V; i++)
        if(order[i] == 0)
            find(i, 0);
            
    printf("%d\n", iscut.size());
    
    sort(iscut.begin(), iscut.end());
    
    for(int i=0; i < iscut.size(); i++)
        printf("%d %d\n", iscut[i].first, iscut[i].second);
            
    printf("\n");
}