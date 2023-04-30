from flask import Flask
from flask import render_template
from flask import request
from wtforms import Form, StringField, validators,SelectField,IntegerField
from wtforms.validators import DataRequired,Length,Regexp

class ContactForm(Form):
    rels=('Reloj GMT-964','Reloj GMT-01-Azul','Reloj GMT-01 Oro','Reloj GMT-01 Plata','Reloj GMT-01 Transparente')
    #producto = SelectField('Selecciona', [validators.DataRequired(),validators.Length(min=10)],choices=[(p,p)for p in prods])
 
    prods=('Paquete SkinCare')
    mpago =('Pago contra entrega','Depósito','Transferencia')
    mentrega =('Recoger en tienda (Punta alta)','Cotizar envío','Acordar')
    username = StringField('Nombre', [validators.DataRequired(),validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.DataRequired(),validators.Length(min=6, max=35)])
    message = StringField('Mensaje', [validators.DataRequired(),validators.Length(min=10)])
    producto = SelectField('Selecciona', [validators.DataRequired(),validators.Length(min=10)],choices=[prods])
    contactnum = StringField('Número de contacto',[validators.DataRequired(),validators.Length(min=10, max=10)])
    metodoentrega = SelectField('Entrega', [validators.DataRequired(),validators.Length(min=1)],choices=[(x,x)for x in mentrega])
    metodopago = SelectField('Método de pago', [validators.DataRequired(),validators.Length(min=1)],choices=[(x,x)for x in mpago])
    reloj = SelectField('Selecciona modelo', [validators.DataRequired(),validators.Length(min=10)],choices=[(x,x)for x in rels])

app = Flask(__name__)

@app.route('/contacto/', methods=['GET', 'POST'])
def contacto():
    form = ContactForm(request.form)
    if request.method == 'POST' and form.validate():
        log_user = str('Hola ') + request.form['username'] + '!'
        user_message = request.form['message']
        anuncio_registro='Recibirás un mensaje al correo proporcionado ' + request.form['email'] 
        return render_template('message.html', log_user=log_user,user_message=user_message,anuncio_registro=anuncio_registro)
    return render_template('contacto.html', form=form)


@app.route("/", methods=['GET', 'POST'])
def landing_page():
    form = ContactForm(request.form)

    if request.method == 'POST':

        log_user = request.form['username']
        phone=request.form['contactnum']
        metodo_entrega=request.form['metodoentrega']
        metodo_pago=request.form['metodopago']
        prod_in = request.form.get('producto', None)
        if prod_in == 'Paquete SkinCare':
            select_pedido = request.form['producto']
            simg = "static/images/img_4.jpg"
            prod_desc = "1 Banda sujetador de cabello <br>1 Pulpito exfoliador <br>1 Esponja de maquillaje<br>7 Diferentes mascarillas para cara.<br>2 Mascarillas de animalito para cara.<br>3 Mascarillas para labios.<br>4 Mascarillas para ojeras.<br>3 Artículos variados. "
            prod_desc = prod_desc.split('<br>')

        else:
            prod_in = request.form.get('reloj', None)
        if prod_in == 'Reloj GMT-964':
            select_pedido = request.form['reloj']
            simg = 'static/images/watch7.jpg'
            prod_desc = 'Reloj geométrico de movimiento automático <br> Mecanismo a la vista <br> Caja de acero inoxidable<br>Diámetro de caja 42mm'
            prod_desc = prod_desc.split('<br>')
        if prod_in == 'Reloj GMT-01-Azul':
            select_pedido = request.form['reloj']
            simg = 'static/images/mgt01-azul.jpg'
            prod_desc = 'Reloj automático <br> Mecanismo a la vista <br>Acero inoxidable color azul'
            prod_desc = prod_desc.split('<br>')

        if prod_in == 'Reloj GMT-01 Oro':
            select_pedido = request.form['reloj']
            simg = 'static/images/watch4.jpg'
            prod_desc = 'Reloj automático <br> Mecanismo a la vista <br>Acero inoxidable color plata con dorado'
            prod_desc = prod_desc.split('<br>')

        if prod_in == 'Reloj GMT-01 Plata':
            select_pedido = request.form['reloj']
            simg = 'static/images/platanegro.jpg'
            prod_desc = 'Reloj automático <br> Mecanismo a la vista <br>Acero inoxidable color plata con negro'
            prod_desc = prod_desc.split('<br>')

        if prod_in == 'Reloj GMT-01 Transparente':
            select_pedido = request.form['reloj']
            simg = 'static/images/transparente.jpg'
            prod_desc = 'Reloj mecánico de diseño transparente <br> Plateado-dorado-transparente <br> Correa de acero inoxidable'
            prod_desc = prod_desc.split('<br>')

        return render_template('message.html', metodo_entrega=metodo_entrega,metodo_pago=metodo_pago,log_user=log_user,select_pedido=select_pedido,simg=simg,prod_desc=prod_desc,phone=phone)

    return render_template('inicio.html',form=form)

@app.route("/comprarsc", methods=['GET', 'POST'])
def comprarsc():
    form = ContactForm(request.form)
    if request.method == 'POST':
        log_user = str('Hola ') + request.form['username'] + '!'
        select_pedido='Seleccionaste el producto paquete SkinCare!'
        simg = "static/images/img_4.jpg"
        prod_desc = "1 Banda sujetador de cabello <br>1 Pulpito exfoliador <br>1 Esponja de maquillaje<br>7 Diferentes mascarillas para cara.<br>2 Mascarillas de animalito para cara.<br>3 Mascarillas para labios.<br>4 Mascarillas para ojeras.<br>3 Artículos variados. "
        prod_desc = prod_desc.split('<br>')

        return render_template('pedidosc.html', log_user=log_user,select_pedido=select_pedido,simg=simg,prod_desc=prod_desc)

@app.route("/acerca/")
def  acerca():
    return render_template('acerca.html')

@app.route("/portafolio/")
def  portafolio():
    return render_template('portafolio.html')

if __name__ == "__main__":
    app.run(port=5001,debug=True)

