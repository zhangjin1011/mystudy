__author__ = "zhang jin"

'''
程序练习：
要求：
1. 打印省、市、县三级菜单
2. 可返回上一级
3. 可随时退出程序

'''
list1 = {
'江西省':{
    "抚州市":{
        "崇仁县":["我爱我家","链家"],
        "宜黄县":["宜家","拍拍贷"]
    },
    "南昌市":{
        "南昌县": ["人民广场", "八一广场"],
        "南开县": ["川菜", "粤菜"]
    }
}
,

'河北省':{
     "石家庄市":{
          "无极县":["你我贷","壹基金"],
          "新乐县":["zhangjin","zhangyin"],
     },
      "郑州市":{
          "郑州县":[1,2],
          "张江县":[3,4],
}
}
}

exit_flat = False
while not exit_flat:
    for i1 in list1:
        print(i1)
    choice = input("输入1》》：")
    if choice in  list1:
        while not exit_flat:
            for i2 in list1[choice]:
                print('\t',i2)
            choice2 = input("输入2》》：")
            if choice2 in list1[choice]:
                while not exit_flat:

                    for i3 in list1[choice][choice2]:
                        print('\t\t',i3)
                    choice3 = input("输入3》》：")
                    if choice3 in list1[choice][choice2]:
                        for i4 in list1[choice][choice2][choice3]:
                            print('\t\t\t',i4)
                        choice4 = input("最后一层，返回输入b:")
                        if choice4 == "b":
                            pass
                        elif choice4 == "q":
                            exit_flat = True
                    if choice3 == "b":
                        break
                    elif choice3 == "q":
                        exit_flat = True
            if choice2 == "b":
                break
            elif choice2 == "q":
                exit_flat = True













