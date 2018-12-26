#include<stdio.h>

int bambus[501][501];
int dp[501][501];

int dx[4] = { 0, 0 ,1 ,-1};
int dy[4] = { -1, 1, 0 ,0};

int N;
int ans;

void dfs(int cy, int cx)
{
    int local_m = 0;  
    
    for(int i = 0 ; i< 4; i++)
    {
        int nx = cx + dx[i];
        int ny = cy + dy[i];
        
        if(nx < 0 || nx >= N || ny < 0 || ny >= N)
            continue;
        
        if(bambus[ny][nx] > bambus[cy][cx])
        {
            if(dp[ny][nx] == 0)
                dfs(ny, nx);
                
            if(local_m < dp[ny][nx])
                local_m = dp[ny][nx];
        }
    }
    
    dp[cy][cx] = local_m + 1;
        
    if(ans < dp[cy][cx])
        ans = dp[cy][cx];
    
}

int main()
{
    scanf("%d", &N);
    
    for(int i =0 ; i< N; i++)
        for(int j=0; j < N; j++)
            scanf("%d", &bambus[i][j]);
            
    for(int i =0 ; i< N; i++)
        for(int j=0; j < N; j++)
            if(dp[i][j] == 0)
                dfs(i, j);
                
    for(int i =0 ; i< N; i++)
    {
        for(int j=0; j < N; j++)
            printf("%d", dp[i][j]);
        printf("\n");    
    }
                
    printf("%d", ans);
    
    return 0;
}