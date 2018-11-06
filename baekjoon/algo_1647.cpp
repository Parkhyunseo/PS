#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <functional>

#define MAX_NODE 10001

using namespace std;

typedef pair<int, int> pii;

bool visit[MAX_NODE];
vector<pii> vc[MAX_NODE];
int maxCost = 0;

int prim(int start)
{
    visit[start] = true;
    
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    
    for(int i = 0 ; i <vc[start].size(); i++)
    {
        int next = vc[start][i].first;
        int nextCost = vc[start][i].second;
        
        pq.push(pii(nextCost, next));
    }
    
    int ans = 0;
    
    while(!pq.empty())
    {
        int here = pq.top().second;
        int hereCost = pq.top().first;
        
        pq.pop();
        
        if(visit[here])
            continue;
            
        visit[here] = true;
        
        if(maxCost < hereCost)
            maxCost = hereCost;
        ans += hereCost;
        
        for(int i=0; i < vc[here].size(); i++)
        {
            int there = vc[here][i].first;
            int thereCost = vc[here][i].second;
            
            pq.push(pii(thereCost, there));
        }
    }
    
    return ans;
}


int main()
{
    int V, E, result;
    scanf("%d %d", &V, &E);
    
    for(int i=0; i < E; i++)
    {
        int from, to, val;
        scanf("%d %d %d", &from, &to, &val);
        
        vc[from].push_back(pii(to, val));
        vc[to].push_back(pii(from, val));
    }
    
    result = prim(1);
    printf("%d", result-maxCost);
    return 0;
}