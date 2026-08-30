team = input()
souvenir = input()
purchase_souvenir = int(input())

total = 0.0
is_valid_country = True
is_valid_souvenir = True

if team == 'Argentina':
    if souvenir == 'flags':
        total = purchase_souvenir * 3.25
    elif souvenir == 'caps':
        total = purchase_souvenir * 7.20
    elif souvenir == 'posters':
        total = purchase_souvenir * 5.10
    elif souvenir == 'stickers':
        total = purchase_souvenir * 1.25
    else:
        is_valid_souvenir = False
elif team == 'Brazil':
    if souvenir == 'flags':
        total = purchase_souvenir * 4.20
    elif souvenir == 'caps':
        total = purchase_souvenir * 8.50
    elif souvenir == 'posters':
        total = purchase_souvenir * 5.35
    elif souvenir == 'stickers':
        total = purchase_souvenir * 1.20
    else:
        is_valid_souvenir = False
elif team == 'Croatia':
    if souvenir == 'flags':
        total = purchase_souvenir * 2.75
    elif souvenir == 'caps':
        total = purchase_souvenir * 6.90
    elif souvenir == 'posters':
        total = purchase_souvenir * 4.95
    elif souvenir == 'stickers':
        total = purchase_souvenir * 1.10
    else:
        is_valid_souvenir = False
elif team == 'Denmark':
    if souvenir == 'flags':
        total = purchase_souvenir * 3.10
    elif souvenir == 'caps':
        total = purchase_souvenir * 6.50
    elif souvenir == 'posters':
        total = purchase_souvenir * 4.80
    elif souvenir == 'stickers':
        total = purchase_souvenir * 0.90
    else:
        is_valid_souvenir = False

else:
    is_valid_country = False

if not is_valid_country:
    print('Invalid country!')
elif not is_valid_souvenir:
    print('Invalid stock!')
else:
    print(f'Pepi bought {purchase_souvenir} {souvenir} of {team} for {total:.2f} lv.')
