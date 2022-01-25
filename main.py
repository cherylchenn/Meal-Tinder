# import packages
from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_required, current_user
from __init__ import create_app, db
from models import User

# main blueprint
main = Blueprint('main', __name__)

@main.route('/') 
def index():
    return render_template('index.html') # return the index page (first page with access to login / signup)

@main.route('/home')
@login_required
def home():
    return render_template('main-page.html') # return the main page

@main.route('/recommendations') # EDIT
@login_required
def recommend():
    # query the database for the current user's id (primary key)
    y = User.query.get(current_user.id)

    # assign the current user's attributes to the following variables
    low_price = y.low_price
    med_price = y.med_price
    high_price = y.high_price
    small_size = y.small_size
    med_size = y.med_size
    large_size = y.large_size
    low_health = y.low_health
    med_health = y.med_health
    high_health = y.high_health

    # return the recommend.html template with variables that will be referenced there
    return render_template('recommend.html', low_price=low_price, med_price=med_price, high_price=high_price, small_size=small_size, med_size=med_size, large_size=large_size, low_health=low_health, med_health=med_health, high_health=high_health, 
                            dislike1=y.dislike1, dislike2=y.dislike2, dislike3=y.dislike3, dislike4=y.dislike4, dislike5=y.dislike5, dislike6=y.dislike6, dislike7=y.dislike7, dislike8=y.dislike8, dislike9=y.dislike9, dislike10=y.dislike10, 
                            dislike11=y.dislike11, dislike12=y.dislike12, dislike13=y.dislike13, dislike14=y.dislike14, dislike15=y.dislike15, dislike16=y.dislike16, dislike17=y.dislike17, dislike18=y.dislike18, dislike19=y.dislike19, dislike20=y.dislike20, 
                            dislike21=y.dislike21, dislike22=y.dislike22, dislike23=y.dislike23, dislike24=y.dislike24, dislike25=y.dislike25, dislike26=y.dislike26, dislike27=y.dislike27, dislike28=y.dislike28, dislike29=y.dislike29, dislike30=y.dislike30, 
                            dislike31=y.dislike31, dislike32=y.dislike32, dislike33=y.dislike33, dislike34=y.dislike34, dislike35=y.dislike35, dislike36=y.dislike36, dislike37=y.dislike37, dislike38=y.dislike38, dislike39=y.dislike39, dislike40=y.dislike40, 
                            dislike41=y.dislike41, dislike42=y.dislike42, dislike43=y.dislike43, dislike44=y.dislike44, dislike45=y.dislike45, dislike46=y.dislike46, dislike47=y.dislike47, dislike48=y.dislike48, dislike49=y.dislike49, dislike50=y.dislike50, 
                            dislike51=y.dislike51, dislike52=y.dislike52, dislike53=y.dislike53, dislike54=y.dislike54, dislike55=y.dislike55, dislike56=y.dislike56, dislike57=y.dislike57, dislike58=y.dislike58, dislike59=y.dislike59, dislike60=y.dislike60, 
                            dislike61=y.dislike61, dislike62=y.dislike62, dislike63=y.dislike63, dislike64=y.dislike64, dislike65=y.dislike65, dislike66=y.dislike66, dislike67=y.dislike67, dislike68=y.dislike68, dislike69=y.dislike69, dislike70=y.dislike70, 
                            dislike71=y.dislike71, dislike72=y.dislike72, dislike73=y.dislike73, dislike74=y.dislike74, dislike75=y.dislike75, dislike76=y.dislike76, dislike77=y.dislike77, dislike78=y.dislike78, dislike79=y.dislike79, 
                            like1=y.like1, like2=y.like2, like3=y.like3, like4=y.like4, like5=y.like5, like6=y.like6, like7=y.like7, like8=y.like8, like9=y.like9, like10=y.like10, 
                            like11=y.like11, like12=y.like12, like13=y.like13, like14=y.like14, like15=y.like15, like16=y.like16, like17=y.like17, like18=y.like18, like19=y.like19, like20=y.like20, 
                            like21=y.like21, like22=y.like22, like23=y.like23, like24=y.like24, like25=y.like25, like26=y.like26, like27=y.like27, like28=y.like28, like29=y.like29, like30=y.like30, 
                            like31=y.like31, like32=y.like32, like33=y.like33, like34=y.like34, like35=y.like35, like36=y.like36, like37=y.like37, like38=y.like38, like39=y.like39, like40=y.like40, 
                            like41=y.like41, like42=y.like42, like43=y.like43, like44=y.like44, like45=y.like45, like46=y.like46, like47=y.like47, like48=y.like48, like49=y.like49, like50=y.like50, 
                            like51=y.like51, like52=y.like52, like53=y.like53, like54=y.like54, like55=y.like55, like56=y.like56, like57=y.like57, like58=y.like58, like59=y.like59, like60=y.like60, 
                            like61=y.like61, like62=y.like62, like63=y.like63, like64=y.like64, like65=y.like65, like66=y.like66, like67=y.like67, like68=y.like68, like69=y.like69, like70=y.like70, 
                            like71=y.like71, like72=y.like72, like73=y.like73, like74=y.like74, like75=y.like75, like76=y.like76, like77=y.like77, like78=y.like78, like79=y.like79)

