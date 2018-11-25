#include<iostream>
#include<cstring>
#include<queue>

using namespace std;

int grid[301][301];
int visit[301][301];

int d[8][2] = { {2,1}, {1,2}, {2,-1}, {1,-2}, {-2,1}, {-1, 2}, {-2,-1}, {-1,-2}};
int I;
int tx, ty;

struct data{
    int x;
    int y;
    int count;
};

int bfs(int sx, int sy)
{
    queue<data> q;
    q.push({sx, sy, 0});
    visit[sy][sx] = 1;
    
    while(!q.empty())
    {
        int cx = q.front().x;
        int cy = q.front().y;
        int count = q.front().count;
        q.pop();
        
        if(cx == tx && cy == ty)
        {
            printf("%d\n", count);
            break;
        }
        
        for(int i=0 ; i < 8 ; i++)
        {
            int nx, ny;
            nx = cx + d[i][0];
            ny = cy + d[i][1];
                        
            if(nx < 0 || nx >= I || ny < 0 || ny >= I)
                continue;
                    
            if(!visit[ny][nx])
            {
                visit[ny][nx] = 1;
                q.push({nx, ny, count+1});
            }
            
        }
    }
}

int main()
{
    int T;
    scanf("%d", &T);
    
    while(T--)
    {
        memset(grid, 0, sizeof(grid));
        memset(visit, 0, sizeof(visit));
        
        scanf("%d", &I);
        
        int sx, sy;
        scanf("%d %d", &sx, &sy);
        
        scanf("%d %d", &tx, &ty);
        
        bfs(sx, sy);
    }
}