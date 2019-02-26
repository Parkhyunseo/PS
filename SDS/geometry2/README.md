Convex Hull (볼록 껍질)
1. Javis March O(H*N), H : 볼록껍질 수 , N : 점 수
    1. 최초 극단점 찾기 (제일 왼쪽 아래)
    2. 다음 극단점 찾기 (이전이 제일 왼쪽 아래면 다음 극단점 후보들을 ccw가 양수인지 확인하여
    3. 극단점 후보로만들고, 아니면 취소
    3. 반복
2. Graham Scan O(N logN)
    1. 각도 정렬 -> 기울기 순?(가장 왼쪽 아래니까)
        1. 기울기 순
        2. Arc Tan 2
        3. 외적 or CCW
    2. 각도 순 탐색
    3. 완료
3. Monotone Chain O(N logN)
    1. X축 정렬
    2. 위 껍질 탐색
    3. 아래 껍질 탐색
    4. 병합

Rotating Calipers
ccw가 반시계에서 시계로 바뀌게 되는 점

가장 먼 두 점