@main.route('/recform')
@login_required
def form():
    return render_template('rec-form.html') # return the recommendations form

@main.route('/submit_rec', methods=['GET', 'POST']) # EDIT
@login_required
def submit():
    if request.form == "GET":
        return render_template('rec-form.html') # return the recommendations form page
    else: # if POST is requested (submit button pressed)
        z = User.query.get(current_user.id)
        # refreshing "meal" variables
        z.low_price = False 
        z.med_price = False 
        z.high_price = False 
        z.small_size = False 
        z.med_size = False
        z.large_size = False
        z.low_health = False
        z.med_health = False
        z.high_health = False

        # refreshing dislike variables
        z.dislike1 = False
        z.dislike2 = False
        z.dislike3 = False
        z.dislike4 = False
        z.dislike5 = False
        z.dislike6 = False
        z.dislike7 = False
        z.dislike8 = False
        z.dislike9 = False
        z.dislike10 = False
        z.dislike11 = False
        z.dislike12 = False
        z.dislike13 = False
        z.dislike14 = False
        z.dislike15 = False
        z.dislike16 = False
        z.dislike17 = False
        z.dislike18 = False
        z.dislike19 = False
        z.dislike20 = False
        z.dislike21 = False
        z.dislike22 = False
        z.dislike23 = False
        z.dislike24 = False
        z.dislike25 = False
        z.dislike26 = False
        z.dislike27 = False
        z.dislike28 = False
        z.dislike29 = False
        z.dislike30 = False
        z.dislike31 = False
        z.dislike32 = False
        z.dislike33 = False
        z.dislike34 = False
        z.dislike35 = False
        z.dislike36 = False
        z.dislike37 = False
        z.dislike38 = False
        z.dislike39 = False
        z.dislike40 = False
        z.dislike41 = False
        z.dislike42 = False
        z.dislike43 = False
        z.dislike44 = False
        z.dislike45 = False
        z.dislike46 = False
        z.dislike47 = False
        z.dislike48 = False
        z.dislike49 = False
        z.dislike50 = False
        z.dislike51 = False
        z.dislike52 = False
        z.dislike53 = False
        z.dislike54 = False
        z.dislike55 = False
        z.dislike56 = False
        z.dislike57 = False
        z.dislike58 = False
        z.dislike59 = False
        z.dislike60 = False
        z.dislike61 = False
        z.dislike62 = False
        z.dislike63 = False
        z.dislike64 = False
        z.dislike65 = False
        z.dislike66 = False
        z.dislike67 = False
        z.dislike68 = False
        z.dislike69 = False
        z.dislike70 = False
        z.dislike71 = False
        z.dislike72 = False
        z.dislike73 = False
        z.dislike74 = False
        z.dislike75 = False
        z.dislike76 = False
        z.dislike77 = False
        z.dislike78 = False
        z.dislike79 = False

        # price values
        form_price = request.form.get('price')
        if form_price == "1" or form_price == "2":
            z.low_price = True
        elif form_price == "3":
            z.med_price = True
        else:
            z.high_price = True

        # portion values
        form_portion = request.form.get('portion')
        if form_portion == "1" or form_portion == "2":
            z.small_size = True
        elif form_portion == "3":
            z.med_size = True
        else:
            z.large_size = True
        
        # nutrition values
        form_nutrition = request.form.get('nutritional')
        if form_nutrition == "1" or form_nutrition == "2":
            z.low_health = True
        elif form_nutrition == "3":
            z.med_health = True
        else:
            z.high_health = True 
        
        db.session.commit() # save the changes to the database
        return redirect(url_for('main.recommend')) # redirect to the recommend() function

