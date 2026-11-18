menu={"pizza":5000,"banhmi":10000, "banh bao": 15000}
reciept={}
monan="monan"
for key, value in menu.items():
    if isinstance(value, str):
     print (f"{key:15} {value:}")
     print ("*"*40)
    else:
       print (f"{key:15} {value:,} vnd")
while True:
      monan=str(input("Nhap mon an cua ban: "))
      if monan.lower() in menu:
         soluong=int(input("Nhap so luong mon banj mun oder: "))
         soluong=reciept.update({monan: soluong})
      elif monan.lower () == "q":
         print ("Cam on quy khach")
         break
      else:  
         print("Vui long nhap lai vi khong co mon do")
print ("*"*40)
print ("HOA DON CUA QUY KHACH LA:") 
print ("*"*40)
tong=0
for doan, soluong in reciept.items():
   if doan in menu:
      gia = menu[doan]
      tong +=gia
      print (f"{doan:10} {soluong:10} {gia} ")
print ({f"Vậy tổng tiền của bạn phải trả là {tong} DITMEE TK BA TAUUU, m là 3 tàu"})
    

