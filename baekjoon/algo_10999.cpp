#include<iostream>
#include<math.h>
#include<stdio.h>

using namespace std;

typedef long long;

ll init(vector<int> &tree, vector<int> arr, int node, int start, int end)
{
    if(start == end){
        return tree[node] = arr[start];
    }
    
    int mid = (start+end) >> 2;
    return init(tree, arr, node*2, start, mid) + init(tree, arr, node*2+1, mid+1, end);
}

ll update(vector<int> &tree, int start, int end, int node, int left, int rgiht, ll plus)
{
    if(!(start <= index && index <= end))
        return;
        
    tree[node] += plus;
    
    if(start != end){
        int mid = (start+end) >> 2;    
        update(tree, start, mid, node*2, index, plus);
        update(tree, mid+1, end, node*2+1, index, plus);
    }
}

ll sum(vector<int> &tree int start, int end, int node, int left, int right)
{
    if( left < start or right > end)
        return 0;
    
    if( start <= left && right <= end)
        return tree[node];
        
    int mid = (start+end) >> 2;
    return sum(tree, start, mid, node*2, left, right) + sum(tree, start, mid, node*2+1, left, right)
}

int main(){
    int N, M, K;
    scanf("%d %d %d", &N, &M, &K);
    
    vector<int> tree(4*N);
    vector<int> arr(N);
    
    for(int i=0; i<N; i++)
        scanf("%d", &arr[i]);
    
    M += K;
    
    while(M--){
        int get;
        scanf("%d", &get);
        
        if(get==1){
            int pos;
            ll val, plus;
            scanf("%d %d %d", &pos, &val, &plus);
            arr[pos-1] += plus;
            update(tree, 0, N-1, 1, pos-1, val);
        }else if(get==2){
            int left, right;
            scanf("%d %d",&left, &right);
            sum(tree, 0, N-1, 1, left, right);
        }
    }
}