@main.route('/dislike', methods=['GET', 'POST']) # EDIT
@login_required
def dislike():
    # query the database for the current user's id
    x = User.query.get(current_user.id)
    # assign the value of the form option with the name "dislike" to the variable
    dislike = request.form.get('dislike')

    if dislike == "1":
        x.dislike1 = True
    elif dislike == "2":
        x.dislike2 = True
    elif dislike == "3":
        x.dislike3 = True
    elif dislike == "4":
        x.dislike4 = True
    elif dislike == "5":
        x.dislike5 = True
    elif dislike == "6":
        x.dislike6 = True
    elif dislike == "7":
        x.dislike7 = True
    elif dislike == "8":
        x.dislike8 = True
    elif dislike == "9":
        x.dislike9 = True
    elif dislike == "10":
        x.dislike10 = True
    elif dislike == "11":
        x.dislike11 = True
    elif dislike == "12":
        x.dislike12 = True
    elif dislike == "13":
        x.dislike13 = True
    elif dislike == "14":
        x.dislike14 = True
    elif dislike == "15":
        x.dislike15 = True
    elif dislike == "16":
        x.dislike16 = True
    elif dislike == "17":
        x.dislike17 = True
    elif dislike == "18":
        x.dislike18 = True
    elif dislike == "19":
        x.dislike19 = True
    elif dislike == "20":
        x.dislike20 = True
    elif dislike == "21":
        x.dislike21 = True
    elif dislike == "22":
        x.dislike22 = True
    elif dislike == "23":
        x.dislike23 = True
    elif dislike == "24":
        x.dislike24 = True
    elif dislike == "25":
        x.dislike25 = True
    elif dislike == "26":
        x.dislike26 = True
    elif dislike == "27":
        x.dislike27 = True
    elif dislike == "28":
        x.dislike28 = True
    elif dislike == "29":
        x.dislike29 = True
    elif dislike == "30":
        x.dislike30 = True
    elif dislike == "31":
        x.dislike31 = True
    elif dislike == "32":
        x.dislike32 = True
    elif dislike == "33":
        x.dislike33 = True
    elif dislike == "34":
        x.dislike34 = True
    elif dislike == "35":
        x.dislike35 = True
    elif dislike == "36":
        x.dislike36 = True
    elif dislike == "37":
        x.dislike37 = True
    elif dislike == "38":
        x.dislike38 = True
    elif dislike == "39":
        x.dislike39 = True
    elif dislike == "40":
        x.dislike40 = True
    elif dislike == "41":
        x.dislike41 = True
    elif dislike == "42":
        x.dislike42 = True
    elif dislike == "43":
        x.dislike43 = True
    elif dislike == "44":
        x.dislike44 = True
    elif dislike == "45":
        x.dislike45 = True
    elif dislike == "46":
        x.dislike46 = True
    elif dislike == "47":
        x.dislike47 = True
    elif dislike == "48":
        x.dislike48 = True
    elif dislike == "49":
        x.dislike49 = True
    elif dislike == "50":
        x.dislike50 = True
    elif dislike == "51":
        x.dislike51 = True
    elif dislike == "52":
        x.dislike52 = True
    elif dislike == "53":
        x.dislike53 = True
    elif dislike == "54":
        x.dislike54 = True
    elif dislike == "55":
        x.dislike55 = True
    elif dislike == "56":
        x.dislike56 = True
    elif dislike == "57":
        x.dislike57 = True
    elif dislike == "58":
        x.dislike58 = True
    elif dislike == "59":
        x.dislike59 = True
    elif dislike == "60":
        x.dislike60 = True
    elif dislike == "61":
        x.dislike61 = True
    elif dislike == "62":
        x.dislike62 = True
    elif dislike == "63":
        x.dislike63 = True
    elif dislike == "64":
        x.dislike64 = True
    elif dislike == "65":
        x.dislike65 = True
    elif dislike == "66":
        x.dislike66 = True
    elif dislike == "67":
        x.dislike67 = True
    elif dislike == "68":
        x.dislike68 = True
    elif dislike == "69":
        x.dislike69 = True
    elif dislike == "70":
        x.dislike70 = True
    elif dislike == "71":
        x.dislike71 = True
    elif dislike == "72":
        x.dislike72 = True
    elif dislike == "73":
        x.dislike73 = True
    elif dislike == "74":
        x.dislike74 = True
    elif dislike == "75":
        x.dislike75 = True
    elif dislike == "76":
        x.dislike76 = True
    elif dislike == "77":
        x.dislike77 = True
    elif dislike == "78":
        x.dislike78 = True
    else:
        x.dislike79 = True
               
    db.session.commit() # save the changes to the database
    return redirect(url_for('main.recommend')) # redirect to the recommend() function

