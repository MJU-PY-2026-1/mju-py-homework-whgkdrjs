# 파일이름 :대학생들을 위한 주식 수익관리 프로그램
# 작 성 자 :조항건
stock_names = []
stock_quantities = []
name = input('사용자 이름을 입력하시오:')
age = int(input('사용자의 나이를 입력하시오:'))
for i in range(5):
    stock_name = input('주식의 이름을 입력하시오:')
    stock_names.append(stock_name)
stock_names.pop(4)
print()
stock_quantity1 = int(input(f'{stock_names[0]}주식의 수량을 입력하시오:'))
stock_quantities.append(stock_quantity1)
stock_quantity2 = int(input(f'{stock_names[1]}주식의 수량을 입력하시오:'))
stock_quantities.append(stock_quantity2)
stock_quantity3 = int(input(f'{stock_names[2]}주식의 수량을 입력하시오:'))
stock_quantities.append(stock_quantity3)
stock_quantity4 = int(input(f'{stock_names[3]}주식의 수량을 입력하시오:'))
stock_quantities.append(stock_quantity4)
print()
now_price1 = float(input(f'{stock_names[0]}주식의 현재 가격을 입력하시오:'))
now_price2 = float(input(f'{stock_names[1]}주식의 현재 가격을 입력하시오:'))
now_price3 = float(input(f'{stock_names[2]}주식의 현재 가격을 입력하시오:'))
now_price4 = float(input(f'{stock_names[3]}주식의 현재 가격을 입력하시오:'))
print()
purchase_price1 = float(input(f'{stock_names[0]}주식의 매수가격을 입력하시오:'))
purchase_price2 = float(input(f'{stock_names[1]}주식의 매수가격을 입력하시오:'))
purchase_price3 = float(input(f'{stock_names[2]}주식의 매수가격을 입력하시오:'))
purchase_price4 = float(input(f'{stock_names[3]}주식의 매수가격을 입력하시오:'))
print()
rate_1 = (now_price1-purchase_price1)/purchase_price1*100
rate_2 = (now_price2-purchase_price2)/purchase_price2*100
rate_3 = (now_price3-purchase_price3)/purchase_price3*100
rate_4 = (now_price4-purchase_price4)/purchase_price4*100      
print()
print(f'{stock_names[0]}의 수익률={rate_1}%')
print(f'{stock_names[1]}의 수익률={rate_2}%')
print(f'{stock_names[2]}의 수익률={rate_3}%')
print(f'{stock_names[3]}의 수익률={rate_4}%')
print()
max_stock = max(stock_quantities)
if stock_quantity1 == max(stock_quantities):
    print(f'가장 많이 보유한 주식: {stock_names[0]} 수량: {max_stock}')
if stock_quantity2 == max(stock_quantities):
    print(f'가장 많이 보유한 주식: {stock_names[1]} 수량: {max_stock}')
if stock_quantity3 == max(stock_quantities):
    print(f'가장 많이 보유한 주식: {stock_names[2]} 수량: {max_stock}')
if stock_quantity4 == max(stock_quantities):
    print(f'가장 많이 보유한 주식: {stock_names[3]} 수량: {max_stock}')
print()
min_stock = min(stock_quantities)
if stock_quantity1 == min(stock_quantities):
    print(f'가장 적게 보유한 주식: {stock_names[0]} 수량: {min_stock}')
if stock_quantity2 == min(stock_quantities):
    print(f'가장 적게 보유한 주식: {stock_names[1]} 수량: {min_stock}')
if stock_quantity3 == min(stock_quantities):
    print(f'가장 적게 보유한 주식: {stock_names[2]} 수량: {min_stock}')
if stock_quantity4 == min(stock_quantities): 
    print(f'가장 적게 보유한 주식: {stock_names[3]} 수량: {min_stock}')
print()

sums_quantities = 0
for num in stock_quantities:
    sums_quantities += num
print(f'보유한 총 주식의 수:{sums_quantities}개')




if rate_1 > 100:
    print(f'{stock_names[0]}의 수익률이 엄청 나시군요!! ')
elif rate_1 < 0:
    print(f'{stock_names[0]}의 수익률이 마이너스 입니다 ㅠㅠ 부분 매도를 추천드립니다')
    
else:
    print(f'{stock_names[0]}의 수익률이 플러스 입니다!! 부분 매도를 추천드립니다')
print()
if rate_2 > 100:
    print(f'{stock_names[1]}의 수익률이 엄청 나시군요!! ')
elif rate_2 < 0:
    print(f'{stock_names[1]}의 수익률이 마이너스 입니다 ㅠㅠ 부분 매도를 추천드립니다')
    
else:
    print(f'{stock_names[1]}의 수익률이 플러스 입니다!! 부분 매도를 추천드립니다')
print()
if rate_3 > 100:
    print(f'{stock_names[2]}의 수익률이 엄청 나시군요!! ')
elif rate_3 < 0:
    print(f'{stock_names[2]}의 수익률이 마이너스 입니다 ㅠㅠ 부분 매도를 추천드립니다')
else:
    print(f'{stock_names[2]}의 수익률이 플러스 입니다!! 부분 매도를 추천드립니다')
print()
if rate_4 > 100:
    print(f'{stock_names[3]}의 수익률이 엄청 나시군요!! ')
elif rate_4 < 0:
    print(f'{stock_names[3]}의 수익률이 마이너스 입니다 ㅠㅠ 부분 매도를 추천드립니다')
else:
    print(f'{stock_names[3]}의 수익률이 플러스 입니다!! 부분 매도를 추천드립니다')
print()
if rate_1 > 50 and rate_2 > 50 and rate_3 > 50 and rate_4 > 50:
    print(f'당신은 워렌버핏 급 주식 고수입니다')
if rate_1 < 0 and rate_2 < 0 and rate_3 < 0 and rate_4 < 0:
    print(f'당신은 주식시장에서 떠나야합니다..ㅠㅠ')
