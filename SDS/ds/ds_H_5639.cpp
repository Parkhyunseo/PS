#include<iostream>

typedef struct Node{
    int value;
    Node *parent;
    Node *left;
    Node *right;
}Node;

void postorder(Node node)
{
    if(node == 0)
        return;
        
    postorder(node.left);
    postorder(node.right);
    printf("%d\n", node.value);
}

int main()
{
    Node root;
    int value;
    
    scanf("%d", &value);
    root = Node(value, 0, 0, 0);
    
    while(scanf("%d", &value) != -1)
    {
        Node node = root;
        while(1)
        {
            if(value > node.value)
            {
                if(node.right != 0)
                    node = node.right;
                else
                    node.right = Node(value, node, 0, 0);
                    break;
            }else{
                if(node.right != 0)
                    node = node.right;
                else
                    node.right = Node(value, node, 0, 0);
                    break;
            }
        }
    }
    
    postorder(root);
}
