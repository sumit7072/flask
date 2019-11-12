from flask import request,render_template
from samplesss.model import db,app,Hospital


@app.route("/hospital/welcome/")
def welcome_page():
    return render_template("sample.html",hospitals=Hospital.query.all(),
                           hid=0)#obj=Hospital(hid=0,hname="",hadr="",hfloors=0,hambulance=0)

@app.route("/hospital/save/",methods=['POST'])
def hospital_save():
    print(request.form)
    # if int(request.form['hid'])>0:
    hospital=Hospital.query.filter_by(hid=int(request.form["hid"])).first()
    if hospital:
        hospital.hname=request.form['hname']
        hospital.hadr=request.form['hadr']
        hospital.hfloors=request.form['hfloors']
        hospital.hambulance=request.form['hambulance']
        db.session.commit()
        msg="Hospital updated succesfully....!"
    else:
        hospital=Hospital(hname=request.form["hname"],
                          hadr=request.form["hadr"],
                          hfloors=request.form['hfloors'],
                          hambulance=request.form['hambulance'])

        db.session.add(hospital)
        db.session.commit()
        msg="Hospital added succesfully...!"
    return render_template("sample.html",  hid=0,
                           msg=msg,hospitals=Hospital.query.all())

@app.route('/hospital/edit/<int:hid>',methods=['GET'])
def edit_method(hid):
    hospital=Hospital.query.filter_by(hid=hid).first()
    hospital.hname=hospital.hname
    hospital.hadr=hospital.hadr
    hospital.hfloors=hospital.hfloors
    hospital.hambulance=hospital.hambulance

    return render_template("sample.html",hospitals=Hospital.query.all(),hid=hospital.hid)

@app.route('/hospital/delete/<int:hid>',methods=['GET'])
def delete_method(hid):
    hospital = Hospital.query.filter_by(hid=hid).first()
    if hospital:
      db.session.delete(hospital)
      db.session.commit()
      msg="deleted......"
    return render_template("sample.html",hospitals=Hospital.query.all(),hid=0,msg=msg)





if __name__ == '__main__':
    app.run(debug=True)