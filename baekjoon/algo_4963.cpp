#include<iostream>
#include<utility>
#include<queue>

using namespace std;

int grid[50][50];

int d[8][2] = { {1,1}, {1,0}, {1,-1}, {0, 1}, {0, -1}, {-1, 1}, {-1,0}, {-1,-1}};

int W, H;

const int SEA = 0;
const int GROUND = 1;

void dfs(int x, int y)
{
    grid[y][x] = SEA;
    
    for(int i=0 ; i < 8 ; i++)
    {
        int nx, ny;
        nx = x + d[i][0];
        ny = y + d[i][1];
                    
        if(nx < 0 || nx >= W || ny < 0 || ny >= H)
            continue;
                
        if(grid[ny][nx] == SEA)
            continue;
            
        dfs(nx, ny);
    }
}

int main()
{
    while(true)
    {
        scanf("%d %d", &W, &H);
        
        if(W==0 && H==0)
            break;
            
        for(int i=0; i < H; i++)
            for(int j=0; j < W; j++)
                scanf("%d", &grid[i][j]);
                
        int count = 0;
        for(int i=0; i< H; i++)
        {
            for(int j=0; j< W; j++)
            {
                if(grid[i][j] == GROUND)
                {
                    dfs(j, i);
                    count++;   
                }
            }
        }
            
        printf("%d\n", count);
    }
}