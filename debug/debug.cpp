#include <iostream>

using namespace std;

int d[11];

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t;
    int n;

    cin >> t;

    d[1] = 1;
    d[2] = 2;
    d[3] = 4;
    while (t--){
        cin >> n;

        for (int i = 4; i <= n; i++){
            d[i] = d[i-1] + d[i-2] + d[i-3];
        }
        cout << d[n] << '\n';
    }
    return 0;
}