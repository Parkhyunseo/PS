#include<iostream>
#include<vector>
#include<string.h>

#define MAX 10000

using namespace std;

int T;
int times[MAX];
int memoization[MAX];

int bfs(vector<int> &graph, int here)
{
    if(memoization[here] != -1)
        return memoization[here];
        
    int result = 0;
    
    for(int i=0; i<graph[here].size(); i++)
        result = max(result, bfs(graph[here][i]));
        
    memoization[here] = result + times[here];
    
    return memoization[here];
}

int main()
{
    scanf("%d", &T);
    
    while(T--)
    {
        vector<int> graph[MAX];
        memset(times, 0, sizeof(times));
        memset(memoization, 0, sizeof(memoization));
        
        int N, K;
        
        scanf("%d %d", &N, &K);
        
        for(int i=1; i <=N; i++)
            scanf("%d", &times[i]);
            
        for(int i=0; i < K; i++)
        {
            int from, to;
            scanf("%d %d", &from ,&to);
            
            graph[to].push_back(from);
        }
        
        int find;
        scanf("%d", &find);
        
        printf("%d", bfs(graph, find));
    }
}
