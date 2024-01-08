from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'clave_secreta'  # Cambia esto por una clave segura en un entorno de producción

# Datos ficticios para el dashboard
facturacion_dia = {'Producto A': 120, 'Producto B': 150, 'Producto C': 80}
facturacion_semana = {'Producto A': 300, 'Producto B': 450, 'Producto C': 200}
facturacion_mes = {'Producto A': 800, 'Producto B': 1200, 'Producto C': 500}

stock_actual = 100
por_cobrar = 5000

# Usuario de ejemplo
usuario_valido = {'usuario': 'Alonso', 'contraseña': 'ti$$'}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        if usuario == usuario_valido['usuario'] and contraseña == usuario_valido['contraseña']:
            session['usuario'] = usuario
            return redirect(url_for('dashboard'))
        else:
            mensaje_error = 'Credenciales incorrectas. Intenta de nuevo.'
            return render_template('login.html', mensaje_error=mensaje_error)
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'usuario' in session:
        return render_template('dashboard.html', 
                               facturacion_dia=facturacion_dia,
                               facturacion_semana=facturacion_semana,
                               facturacion_mes=facturacion_mes,
                               stock_actual=stock_actual,
                               por_cobrar=por_cobrar)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