@main.route('/like', methods=['GET', 'POST']) # EDIT
@login_required
def like():
    # query the database for the current user's id
    x = User.query.get(current_user.id)
    # assign the value of the form option with the name "like" to the variable
    like = request.form.get('like')
    
    if like == "1":
        x.like1 = True
    elif like == "2":
        x.like2 = True
    elif like == "3":
        x.like3 = True
    elif like == "4":
        x.like4 = True
    elif like == "5":
        x.like5 = True
    elif like == "6":
        x.like6 = True
    elif like == "7":
        x.like7 = True
    elif like == "8":
        x.like8 = True
    elif like == "9":
        x.like9 = True
    elif like == "10":
        x.like10 = True
    elif like == "11":
        x.like11 = True
    elif like == "12":
        x.like12 = True
    elif like == "13":
        x.like13 = True
    elif like == "14":
        x.like14 = True
    elif like == "15":
        x.like15 = True
    elif like == "16":
        x.like16 = True
    elif like == "17":
        x.like17 = True
    elif like == "18":
        x.like18 = True
    elif like == "19":
        x.like19 = True
    elif like == "20":
        x.like20 = True
    elif like == "21":
        x.like21 = True
    elif like == "22":
        x.like22 = True
    elif like == "23":
        x.like23 = True
    elif like == "24":
        x.like24 = True
    elif like == "25":
        x.like25 = True
    elif like == "26":
        x.like26 = True
    elif like == "27":
        x.like27 = True
    elif like == "28":
        x.like28 = True
    elif like == "29":
        x.like29 = True
    elif like == "30":
        x.like30 = True
    elif like == "31":
        x.like31 = True
    elif like == "32":
        x.like32 = True
    elif like == "33":
        x.like33 = True
    elif like == "34":
        x.like34 = True
    elif like == "35":
        x.like35 = True
    elif like == "36":
        x.like36 = True
    elif like == "37":
        x.like37 = True
    elif like == "38":
        x.like38 = True
    elif like == "39":
        x.like39 = True
    elif like == "40":
        x.like40 = True
    elif like == "41":
        x.like41 = True
    elif like == "42":
        x.like42 = True
    elif like == "43":
        x.like43 = True
    elif like == "44":
        x.like44 = True
    elif like == "45":
        x.like45 = True
    elif like == "46":
        x.like46 = True
    elif like == "47":
        x.like47 = True
    elif like == "48":
        x.like48 = True
    elif like == "49":
        x.like49 = True
    elif like == "50":
        x.like50 = True
    elif like == "51":
        x.like51 = True
    elif like == "52":
        x.like52 = True
    elif like == "53":
        x.like53 = True
    elif like == "54":
        x.like54 = True
    elif like == "55":
        x.like55 = True
    elif like == "56":
        x.like56 = True
    elif like == "57":
        x.like57 = True
    elif like == "58":
        x.like58 = True
    elif like == "59":
        x.like59 = True
    elif like == "60":
        x.like60 = True
    elif like == "61":
        x.like61 = True
    elif like == "62":
        x.like62 = True
    elif like == "63":
        x.like63 = True
    elif like == "64":
        x.like64 = True
    elif like == "65":
        x.like65 = True
    elif like == "66":
        x.like66 = True
    elif like == "67":
        x.like67 = True
    elif like == "68":
        x.like68 = True
    elif like == "69":
        x.like69 = True
    elif like == "70":
        x.like70 = True
    elif like == "71":
        x.like71 = True
    elif like == "72":
        x.like72 = True
    elif like == "73":
        x.like73 = True
    elif like == "74":
        x.like74 = True
    elif like == "75":
        x.like75 = True
    elif like == "76":
        x.like76 = True
    elif like == "77":
        x.like77 = True
    elif like == "78":
        x.like78 = True
    else:
        x.like79 = True

    db.session.commit() # save the changes to the database
    return redirect(url_for('main.recommend')) # redirect to the recommend() function

