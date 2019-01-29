// root 를찾는다 (아무도 가르키는 사람이 없으며 가르키는 게 있는 번호)
// 탐색해서 중복되는게 없다면 tree

int main()
{
    while(1)
    {
        int u, v;
        int tree[10];
        
        for(int i=0; i< 10; i++)
            tree[i] = -1;
        
        while(1)
        {
            scanf("%d, %d", &u, &v);
            
            if(u == 0 || v ==0)
                break;
            
            tree[u] = v;
        }
        
        
    }
}