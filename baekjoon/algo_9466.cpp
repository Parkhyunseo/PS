#include<stdio.h>
#include<iostream>
#include<string.h>

using namespace std;

int arr[100001];
int visit[100001];
int closed[100001];

int count;

void dfs(int here)
{
    int next = arr[here];
    visit[here]=1;
    
    if(visit[next])
    {
        if(!closed[next])
        {
            for(int i=next; here!=i; i=arr[i])
                count++;
            count++;
        }
    }else
        dfs(arr[here]);
        
    closed[here]=1;
}

int main()
{
    int T;
    cin >> T;
    
    while(T--)
    {
        int N;
        cin >> N;
        
        memset(arr, 0, sizeof(arr));
        memset(visit, 0, sizeof(visit));
        memset(closed, 0, sizeof(closed));
        
        count = 0;
        
        for(int i=1; i<= N;i++)
            cin >> arr[i];
            
        for(int i=1; i<= N;i++)
            if(!visit[i])
                dfs(i);
        printf("%d\n", N-count);
    }
}