@main.route('/unlike', methods=['GET', 'POST']) # EDIT
def unlike():
    # query the database for the current user's id
    x = User.query.get(current_user.id)
    # assign the value of the form option with the name "unlike" to the variable
    unlike = request.form.get('unlike')

    if unlike == "1":
        x.like1 = False
    elif unlike == "2":
        x.like2 = False
    elif unlike == "3":
        x.like3 = False
    elif unlike == "4":
        x.like4 = False
    elif unlike == "5":
        x.like5 = False
    elif unlike == "6":
        x.like6 = False
    elif unlike == "7":
        x.like7 = False
    elif unlike == "8":
        x.like8 = False
    elif unlike == "9":
        x.like9 = False
    elif unlike == "10":
        x.like10 = False
    elif unlike == "11":
        x.like11 = False
    elif unlike == "12":
        x.like12 = False
    elif unlike == "13":
        x.like13 = False
    elif unlike == "14":
        x.like14 = False
    elif unlike == "15":
        x.like15 = False
    elif unlike == "16":
        x.like16 = False
    elif unlike == "17":
        x.like17 = False
    elif unlike == "18":
        x.like18 = False
    elif unlike == "19":
        x.like19 = False
    elif unlike == "20":
        x.like20 = False
    elif unlike == "21":
        x.like21 = False
    elif unlike == "22":
        x.like22 = False
    elif unlike == "23":
        x.like23 = False
    elif unlike == "24":
        x.like24 = False
    elif unlike == "25":
        x.like25 = False
    elif unlike == "26":
        x.like26 = False
    elif unlike == "27":
        x.like27 = False
    elif unlike == "28":
        x.like28 = False
    elif unlike == "29":
        x.like29 = False
    elif unlike == "30":
        x.like30 = False
    elif unlike == "31":
        x.like31 = False
    elif unlike == "32":
        x.like32 = False
    elif unlike == "33":
        x.like33 = False
    elif unlike == "34":
        x.like34 = False
    elif unlike == "35":
        x.like35 = False
    elif unlike == "36":
        x.like36 = False
    elif unlike == "37":
        x.like37 = False
    elif unlike == "38":
        x.like38 = False
    elif unlike == "39":
        x.like39 = False
    elif unlike == "40":
        x.like40 = False
    elif unlike == "41":
        x.like41 = False
    elif unlike == "42":
        x.like42 = False
    elif unlike == "43":
        x.like43 = False
    elif unlike == "44":
        x.like44 = False
    elif unlike == "45":
        x.like45 = False
    elif unlike == "46":
        x.like46 = False
    elif unlike == "47":
        x.like47 = False
    elif unlike == "48":
        x.like48 = False
    elif unlike == "49":
        x.like49 = False
    elif unlike == "50":
        x.like50 = False
    elif unlike == "51":
        x.like51 = False
    elif unlike == "52":
        x.like52 = False
    elif unlike == "53":
        x.like53 = False
    elif unlike == "54":
        x.like54 = False
    elif unlike == "55":
        x.like55 = False
    elif unlike == "56":
        x.like56 = False
    elif unlike == "57":
        x.like57 = False
    elif unlike == "58":
        x.like58 = False
    elif unlike == "59":
        x.like59 = False
    elif unlike == "60":
        x.like60 = False
    elif unlike == "61":
        x.like61 = False
    elif unlike == "62":
        x.like62 = False
    elif unlike == "63":
        x.like63 = False
    elif unlike == "64":
        x.like64 = False
    elif unlike == "65":
        x.like65 = False
    elif unlike == "66":
        x.like66 = False
    elif unlike == "67":
        x.like67 = False
    elif unlike == "68":
        x.like68 = False
    elif unlike == "69":
        x.like69 = False
    elif unlike == "70":
        x.like70 = False
    elif unlike == "71":
        x.like71 = False
    elif unlike == "72":
        x.like72 = False
    elif unlike == "73":
        x.like73 = False
    elif unlike == "74":
        x.like74 = False
    elif unlike == "75":
        x.like75 = False
    elif unlike == "76":
        x.like76 = False
    elif unlike == "77":
        x.like77 = False
    elif unlike == "78":
        x.like78 = False
    else:
        x.like79 = False

    db.session.commit() # save the changes to the database
    return redirect(url_for('main.favourite')) # redirect to the favourite() function

