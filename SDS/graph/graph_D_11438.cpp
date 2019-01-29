#include<iostream>
#include<vector>
#include<cstdio>
#include<cmath>

using namespace std;

#define MAX_NODE 100001

int dp[MAX_NODE][20];
int depth[MAX_NODE];

vector<int> graph[MAX_NODE];

int max_level;

int get_tree(int here, int parent)
{
    depth[here] = depth[parent] + 1;
    
    dp[here][0] = parent;
    
    for(int i=1; i<=max_level; i++)
    {
        int tmp = dp[here][i-1];
        dp[here][i] = dp[tmp][i-1];
    }
    
    int len = graph[here].size();
    for(int i=0; i < len ;i++)
    {
        int there = graph[here][i];
        if(there != parent)
            get_tree(there, here);
    }
}

int main()
{
    int N, M;
    
    scanf("%d", &N);
    
    max_level = (int)floor(log2(MAX_NODE));
    
    for(int i=0; i < N-1; i++)
    {
        int a, b;
        scanf("%d %d", &a, &b);
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    
    depth[0] = -1;
    
    get_tree(1, 0);
    
    scanf("%d", &M);
    
    while(M--)
    {
        int a, b;
        
        scanf("%d %d", &a, &b);
        
        if(depth[a] != depth[b])
        {
            if(depth[a] > depth[b])
            {
                int tmp = a;
                a = b;
                b = tmp;
            }
            
            for(int i=max_level; i >= 0; i--)
            {
                if(depth[a] <= depth[dp[b][i]])
                    b = dp[b][i];
            }
        }
        
        int lca = a;
        
        if(a != b)
        {
            for(int i=max_level; i >= 0; i--)
            {
                if(dp[a][i] != dp[b][i])
                {
                    a = dp[a][i];
                    b = dp[b][i];
                }
                lca = dp[a][i];
            }
        }
        
        printf("%d\n", lca);
    }
    
}