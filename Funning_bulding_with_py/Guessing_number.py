from random import randrange
while True:
    x=int(input("Mời nhập số bắt đầu để bạn đoán: "))
    y=int(input("Mời nhập số kết thúc để bạn đoán: "))
    a=randrange(x,y)

    print ("*"*40)
    print (f"Bắt đầu game, số của bạn bắt đầu từ {x}đến {y}")
    print ("*"*40)
    print ("Bạn có 5 lượt để chơi")
    i=5
    while i>0:
        guess=int(input("Nhập số mà bạn đoán vào: "))
        if guess >y or guess<x:
            print ("Ngoài vùng tìm kiếm")
        elif guess == a:
            print (f"Chúc mừng bạn đã đúng đáp án là {a}")
            break
        elif guess < a:
            print (" Số này bé hơn đáp án")
            i-=1
            print(f"Bạn chỉ còn {i} lượt ")
        elif guess > a:
            print (" Số này lớn hơn đáp án")
            i-=1
            print(f"Bạn chỉ còn {i} lượt ")
            
    if guess !=a:
        print ("Bạn đã hết lượt chơi ")
    else:
        pass
    ans=str(input("Bạn có muốn chơi tiếp không (nhập q/Q để out)"))
    if ans.lower() == "q":
        print (" CON GÀ MINH QUAN")
        break


    