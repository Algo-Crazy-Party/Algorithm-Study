#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, M;
vector<int> lesson;
int low, high; // 블루레이 용량 투포인터 갈기기

int main() {
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

    cin >> N >> M;
    high = 0;

    lesson.resize(N);
    for (int i = 0; i < N; i++)
    {
        cin >> lesson[i];
        high += lesson[i]; // 모든 블루레이영상 1개에 담을만큼 용량
    }

    low = *max_element(lesson.begin(), lesson.end()); // 제일 큰 영상 하나만 담을 용량

    while (low < high) {
        int mid = (low + high) / 2;
        int cnt = 0; // 블루레이 갯수
        int sum = 0; // 블루레이 하나에 담긴 영상 용량

        for (int j = 0; j < N; j++)
        {
            if (sum+lesson[j] > mid) { // 블루레이 용량 초과
                cnt++; // 블루레이 갯수 증가
                sum = 0; // 블루레이 용량 초기화
            }
            sum += lesson[j]; // 블루레이에 영상 추가
        }
        if (sum > 0) cnt++; 
        // 마지막에 sum만큼 남아서 블루레이 하나 더 필요할때

        if (cnt <= M) {
            high = mid;
        } else {
            low = mid + 1;
        }
    }
    
    cout << low << endl;
    return 0;
}