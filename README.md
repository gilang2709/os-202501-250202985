# Perbedaan Monolitik Kernel, Micro cernel, dan Layered Architekture

## 1 Monolithic KERNEL
Monolithic kernel adalah sistem arsitektur sistem operasi di mana seluruh komponen utamanya berupa pengelolaan proses, memori, sistem file, maupun driver perangkat digabungkan dalam bentuk satu entitas monolitik sehingga berjalan pada tingkat kernel dengan akses langsung.

### Kelebihan
Desain ini unggul dalam kecepatan eksekusi karena semua komponen saling berinteraksi langsung tanpa hambatan tambahan, membuat OS sangat responsif untuk aplikasi berat seperti server web atau game. Selain itu, penggunaan sumber daya seperti memori dan prosesor jadi lebih hemat, serta pengembangannya relatif sederhana karena kode terintegrasi rapat, memudahkan penambahan fitur baru dan dukungan hardware luas tanpa komplikasi berlebih.

### Kekurangan
Di sisi lain, keamanannya lemah karena kesalahan kecil di satu modul bisa meruntuhkan seluruh sistem, tanpa mekanisme isolasi yang kuat. Pemeliharaan juga menantang akibat ukuran kode yang besar dan ketergantungan antar-bagian, sehingga debugging memakan waktu dan perubahan berpotensi berisiko tinggi. Apalagi, kerentanan terhadap serangan lebih besar karena akses penuh ke hardware, membuatnya kurang ideal untuk lingkungan yang butuh modularitas tinggi atau kestabilan mutlak.