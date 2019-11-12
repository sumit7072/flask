from  flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="mysql+pymysql://root:12345@localhost/pydb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)


class Hospital(db.Model):
    __tablename__="Hospital_Info"
    hid=db.Column("HOSPITAL_ID",db.Integer(), db.Sequence("seq_hosp_id") ,primary_key=True)
    hname=db.Column("HOSPITAL_NAME",db.String(80),unique=False,nullable=False)
    hadr=db.Column("HOSPITAL_ADDRESS",db.String(80),unique=False,nullable=False)
    hfloors=db.Column("HOSPITAL_FLOORS",db.Integer(),unique=False,nullable=False)
    hambulance=db.Column("HOSPITAL_AMBULANCE",db.Integer(),unique=False,nullable=False)

    def __str__(self):
        # if self.__dict__.__contains__('_sa_instance_state'):
            # self.__dict__.pop('_sa_instance_state')

        return f'\n{self.__dict__}'
    def __repr__(self):
        return str(self)

db.create_all()
# if __name__=="__main__":
    # app.run(debug=True)



def __repr__(self):
    return str(self)