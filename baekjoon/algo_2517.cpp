#include<iostream>
#include<vector>
#include<math>

typedef long long ll;

ll arr[500000];

ll init(vector<ll> &arr, vector<ll> &tree, int node, int start, int end)
{
    if(start == end)
        return tree[node] = arr[start];
        
    int mid = (start + end) >> 1;
    
    return tree[node] = init(arr, tree, node*2, start, mid) + init(arr,tree, node*2+1, mid+1, end);
}

ll query(vector<ll> tree, int node, int start, int end, int left, int right)
{
    if(end < left || start > right)
        return 0;
    
    if(left <= start && end <= right)
        return tree[node];
        
    
    int mid = ( start + end ) >> 1;
        
    return query(tree, node*2, start, mid, left, right) + query(tree, node*2+1, mid+1, end, left, right);
}

void update(vector<ll> &tree, int node, int start, int end, int index, intll diff)
{
    // 범위를 벗어났다.
    if(!(start <= index && index <= end))
        return;
        
    // 차이를 업데이트
    tree[node] += diff;
    
    // end point가 아니라면
    if(start != end)
    {
        int mid = (start + end) >> 1;
        update(tree, node*2, start, mid, index, diff);
        update(tree, node*2+1, mid+1, end, index, diff);
    }
}

int main()
{
    int N;
    scanf("%d", N);
    
    int h = (int)ceil(log2(n));
    int tree_size = (1 << (h+1));
    
    vector<ll> arr(N)
    vector<ll> tree(tree_size);
    
    for(int i = 0; i < N; i++)
        scanf("%d", &arr[i]);
        
    init(arr, tree, 1, 0, N-1);
    
    for(int i = 0; i < N; i++)
    {
        int get;
        scanf("%d", &get);
    }
    
}