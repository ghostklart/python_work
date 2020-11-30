#copy of user_profile.py
def build_profile(first, last, **user_info):
    """building dictionary with user information"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('david', 'macintosh', username = 'tester',
                            ip_address = '192.168.0.100', 
                            login_date  = '11-05-2020')

print(user_profile)