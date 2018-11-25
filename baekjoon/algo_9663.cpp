#include<iostream>

using namespace std;

int col[15];
int count;
int N;

int check(int here)
{
    for(int i=0; i < here; i++)
    {
        if(col[i]==col[here] || abs(col[here] - col[i]) == abs(here-i))
            return 0;
    }
    
    return 1;
}

void dfs(int depth)
{
    if(depth == N)
    {
        count += 1;
    }else
    {
        for(int i =0; i < N; i++)
        {
            col[depth] = i;
            if(check(depth))
                dfs(depth+1);
        }
    }
}

int main()
{
    scanf("%d", &N);
    
    dfs(0);
    printf("%d", count);
}