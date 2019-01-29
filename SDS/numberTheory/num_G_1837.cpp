#include<iostream>
#include<vector>
#include<math.h>

using namespace std;

#define MAX 100001

bool primes[MAX];

void che()
{
    for(int i=2; i < int(sqrt(MAX))+1 ; i++)   
    {
        if(!primes[i])
        {
            for(int j=i*i; j <= MAX ; j += i)
                primes[j] = true;
        }
    }
}

int main()
{
    int P, K;
    int find = 0;
    scanf("%d %d", &P, &K);
    
    for(int i=2; i<= K ; i++)
    {
        if(!primes[i])
        {
            if(P % i == 0)
            {
                find = 1;
                printf("BAD %d\n", i);
                break;
            }
        }
    }
        
    if(!find)
        printf("GOOD\n");
}