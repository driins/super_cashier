# Final Project Python - Super Cashier

## Latar Belakang Problem
Super cashier merupakan program yang dibuat dengan menggunakan bahasa pemrograman python untuk memenuhi Final Project Python Sekolah Data Pacmann. 
Program super cashier ini memungkinkan customer untuk melakukan pembelanjaan secara self service melalui sebuah sistem kasir supermarket sehingga customer dapat melakukan input item yang ingin dibeli, banyaknya item yang ingin dibeli, serta menghitung total harga yang harus dibayarkan serta customer dapat melakukan pembelian secara jarak jauh.

## Requirements / Objectives
1. Customer membuat ID transaksi dengan menggunakan fitur objek dari class: <br>
  `trnsct_123 = Transaction()`
2. Customer menginput nama item, jumlah item, dan harga barang dengan method <br>
`add_item([<nama item>, <jumlah item>, <harga per item>])`
3. Jika terjadi kesalahan penginputan, customer dapat melakukan update dengan menggunakan method berikut:<br>
  a. `update_item_name(<nama item>, <update nama item>)` untuk melakukan update nama item <br>
  b. `update_item_qty(<nama item>, <update jumlah item>)` untuk melakukan update jumlah item <br>
  c. `update_item_price(<nama item>, <update harga item>)` untuk melakukan update harga item
4. Jika customer melakukan pembatalan, customer dapat: <br>
  a. Menghapus salah satu dari nama item sehingga jumlah item dan harga item ikut terhapus dengan menggunakan <br> `delete_item(<nama item>)` <br>
  b. Menghapus seluruh transaksi atau melakukan reset transaksi dengan `reset_transaction()`
5. `check_order()` untuk melakukan pengecekan input data pembelanjaan sudah benar atau belum. <br>
  a. Output **"Pemesanan sudah benar"** akan muncul jika tidak terjadi kesalahan input. <br>
  b. Output **"Terjadi kesalahan input data"** akan muncul jika terjadi kesalahan input. <br>
  c. `show_order()` untuk menampilkan daftar pesanan customer
6. Perhitungan total belanja menggunakan method `total_price()` dengan ketentuan sebagai berikut: <br>
  a. Diskon 10% untuk total pembelanjaan diatas Rp 500.000
  b. Diskon 8% untuk total pembelanjaan diatas Rp 300.000
  c. Diskon 5% untuk total pembelanjaan diatas Rp 200.000

## Flowchart

