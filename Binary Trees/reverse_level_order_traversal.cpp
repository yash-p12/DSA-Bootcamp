// Problem Link :  https://practice.geeksforgeeks.org/problems/reverse-level-order-traversal/1

#include<bits/stdc++.h>
using namespace std;
struct Node
{
    int data;
    struct Node* left;
    struct Node* right;
};
vector<int> reverseLevelOrder(Node *node)
{
   vector<int>v;
        queue<Node*>q;
        q.push(node);
        while(!q.empty()){
            Node * curr = q.front();
            q.pop();
            v.push_back(curr->data);
            if(curr->right!=NULL){
                q.push(curr->right);
            }
            if(curr->left!=NULL){
                q.push(curr->left);
            }
        }
        reverse(v.begin(),v.end());
        return v;
}