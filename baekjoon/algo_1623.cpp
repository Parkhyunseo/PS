#include<iostream>
#include<queue>

int grid[50][50];
int visited[50][50];
vector<int> track;
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};
int N;
int L, R;
int end;

int bfs(sx,sy)
{
    queue<pair<int, int>> q;
    q.push(make_pair(sx, sy));
    
    while(!q.empty())
    {
        cx = item.front().first();
        cy = item.front().second();
        track.push()
        q.pop();
        
        for(int i=0; i < N; i++)
        {
            int nx, ny;
            nx = cx + dx[i];
            ny = cy + dy[i];
            
            if(nx < 0 || nx >= N || ny < 0 || ny >= N)
                continue;
                
            if(visited[ny][nx])
                continue;
            
            int diff = grid[cy][cx] - grid[ny][nx];
            if(diff < L || diff > R)
                continue;
                
            q.push(make_pair(dx, dy));
        }
    }
}

int main()
{
    scanf("%d %d %d", &N, &L, &R);
    
    for(int i=0; i<N; i++)
        for(int j=0; j<N; j++)
            scanf("%d", &grid[i][j])
    
    while(!end)
    {
        for(int i=0; i<N; i++)
        {
            for(int j=0; j<N; j++)
            {
                if(!visited[i][j]){
                    bfs(i, j);
                    if(track.size() < 0)
                    {
                        
                    }else
                    {
                        track.clear();   
                    }
                }
            }
        }    
    }
    
}