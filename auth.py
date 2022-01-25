# import packages
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from flask_login import login_user, logout_user, login_required
from __init__ import db


auth = Blueprint('auth', __name__) # create a Blueprint object that is named 'auth'

@auth.route('/login', methods=['GET', 'POST'])
def login(): 
    if request.method == 'GET':
        return render_template('login.html') # return the login page
    else: # if POST is requested (submit button pressed)
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password: # if input boxes are empty
            flash('Please fill in all categories.')
            return redirect(url_for('auth.login')) # reload page
        remember = True if request.form.get('remember') else False

        user = User.query.filter_by(username=username).first() # check if the username actually exists
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if not user:
            flash('Please sign up before!')
            return redirect(url_for('auth.signup')) # redirect to signup() function
        elif not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page
        
        # if the above check passes, the user has the right credentials + they can be logged in
        login_user(user, remember=remember)
        return redirect(url_for('main.home')) # redirect to home() function in main.py

@auth.route('/signup', methods=['GET', 'POST'])
def signup(): 
    if request.method=='GET':
        return render_template('signup.html') # return sign-up page
    else: # if POST is requested (submit button pressed)
        email = request.form.get('email')
        username = request.form.get('username')
        name = request.form.get('name')
        password = request.form.get('password')
        if not email or not username or not name or not password: # if input boxes are empty
            flash('Please fill in all categories.')
            return redirect(url_for('auth.signup')) # reload page
        user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database
        user2 = User.query.filter_by(username=username).first() # if this returns a user, then the username already exists in database
        if (user and user2) or (user or user2): 
            flash('Email address and/or username already exist. Please try again.')
            return redirect(url_for('auth.signup')) # reload page
        # create a new user with the form data & defaults. Hash the password so the plaintext version isn't saved.
        new_user = User(email=email, username=username, name=name, password=generate_password_hash(password, method='sha256'), 
                        low_price=False, med_price=False, high_price=False, small_size=False, med_size=False, large_size=False, low_health=False, med_health=False, high_health=False, 
                        dislike1=False, dislike2=False, dislike3=False, dislike4=False, dislike5=False, dislike6=False, dislike7=False, dislike8=False, dislike9=False, dislike10=False, 
                        dislike11=False, dislike12=False, dislike13=False, dislike14=False, dislike15=False, dislike16=False, dislike17=False, dislike18=False, dislike19=False, dislike20=False, 
                        dislike21=False, dislike22=False, dislike23=False, dislike24=False, dislike25=False, dislike26=False, dislike27=False, dislike28=False, dislike29=False, dislike30=False, 
                        dislike31=False, dislike32=False, dislike33=False, dislike34=False, dislike35=False, dislike36=False, dislike37=False, dislike38=False, dislike39=False, dislike40=False, 
                        dislike41=False, dislike42=False, dislike43=False, dislike44=False, dislike45=False, dislike46=False, dislike47=False, dislike48=False, dislike49=False, dislike50=False, 
                        dislike51=False, dislike52=False, dislike53=False, dislike54=False, dislike55=False, dislike56=False, dislike57=False, dislike58=False, dislike59=False, dislike60=False, 
                        dislike61=False, dislike62=False, dislike63=False, dislike64=False, dislike65=False, dislike66=False, dislike67=False, dislike68=False, dislike69=False, dislike70=False, 
                        dislike71=False, dislike72=False, dislike73=False, dislike74=False, dislike75=False, dislike76=False, dislike77=False, dislike78=False, dislike79=False,
                        like1=False, like2=False, like3=False, like4=False, like5=False, like6=False, like7=False, like8=False, like9=False, like10=False, 
                        like11=False, like12=False, like13=False, like14=False, like15=False, like16=False, like17=False, like18=False, like19=False, like20=False, 
                        like21=False, like22=False, like23=False, like24=False, like25=False, like26=False, like27=False, like28=False, like29=False, like30=False, 
                        like31=False, like32=False, like33=False, like34=False, like35=False, like36=False, like37=False, like38=False, like39=False, like40=False, 
                        like41=False, like42=False, like43=False, like44=False, like45=False, like46=False, like47=False, like48=False, like49=False, like50=False, 
                        like51=False, like52=False, like53=False, like54=False, like55=False, like56=False, like57=False, like58=False, like59=False, like60=False, 
                        like61=False, like62=False, like63=False, like64=False, like65=False, like66=False, like67=False, like68=False, like69=False, like70=False, 
                        like71=False, like72=False, like73=False, like74=False, like75=False, like76=False, like77=False, like78=False, like79=False)
        
        db.session.add(new_user) # add the new user to the database
        db.session.commit() # save changes to the database
        flash("Successful sign-up! Please login now.")
        return redirect(url_for('auth.login')) # redirect to login() function

@auth.route('/logout')
@login_required
def logout():
    logout_user() # log the user out
    return redirect(url_for('main.index')) # redirect to index() function in main.py