#include<iostream>
#include<string.h>

#define MAX 99999999;

using namespace std;

int T;
int K;

int files[501];
int sumFiles[501];
int dp[501][501];

int main()
{
    scanf("%d", &T);
    
    while(T--)
    {
        memset(dp, 0, sizeof(dp));
        memset(files, 0, sizeof(files));
        
        scanf("%d", &K);
        
        for(int k=1; k <= K; k++)
        {
            scanf("%d", &files[k]);
            sumFiles[k] = sumFiles[k-1] + files[k];
        }
            
        for(int end=2; end <= K; end++)
        {
            for(int start=end-1; start > 0; start--)
            {
                dp[start][end] = MAX;
                
                for(int mid=start; mid <= end; mid++)
                    dp[start][end] = min(dp[start][end], 
                                    dp[start][mid] + dp[mid+1][end]);
                                    
                dp[start][end] += sumFiles[end] - sumFiles[start-1];
            }
        }
        
        printf("%d\n", dp[1][K]);
    }
}