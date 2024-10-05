def calculate_bonus(users: dict) -> list:
    bonus_users = []
    for user_id, user_data in users.items():
        referrals = user_data['referrals']
        first_level_referrals = []
        for referral in referrals:
            if users[referral]['package'] >= 1500:
                second_level_referrals = [r for r in users[referral]['referrals'] if users[r]['package'] >= 1500]
                if len(second_level_referrals) >= 2:
                    first_level_referrals.append([referral] + second_level_referrals[:2])
            if len(first_level_referrals) == 2:
                bonus_users.append((user_id, first_level_referrals))
                first_level_referrals = []
    return bonus_users

users = {
    1: {'packages': 1500, 'referrals': [2, 3, 14, 15]},
    2: {'package': 1500, 'referrals': [4, 5]},
    3: {'package': 1500, 'referrals': [6, 7]},
    4: {'package': 1500, 'referrals': []},
    5: {'package': 1500, 'referrals': [8, 9]},
    6: {'package': 1500, 'referrals': [10, 11]},
    7: {'package': 3000, 'referrals': [12, 13]},
    8: {'package': 1500, 'referrals': []},
    9: {'package': 1500, 'referrals': []},
    10: {'package': 1500, 'referrals': []},
    11: {'package': 1500, 'referrals': []},
    12: {'package': 1500, 'referrals': []},
    13: {'package': 1500, 'referrals': []},
    14: {'package': 1500, 'referrals': [16, 17]},
    15: {'package': 1500, 'referrals': [18, 19]},
    16: {'package': 1500, 'referrals': []},
    17: {'package': 1500, 'referrals': []},
    18: {'package': 1500, 'referrals': []},
    19: {'package': 1500, 'referrals': []},
}
print(calculate_bonus(users))
