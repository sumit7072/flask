from samplesss.model import db,app,Hospital

from flask import render_template,request,session, redirect,url_for

@app.route("/hospital/welcome/")
def welcome_page():
    return render_template("sample.html",hospitals=Hospital.query.all(),
                           obj=Hospital(hid=0,hname="",hadr="",hfloors=0,hambulance=0))


@app.route("/hospital/save/",methods=["POST"])
def save_page():
    print('*'*30,request.form['hid'])
    print('html website.....user filled.......................',request.form)
    hospitals = Hospital.query.filter_by(hid=int(request.form['hid'])).first()
    print('hospitals:------------------- ', hospitals)
    if hospitals and int(request.form['hid'])>0:
        msg = 'already exist'

        return render_template("sample.html", hospitals=Hospital.query.all(),
                            msg=msg, obj=hospitals)
    else:

        hospitals=Hospital(hname=request.form['hname'],
            hadr=request.form['hadr'],
            hfloors=request.form['hfloors'],
            hambulance=request.form['hambulance'])#hid=request.form['hid']----auto generate
        db.session.add(hospitals)
        db.session.commit()
        msg = 'Hospital added succesfully....'

    # return render_template("sample.html", hospitals=Hospital.query.all(),
    #                                 msg=msg,
    #                            obj=Hospital.query.filter_by(hid=int(request.form['hid'])).first())
    return redirect(url_for('welcome_page'))

@app.route('/hospital/edit/',methods=['GET'])
def edit_method():
    # if int(request.form["hid"])>0:
    hospitals= Hospital.query.filter_by(hid=int(request.form['hid'])).first()
    if hospitals:
        hospitals.hname=request.form['hname']
        hospitals.hadr=request.form['hadr']
        hospitals.hfloors=request.form['hfloors']
        hospitals.hambulance=request.form['hambulance']
        db.session.commit()
        msg="Hospital updated succesfully....!"
        return render_template("sample.html", hospitals=Hospital.query.all(),
                           msg=msg,
                           obj=hospitals)

if __name__=="__main__":
    app.run(debug=True)

