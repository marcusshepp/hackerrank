#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int n;
    int nn;
    cin>>n;
    cin>>nn;
    for(int i = n; i <= nn; i++){
       if(i > 9){
           if(i % 2 == 0){
               cout<<"even";
           } else {
               cout<<"odd";
           }
       } else if(i == 1){
           cout<<"one";
       } else if(i == 2){
           cout<<"two";
       } else if(i == 3){
           cout<<"three";
       } else if(i == 4){
           cout<<"four";
       } else if(i == 5){
           cout<<"five";
       } else if(i == 6){
           cout<<"six";
       } else if(i == 7){
           cout<<"seven";
       } else if(i == 8){
           cout<<"eight";
       } else if(i == 9){
           cout<<"nine";
       }
       cout<<"\n";
    }
    return 0;
}