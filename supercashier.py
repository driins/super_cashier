
from tabulate import tabulate

# class Transaction sebagai parent class
class Transaction:
  def __init__ (self):
      """ Fungsi inisialisasi untuk class Transaction sebagai parent class.
      orders bertipe data dictionary, berguna untuk menyimpan data pemesanan customer
      """
      self.orders = dict()
  
  # Method untuk input nama item, jumlah item, dan harga item (add_item)
  def add_item (self, item_name, item_qty, item_price):
      """ Method untuk menginputkan item yang akan dipesan
      terdiri dari input nama item (sebagai key), jumlah item, dan harga item.
      Inputan jumlah item dan harga item harus bertipe data integer agar dapat dikalkulasikan
      """
      if type(item_qty)!=int:
        print("Jumlah item harus berupa angka")
      elif type(item_price)!=int:
        print("Harga item harus berupa angka")
      else:
        self.orders.update({item_name: [item_qty, item_price]})
        print(f"Anda berhasil menambahkan item {item_name}, {item_qty} pcs dengan harga per item {item_price}")
  
  # Method untuk update pesanan 
  def update_item_name(self, item_name, new_item_name):
    """ 
    Method untuk memperbaiki kesalahan input nama item
    """
    temp = self.orders[item_name]
    self.orders.pop(item_name)
    self.orders.update({new_item_name:temp})
    self.show_orders()
    print(f"Anda telah mengubah item {item_name} menjadi {new_item_name}")

  def update_item_qty(self, item_name, new_item_qty):
    """ 
    Method untuk memperbaiki kesalahan input jumlah item
    """
    if type(new_item_qty)!=int:
      print("Masukkan jumlah item harus dalam bentuk angka")
    else:
      self.orders[item_name][0] = new_item_qty

    self.show_orders()
    print(f"Anda telah mengubah item {item_name} menjadi {new_item_qty} pcs")
    
  def update_item_price(self, item_name, new_item_price):
    """ 
    Method untuk memperbaiki kesalahan input harga item
    """
    if type(new_item_price)!=int:
      print("Masukkan harga item harus dalam bentuk angka")
    else:
      self.orders[item_name][1] = new_item_price

    self.show_orders()
    print(f"Anda telah mengubah item {item_name} menjadi Rp {new_item_price},-")
      
  # Menampilkan data pesanan customer yang telah masuk dalam bentuk tabel
  def show_orders(self):
    """ 
    Method untuk menmpilkan data pesanan dalam bentuk tabel
    terdiri dari Nama Item, Jumlah Item, Harga per Item, dan Total Harga
    """ 
    show_orders = []
    orders_head = ["No.", "Nama Item", "Jumlah Item", "Harga/Item", "Total Harga"]
    show_orders.append(orders_head)

    n = 0  
    for key, value in self.orders.items():
      n += 1
      table_no = n
      item_name = key
      item_qty = value[0]
      item_price = value[1]
      total = item_qty * item_price
      item_data = [table_no, item_name, item_qty, item_price, total]
      show_orders.append(item_data)
      
    print(tabulate(show_orders, tablefmt="fancy_grid"))  
  
  # Method untuk menghapus item yang batal dibeli customer
  def delete_item(self, item_name):
    """
    Method untuk menghapus salah satu item yang batal dibeli customer. 
    Penghapusan dilakukan menggunakan parameter nama item
    untuk kemudian jumlah dan harga item tersebut akan ikut terhapus
    """
    try:
      self.orders.pop(item_name)
      print(f"Anda berhasil menghapus pesanan {item_name}")
      print("")
    except KeyError:
     print(f"Nama barang {item_name} ada pada daftar pemesanan")  

  # Method untuk menghapus semua transaksi
  def reset_transaction(self):
    """
    Method untuk menghapus seluruh item yang dipesan
    termasuk setiap detail jumlah dan harga itemny ikut terhapus.
    """
    transaction = {}
    self.orders = transaction
    print ("Semua item berhasil dihapus. Sekarang, Anda tidak memiliki daftar pesanan")
  
  # Method untuk cek input pesanan
  def check_order(self):
    """
    Method untuk cek detail pesanan sudah sesuai.
    Akan menmpilkan output pesanan sudah benar jika tidak terdapat kesalahan input
    begitupun sebaliknya
    """
    for key, value in self.orders.items():
        item_name = key
        item_qty = value[0]
        item_price = value[1]
            
    if type(item_name) == str and type(item_qty) == int and type(item_price) == int:
      print("Pemesanan sudah benar")
    else: 
      print("Terdapat kesalahan input pesanan")
  
  # Method untuk menghitung total harga belanja
  def total_price(self):
    self.total_price = 0
    for value in self.orders.values():
      item_qty = value[0]
      item_price = value[1]
      self.total_price += (item_qty * item_price)
    get_discount, discount = self.get_discount(self.total_price)
    self.final_price = self.total_price * (1 - discount)

    if get_discount == True:
      print(f"Selamat! Anda mendapat diskon {discount * 100:.0f}%")
      print(f"Total belanja Anda menjadi Rp.{self.final_price:.2f}")
    else:
      print(f"Total yang harus Anda bayar adalah Rp.{self.total_price}")
  
  def get_discount(self, total_price):
    self.total_price = total_price
    if self.total_price <= 200000:
      get_discount = False
      discount = 0.0
    else:
      get_discount = True
      if self.total_price > 500000:
        discount = 0.1
      elif total_price > 300000:
        discount = 0.08
      elif total_price > 200000:
        discount = 0.05
      
    return get_discount, discount
  