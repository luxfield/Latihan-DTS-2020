# nama file p1.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
priority = 2

#netacad email cth: 'abcd@gmail.com'
email='suryaefendi72@gmail.com'
 
# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini

#static typing, referensi PEP 484 https://www.python.org/dev/peps/pep-0484/
#f-string, referensi PEP 498 https://www.python.org/dev/peps/pep-0498/
#underscore in numeric literal, referensi PEP 515 https://www.python.org/dev/peps/pep-0515/

#Graded

def letter_catalog(items: list,letter: str='A')->list:
  # MULAI KODEMU DI SINI
  return [x for x in items if x[0] == letter]

#Graded

def counter_item(items: list)->dict:
  # MULAI KODEMU DI SINI
  return {i:items.count(i) for i in sorted(items)}

#Graded

# dua variable berikut jangan diubah
fruits = ['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries','Date Fruit','Grapes','Guava','Jackfruit','Kiwifruit']
prices = [6,5,3,10,12,7,14,15,8,7,9]

# list buah
chart = ['Blueberries','Blueberries','Grapes','Apple','Apple','Apple','Blueberries','Guava','Jackfruit','Blueberries','Jackfruit']

# MULAI KODEMU DI SINI
fruit_price: dict = dict(zip(fruits,prices))

def total_price(dcounter: list,fprice: list)->int:
  # MULAI KODEMU DI SINI
  return sum([{k: v for k,v in sorted(dcounter.items())}.get(k) * {k:v for k,v in fprice.items() if k in dcounter}.get(k) for k in set({k:v for k,v in fprice.items() if k in dcounter}) & set({k:v for k,v in sorted(dcounter.items())})])

#Graded

def discounted_price(total: int,discount: float,minprice: int=100)->str:
  # MULAI KODEMU DI SINI
  return total if total < minprice else total - total * (discount / 1_00)

#Graded

def print_summary(items: list,fprice: dict)->str:
  # MULAI KODEMU DI SINI
  for key,values in {key: [value , {k: {k:v for k,v in sorted(counter_item(items).items())}.get(k) * {k:v for k,v in fprice.items()}.get(k) for k in set({k:v for k,v in fprice.items()}) & set({k:v for k,v in sorted(counter_item(items).items())})}[key]] for key, value in counter_item(items).items()}.items():
        jumlah, harga = values
        print(f'{jumlah} {key} : {harga}')
  print(f'total : {total_price(counter_item(items),fruit_price)}')
  print(f'discount price : {discounted_price(total_price(counter_item(items),fruit_price),10,minprice=100)}')
  