## Penjelasan atau Snippet Code
  1. Class Transaction sebagai parent class beserta inisialisasi attribute dengan __init__() <br>
    ![image](https://user-images.githubusercontent.com/87298693/232326495-e580a7f4-34be-46b6-8d00-65ecd91cc7bc.png)
  2. Method add_item() <br>
    ![image](https://user-images.githubusercontent.com/87298693/232326650-42f9a3f2-c3fc-4a31-9047-05863d9fa341.png)
  3. Method update item: <br>
    a. update_item_name() <br>
    ![image](https://user-images.githubusercontent.com/87298693/232326724-8378199b-2307-41b6-a65b-228687e50661.png)
    <br>
    b. update_item_qty() <br>
    ![image](https://user-images.githubusercontent.com/87298693/232326792-74c417a3-c4a1-48e7-95cf-5d59790a796c.png)    <br>
    c. update_item_price() <br>
    ![image](https://user-images.githubusercontent.com/87298693/232326812-b913854f-2eff-455e-8dc3-1f8befe84c51.png)    <br>
  4. Method show_orders() <br>
    ![image](https://user-images.githubusercontent.com/87298693/232326856-0d96cd58-79ac-48b0-a663-d1b191073982.png) <br>
  5. Method delete_item() <br>
    ![image](https://user-images.githubusercontent.com/87298693/232326919-7f001011-8918-4735-adf4-3d2a201a7635.png)
    <br>
  5. Method reset_transaction() <br>
    ![image](https://user-images.githubusercontent.com/87298693/232326967-3663309d-975f-4691-824f-7126ed1c02ca.png)
  6. Method check_orders() <br>
    ![image](https://user-images.githubusercontent.com/87298693/232327021-c932bb04-7425-488f-a6c3-838f316b80a8.png)
    <br>
  7. Method total_price() yang terhubung juga dengan method get_discount()<br>
    ![image](https://user-images.githubusercontent.com/87298693/232327097-fef08cec-4ea7-48f0-a3aa-770e6edb7b11.png)
    <br>
    ![image](https://user-images.githubusercontent.com/87298693/232327126-ecc90e36-d6df-4637-9061-2edd1f0ca8a6.png)
  
## Demonstrasi Code dengan TEST CASE
  **TEST CASE 1** <br>
  ![image](https://user-images.githubusercontent.com/87298693/232312529-cfc12287-5273-49e3-a14a-1d38660a1b2a.png)
  <br>Hasil test case add_item(): <br>
  ![image](https://user-images.githubusercontent.com/87298693/232325931-9d1447d5-6cc1-4564-96d6-1998866d180a.png)
  <br> Menampilkan tabel pesanan dengan show_orders(): <br>
  ![image](https://user-images.githubusercontent.com/87298693/232325977-6d6d45b1-da9a-457b-ae81-16a8f4a7dc54.png)

  **TEST CASE 2** <br>
  <br>Hasil test case update_item(): <br>
  ![image](https://user-images.githubusercontent.com/87298693/232326016-630375c7-1892-41df-b8af-d9aad7877498.png)
  <br>
  ![image](https://user-images.githubusercontent.com/87298693/232326062-2c2ad0ee-55cc-4d1a-ac11-6279cffc9ed6.png)

  **TEST CASE 3** <br>
  ![image](https://user-images.githubusercontent.com/87298693/232312548-95a2512b-fb18-4f98-aa74-877916c8613b.png)
  <br>
  ![image](https://user-images.githubusercontent.com/87298693/232312626-a78c18bf-e726-4f63-bd8a-17b693a67f29.png)
  <br>Hasil test case delete_item(): <br>
  ![image](https://user-images.githubusercontent.com/87298693/232326232-0ab4496c-03c7-4c31-be8a-66b5d0898f27.png)
  <br>Hasil test case reset_transaction(): <br>
  ![image](https://user-images.githubusercontent.com/87298693/232326245-b48c229f-41a9-40e9-b9fe-01aa14086c70.png)

  **TEST CASE 4** <br>
  ![image](https://user-images.githubusercontent.com/87298693/232326298-88d4d7c2-2d09-4f5c-a563-aed77c7a64c2.png)
  <br>
  ![image](https://user-images.githubusercontent.com/87298693/232326317-3d5b64c3-c563-4f26-9fdd-b9a1148ada0c.png)
  <br>Hasil test case check_orders(): <br>
  ![image](https://user-images.githubusercontent.com/87298693/232326337-447d93ec-e998-465c-b87c-35348037405e.png)

  **TEST CASE 5** <br>
  ![image](https://user-images.githubusercontent.com/87298693/232312660-ab75e1ee-8002-4a8a-8990-31f0c304c652.png)
  <br>Hasil test case total_price(): <br>
  ![image](https://user-images.githubusercontent.com/87298693/232326363-899194b5-0362-4e20-9dd2-0b4b6b6f4a4a.png)

## Kesimpulan
  Program berjalan sesuai harapan. Namun, sistem kasir tersebut masih belum menggunakan database untuk record transaksinya dan belum terdapat fitur untuk menghindari duplikasi item yang diinputkan.

## Saran Pengembangan
  - Membuat tampilan pemilihan menu
  - Melakukan koneksi program yang dibuat dengan database agar record tersimpan dengan baik dan terhindar dari duplikasi item yang sama.
