#include<vector>
#include<iostream>
#include<cstring>
#include<algorithm>

using namespace std;

int dp[100001];

int main()
{
    int T = 3, i, j;
    
    while(T--)
    {
        int N, total = 0;
        vector<pair<int, int>> coins;
        
        scanf("%d", &N);
        
        memset(dp, 0, sizeof(dp));
        
        dp[0]=1;
        for(i=0; i< N; i++)
        {
            int val, count;
            scanf("%d %d", &val, &count);
            
            coins.push_back({val, count});
            //for(j=1; j <= count ; j++)
            //    dp[val*j] = 1;
            
            total += val*count;
        }
        
        sort(coins.begin(), coins.end());
        
        for(int i =1; i<=coins[0].second; i++)
            dp[i*coins[0].first] = 1;
        
        for(i=1; i<N; i++)
        {
            int val, count;
            val = coins[i].first;
            count = coins[i].second;
            
            for(j=total/2 ; j >= 0 ; j--)
            {
                if(!dp[j])
                    continue;
                    
                for(int c=1; c <= count; c++)
                {
                    if (j + c * val > total / 2)
						break;
						
                    dp[j+val*c] = 1;
                }
            }
        }
        
        printf("%d\n", dp[total/2]);
    }
}