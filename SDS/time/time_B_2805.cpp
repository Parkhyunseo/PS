#include<stdio.h>
#include<algorithm>

using namespace std;

int ans;
int height[1000000];

bool desc(int a, int b)
{
    return a > b;
}

int main()
{
    int N, M;
    int MAX = 0;
    
    scanf("%d %d", &N, &M);

    for(int i=0; i<N; i++)
    {
        scanf("%d", &height[i]);
        MAX += height[i];
    }
    
    sort(height, height+N,  desc);
    
    int low = 0;
    int high = height[0];
    int mid = 0;
    
    while(low <= high)
    {
        int total = MAX;
        
        mid = (low + high) >> 1;
        
        for(int i =0; i< N; i++)
        {
            if(height[i] >= mid)
                total -= mid;
            else
                total -= height[i];
        }
        
        if(total == M)
        {
            ans = mid;
            break;
        }
        
        if(M < total)
            low = mid + 1;
        else
        {
            ans = mid;
            high = mid - 1;
        }
    }
    
    if(ans == -1)
        ans = (low + high) >> 1;
    
    printf("%d", ans);
}