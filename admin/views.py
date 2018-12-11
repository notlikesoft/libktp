from flask import render_template, request, redirect, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from . import admin
from config import koneksi
import sys, re, os

# inisialisasi database
db = koneksi.connections()
cur = db.cursor()

@admin.route('/admin')
def dashboard():
	if 'user_admin' in session: # cek apakah session sudah ada,
		# maka kita hanya kasih pass, atau membiarkan saja
		pass
	else: # jika user belum login, maka akan redirect ke halaman login
		flash('Eittsss ! Mau kemana ? Jangan nakal ya, bro.', 'error')
		return redirect('/admin/login')

	query = cur.execute('SELECT id, nik, nama, tempat_lahir, tgl_lahir, jk FROM ktp ORDER BY id DESC')
	result = cur.fetchall()

	return render_template('admin/dashboard.html', title='Dashboard Admin', result=result)

@admin.route('/admin/save-ktp', methods=['GET', 'POST'])
def save_ktp():

	if 'user_admin' in session: # cek apakah session sudah ada,
		# maka kita hanya kasih pass, atau membiarkan saja
		pass
	else: # jika user belum login, maka akan redirect ke halaman login
		flash('Eittsss ! Mau kemana ? Jangan nakal ya, bro.', 'error')
		return redirect('/admin/login')

	if request.method == 'POST':
		nik = request.form['nik_input']
		nama = request.form['nama']
		tempat_lahir = request.form['tempat_lahir']
		tgl_lahir = request.form['tgl_lahir']
		jk = request.form['jk']
		gol_darah = request.form['gol_darah']
		agama = request.form['agama']
		alamat = request.form['alamat']
		rt_rw = request.form['rt_rw']
		kel_desa = request.form['kel_desa']
		kecamatan = request.form['kecamatan']
		status_perkawinan = request.form['status_perkawinan']
		pekerjaan = request.form['pekerjaan']
		kewarganegaraan = request.form['kewarganegaraan']
		berlaku_hingga = request.form['berlaku_hingga']

		# simpan data ktp ke database
		cur.execute('INSERT INTO ktp(nik, nama, tempat_lahir, tgl_lahir, jk, gol_darah, agama, alamat, rt_rw, \
			kel_desa, kecamatan, status_perkawinan, pekerjaan, kewarganegaraan, berlaku_hingga) VALUES \
			(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (nik, nama, tempat_lahir, tgl_lahir, \
			jk, gol_darah, agama, alamat, rt_rw, kel_desa, kecamatan, status_perkawinan, pekerjaan, \
			kewarganegaraan, berlaku_hingga))
		db.commit()

		flash('KTP berhasil di simpan.', 'success')

		return redirect('/admin')

	else:
		return render_template('admin/input_ktp.html', title='LIBKTP - Input KTP')

@admin.route('/delete/ktp/<int:id_ktp>')
def delete_ktp(id_ktp):

	if 'user_admin' in session: # cek apakah session sudah ada,
		# maka kita hanya kasih pass, atau membiarkan saja
		pass
	else: # jika user belum login, maka akan redirect ke halaman login
		flash('Eittsss ! Mau kemana ? Jangan nakal ya, bro.', 'error')
		return redirect('/admin/login')

	cur.execute('DELETE FROM ktp WHERE id = %s', (id_ktp,))
	db.commit()

	flash('KTP berhasil di hapus.', 'success')
	return redirect('/admin')

@admin.route('/edit/ktp/<int:id_ktp>', methods=['GET', 'POST'])
def edit_ktp(id_ktp):

	if 'user_admin' in session: # cek apakah session sudah ada,
		# maka kita hanya kasih pass, atau membiarkan saja
		pass
	else: # jika user belum login, maka akan redirect ke halaman login
		flash('Eittsss ! Mau kemana ? Jangan nakal ya, bro.', 'error')
		return redirect('/admin/login')

	query = cur.execute('SELECT * FROM ktp WHERE id = %s', (id_ktp,))
	result = cur.fetchall()

	for row in result:
		get_ktp = { 'nik': row[1], 'nama': row[2], 'tempat_lahir': row[3], 'tgl_lahir': row[4], 'jk': row[5],
			'gol_darah': row[6], 'agama': row[7], 'alamat': row[8], 'rt_rw': row[9], 'kel_desa': row[10], 'kecamatan': row[11],
			'status_perkawinan': row[12], 'pekerjaan': row[13], 'kewarganegaraan': row[14], 'berlaku_hingga': row[15]
		}

	if request.method == 'POST':
		nik = request.form['nik_input']
		nama = request.form['nama']
		tempat_lahir = request.form['tempat_lahir']
		tgl_lahir = request.form['tgl_lahir']
		jk = request.form['jk']
		gol_darah = request.form['gol_darah']
		agama = request.form['agama']
		alamat = request.form['alamat']
		rt_rw = request.form['rt_rw']
		kel_desa = request.form['kel_desa']
		kecamatan = request.form['kecamatan']
		status_perkawinan = request.form['status_perkawinan']
		pekerjaan = request.form['pekerjaan']
		kewarganegaraan = request.form['kewarganegaraan']
		berlaku_hingga = request.form['berlaku_hingga']

		cur.execute('UPDATE ktp SET nik = %s, nama = %s, tempat_lahir = %s, tgl_lahir = %s, \
			jk = %s, gol_darah = %s, agama = %s, alamat = %s, rt_rw = %s, kel_desa = %s, kecamatan = %s, \
			status_perkawinan = %s, pekerjaan = %s, kewarganegaraan = %s, berlaku_hingga = %s WHERE id = %s', \
			(nik, nama, tempat_lahir, tgl_lahir, jk, gol_darah, agama, alamat, rt_rw, kel_desa, kecamatan, \
			status_perkawinan, pekerjaan, kewarganegaraan, berlaku_hingga, id_ktp,))
		db.commit()

		flash('KTP berhasil di edit.', 'success')
		return redirect('/admin')
	else:
		return render_template('admin/edit_ktp.html', title='LIBKTP - Edit KTP', getktp=get_ktp)

@admin.route('/admin/inbox')
def inbox():

	if 'user_admin' in session: # cek apakah session sudah ada,
		# maka kita hanya kasih pass, atau membiarkan saja
		pass
	else: # jika user belum login, maka akan redirect ke halaman login
		flash('Eittsss ! Mau kemana ? Jangan nakal ya, bro.', 'error')
		return redirect('/admin/login')

	query = cur.execute('SELECT * FROM contact ORDER BY id DESC')
	result = cur.fetchall()

	return render_template('admin/inbox.html', titl='LIBKTP - Inbox', result=result)

@admin.route('/admin/delete/inbox/<int:id_inbox>')
def delete_inbox(id_inbox):

	if 'user_admin' in session: # cek apakah session sudah ada,
		# maka kita hanya kasih pass, atau membiarkan saja
		pass
	else: # jika user belum login, maka akan redirect ke halaman login
		flash('Eittsss ! Mau kemana ? Jangan nakal ya, bro.', 'error')
		return redirect('/admin/login')

	cur.execute('DELETE FROM contact WHERE id = %s', (id_inbox,))
	db.commit()

	return redirect('/admin/inbox')

@admin.route('/admin/add-account', methods=['GET', 'POST'])
def add_account():

	if 'user_admin' in session: # cek apakah session sudah ada,
		# maka kita hanya kasih pass, atau membiarkan saja
		pass
	else: # jika user belum login, maka akan redirect ke halaman login
		flash('Eittsss ! Mau kemana ? Jangan nakal ya, bro.', 'error')
		return redirect('/admin/login')

	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']

		if username == '':
			flash('Username tidak boleh kosong', 'error')
		elif password == '':
			flash('Password tidak boleh kosong', 'error')
		else:
			pw_hash = generate_password_hash(password)
			cur.execute('INSERT INTO admin(username, password) VALUES (%s, %s)', (username, pw_hash,))
			db.commit()

			flash('Akun admin berhasil di tambahkan', 'success')

			return redirect('/admin/data-account')

		return redirect('/admin/add-account')

	else:
		return render_template('admin/add_account.html', title='LIBKTP - Tambah Akun Admin')

@admin.route('/admin/data-account')
def data_account():

	query = cur.execute('SELECT * FROM admin ORDER BY id DESC')
	result = cur.fetchall()

	return render_template('admin/data_account.html', title='LIBKTP - Data Akun Admin', result=result)


@admin.route('/admin/delete-account/<int:id_admin>')
def delete_account(id_admin):
	if 'user_admin' in session: # cek apakah session sudah ada,
		# maka kita hanya kasih pass, atau membiarkan saja
		pass
	else: # jika user belum login, maka akan redirect ke halaman login
		flash('Eittsss ! Mau kemana ? Jangan nakal ya, bro.', 'error')
		return redirect('/admin/login')

	cur.execute('DELETE FROM admin WHERE id = %s', (id_admin,))
	db.commit()

	flash('Akun admin berhasil di hapus.', 'success')
	return redirect('/admin/data-account')

@admin.route('/admin/logout')
def logout():
	# hapus session jika ada session
	session.pop('user_admin', None)
	flash('Anda berhasil keluar.', 'success')
	return redirect('/admin/login')