from flask import Flask, render_template, flash, redirect, request, session
from werkzeug.security import generate_password_hash, check_password_hash
import sys, re
from config import koneksi

app = Flask(__name__, template_folder='template')

app.secret_key = '123***912' # secret key

# inisialisasi database
db = koneksi.connections()
cur = db.cursor()

@app.route('/')
def index():

	return render_template('index.html', title='LIBKTP - Aplikasi Pengumpulan Data KTP dan Pencarian')

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():

	if 'user_admin' in session: # jika user (admin) sudah berhasil login
		return redirect('/admin')

	if request.method == 'POST':
		
		username = request.form['username']
		password = request.form['password']

		query = cur.execute('SELECT username, password FROM admin WHERE username = %s', (username,))
		result = cur.fetchall()

		for row in result: 
			data_admin = { 'password': row[1] }

		if query > 0: # jika data ada di database, maka
			# cek apakah password yang dimasukan cocok dengan yang ada di database
			if check_password_hash(data_admin['password'], password):
				# buat session
				session['user_admin'] = username

				# alihkan ke halaman dashboard admin
				return redirect('/admin')
			else:
				flash('Password salah.', 'error')
				return redirect('/admin/login')
		else:
			flash('Username salah.', 'error')
			return redirect('/admin/login')
	else:
		return render_template('login_admin.html', title='Login Admin')

@app.route('/search-ktp')
def search_ktp():

	search = request.args.get('nik')
	
	# cari data ktp yang ada di database
	query = cur.execute('SELECT * FROM ktp WHERE nik LIKE %s ORDER BY id DESC', ('%' + search + '%',))
	result = cur.fetchall()

	return render_template('search_ktp.html', title='LIBKTP - Kamu mencari NIK ' + search, result=result, count=query, search=search)

@app.route('/detail-ktp/<int:id_ktp>')
def detail_ktp(id_ktp):

	# ambil data ktp di database sesuai id ktp
	query = cur.execute('SELECT * FROM ktp WHERE id = %s', (id_ktp,))
	result = cur.fetchall()

	for row in result:
		get_ktp = { 'nik': row[1], 'nama': row[2], 'tempat_lahir': row[3], 'tgl_lahir': row[4], 'jk': row[5],
			'gol_darah': row[6], 'agama': row[7], 'alamat': row[8], 'rt_rw': row[9], 'kel_desa': row[10], 'kecamatan': row[11],
			'status_perkawinan': row[12], 'pekerjaan': row[13], 'kewarganegaraan': row[14], 'berlaku_hingga': row[15]
		}

	return render_template('detail_ktp.html', title='LIBKTP - ' + get_ktp['nama'], getktp=get_ktp)

@app.route('/contact', methods=['POST'])
def contact():

	nama = request.form['nama_contact']
	email = request.form['email_contact']
	no_telp = request.form['no_hp']
	isi = request.form['isi_contact']

	cur.execute('INSERT INTO contact(nama, email, no_telp, isi) VALUES (%s, %s, %s, %s)', (nama, email, no_telp, isi,))
	db.commit()

	# pesan sweetalert
	add_sweetalert = True

	return render_template('index.html', title='LIBKTP - Aplikasi Pengumpulan Data KTP dan Pencarian', msg=add_sweetalert)

# buat blueprint biar rapih
from admin import admin as admin_blueprint
app.register_blueprint(admin_blueprint)

if __name__ == '__main__':
	app.run(debug=True)