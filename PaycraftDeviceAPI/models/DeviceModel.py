from db import db # importing SQLAlchemy Object

class Device(db.Model):
    
    """ Referring the tablename along with column as required and create if not exists."""
    __tablename__ = 'devicedesc'
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer)
    password = db.Column(db.String(40))
    cpu_usage = db.Column(db.Float(precision=2))

    def __init__(self,device_id,password,cpu_usage):
        self.device_id = device_id
        self.password = password
        self.cpu_usage= cpu_usage

    def json(self):
        return {'device_id':self.device_id, 'cpu_usage':self.cpu_usage}

    @classmethod
    def get_by_id(cls,id_):
        return cls.query.filter_by(id= id_).first()

    @classmethod
    def get_by_device_id(cls, dev_id):
        return cls.query.filter_by(device_id=dev_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

       
