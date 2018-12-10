#include<iostream>
#include<cstring>
#include<queue>

using namespace std;

int grid[1001][1001];
//int visit[301][301];

int d[4][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1}};

struct data{
    int x;
    int y;
    int count;
};

int main()
{
    int M, N;
    int ans = 0;
    
    scanf("%d %d", &M, &N);
    
    queue<data> q;
    
    for(int i=0; i<N; i++)
        for(int j=0; j<M; j++)
        {
            scanf("%d", &grid[i][j]);
            if(grid[i][j] == 1)
                q.push({j, i, 0});
        }
            
    
    while(!q.empty())
    {
        int cx = q.front().x;
        int cy = q.front().y;
        int count = q.front().count;
        q.pop();
        
        ans = ans > count ? ans : count;
        
        for(int i=0 ; i < 4 ; i++)
        {
            int nx, ny;
            nx = cx + d[i][0];
            ny = cy + d[i][1];
                        
            if(nx < 0 || nx >= M || ny < 0 || ny >= N)
                continue;
                    
            if(grid[ny][nx] != -1 && grid[ny][nx] != 1)
            {
                grid[ny][nx] = 1;
                q.push({nx, ny, count+1});
            }
        }
    }
    
    
    for(int i=0; i<N; i++)
        for(int j=0; j<M; j++)
        {
            if(grid[i][j] == 0)
            {
                printf("-1");
                return 0;
            }
        }
    
    printf("%d", ans);
}