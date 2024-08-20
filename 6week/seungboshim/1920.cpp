#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, M;
vector<int> A;
vector<int> B;

int binarySearch(int b) {
    int left = 0;
    int right = N-1;
    int mid;

    while (left <= right) {
        mid = (left + right) / 2;
        
        if (A[mid] == b) {
            return 1;
        }

        if (A[mid] < b) {
            left = mid+1;
        } else {
            right = mid-1;
        }
    }
    return 0;
}

int main() {
    cin >> N;
    A.resize(N);
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }
    
    cin >> M;
    B.resize(M);
    for (int i=0; i<M; i++) {
        cin >> B[i];
    }

    sort(A.begin(), A.end());

    for (auto &&i : B)
    {
       cout << binarySearch(i) << '\n';
    }
    return 0;
}