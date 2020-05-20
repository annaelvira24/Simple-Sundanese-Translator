# Simple Sundanese Translator
Simple Sundanese to Bahasa Indonesia translator using Pattern Matching

## Latar Belakang
Pada suatu hari, ada mahasiswa bernama Riyugan yang baru pindah ke Bandung. Pada awalnya dia mengalami kesulitan untuk bersosialisai dengan lingkungan sekitar karena orang-orang di lingkungannya yang baru hanya berbicara dalam bahasa Sunda. Beruntungnya Riyugan punya teman dari kampung halamannya, yaitu Anda, untuk diminta membuat penerjemah sederhana dari Bahasa Sunda ke Bahasa Indonesia begitu pula sebaliknya untuk memudahkan dirinya bersosialisasi dengan lingkungan barunya di Bandung.

## Getting Started
### Prerequisites
python 3
```
Windows : download python dari https://www.python.org/downloads/windows/ dan lakukan isntalasi
Linux : sudo apt-get install python3
```

Flask 1.1.2
```
Windows: pip install -U flask
Linux : sudo apt install python3-flask
```

### Instalasi
1. Buka cmd atau terminal di directory folder scr
2. Jalankan perintah berikut di cmd atau terminal
```
Windows : py web.py
Linux : python3 web.py
```
3. Akan muncul tulisan berikut di cmd atau terminal
```
 * Serving Flask app "web" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 301-019-789
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 ```
4. Copy alamat url http://127.0.0.1:5000/ yang muncul 
5. Buka browser (disarankan mozila firefox atau chrome)
6. Paste url

## Contoh Kasus Uji
```
Sunda - Indonesia
Sunda : nami abdi Riyugan
Indonesia : nama saya Riyugan
```

```
Sunda - Indonesia
Sunda : abdi teh sanes jalma Bandung
Indonesia : saya bukan orang Bandung
```

```
Sunda - Indonesia
Sunda : anjeun sumping ti mana?
Indonesia : kamu tiba dari mana?
```

```
Indonesia - Sunda
Indonesia : nama saya Riyugan
Sunda : nami abdi Riyugan
```

```
Indonesia - Sunda
Indonesia : nama adik kamu siapa?
Sunda : nami rai anjeun teh saha?
```

```
Indonesia - Sunda
Indonesia : saya tidak bisa bahasa Sunda
Sunda : abdi henteu tiasa bahasa Sunda
```

## Sample Screen
<img src="sample1.jpg"/>

## Video demo
Video demo aplikasi daat dilihat pada link berikut
https://youtu.be/SkvzpmMLujk 


## Built With
* [Python](https://docs.python.org/3/)
* [Flask](https://pypi.org/project/Flask/)

## Author
Anna Elvira Hartoyo - 13518045
