from collections import defaultdict

def solution(friends, gifts):
    n = len(friends)
    gift_count = defaultdict(lambda: defaultdict(int))
    gift_index = defaultdict(int)
    next_month_gifts = defaultdict(int)

    # 선물 주고받은 횟수와 선물 지수 계산
    for gift in gifts:
        giver, receiver = gift.split()
        gift_count[giver][receiver] += 1
        gift_index[giver] += 1
        gift_index[receiver] -= 1

    # 다음 달 선물 계산
    for i in range(n):
        for j in range(i+1, n):
            friend1, friend2 = friends[i], friends[j]
            if gift_count[friend1][friend2] > gift_count[friend2][friend1]:
                next_month_gifts[friend1] += 1
            elif gift_count[friend1][friend2] < gift_count[friend2][friend1]:
                next_month_gifts[friend2] += 1
            else:
                if gift_index[friend1] > gift_index[friend2]:
                    next_month_gifts[friend1] += 1
                elif gift_index[friend1] < gift_index[friend2]:
                    next_month_gifts[friend2] += 1

    # 가장 많은 선물을 받을 친구의 선물 수 반환
    return max(next_month_gifts.values()) if next_month_gifts else 0