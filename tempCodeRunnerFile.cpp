#include<bits/stdc++.h>
using namespace std;

int main(){
    int i = 2;
    string str = "HELLO WORLD";
    cout << str[i] << " " << str.length() << endl;
    str.erase(i, 2);
    cout << str[i] << " " << str.length() << endl;
    return 0;
}