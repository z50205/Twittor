from datetime import datetime
from twittor import db,login_manager

class Tweet (db.Model):
    id=db.Column(db.String(36),primary_key=True)
    body=db.Column(db.String(140))
    create_time=db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    all_files_name=db.Column(db.String(140))

    
    def __repr__(self):
        return 'id={},tweet={},create time={},user_id={},all_files_name={}'.format(
             self.id,self.body,self.create_time,self.all_files_name
        )