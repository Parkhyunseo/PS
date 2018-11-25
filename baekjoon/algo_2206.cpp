#include<iostream>
#include<queue>

using namespace std;

struct Position{
    int x, y, k=0, count=0;
    Position(int x, int y, int k, int count): x(x), y(y), k(k), count(count){}
};

int N, M;
char map[1001][1001];
int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};
bool visit[1001][1001][2];

int main()
{
    scanf("%d %d", &N, &M);
    
    for(int i=0; i< N; i++)
        cin >> map[i];
    
    queue<Position> q;
    q.push(Position(0,0,0,1));
    visit[0][0][0] = 1;
    
    while(!q.empty())
    {
        int here_x = q.front().x;
        int here_y = q.front().y;
        int here_k = q.front().k;
        int here_count = q.front().count;
        q.pop();
        
        if(here_x == M-1 && here_y == N-1)
        {
            printf("%d\n", here_count);
            return 0;
        }
        
        for(int i=0; i<4; i++)
        {
            int nx = here_x + dx[i];
            int ny = here_y + dy[i];
            
            if(nx < 0|| nx >= M || ny < 0 || ny >= N)
                continue;
                
            if(visit[ny][nx][here_k])
                continue;
                
            if(map[ny][nx] == '1')
            {
                if(here_k < 1)
                {
                    q.push(Position(nx, ny, here_k+1, here_count+1));
                    visit[ny][nx][1] = 1;
                }
                continue;
            }
            q.push(Position(nx, ny, here_k, here_count+1));
            visit[ny][nx][here_k] = 1;
        }
    }
    printf("-1\n");
}