from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        num1 = float(request.form.get('num1', 0))
        num2 = float(request.form.get('num2', 0))
        operation = request.form.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Undefined'

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

"""
🔹 from flask import Flask, request, render_template
Bu satirla Flask kutuphanesini projeye dahil ediyorsun.
Yani: "Web sitesi yapmak icin gerekli araclari getir."

🔹 app = Flask(__name__)
Bu satirla bir Flask uygulamasi baslatiyorsun.
Yani: "Benim web sitem burada basliyor."

🔹 @app.route('/', methods=['GET', 'POST'])
Bu satir, anasayfa acildiginda ne yapilacagini soyluyor.
GET: Sayfa ilk acildiginda calisir.
POST: Form gonderilince calisir.

🔹 def index():
Bu, yukaridaki yol (route) calistiginda ne yapilacagini belirleyen kisim.
Yani: "Kullanici sayfaya gelince ne yapayim?"

🔹 result = None
Baslangicta sonuc yok, o yuzden bos birakiliyor.
Yani: "Henuz islem yapilmadi."

🔹 if request.method == 'POST':
Eger kullanici butona tiklayip formu gonderirse bu kisim calisir.
Yani: "Kullanici bir sey hesaplamak istedi mi?"

🔹 num1, num2, operation

num1: Kullanicinin yazdigi ilk sayi.

num2: Ikinci sayi.

operation: Hangi islem secilmis (topla, cikar, carp, bol).

🔹 Islem yapiliyor:

python
Kopyala
Düzenle
if operation == 'add':
    result = num1 + num2
Yani: "Topla dediyse iki sayiyi topla."
Digerleri de ayni sekilde cikar, carp, bol.

🔹 render_template('index.html', result=result)
HTML sayfasini ac ve sonucu icine yerlestir.
Yani: "Sayfayi goster, sonucu da ekle."

🔹 if __name__ == '__main__':
Bu kod, dosyayi calistirdiginda Flask sunucusunu baslatir.
Yani: "Programi baslat."


 """