from flask import render_template, redirect, url_for, flash, request
from app import app, log
from app.forms import LoginForm
from app.models import User
from flask_login import login_user, login_required, logout_user, UserMixin, login_manager, current_user

# ROUTING
@app.route('/')
def index():
    ''' index page '''
    log.info("someone is accessing index.html!!!")
    return render_template('index.html', title='Flavor')

@app.route('/secure', methods=['GET', 'POST'])
@login_required
def secure_page():
    ''' testing a secure area for User login '''
    return 'This is a secure area for Logged-in users only!!!'


# ERROR HANDLERS
@app.errorhandler(404)
def page_not_found(error):
    log.error('Page not found: %s', (request.path))
    return render_template('error.html', title='404 Error', msg=request.path)

@app.errorhandler(500)
def internal_server_error(error):
    log.error('Server Error: %s' % error)
    return render_template('error.html', title='500 Error', msg=error)

@app.errorhandler(Exception)
def unhandled_exception(e):
    log.error('Unhandled Exception: %s' % str(e))
    return render_template('error.html', title='Exception', msg=str(e)), 500

@app.route('/exception')
def exception():
    ''' test exception handling '''
    raise Exception('THIS IS AN EXCEPTION DUDE')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Invalid Email or Password')
                return redirect(url_for('login'))
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
        else:
            flash('check for proper Email format, must be in form of username@company.com')
            return render_template('login.html', title='Sign In', form=form)\

    if request.method == 'GET':
        return render_template('login.html', title='Sign In', form=form)
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))