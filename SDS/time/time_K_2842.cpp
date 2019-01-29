#include<iostream>
#include<algorithm>
#include<vector>
#include <string.h> 

using namespace std;

int N;
int result = 100000000;

int dx[8] = {-1, -1, -1, 1, 1, 1, 0, 0};
int dy[8] = {0 , -1, 1, 0, -1, 1, -1, 1};

int sx, sy;
int post_office_count;

char grid[52][52];
int stemina[52][52];
int visited[52][52];

vector<int> stemina_set;

int dfs(int x, int y, int left, int right)
{
    if( x < 1 || x > N || y < 1 || y > N)
        return 0;
        
    if(visited[y][x])
        return 0;
        
    if(stemina[y][x] < left || stemina[y][x] > right)
        return 0;
    
    int total = 0;
        
    visited[y][x] = 1;
    
    if(grid[y][x] == 'K')
        total += 1;
        
    for(int i=0; i< 8; i++)
        total += dfs(x+dx[i], y+dy[i], left, right);
        
    return total;
}

int main()
{
    scanf("%d", &N);
    
    for(int i=1; i<=N; i++)
    {
        scanf("%s", grid[i]+1);
        for(int j=1; j<=N; j++)
        {
            if(grid[i][j] == 'P')
            {
                sx = j;
                sy = i;
            }else if(grid[i][j] == 'K')
                post_office_count++;
        }
    }
    
    for(int i=1; i<=N; i++)
    {
        for(int j=1; j<=N; j++)
        {
            scanf("%d", &stemina[i][j]);
            stemina_set.push_back(stemina[i][j]);
        }
    }
    
    sort(stemina_set.begin(), stemina_set.end());
    stemina_set.erase(unique(stemina_set.begin(), stemina_set.end()), stemina_set.end());
    
    int left = 0;
    
    for(int right=0 ; right<stemina_set.size() ;right++)
    {
        while(true)
        {
        //    for(int i=0; i<N; i++)
        //        for(int j=0; j<N; j++)
        //            visited[i][j] = 0;
            memset(visited, 0, sizeof(visited));
                    
            if(dfs(sx, sy, stemina_set[left] ,stemina_set[right]) != post_office_count)
                break;
            
            result = min(result, stemina_set[right] - stemina_set[left]);
                
            left++;
        }
    }
    
    printf("%d", result);
}
