from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("inicio.html")


@app.route("/clientes", methods=["GET", "POST"])
def clientes():

    if request.method == "POST":

        nombre = request.form["nombre"]
        nit = request.form["nit"]
        correo = request.form["correo"]
        telefono = request.form["telefono"]
        direccion = request.form["direccion"]

        return render_template(
            "clientes_confirmacion.html",
            nombre=nombre,
            nit=nit,
            correo=correo,
            telefono=telefono,
            direccion=direccion
        )

    return render_template("clientes.html")

@app.route("/proveedores", methods=["GET", "POST"])
def proveedores():

    if request.method == "POST":

        empresa = request.form["empresa"]
        contacto = request.form["contacto"]
        nit = request.form["nit"]
        tipo = request.form["tipo"]
        pago = request.form["pago"]

        activo = request.form.get("activo")

        if activo:
            estado = "Sí"
        else:
            estado = "No"

        return render_template(
            "proveedores_confirmacion.html",
            empresa=empresa,
            contacto=contacto,
            nit=nit,
            tipo=tipo,
            pago=pago,
            activo=estado
        )

    return render_template("proveedores.html")


if __name__ == "__main__":
    app.run(debug=True)