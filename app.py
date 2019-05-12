from flask import Flask, render_template, redirect, url_for, request
import pandas as pd

app = Flask(__name__)
header = ['name', 'department', 'order']
orders = pd.DataFrame(columns=header)
menu = ""

@app.route('/')
def welcome():
    return redirect('/login')

@app.route('/manage',methods=['GET', 'POST'])
def manage():
    global orders,menu
    if request.method == 'POST':
        if(request.form['menu']):
            menu = request.form['menu']
    return render_template('manage.html',orders = orders, menu = menu)

@app.route('/order', methods=['GET', 'POST'])
def order():
    name = ""
    department = ""
    order = ""
    global orders, menu
    if request.method == 'POST':
        if(request.form['fullname']):
            name = request.form['fullname']
        if (request.form['department']):
            department = request.form['department']
        if (request.form['order']):
            order = request.form['order']
        orders = orders.append({'fullname':name,'department':department,'order':order},ignore_index=True)
        return redirect('/login')
    return render_template('order.html', menu = menu)

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            return redirect('/manage')
        if request.form['username'] == 'user' and request.form['password'] == 'user':
            return redirect('/order')
        error = "nhap sai ten hoac mat khau"
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(host='localhost', port=5100, debug=True)
    print(orders)
    #aaa