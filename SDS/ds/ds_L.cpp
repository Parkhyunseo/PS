// O(NlogN)

// map으로 중복을 제거하거나
// 이전 값보다 작은 값이 나온다 안곱한다.
#include<stdio.h>
#include<queue>

using namespace std;

long long primes[101];

long long INT_MAX = 2147483649;

priority_queue<long long, vector<long long>, greater<long long>> pq;

int main()
{
    int K, N;
    int point =0;
    
    scanf("%d %d", &K, &N);
    
    for(int i=0; i < K; i++)
    {
        scanf("%lld", &primes[i]);
        pq.push(primes[i]);
    }
    
    long long small;
    while(!pq.empty() && point < N)
    { 
        small = pq.top();
        pq.pop();
        
        for(int i=0; i < K; i++)
        {
            long long temp = small*primes[i];
            pq.push(temp);
            
            // ******  중요 ***********
            if(small % primes[i] == 0)
                break;
            
        }
        point += 1;
    }
    
    printf("%lld\n", small);
}