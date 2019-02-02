#include<iostream>
#include<string.h>
#include<algorithm>

#define MAX 1001

using namespace std;

int cards[MAX];
int dp[MAX][MAX][2];

// turn => (0, 나), (1, 적)
int get(int lp, int rp, int turn)
{
    int& result = dp[lp][rp][turn];
    
    if(lp == rp)
    {
        if(turn == 0)
            return cards[lp];
        else
            return 0;
    }        
    
    
    if(result != -1)
        return result;


    if(turn == 0)
        result = max(cards[lp] + get(lp+1, rp, turn^1), cards[rp] + get(lp, rp-1, turn^1));
    else
        result = min(get(lp+1, rp, turn^1), get(lp, rp-1, turn^1));
        
    return result;
}

int main()
{
    int T;
    scanf("%d", &T);
    
    while(T--)
    {
        int N;
        scanf("%d", &N);
        
        memset(dp, -1, sizeof(dp));
        
        for(int i=0; i< N; i++)
            scanf("%d", &cards[i]);
            
        printf("%d\n", get(0, N-1, 0));
        
    }
    
}