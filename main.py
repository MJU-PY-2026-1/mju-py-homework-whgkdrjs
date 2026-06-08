# 파일이름 :대학생들을 위한 주식 수익관리 프로그램 ver3.0
# 작 성 자 :조항건
portfolio = []
is_data_entered = False

# 수익률 계산
def calculate_rate(now_price, purchase_price):
    try:
        return(now_price - purchase_price) / purchase_price * 100
    except ZeroDivisionError:
        return 0.0
# 주식 정보 입력
def input_data():
    global is_data_entered,portfolio
    portfolio = []
    print('\n---[1.주식 정보 입력]---')

    while True:
        try:
            people_count = int(input('총 몇명의 투자자 데이터를 입력하시겠습니까?:'))
            break
        except ValueError:
            print('[오류] 숫자로만 정확히 입력해주세요')
    for p in range(people_count):
        print(f'\n======================')
        user_name = input(f'{p+1}번째 투자자의 이름을 입력하시오: ')

        while True:
            try:
             stock_count = int(input(f'{user_name}님이 보유한 주식은 몇 종류입니까?: '))
             break
            except ValueError:
                print('[오류]숫자로만 정확히 입력해주세요.')
    
        for s in range(stock_count):
            print(f'--------------------')
            stock_name = input(f'({s+1})주식 이름을 입력하시오: ')

            while True:
                try:
                    quantitiy = int(input(f'{stock_name}의 수량을 입력하시오:'))
                    now_price = float(input(f'{stock_name}의 현재가격을 입력하시오:'))
                    purchase_price = float(input(f'{stock_name}의 매수가격을 입력하시오:'))
                    break
                except ValueError:
                    print('[오류] 수량과 가격은 숫자로만 입력 가능합니다. 다시 입력해주세요.')

            rate = calculate_rate(now_price,purchase_price)
            portfolio.append([user_name,stock_name,quantitiy,now_price,purchase_price,rate])

    is_data_entered = True
    print('\n[성공] 모든 투자자의 주식 정보 입력이 완료 되었습니다!')

def view_data():
    if not is_data_entered or len(portfolio) == 0:
        print('[안내] 데이터가 없습니다. 1번 메뉴에서 입력하거나 5번으로 불러와주세요')
        return
    print('\n[2.보유 주식 조회 (전체 사용자)]---')
    print(f'{'투자자':<10}ㅣ{'주식명':<12}ㅣ{'수량':<6}ㅣ{'현재가':<10}ㅣ{'매수가':<10}ㅣ{'수익률'}')
    print('-'*75)

    for i in range(len(portfolio)):
        user_name =portfolio[i][0]
        stock_name =portfolio[i][1]
        quantity =portfolio[i][2]
        now_price =portfolio[i][3]
        purchase_price =portfolio[i][4]
        rate =portfolio[i][5]

        print(f'{user_name:<10}ㅣ{stock_name:<12}ㅣ{quantity:<6}ㅣ{now_price:<10}ㅣ{purchase_price:<10}ㅣ{rate:.2f}%')

def analyze_data():
    if not is_data_entered or len(portfolio) == 0:
        print('\n[안내] 데이터가 없습니다. 먼저 데이터를 입력해주세요.')
        return
    print('\n---[3. 포트폴리오 통합 분석]---')

    max_row = portfolio[0]
    min_row = portfolio[0]
    total_quantity = 0

    for i in range(len(portfolio)):
        current_quantity = portfolio[i][2]
        total_quantity += current_quantity

        if current_quantity > max_row[2]:
            max_row = portfolio[i]
        if current_quantity < min_row[2]:
            min_row = portfolio[i]
    
    print(f'>최고 수량 보유자:{max_row[0]}님 ({max_row[1]}/{max_row[2]}개)')
    print(f'>최저 수량 보유자:{min_row[0]}님 ({min_row[1]}/{min_row[2]}개)')
    print(f'>전체 투자자 총 주식 수:{total_quantity}개\n')

    for i in range(len(portfolio)):
        user_name =portfolio[i][0]
        stock_name =portfolio[i][1]
        rate = portfolio[i][5]

        if rate>100:
            print(f'>{user_name}님의 {stock_name}:수익률이 엄청나시군요!')
        elif rate < 0:
            print(f'>{user_name}님의 {stock_name}:수익률이 마이너스 입니다. 부분 매도를 추천합니다ㅠㅠ')
        else:
            print(f'>{user_name}님의 {stock_name}:수익률이 플러스 입니다! 일부 수익실현을 추천합니다!')

def save_data():
    if not is_data_entered or len(portfolio)==0:
        print('\n저장할 데이터가 없습니다.')
        return
    try:
        with open('stock_data.txt','w',encoding ='utf-8') as f:
            for i in range(len(portfolio)):
                f.write(f'{portfolio[i][0]},{portfolio[i][1]},{portfolio[i][2]},{portfolio[i][3]},{portfolio[i][4]},{portfolio[i][5]}')
        print('\n[성공] 데이터가 stock_data.txt 파일에 저장되었습니다.')
    except Exception as e:
        print(f'\n[오류] 파일 저장 중 문제 발생:{e}')

def load_data():
    global is_data_entered, portfolio
    try:
        with open('stock_data.txt','r',encoding ='utf-8') as f:
            portfolio = []
            for line in f:
                data = line.strip().split(',')
                if len(data) ==6:
                    portfolio.append([data[0],data[1],int(data[2]),float(data[3]),float(data[4]),float(data[5])])
            is_data_entered = True
            print('\n[성공] 파일에서 데이터를 정상적으로 불러왔습니다')
    except FileNotFoundError:
        print('\n[오류] 저장된 파일(stock_data.txt)이 없습니다. 먼저 데이터를 저장해주세요.')

print('환영합니다! 주식관리 프로그램을 시작합니다')


while True:
    print('='*30)
    print(f'주식 수익관리 시스템 ver.4')
    print('1. 투자자 정보 및 주식 입력')
    print('2. 전체 투자자 데이터 조회 (표 포맷)')
    print('3. 포트폴리오 분석')
    print('4. 파일 저장')
    print('5. 파일 불러오기')
    print('6. 프로그램 종료')
    print('='*30)

    choice = input('원하시는 메뉴 번호를 입력하세요: ')

    if choice == '1':
        input_data()
    elif choice == '2':
        view_data()
    elif choice == '3':
        analyze_data()
    elif choice == '4':
        save_data()
    elif choice == '5':
        load_data()
    elif choice =='6':
        print('\n프로그램을 종료합니다. 성투하세요!')
        break
    else:
        print('\n[오류] 잘못된 입력 입니다. 1~6 사이의 숫자를 입력해주세요')
