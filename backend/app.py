from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_sesiones'

# Usuarios de ejemplo
usuarios = {
    'admin': {'password': 'adminpass', 'role': 'administrador'},
    'encargado1': {'password': 'encargadopass', 'role': 'encargado'},
    'operario1': {'password': 'operariopass', 'role': 'operario'}
}

@app.route('/')
def index():
    role = session.get('role', 'invitado')  # Obtener el rol de la sesión o establecer como 'invitado'
    return render_template('index.html', role=role)

# Página de inicio de sesión
@app.route('/iniciar_sesion', methods=['GET', 'POST'])
def iniciar_sesion():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = usuarios.get(username)
        if user and user['password'] == password:
            session['user'] = username
            session['role'] = user['role']
            
            # Redirigir al perfil correspondiente
            return redirect(url_for('index'))
        else:
            return "Usuario o contraseña incorrectos", 401
    
    return render_template('iniciar_sesion.html')

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.clear()  # Limpiar la sesión
    return redirect(url_for('iniciar_sesion'))

if __name__ == '__main__':
    app.run(debug=True)
