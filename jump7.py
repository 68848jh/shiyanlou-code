# 使用while循环编写逢7过
a = 0
while a < 100:
    a = a + 1
        if a % 7 == 0:
                continue
                    elif a % 10 == 7:
                            continue
                                elif a // 10 == 7:
                                        continue
                                            print(a)


                                            #使用for循环打印逢7过


                                                for i in range(1, 101):
                                                    if i % 7 == 0:
                                                            continue
                                                                elif i % 10 == 7:
                                                                        continue
                                                                            elif i // 10 == 7:
                                                                                    continue
                                                                                        print(i)
