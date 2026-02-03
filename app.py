from flask import Flask, render_template, request
from db import insertar_usuario, obtener_mail

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/getmail", methods=["GET", "POST"])
def getmail():
    resultado = None
    error = None

    if request.method == "POST":
        nombre = request.form.get("nombre")

        if nombre:
            dato = obtener_mail(nombre)

            if dato:
                resultado = f"El correo de {nombre} es: {dato[0]}"
            else:
                error = f"No existe ningún usuario llamado '{nombre}'."

    return render_template("getmail.html", resultado=resultado, error=error)

@app.route("/addmail", methods=["GET", "POST"])
def addmail():
    mensaje = None
    error = None

    if request.method == "POST":
        nombre = request.form.get("nombre")
        mail = request.form.get("mail")

        try:
            insertar_usuario(nombre, mail)
            mensaje = f"Usuario {nombre} añadido correctamente."
        except Exception as e:
            error = "Error al insertar usuario."

    return render_template("addmail.html", mensaje=mensaje, error=error)

if __name__ == "__main__":
    app.run(debug=True)
