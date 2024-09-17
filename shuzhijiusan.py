import math

choice = input('请选择算法 二分法 迭代法 Newton法 割线法')
if choice == '二分法':
    #初始参数输入
    print('二分法开始计算')
    a = float(input('请输入零点所在区间的左端点：'))
    b = float(input('请输入零点所在区间的右端点：'))
    err = float(input('请输入容许误差：'))
    expression = input('请输入函数表达式（变量以x表示）：')
    # 计算迭代次数
    n1 = math.log(b-a)-math.log(err)
    n2 = math.log(2)
    n3 = n1/n2
    n =int(n3)+1
    print('预计迭代次数为：',n)
    #开始迭代
    k=0
    while k < n:
        x = (a + b) / 2
        if eval(expression) == 0:
            print('实际迭代次数为',k,"根为",x)
            break
        x = float((a + b) / 2)
        x = a
        k = k + 1
        fa = float(eval(expression))
        x = (a + b) / 2
        fx = float(eval(expression))
        if fa*fx<0:
           b = x
           fb = fx
        else:
           a = x
           fa = fx
        print("已循环次数:",k,"当前x值:",x,"当前a值",a,"当前b值",b)
elif choice == '迭代法':
    print('迭代法开始计算')
    # 初始参数输入
    x0 = float(input('请输入初值x0（最好先用二分法筛选一下 别上来就给我乱填嗷！！！）：'))
    err = float(input('请输入容许误差：'))
    l=float(input('L值：'))
    expression = input('请输入函数表达式（变量以x表示）：')
    # 计算最大迭代次数
    x = x0
    x1 = eval(expression)
    n1 = abs(x0-x1)
    n2 = 1-l
    n3 = math.log(n1/n2)
    n4 = math.log(err)-n3
    n5 = n4/math.log(l)
    n = int(n5)+1
    print('预计最大迭代次数为：',n)
    #开始迭代
    errt = (1-l)*err
    print("真实容许误差为",errt)
    k=0
    while k < n:
        x2 = x
        x = float(eval(expression))
        if abs(x - x2) < errt:
            print('实际迭代次数为', k+1, "数值解为", x, "误差为", abs(x - x2))
            break
        k = k + 1
        print("已循环次数:",k,"当前x值:",x)

elif choice == 'Newton法':
    print('Newton法开始计算')
    # 初始参数输入
    x0 = float(input('请输入初值x0（最好先用二分法筛选一下 别上来就给我乱填嗷！！！）：'))
    err = float(input('请输入容许误差：'))
    n = int(input('请输入最大迭代次数（输入0则表示不限制迭代次数）：'))
    expression1 = input('请输入函数表达式（变量以x表示）：')
    expression2 = input('请输入导函数表达式（变量以z表示）：')
    z = x0
    if eval(expression2) == 0:
        print('导函数为0，无法求解')
        exit()
    # 开始迭代
    k=0
    if n == 0:
        x = x0
        z = x0
        while True:
            x1 = float(eval(expression1))
            x2 = float(eval(expression2))
            x3=x1/x2
            x4= x
            x = x-x3
            z = x
            if abs(x-x4)<err:
                print('实际迭代次数为',k+1,"数值解为",x,"误差为",abs(x-x4))
                break
            k=k+1
            print("已循环次数:",k,"当前x值:",x)

    else:
        x = x0
        z = x0
        while k < n:
            x1 = float(eval(expression1))
            x2 = float(eval(expression2))
            x3 = x1 / x2
            x4 = x
            x = x - x3
            z = x
            if abs(x - x4) < err:
                print('实际迭代次数为', k+1, "数值解为", x, "误差为", abs(x - x4))
                break
            k = k + 1
            print("已循环次数:", k, "当前x值:", x)
        if abs(x - x4) > err:
           print('以达到最大迭代次数，仍未收敛')
elif choice == '割线法':
    print('割线法开始计算')
    # 初始参数输入
    choice1 = input('请选择单点割线法或两点割线法')
    if choice1 == '单点割线法':
            print('单点割线法开始计算')
            x0 = float(input('请输入初值x0：'))
            x1 = float(input("请输入初值x1："))
            err = float(input('请输入容许误差：'))
            expression = input('请输入函数表达式（变量以x表示）：')
            n = int(input('请输入最大迭代次数（输入0则表示不限制迭代次数）：'))
            # 开始迭代
            k = 0
            if n == 0:
                x = x0
                fx0 = float(eval(expression))
                x =x1
                while True:
                    k = k + 1
                    x2 = x
                    fxk = float(eval(expression))
                    x8 = fxk/(fxk - fx0 )
                    x9 = x - x0
                    x = x - x8 * x9
                    if abs(x - x2) < err:
                        print('实际迭代次数为', k, "数值解为", x, "误差为", abs(x - x2))
                        break
                print("已循环次数:", k, "当前x值:", x)
            else:
                x = x0
                fx0 = float(eval(expression))
                x = x1
                while k < n:
                    k = k + 1
                    x2 = x
                    fxk = float(eval(expression))
                    x8 = fxk/(fxk - fx0 )
                    x9 = x - x0
                    x = x - x8 * x9
                    if abs(x - x2) < err:
                        print('实际迭代次数为', k, "数值解为", x, "误差为", abs(x - x2))
                        break
                    print("已循环次数:", k, "当前x值:", x)
                if abs(x - x2) > err:
                    print('以达到最大迭代次数，仍未收敛')
    elif choice1 == '两点割线法':
            print('两点割线法开始计算')
            x0 = float(input('请输入初值x0：'))
            x1 = float(input("请输入初值x1："))
            err = float(input('请输入容许误差：'))
            expression = input('请输入函数表达式（变量以x表示）：')
            n = int(input('请输入最大迭代次数（输入0则表示不限制迭代次数）：'))
            if n == 0:
                xk1 = x0
                xk = x1
                k = 0
                while True:
                    k = k + 1
                    x = xk1
                    yk1 = float(eval(expression))
                    x = xk
                    yk = float(eval(expression))
                    sub1 = xk - xk1
                    sub2 = yk - yk1
                    sum1 = sub1 / sub2
                    sum2 = sum1 * yk
                    xk1 = xk
                    xk = xk - sum2
                    if abs(xk - xk1) < err:
                        print('实际迭代次数为', k, "数值解为", xk, "误差为", abs(xk - xk1))
                        break
                    print("已循环次数:", k, "当前x值:", xk)
            else:
                xk1 = x0
                xk = x1
                k = 0
                while k < n:
                        k = k + 1
                        x = xk1
                        yk1 = float(eval(expression))
                        x = xk
                        yk = float(eval(expression))
                        sub1 = xk - xk1
                        sub2 = yk - yk1
                        sum1 = sub1 /sub2
                        sum2 = sum1 * yk
                        xk1 = xk
                        xk = xk - sum2
                        if abs(xk - xk1) < err:
                            print('实际迭代次数为', k, "数值解为", xk, "误差为", abs(xk - xk1))
                            break
                        print("已循环次数:", k, "当前x值:", xk)
                if abs(xk - xk1) > err:
                    print('以达到最大迭代次数，仍未收敛')
else:print('操你妈 什么都不选？！！那你让老子算什么？！！')

