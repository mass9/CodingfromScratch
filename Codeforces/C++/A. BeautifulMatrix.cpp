#include<bits/stdc++.h>
using namespace std;

int main()
{
    int r=5,c=5, a[100][100], ri,ci;
    for(int i=0;i<r;i++)
        for(int j=0 ;j<c;j++)
        {
            // cout<<"Taking inputs for the array.\n";
            cin>>a[i][j];
        }
    
     for(int i=0;i<r;i++)
        for(int j=0 ;j<c;j++)
        {
            if (a[i][j] == 1){
                ri=i;
                ci=j;
            }
        }
    // cout<<"Row detected: "<<ri<<"\n";
    // cout<<"coloumn detected: "<<ci<<"\n";
    // cout<<"Number of moves are: "<<(abs(2-ri) + abs(2-ci));
    cout<<(abs(2-ri) + abs(2-ci));

    return 0;
}