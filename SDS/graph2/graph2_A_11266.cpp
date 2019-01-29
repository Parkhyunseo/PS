#include<iostream>
#include<vector>

#define MAX_V 10001

using namespace std;

bool iscut[MAX_V];
int order[MAX_V];
vector<int> graph[MAX_V];

int count = 0;

int find(int here, bool root)
{
    ++count;
    order[here] = count;
    
    int minOrder = order[here];
    int childCount = 0;
    
    for(int i=0; i < graph[here].size(); i++)
    {
        int there = graph[here][i];
        
        if(order[there])
        {
            minOrder = min(minOrder, order[there]);
            continue;
        }
        
        childCount += 1;
        
        int prev = find(there, false);
        
        if(!root && prev >= order[here])
            iscut[here] = true;
            
        minOrder = min(minOrder, prev);
    }
    
    if(root && childCount >= 2)
        iscut[here] = true;
        
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
            find(i, true);
            
    int c = 0;
    for(int i=1; i <= V; i++)
        if(iscut[i])
            c += 1;
            
    printf("%d\n", c);
    
    for(int i=1; i <= V; i++)
        if(iscut[i])
            printf("%d ", i);
            
    printf("\n");
}