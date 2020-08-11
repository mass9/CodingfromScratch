#include<bits/stdc++.h>
using namespace std;

int main(){
    char s1[1000],s2[1000];
    int result=0,res;
    cin>>s1;
    cin>>s2;

    for (int i=0; i<strlen(s1); i++){
        s1[i]=tolower(s1[i]);
        s2[i]=tolower(s2[i]);

    }
    res = strcmp(s1,s2);
    if(res < 0 ){
        result = -1;
    }

    if (res > 0){
        result= 1;
    }

    cout<<result;

return 0;
}