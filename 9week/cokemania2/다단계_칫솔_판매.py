# https://school.programmers.co.kr/learn/courses/30/lessons/77486
# 다단계 칫솔 판매


def to_dict(enroll, referral):
    """
    조직도 그리기
    """
    tree_map = {}

    for e, r in list(zip(enroll, referral)):
        tree_map[e] = r

    return tree_map

def calculate_tip(amount):
    """
    10%의 금액을 계산
    """
    return amount // 10

def distribute_money(tree_map, money_map, seller, tip):
    """
    팁을 분배
    """
    if seller == '-':
        return

    tip_of_tip = calculate_tip(tip)
    money_map[seller] += tip_of_tip
    if tip_of_tip != 0:
        distribute_money(tree_map, money_map, tree_map[seller], tip_of_tip)


def solution(enroll, referral, seller, amount):
    answer = []

    tree_map = to_dict(enroll, referral)
    money_map = dict({e: 0 for e in enroll})
    for s, a in list(zip(seller, amount)):
        price = a * 100
        tip = calculate_tip(price)
        money_map[s] += (price - tip)
        distribute_money(tree_map, money_map, tree_map[s], tip)
    
    return [money_map[e] for e in enroll]

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))

