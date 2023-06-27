per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = input('money = ')

deposit = []

TKB = per_cent.get('ТКБ') * int(money)
deposit.append(int(TKB))

CKB = per_cent.get('СКБ') * int(money)
deposit.append(int(CKB))

VTB = per_cent.get('ВТБ') * int(money)
deposit.append(int(VTB))

SBER = per_cent.get('СБЕР') * int(money)
deposit.append(int(SBER))

print('deposit =', deposit)

print('Максимальная сумма, которую вы можете заработать —', int(max(deposit)))