#include<iostream>
#include<algorithm>
#include<string.h>

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    
    int points[1001];
    
    while(T--)
    {
        int N;
        int count = 0, target, k;
        scanf("%d", &N);
        
        memset(points, 1e9, sizeof(points));
        
        for(int i=0; i < N; i++)
            scanf("%d", &points[i]);
            
        sort(points, points+N);
        
        for(int i=0; i < N-2; i++)
        {
            k = i+2;
            for(int j=i+1; j < N-1; j++)
            {
                int diff = points[j] - points[i];
                target = points[j] + diff;
                
                while(k < N && points[k] < target)
                    k++;
                    
                if(k != N)
                {
                    if(points[k] == target)
                        count++;
                }else
                    break;
            }
        }
        
        printf("%d\n", count);
    }
}