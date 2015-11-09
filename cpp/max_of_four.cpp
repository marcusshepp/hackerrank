#include <iostream>
#include <cstdio>
using namespace std;

int max_of_four(int a, int b, int c, int d){
    int holder;
    if(a > b && a > c && a > d){
        holder = a;
    }else if(b > a && b > c && b > d){
        holder = b;
    }else if(c > b && c > a && c > d){
        holder = c;
    }else if(d > b && d > c && d > a){
        holder = d;
    }
    return holder;
}
int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    return 0;
}