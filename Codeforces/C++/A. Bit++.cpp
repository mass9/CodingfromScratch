#include <bits/stdc++.h>

using namespace std;

int main(){
    int t,x=0;
    string s;
    cin>>t;

    while (t>0){
        cin>>s;
        if (s.find('+') !=string::npos){
            x+=1;
        }
        else{
            x-=1;
        }   
        t -=1;
    }
    cout<<x;
return 0;
}