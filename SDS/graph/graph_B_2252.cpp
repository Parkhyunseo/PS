#include<iostream>
#include<queue>

using namespace std;

int main()
{
    priority_queue<pair<int, int>> pq;
    
    int N, M;
    
    scanf("%d %d", &N, &M);
    
    int students[N];
    
    for(int i=1; i <= N; i++)
        students[i] = 1;
    
    for(int i=0; i < M; i++)
    {
        int front, back;
        
        scanf("%d %d", &front, &back);
        
        students[front] += students[back];
    }
    
    for(int i=1; i <= N; i++)
        pq.push({students[i], i});
        
    for(int i=0; i < N; i++)
    {
        pair<int, int> height = pq.top();
        pq.pop();
        printf("%d ", height.second);
    }
}