from flask import Flask, render_template

# Inicializamos la aplicación Flask
app = Flask(__name__)

# RUTA 1: La página principal que mostrará el mapa.
# Cuando alguien visite "http://127.0.0.1:5000/" se ejecutará esta función.
@app.route('/')
def mostrar_mapa():
    """Renderiza la plantilla del mapa."""
    return render_template('index.html')

# RUTA 2: Una ruta interna que devuelve solo el HTML del formulario.
# El JavaScript del mapa llamará a esta ruta para obtener el formulario.
@app.route('/formulario')
def obtener_formulario():
    """Renderiza la plantilla del formulario para ser usada en el popup."""
    # Nota: Aquí podrías pasarle datos al formulario si lo necesitaras.
    # Por ejemplo: return render_template('nuevoEstudiante.html', tipos_reporte=lista)
    return render_template('nuevoEstudiante.html')

# Esto es necesario para ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)