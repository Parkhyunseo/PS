#include<iostream>
#include<vector>
#include<string.h>

#define K 64321
int realtions[502][502];
int degree[502];

int main()
{
    int N, M;
    int i, j, k;
    int result = 0;
    
    scanf("%d %d", &N, &M);
    
    for(int i=1; i<=N; i++)
        for(int i=1; i<=N; i++)
            realtions[i][j] = K;
    
    for(int m=0; m < M; m++)
    {
        int f, t;
        scanf("%d %d", &f, &t);
        
        realtions[f][t] = 1;
    }
    
    for(int k=1; k<= N;k++)
        for(int j=1; j<= N; j++)
            for(int i=1; i<= N; i++)
                if(realtions[i][j] > realtions[i][k] + realtions[k][j])
                    realtions[i][j] = realtions[i][k] + realtions[k][j];
                    
    for(int i=1; i<=N ;i++)
    {
        for(int j=1; j<=N ;j++)
        {
            printf("%d ", realtions[i][j]);
            if(realtions[i][j] != K)
            {
                degree[i] += 1;
                degree[j] += 1;
            }
        }
        printf("\n");
    }
    
    for(int i=1; i<=N ;i++)
        if(degree[i] == N-1)
            result += 1;
            
    printf("%d", result);
    
}

/*
        int lca = a;
 
        // a와 b가 다르다면 현재 깊이가 같으니
        // 깊이를 계속 올려 서로 다른 노드의 조상이 같아질 때까지 반복한다.
        // 즉, 서로 다른 노드(2,3)의 조상이 1로 같다면 lca = ac[2][0]에 의해 2의 조상이 1임을 알 수 있고
        // 마찬가지로 ac[3][0] 또한 3의 조상이 1임을 알게되며 알고리즘이 끝이난다.
        if (a != b)
        {
            for (int i = max_level; i >= 0; i--)
            {
                if (ac[a][i] != ac[b][i])
                {
                    a = ac[a][i];
                    b = ac[b][i];
                }
                lca = ac[a][i];
            }
        }


출처: https://www.crocus.co.kr/660 [Crocus]
*/