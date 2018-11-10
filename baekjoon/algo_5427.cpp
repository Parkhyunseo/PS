#include <iostream>
#include <cstdio>
#include <queue>
#include <vector>
#include <string.h>
#define MAX_SIZE 1000

using namespace std;

typedef struct
{
    int x;
    int y;
    int sec;
    bool type;
} pos;

vector<pair<int, int>> v;

bool visit[MAX_SIZE][MAX_SIZE];
char map[MAX_SIZE][MAX_SIZE];
int n, m;
int sx, sy;

void input()
{
    scanf("%d %d", &n, &m);
    getchar();
    
    for(int i=0; i<m; i++)
    {
        for(int j=0; j<n; j++)
        {
            char c = getchar();
            map[i][j] = c;
            if(c=='*')
                v.push_back(make_pair(i, j));
            else if(c=='@')
            {
                sx = i;
                sy = j;
            }
        }
        getchar();
    }
}

int bfs()
{
    queue<pos> q;
    
    for(int i=0; i<v.size(); i++)
        q.push(pos{v[i].first, v[i].second, 0, false});
    q.push(pos{sx, sy, 0, true});
    
    visit[sx][sy] = 1;
    int dx[4] = {0, 0, 1, -1};
    int dy[4] = {1,-1, 0, 0};
    
    while(!q.empty()) 
    {
        pos pop_data = q.front();
        q.pop();
        
        int x = pop_data.x;
        int y = pop_data.y;
        int sec = pop_data.sec;
        int type = pop_data.type;
        
        if(type && (x == 0 || x == m-1 || y == 0 || y == n-1))
            return sec + 1;
            
        for(int i=0; i<4 ;i++)
        {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if(nx< 0 || ny <0 || nx >= m || ny >= n)
                continue;
            if(map[nx][ny] == '#' || map[nx][ny] == '*')
                continue;
            if(visit[nx][ny])
                continue;
            
            if(type)
                visit[nx][ny] = 1;
            else
                map[nx][ny] = '*';
                
            q.push(pos{nx, ny, sec+1, type});
        }
    }
    
    return 0;
}

int main()
{
    int T, W, H, result;
    scanf("%d", &T);
    
    while(T--)
    {
        v.clear();
        memset(visit, 0, sizeof(visit));
        
        input();
     
        int ret = bfs();
        if(ret)
            printf("%d\n", ret);
        else
            printf("IMPOSSIBLE\n");
    }
    return 0;
}