@main.route('/favourites') # EDIT
@login_required
def favourite():
    # query the database for the current user's id
    y = User.query.get(current_user.id)

    # return the favourites.html template with variables that will be referenced there
    return render_template('favourites.html', like1=y.like1, like2=y.like2, like3=y.like3, like4=y.like4, like5=y.like5, like6=y.like6, like7=y.like7, like8=y.like8, like9=y.like9, like10=y.like10, 
                            like11=y.like11, like12=y.like12, like13=y.like13, like14=y.like14, like15=y.like15, like16=y.like16, like17=y.like17, like18=y.like18, like19=y.like19, like20=y.like20, 
                            like21=y.like21, like22=y.like22, like23=y.like23, like24=y.like24, like25=y.like25, like26=y.like26, like27=y.like27, like28=y.like28, like29=y.like29, like30=y.like30, 
                            like31=y.like31, like32=y.like32, like33=y.like33, like34=y.like34, like35=y.like35, like36=y.like36, like37=y.like37, like38=y.like38, like39=y.like39, like40=y.like40, 
                            like41=y.like41, like42=y.like42, like43=y.like43, like44=y.like44, like45=y.like45, like46=y.like46, like47=y.like47, like48=y.like48, like49=y.like49, like50=y.like50, 
                            like51=y.like51, like52=y.like52, like53=y.like53, like54=y.like54, like55=y.like55, like56=y.like56, like57=y.like57, like58=y.like58, like59=y.like59, like60=y.like60, 
                            like61=y.like61, like62=y.like62, like63=y.like63, like64=y.like64, like65=y.like65, like66=y.like66, like67=y.like67, like68=y.like68, like69=y.like69, like70=y.like70, 
                            like71=y.like71, like72=y.like72, like73=y.like73, like74=y.like74, like75=y.like75, like76=y.like76, like77=y.like77, like78=y.like78, like79=y.like79)      

@main.route('/menu')
@login_required
def menu():
    return render_template('menu.html') # return the menu page

@main.route('/profile') 
@login_required
def profile():
    # assign the current user's credentials to variables
    name = current_user.name
    email = current_user.email
    username = current_user.username

    # return the profile.html template with variables that will be referenced there
    return render_template('profile.html', name=name, email=email, username=username)

@main.route('/edit') 
@login_required
def edit():
    # assign the current user's credentials to variables
    name = current_user.name
    email = current_user.email
    username = current_user.username

    # return the edit-profile.html template with variables that will be referenced there
    return render_template('edit-profile.html', name=name, email=email, username=username)

@main.route('/profedit', methods=['GET', 'POST'])
@login_required
def profile_change():
    if request.form == "GET": 
        return render_template('edit-profile.html') # return the edit profile page
    else: # if POST is requested (submit button pressed)
        if not request.form.get('name') or not request.form.get('user') or not request.form.get('email'): # if any of the input boxes are left empty
            flash('Please do not leave anything blank!')
            return redirect(url_for('main.edit')) # redirect to the edit() function
        else:
            # assign the user's inputs to variables
            name = request.form.get('name')
            email = request.form.get('email')
            username = request.form.get('user')
            # returns true if email or username already exist
            user = User.query.filter_by(email=email).first()
            user2 = User.query.filter_by(username=username).first()
            # if the email in the form is not the current user's and already exists:
            if email != current_user.email and user:
                flash('Email address already in use!')
                return redirect(url_for('main.profile_change'))
            # if the username in the form is not the current user's and already exists:
            elif username != current_user.username and user2:
                flash('Username already exists!')
                return redirect(url_for('main.profile_change'))
            else:
                # make sure the profile change is only for the current user
                id = current_user.id
                x = User.query.get(id)
                x.name = name
                x.email = email
                x.username = username
                db.session.commit() # save changes to the database
                
                return redirect(url_for('main.profile')) # redirect to the profile() function
                
@main.route('/submit', methods=['GET', 'POST'])
@login_required
def success():
    if request.form == "GET":
        return render_template('contact-us.html') # return the contact us page
    else: # if POST is requested (submit button pressed)
        if not request.form.get('fullname') or not request.form.get('emailaddress') or not request.form.get('message'): # if any input boxes are left empty
            flash('Please ensure you are filling in the form properly!')
            return redirect(url_for('main.contact')) # redirect to contact() function
        else:
            return render_template('confirm.html') # return the confirm page

@main.route('/contact')
@login_required
def contact():
    return render_template('contact-us.html') # return the contact us page

app = create_app() # initialize the flask app using the __init__.py function
if __name__ == '__main__':
    db.create_all(app=create_app()) # create the SQLite database
    app.run(debug=True) # run the flask app on debug mode