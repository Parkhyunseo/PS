#include<iostream>

using namespace std;

int gcd(int a, int b)
{
    if(a < b)
    {
        int tmp = a;
        a = b;
        b = tmp;
    }
    
    while(b != 0)
    {
        int tmp = b;
        b = a % b;
        a = tmp;
    }
    
    return a;
}

int main()
{
    int T;
    
    scanf("%d", &T);
    
    while(T--)
    {
        int N;
        int count = 0;
        scanf("%d", &N);
        
        for(int i=1; i<N+1; i++)
        {
            for(int j=i+1; j<N+1; j++)
            {
                if(gcd(j,i) == 1)
                    count += 1;
            }
        }
        
        printf("%d\n", count*2+3);
    }
}