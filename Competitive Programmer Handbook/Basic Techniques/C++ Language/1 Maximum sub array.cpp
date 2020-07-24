#include <bits/stdc++.h>

using namespace std;

// how to take array of input()
// how to make functions
// how to operate the functions
// comparing it into different languages
int main(){
    //solution comes here
    int n,best=0,array[10];
    for (int a = 0; a < n; a++){
        for (int b=a; b<n;b++){
            int sum =0;
            for (int k=a ; k<=b; k++  ){
                sum += array[k];
            }
            best = max(best,sum);
        }
    }
cout << best << "\n";
}