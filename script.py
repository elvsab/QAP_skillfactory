per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
print("Введите сумму вклада")
money = input()
deposit_TKB = per_cent.get('ТКБ')*float(money)/100
deposit_SKB = per_cent.get('СКБ')*float(money)/100
deposit_VTB = per_cent.get('ВТБ')*float(money)/100
deposit_SBER = per_cent.get('СБЕР')*float(money)/100
deposit = [int(deposit_TKB), int(deposit_SKB), int(deposit_VTB), int(deposit_SBER)]
print(deposit)
print("Максимальная сумма, которую вы можете заработать - ", max(deposit))
