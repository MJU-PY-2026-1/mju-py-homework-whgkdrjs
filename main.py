# 파일이름 :대학생들을 위한 주식 수익관리 프로그램 ver3.0
# 작 성 자 :조항건
stock_names = []
stock_quantities = []
rates = []
is_data_entered = False

# 수익률 계산
def calculate_rate(now_price, purchase_price):
    rate = (now_price - purchase_price) / purchase_price * 100
    return rate
# 주식 정보 입력
def input_data():
    global is_data_entered
    global stock_names, stock_quantities, rates
    stock_names = []
    stock_quantities = []
    rates = []
    print('\n---[1.주식 정보 입력]---')
    for i in range(4):
        name = input(f'{i+1}번째 주식의 이름을 입력하시오:')
        quantity = int(input(f'{name}주식의 수량을 입력하시오:'))
        now_price = float(input(f'{name}주식의 현재 가격을 입력하시오:'))
        purchase_price = float(input(f'{name}주식의 매수가격을 입력하시오:'))

        stock_names.append(name)
        stock_quantities.append(quantity)
        rates.append(calculate_rate(now_price, purchase_price))
        print('_'*30)
    is_data_entered = True
    print('입력이 완료 되었습니다')

#주식 정보 조회
def view_data():
    if not is_data_entered:
        print('\n먼저 1번 메뉴를 통해 데이터를 입력해주세요.\n')
        return
    print('\n---[2. 보유 주식 조회]---')
    for i in range(4):
        print(f'{stock_names[i]}: 수량 {stock_quantities[i]}개, 수익률 {rates[i]:.2f}%')
        print()

#주식 정보 분석
def analyze_data():
    if not is_data_entered:
        print('\n 먼저 1번 메뉴를 통해 데이터를 입력해주세요')
        return
    print('\n---[3. 포트폴리오 분석]---')

    max_stock = max(stock_quantities)
    min_stock = min(stock_quantities)
    max_index = stock_quantities.index(max_stock)
    min_index = stock_quantities.index(min_stock)

    print(f'> 가장 많이 보유한 주식: {stock_names[max_index]} (수량: {max_stock})')
    print(f'> 가장 적게 보유한 주식: {stock_names[min_index]} (수량: {min_stock})')
    print(f'> 보유한 총 주식의 수: {sum(stock_quantities)}개\n ')

    for i in range(4):
        if rates[i] > 100:
            print(f'> {stock_names[i]}: 수익률이 엄청나시군요!!')
        elif rates[i] < 0:
            print(f'> {stock_names[i]}: 수익률이 마이너스 입니다 더 큰 손실을 막기위해 부분 매도를 추천드립니다ㅠㅠ')
        else:
            print(f'> {stock_names[i]}: 수익률이 플러스 입니다! 일부를 수익 창출하시는 것을 추천 드립니다!! ')
#메인 로직 메뉴
print('환영합니다! 주식관리 프로그램을 시작합니다')
name = input('사용자 이름을 입력하시오:')
age = int(input('사용자의 나이를 입력하시오:'))

while True:
    print('='*30)
    print(f'{name}({age}세)님의 주식 관리 메뉴')
    print('1. 입력')
    print('2. 조회')
    print('3. 분석')
    print('4. 종료')
    print('='*30)

    choice = input('원하시는 메뉴 번호를 입력하세요: ')

    if choice == '1':
        input_data()
    elif choice == '2':
        view_data()
    elif choice == '3':
        analyze_data()
    elif choice == '4':
        print('\n프로그램을 종료합니다. 성투하세요!')
        break
    else:
        print('\n[오류] 잘못된 입력 입니다. 1~4 사이의 숫자를 입력해주세요')
