bitcoin = int(input())
yen = float(input())
commission = float(input())

bitcoin_in_euro = bitcoin * 1168 / 1.95
yen_in_euro = yen * 0.15 * 1.76 / 1.95
total_euro = bitcoin_in_euro + yen_in_euro
total = total_euro * (1 - (commission/100))
print(f"{total:.2f}")