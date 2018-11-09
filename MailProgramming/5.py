"""
정수 배열과 타겟 숫자가 주어지면, 합이 타겟값이 되는 두 원소의 인덱스를 찾으시오.
단, 시간복잡도 O(n) 여야 한다.
"""

nums = list(map(int, input().split()))
target = int(input())
collector = dict()

for i in range(len(nums)):
    diff = target-nums[i]
    if diff in collector:
        print(collector[diff], i)
        break
    collector[nums[i]] = i
    
