from traceback import print_tb


def myFunc():
    print('함수를 호출함.')
    
gVar = 100
   
if __name__ == '__main__':
    print('메인 함수 부분이 실행합니다.')
    myFunc()
    print('전역 변수 값: ', gVar);
    

a = 100; b= 100.123

print(str(a) + '1');
print(str(b) + '1')