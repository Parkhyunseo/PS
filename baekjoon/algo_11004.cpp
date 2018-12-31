#include <iostream>
#include <algorithm>

using namespace std;

int arr[5000005];
int n, k; 

int main() 
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	cin >> n >> k;
    
    for (int i = 0; i < n; i++) 
        cin >> arr[i];
    
    nth_element(arr, arr + k - 1, arr + n);

	cout << arr[k - 1];

    return 0;
}