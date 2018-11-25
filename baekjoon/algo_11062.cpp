#include<iostream>
#include<string.h>
#include<algorithm>

using namespace std;

int dp[1001][1001][2];
int cards[1001];

int solve(int turn, int x, int y)
{
    int& reference = dp[x][y][turn];
    
    if(x == y)
    {
        if(turn == 0)
            return cards[x];
        else
            return 0;
    }
        
    if(reference != -1)
        return reference;
    
    if(turn == 0)
        reference = max(solve(turn^1, x+1, y) + cards[x], solve(turn^1, x, y-1) + cards[y]);
    else
        reference = min(solve(turn^1, x+1, y), solve(turn^1, x, y-1));
    
    return reference;
}
    

int main()
{
    int T;
    cin >> T;
    
    while(T--)
    {
        int N;
        cin >> N;
        memset(dp, -1, sizeof(dp));
        
        for(int i = 0; i < N; i++)
            scanf("%d", &cards[i]);
        printf("%d\n", solve(0, 0, N-1));
    }
    
    return 0;
}