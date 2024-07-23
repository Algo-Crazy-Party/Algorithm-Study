# lecture_cnt, blueray_cnt = map(int, input().split())
# lecture_length_list = list(map(int, input().split()))
# left = max(lecture_length_list)
# right = sum(lecture_length_list)

# while left < right:
#     mid = left + (right - left) // 2
#     bluray_list = []
#     for length in lecture_length_list:
#         if len(bluray_list) == 0 or sum(bluray_list[-1]) + length > mid:
#             bluray_list.append([length])
#         else:
#             bluray_list[-1].append(length)
#     if len(bluray_list) > blueray_cnt:
#         left = mid + 1
#     else:
#         right = mid 

# print(left)


lecture_cnt, blueray_cnt = map(int, input().split())
lecture_length_list = list(map(int, input().split()))
left = max(lecture_length_list)
right = sum(lecture_length_list)

def can_divide(mid):
    count = 1
    current_sum = 0
    for length in lecture_length_list:
        if current_sum + length > mid:
            count += 1
            current_sum = length
            if count > blueray_cnt:
                return False
        else:
            current_sum += length
    return True

while left < right:
    mid = left + (right - left) // 2
    if can_divide(mid):
        right = mid
    else:
        left = mid + 1

print(left)