#include <iostream>
#include <string>
using namespace std;

int main() {
    string a;
    string b;
    cin >> a;
    cin >> b;
    int asize = a.size();
    int bsize = b.size();
    cout << asize << " " << bsize << "\n";
    cout << a + b << "\n";
    string aa = a;
    a[0] = b[0];
    b[0] = aa[0];
    cout << a << " " << b << "\n";   
    return 0;
}