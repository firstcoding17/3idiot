import numpy as np
import matplotlib.pyplot as plt
#코사인 대입 및 식 계산
def f_cos(x,a,b,h,k):
    return a * np.sin(b*(x-h))+k
#사인 대입 및 식 계산
def f_sin(x,a,b,h,k):
    return a * np.sin(b*(x-h))+k


def main():
    #변환할 삼각함수 입력 받기
    print("choose trigonometric functions")
    choice = str(input())

    # f(x) = a 삼각함수(b(x-h)) + k
    a = int(input())#a입력
    b = int(input())#b입력
    h = int(input())#h입력
    k = int(input())#k입력



    # 0부터 4파이까지 그래프 그리기
    x = np.linspace(0,4*np.pi,200)

    #선택
    if choice == 'cos':
        y = f_cos(x,a,b,h,k)
        plt.plot(x,y)
        plt.show()
    elif choice == 'sin':
        y = f_sin(x,a,b,h,k)
        plt.show(x,y)






if __name__ == "__main__":
    # execute only if run as a script
    main()