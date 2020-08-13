#include<bits/stdc++.h>
using namespace std;

int main()
{
    int l,b,c=0;
    cin>>l>>b;

    while (b>=l)
    {
        b*=2;
        l*=3;
        c+=1;
    }
    cout<<c;
    return 0;
}