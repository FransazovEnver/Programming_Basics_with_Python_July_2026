MUSSELS = 7.50

price_of_mackerel = float(input())
price_of_sprat = float(input())
bonito = float(input())
horse_mackerel = float(input())
mussels = int(input())

price_bonito = price_of_mackerel + price_of_mackerel * 0.6
sum_bonito = bonito * price_bonito
price_horse_mackerel = price_of_sprat + price_of_sprat * 0.8
sum_sprat = horse_mackerel * price_horse_mackerel
sum_mussels = mussels * MUSSELS
sum_of_all_fish = sum_bonito + sum_sprat + sum_mussels
print(f'{sum_of_all_fish:.2f}')
