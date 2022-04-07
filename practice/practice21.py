def openAccount():
    print('새로운 계좌가 생성되었습니다.')

def deposit(balance, money): #입금
    print('입금이 완료되었습니다. 잔액은 {}원입니다.'.format(balance+money))
    return balance+money

def withdraw(balance, money): #출금
    if balance>=money: #잔액이 출금액보다 많으면
        print('출금이 완료되었습니다. 잔액은 {}원입니다.'.format(balance-money))
        return balance-money
    else:
        print('출금이 불가합니다. 잔액은 {}원입니다.'.format(balance))
        return balance

def withdrawNight(balance, money): #저녁에 출금
    commission=100 #수수료
    return commission, balance-money-commission

balance=0 #잔액
balance=deposit(balance, 1000)
# balance=withdraw(balance, 2000)
# balance=withdraw(balance, 500)
commission, balance=withdrawNight(balance, 500)
print('수수료는 {0}원이며, 잔액은 {1}원입니다.'.format(commission, balance))