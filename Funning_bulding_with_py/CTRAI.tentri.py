import time
questions=["1. Bạn tên là gì vậy thằng ngu?","2. Bạn bao nhiêu tuổi ?","3. Trong đầu bạn có gì?","4. Bạn yêu ai ?","5. Bạn có?"]
answer= [["A. Minh Quân  ","B. Gia H","C. Huy Cường","D. 🐰"],
         ["A. 17 ","B. 18","C. Tuổi heo","D. TUỔI LỒN"],
         ["A. Não ","B. Gia H","C. Tiền","D. CỨC TÔM"],
         ["A. Ba mẹ ","B. Bản thân","C. Gia H","D. 🐰🐰🐰🐰"],
         ["A. Tiền ","B. CL","C. CON CAK","D. Có cái mõm"]]
cras = ["A","D","D","D","B"]
guesses=[]
num=0
point=0
for question in questions:
    print (questions[num], "\n")
    for ans in answer[num]:
        print (ans,"\n")
    for i in reversed(range(1,6)):
        print (f"Bạn còn {i}s để trả lời câu")
        time.sleep (1)
    guesses.append(str(input("NHẬP ĐÁN ÁN VÀO ĐI TK CHÓ: ")))
    if guesses[num] == cras[num]:
        print ("XIN CHÚC MỪNG TADA TA ĐÀ","\n")
        point+=1
    else:
        print (f"Dap an dung la {cras[num]}")
    num +=1
print ("---"*30)
print (f"{"dap an dung la":<10} {cras}")
print (f"{"dap an cua ban la":<10} {guesses}")
print (f"Tong diem cua ban la {point}/5 CON GÀAAAA=)))" )