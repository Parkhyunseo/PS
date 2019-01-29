#include<iostream>
#include<vector>
#include<math.h>

using namespace std;

#define MAX 10000001

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
    int N;
    scanf("%d", &N);
    
    vector<int> pl;
    for(int i=2; i<= MAX ; i++)
        if(!primes[i])
            pl.push_back(i);
            
    int p = 0;
    while(1)
    {
        if(p >= pl.size() || N <= 1)
            break;
            
        if(N%pl[p] == 0)
        {
            printf("%d\n",pl[p]);
            N /= pl[p];
        }else
            p += 1;
    }
}