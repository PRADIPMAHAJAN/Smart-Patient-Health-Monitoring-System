from flask import Flask,render_template,url_for,flash,redirect
from form import RegistrationForm,LoginForm

app=Flask(__name__,template_folder='template')
app.config['SECRET_KEY']=''

@app.route('/about')
def Deshboard():
    return ' Welcome to my deshboard the deshboard is left to create you can create your deshboard '

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html',title='Register',form=form)

@app.route('/Login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'mahajanpradip@gmail.com' and form.Password.data == 'password':
            flash('you have been logged in!','success')
            return redirect('http://127.0.0.1:1880/=SAdMD4RqAG7qpndUAAAA')
        else:
            flash('login unsuccessfull please check username and password','denger')
    return render_template('login.html',title='Login',form=form)
