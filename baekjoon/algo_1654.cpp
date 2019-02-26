#include<iostream>

using namespace std;

int N, K;
int lines[10001];

int binarySearch(int max)
{
    long long left = 1;
    long long right = max;
    int ans = 0;
    
    while(left <= right)
    {
        long long mid = (left+right) >> 1;
        int count = 0;
        
        for(int k=0; k<K; k++)   
            count += int(lines[k] / mid);
            
        if(count >= N) {
            if(mid > ans)
                ans = mid;
            left = mid + 1;
        }
        else
            right = mid - 1;
    }
    
    return ans;
}

int main()
{
    scanf("%d %d", &K, &N);
    
    int m = 0;
    
    for(int k=0; k < K; k++)
    {
        scanf("%d", &lines[k]);
        m = max(m, lines[k]);
    }
        
    printf("%d", binarySearch(m));
}