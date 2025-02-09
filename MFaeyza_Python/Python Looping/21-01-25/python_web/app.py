from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/process',methods=['POST'])
def process():
    try:
        jumlah_nama = int(request.form['jumlah_nama'])
        if jumlah_nama < 1:
            return "Jumlah Nama Harus Lebih Dari 0. <a href='/'>Kembali</a>"
        return  render_template('form.html', jumlah_nama = jumlah_nama)
    except ValueError:
        return "Input Tidak Valid. <a href='/'>Kembali</a>"

@app.route('/result',methods=['POST'])
def result():
    nama_list = request.form.getlist('nama')
    return render_template('result.html', nama_list=nama_list)

if __name__ == '__main__':
    app.run(debug=true)