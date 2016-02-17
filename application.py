from flask import Flask, render_template, request, session, flash, redirect, url_for, make_response, Response, current_app
from flask.ext.babel import Babel
from flask.ext.mail import Mail
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
     UserMixin, RoleMixin, login_required, roles_required, roles_accepted
from flask.ext.login import current_user
from flask.ext.mobility import Mobility
from forms import UserEditForm
import os, sys, datetime, random, math, csv
from datetime import timedelta
import tinys3
from functools import update_wrapper
from createPlot import *
basedir = os.path.abspath(os.path.dirname(__file__))

# Create app
application = Flask(__name__)
application.config['DEBUG'] = True
application.config['SECRET_KEY'] = 'super-secret'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
#application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://playiqdbinstance.ck2yn3omqkaf.eu-west-1.rds.amazonaws.com:3306/playiqdb?user=playiqdbadmin&password=playiqaws27'

application.config['DEFAULT_MAIL_SENDER'] = 'info@site.com'
application.config['SECURITY_REGISTERABLE'] = True
application.config['SECURITY_CONFIRMABLE'] = True
application.config['SECURITY_RECOVERABLE'] = True
application.config['UCALLOW'] = False
application.config['UCHASH'] = '3VTksGaneihE0RN'
application.config['EXPERTCODES']=['F4MD7GK','FUL3Q9D','V5RGFS9','XLDKDDY','MWVH6ZV','86E9KLP','94BKB6Z','27PTHPS','9M43LWH','F57EJHS','4X2948G','TET6E57','G4Q22BX','H7UK4VL','Z3J6HWK','J4E8Z3W','4BQ7MJK','SQ3E4T7','S7ZMB44','8EZJQTV','HNZ348F','CM9BKMH','C386ZJT','8WNX4GQ','BAUP2AU','9J29J68','TXBH69H','J2ZBVQG','M2ECCE9','XFWN97Y','DQWP88W','BLJSTPG','VNKA3BK','ZTK2STE','5ZSGEAC','XG9MUWC','C9T6ASQ','LMUFCNK','VXESCZA','QZTXQK7','7LBE92C','VKDT3MK','UC8W46N','6VMR2ZC','NSEECMD','QG5LU43','E7P6KQC','QZJ3FT7','83HT8N6','2GF2SRR','S6QNV7A','ZEHYP79','CPEG749','J3FWX42','N4DSSRC','2WCQ6VL','GGCX7VE','GQ82C2M','F5G3SUV','3JBHXQB','NCV3ETG','AZA7GG5','Y9EAYH8','TJGTSTH','XZ2JZ63','VEJT4N3','JNTPD56','ZAPH7PX','623WL4Z','6SQ2DM6','L9WFTZZ','K6PN2YE','4CQS848','NPEJ9EE','H6LTDLS','5EVG8VX','GREH3L5','SZ9TM3W','ALPVDL3','7RCD837','PNDNKLW','TNVFH9E','PS8ELTV','2HJLF9D','MFYXR8Y','LRY3QKE','XEENZEU','E5DCDDL','9VXFVNT','Q5XC5B9','UV3D63M','L2P4PMV','PH4XNLR','BPHXVXA','NF6WJ8M','B3LY6QQ','66W3VYU','UUNN8BB','Q5E5HQR','PF8B4WS']
application.config['PROTEAMCODES']=['IHUW399B','H3920HV8','NGX6BUHN','TN6GF2MB','YGNVIOMH','931A6MOU','MSHSFG2K','P8JZQOIC','BON8POQP','WGUCTOX1','X70D4GRN','AS9R7BF8','RM6O8HPI','4A6GL65Z','VTXG0209','LLKBSAOG','PVRXDA4D','LH3X7W2K','IJCEXVIU','U7CR3A1U','8NR4K8MK','NSP81RYK','UP6310UP','K4G1O4H6','5FOLZ5E7','3SPN8SIG','RGNVWBLH','TIBUWT2D','ALL5PVPZ','0GVQ5JWS','XU48K5B5','QCB8KQYW','ZNZ67H4I','QQ8B1JXE','VUO5865Z','SWJQWXUT','CR9SA9X0','NIOE4D13','Z4U9MP93','JUGTTDD5','WCICXN21','TZGLGR5W','FS3UIUKN','HZL082NB','M5OHXFDD','VRCJZDGF','04SHRU3T','KBP7DJVR','QZR2A4CL','FMA51QE5','UNIVG3VD','CR4OV2LI','LNHJM287','S1LTP9KX','8WUXVKRH','UTWDZ9CM','DD82V68C','09TXF9QA','8WWB71FW','PNK1VTLU','BLOZQLYT','IEA0T3V8','7YYMS4M7','Q53LP0JR','P1D699Y9','CEKPNPJM','9TL7NKHX','F00EL156','9CTA7QFD','8CC7L8GY','CT26L0XT','U145W7HX','FKPR9QAM','PR6FLP35','4PML41UM','05VSSFOS','MFNJM0UJ','36L7X99W','AQMZGKUT','VJL400F2','9RZGM09F','SKR20LCU','H1UTK14N','5MVUA72G','FXSW74RB','0SUTTV27','XNS44S3Q','60Q6I731','4OAZH092','EE7M6XN8','GQ7WYK9O','1RB69SAR','YBDDQSFZ','YHM0QW6K','YT4HHT1S','345YY31N','NY92XA00','1YXD2OG1','W6D6QYKN','0GXL045V','045OCFB2','YAKRZ09C','MAEXL96A','4AVJMGHL','2JOK4XVQ','CK0EO17S','VD11GJL9','2JM48DO9','YNJ2QX5Z','9K2L10LG','92Z41J25','B9SN107S','IMX8E3Z3','ARLUNVCV','K1RGPKHB','VSWLWLE3','Y09WU37V','K9CRBMY0','06Y693MJ','1K605ALL','2Y41F1E7','WZGD7CCU','MYOTERY1','TH2O9EQY','5OS1CFXG','YARTOUUA','2ROITV6H','CNAJRVG0','EKFIFYSA','2MATD2WH','51Q8FIWC','ZMYWR14Y','RUQ2XDCY','WISCXMY8','NMIR141B','52FG2P1K','P7RB2LF7','0Z9T1TW1','VJ7IMCRA','VTVAR7J2','KEGH9Y39','9LWVM742','P8O051DF','NKHR2WBH','SPLT1LX3','W2WRP3S4','UOY14NZ7','7W2GC82N','DHZ70OCM','WI0TWFPT','TMMG1GS3','9ZSP5VM6','6TGRJ9NM','ZXDVK3GT','X4HT3DPH','QVBR819R','MVSB2RSN','HFMN4IYX','V53FBHRY','NF9JT0WN','X2EZ7K71','AOEG1RK6','OC5K4C3S','OQLRAO0R','6HJ6FB1A','6VSQRD5M','M9GF1FVC','FM2SFS5O','023V8DP5','X6G1BMIV','JG1E0BYL','GK3G2TXM','AZDC4V6A','JYIFMHF0','QZHFC15F','BU43S320','ZAZE630G','3M0ILFCS','BK7F3I9V','FSU1LS4O','HVB8GFE0','0D8RDPZ1','PUBMUDRI','CXOK6PQD','4AAJF79U','42R8LV5C','NSX3J8VU','6L0O3UJG','TAM8YMCF','9GU6J53V','OMJW40UV','MQGDR9BK','D7SWNIHC','EJGO9M6F','EUWJITOF','01ATWZ4H','0THU473O','GBG8Y5B0','YOLV35SV','4IL7IMRC','2B8TOAQO','J1VVDSRS','58CG13KK','VIXDCORD','ZNTT3OUJ','RQ9URN0M','U0EJMMX1','JOPHCERW','6X39OSUB','K8G75I4C','ABKW47NX','LMY4UFTJ','546N5K87','OFSYSU77','Q1N1ZQC5','ASV8GM50','UPX7V97E','IKXF2DE4','Y4P1GWBD','DF6AZH9G','H5YVZRWL','X62YNK0C','HROB1SZ2','TQZ56H3A','XCDYLQCM','HQQ38R89','S1T6G100','PTH91WY3','FHRPC83L','69IMJ1GB','U5EUFPVV','L7EK0PZD','D8L1HXXS','1AT74UU3','K3NI2OR4','RX594IMG','C2N3ENJB','G8POQLXM','3JS7IV7X','9ZC13LJX','XHGOW1KD','XR0UOF2X','KQHHEWRY','ELZKL7S4','EKB36TJR','FJWOV6AV','F2IYSWHH','UYRK5LJG','33E95U2V','J2XXXXVD']
application.config['EXPERTGAMECODES']=['Dota 2','League of Legends','StarCraft II','Counter-Strike','StarCraft: Brood War','Counter-Strike: Global Offensive', 'WarCraft III', 'Smite', 'Counter-Strike: Source', 'World of WarCraft', 'Halo 3','OTHER']
application.config['MTURKCODES']=['MTURK14303803','MTURK77921264']
application.config['BATTLENETLEAGUES']=['OTHER','Grandmaster','Master','Diamond','Platinum','Gold','Silver','Bronze']
application.config['COUNTERSTRIKESKILLGROUP']=['OTHER','Silver I','Silver II','Silver III','Silver IV','Silver Elite','Silver Elite Master','Gold Nova I','Gold Nova II','Gold Nova III','Gold Nova Master','Master Guardian I','Master Guardian II','Master Guardian Elite','Distinguished Master Guardian','Legendary Eagle','Legendary Eagle Master','Supreme Master First Class','The Global Elite']

application.config['KICKSTARTERDONORS']=['toigaroun@gmail.com','redmooonman@yahoo.com','efepnr@gmail.com','collie_dogg@hotmail.com','runal@me.com','facebook@iandocherty.com','reseauaumodem@hotmail.com','sarushton107@gmail.com','mattisonenloe@summaxr.com','lmdyble@hotmail.com','robinwebb25@live.co.uk','schoenbaechler.kevin@hotmail.ch','papero91@hotmail.it','4msaustin4@gmail.com','adglass15@gmail.com','kenglass@alumni.upenn.edu','juliecharles@yahoo.com','jake-hartman@hotmail.com','jdblake100@gmail.com','Jessie.sefulu@gmail.com','curlyBJS@hotmail.com','lbcottler@ufl.edu','mrckirkwood@aol.com','cynthia.mundt@gmail.com','briglass2@gmail.com']

application.config.from_object('config.email')

application.config['DBPATH'] = os.path.join(basedir, 'app.db')

# Setup mail extension
mail = Mail(application)

# Setup babel
babel = Babel(application)
	
@babel.localeselector
def get_locale():
    override = request.args.get('lang')

    if override:
        session['lang'] = override

    rv = session.get('lang', 'en')
    return rv

# Create database connection object

db = SQLAlchemy(application)
migrate = Migrate(application, db)

manager = Manager(application)
manager.add_command('db', MigrateCommand)

# Define models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    nickname = db.Column(db.String(255))
    favcolor = db.Column(db.String(255))
    favshape = db.Column(db.String(255))
    favflower = db.Column(db.String(255))
    favband = db.Column(db.String(255)) #<<<new
    favfood = db.Column(db.String(255)) #<<<new
    userinfo_expert_completed = db.Column(db.Boolean())
    promocodes = db.Column(db.Text)
    mturkcompletioncode = db.Column(db.String(255))
    user_tasktable_ANT = db.relationship('tasktable_ANT', backref = 'author', lazy = 'dynamic')
    user_tasktable_LRN = db.relationship('tasktable_LRN', backref = 'author', lazy = 'dynamic')
    user_tasktable_PRC = db.relationship('tasktable_PRC', backref = 'author', lazy = 'dynamic')
    user_tasktable_SYM = db.relationship('tasktable_SYM', backref = 'author', lazy = 'dynamic')
    userinfo_expert = db.relationship('userinfo_expert', backref = 'author', lazy = 'dynamic')
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def __str__(self):
        return '<User id=%s email=%s>' % (self.id, self.email)

class tasktable_ANT(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    rawdata = db.Column(db.Text)
    driftrate = db.Column(db.Float)
    datetime = db.Column(db.DateTime())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __str__(self):
        return '<tasktable_ANT=%s user_id=%s>' % (self.id, self.user_id)

class tasktable_LRN(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    rawdata = db.Column(db.Text)
    accuracy = db.Column(db.Float)
    datetime = db.Column(db.DateTime())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __str__(self):
        return '<tasktable_LRN=%s user_id=%s>' % (self.id, self.user_id)

class tasktable_PRC(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    rawdata = db.Column(db.Text)
    accuracy = db.Column(db.Float)
    driftrate = db.Column(db.Float)
    datetime = db.Column(db.DateTime())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __str__(self):
        return '<tasktable_PRC=%s user_id=%s>' % (self.id, self.user_id)
        
class tasktable_SYM(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    rawdata = db.Column(db.Text)
    accuracy = db.Column(db.Float)
    driftrate = db.Column(db.Float)
    datetime = db.Column(db.DateTime())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __str__(self):
        return '<tasktable_SYM=%s user_id=%s>' % (self.id, self.user_id)
        
class userinfo_expert(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Float)   
    gender = db.Column(db.Integer)
    year_pro_play = db.Column(db.Float)
    game_primary = db.Column(db.Text)
    game_primary_id = db.Column(db.Integer)
    game_primary_hoursweek = db.Column(db.Float)
    game_primary_yearsplayed = db.Column(db.Float)
    
    game_primary_other = db.Column(db.Text)
    game_primary_other_level = db.Column(db.Text)
    game_primary_other_reason = db.Column(db.Text)
    
    game_secondary = db.Column(db.Text)
    game_secondary_id = db.Column(db.Integer)
    game_secondary_hoursweek = db.Column(db.Float)
    game_secondary_yearsplayed = db.Column(db.Float)
    
    specific_dota2_mmr = db.Column(db.Float)
    specific_dota_hero = db.Column(db.Text)
    
    specific_starcraft2_wcspoitns = db.Column(db.Float)   
    specific_starcraft2_battlenetleague = db.Column(db.Text)
    specific_starcraft2_battlenetleague_id = db.Column(db.Integer)          
    specific_starcraft2_battlenetdivision = db.Column(db.Text)
    specific_starcraft_races = db.Column(db.Text)

    specific_counterstrike_skillgroup = db.Column(db.Text)
    specific_counterstrike_skillgroup_id = db.Column(db.Integer)
    specific_counterstrike_teamrating = db.Column(db.Float)
    specific_counterstrike_weapon = db.Column(db.Text)
    
    datetime = db.Column(db.DateTime())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    


    
    def __str__(self):
        return '<userinfo_expert=%s user_id=%s>' % (self.id, self.user_id)
        
# Setup Flask-Security
#from db_manager import User, Role #this is probably wrong
    
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(application, user_datastore)

#db.create_all()

Mobility(application)

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator    
    
# Views
@application.route('/testpage')
@login_required
@roles_accepted('Admin')
def testpage():
    return render_template('testpage.html')

# Views
@application.route('/taskinputjs', methods=['GET', 'POST']) 
@login_required
@roles_accepted('Admin')
def taskinputjs():
    print "taskinputjs..."
    if request.method == 'POST':
		print "post"
		taskName = str(request.form.get('taskName'))
		taskScore = str(request.form.get('taskScore'))
		taskData = str(request.form.get('taskData'))

		print taskName
		print taskScore
		print taskData
		
		session['newscore'] = 1 # yes there's a new score
		session['newscore_name'] = taskName
		session['newscore_score'] = taskScore
		print 'hi'
		if taskName == 'ANT':
			print "analyzing ANT"
			instance_ANT = tasktable_ANT(rawdata=taskData, driftrate=taskScore, datetime=datetime.datetime.utcnow(),user_id=current_user.id)
			db.session.add(instance_ANT)
			db.session.commit()
		elif taskName == 'LRN':
			print "analyzing Learning"
			instance_LRN = tasktable_LRN(rawdata=taskData, accuracy=taskScore, datetime=datetime.datetime.utcnow(),user_id=current_user.id)
			db.session.add(instance_LRN)
			db.session.commit()
		elif taskName == 'PRC':
			print "analyzing Perception (Filter)"
			instance_PRC = tasktable_PRC(rawdata=taskData, driftrate=taskScore, datetime=datetime.datetime.utcnow(),user_id=current_user.id)
			db.session.add(instance_PRC)
			db.session.commit()
		elif taskName == 'SYM':
			print "analyzing Symmetry"
			instance_SYM = tasktable_SYM(rawdata=taskData, accuracy=taskScore, datetime=datetime.datetime.utcnow(),user_id=current_user.id)
			db.session.add(instance_SYM)
			db.session.commit()
		else:
			print "else!"

    return render_template('index.html')


@application.route('/DBbackup')
@login_required
@roles_required('Admin')
def DBbackup():
	
	print "TRYING TO UPLOAD DB TO S3"
	flash('Attempted to upload DB to AWS S3 bucket: playiqdbstore')
		
	do_DBbackup()
		
	return render_template('account.html')

def do_DBbackup():
	# Creating a simple connection
	print "inside do_DBbackup"
	conn = tinys3.Connection('AKIAJ4JQZZAXHPCIWPYQ','C46OJZXhrqdZCKOdx26D1p0vF9ag6JZj4qhlHreN', tls=True, endpoint='s3-eu-west-1.amazonaws.com') #access key, secret key
	
	fileattempt = os.path.join(basedir, 'app.db')
	nowdate = datetime.datetime.strftime(datetime.datetime.now(), '%Y_%m_%d_%H_%M_%S')
	print nowdate
	
	# Uploading a single file
	f = open(fileattempt,'rb')
	
	print conn.upload(nowdate+'_app.db',f,'playiqdbstore')
	print conn.get(nowdate+'_app.db','playiqdbstore')
	
	return

@application.route('/promocode', methods=['GET', 'POST']) 
@login_required
def promocode():
    print 'promocode:'
    if request.method == 'POST':
        submitButton = request.form['submitButton']	
        if submitButton == 'Remove Promo Code':
            promocode_attempt = request.form['promocode_attempt']
            current_user.promocodes =  current_user.promocodes.replace(promocode_attempt, "")
            db.session.commit()
        if submitButton == 'Submit Promo Code':
            promocode_attempt = request.form['promocode_attempt']
            print promocode_attempt
            if promocode_attempt in application.config['PROTEAMCODES']:
                expertuser_role = user_datastore.find_role("Expertuser")
                flash('Valid Promo Code')
                user_datastore.add_role_to_user(current_user, expertuser_role)
                if current_user.promocodes is None:
                    current_user.promocodes = promocode_attempt
                else:
                    current_user.promocodes += ';' + promocode_attempt
                db.session.commit()            
                
            elif promocode_attempt in application.config['EXPERTCODES']:
                #it's in the list of expert promo codes, so check other users to see if used already
                keepsearch = 1
                promocode_found_in_other_user = 0
                userid = 0
                numusers = User.query.count()
                expertuser_role = user_datastore.find_role("Expertuser")
                while keepsearch == 1:
                    try:
                        promocode_other_user = user_datastore.get_user(str(userid)).promocodes
                        if promocode_attempt in promocode_other_user:                            
                            if user_datastore.get_user(str(userid)).has_role('Expertuser'):
                                #found a user who has promocode, and is an active expertuser
                                print 'found a user who has promocode, and is an active expertuser'
                                promocode_found_in_other_user = 1
                                keepsearch = 0
                        userid +=1
                    except:
                        if userid > numusers+1:
                            keepsearch = 0
                        else:
                            userid += 1
                if promocode_found_in_other_user == 1:
                    flash('Promo Code already used')
                    print 'Promo Code already used'
                else:
                    flash('Valid Expert User Promo Code')
                    user_datastore.add_role_to_user(current_user, expertuser_role)
                    if current_user.promocodes is None:
                        current_user.promocodes = promocode_attempt
                    else:
                        current_user.promocodes += ';' + promocode_attempt
                    
                    db.session.commit()
                    
            elif promocode_attempt in application.config['MTURKCODES']:
                mturkuser_role = user_datastore.find_role("Mturkuser")
                flash('Valid Promo Code, Welcome!')
                user_datastore.add_role_to_user(current_user, mturkuser_role)
                if current_user.promocodes is None:
                    current_user.promocodes = promocode_attempt
                else:
                    current_user.promocodes += ';' + promocode_attempt
                db.session.commit() 
                
            elif promocode_attempt == 'KICKSTARTPLAYIQ':
                print "hi KICKSTARTPLAYIQ"
                if current_user.email in application.config['KICKSTARTERDONORS']: # they are a donor w/ right promocode
                    user_role = user_datastore.find_role("User")
                    flash('Valid Promo Code! Welcome, and thank you for your support!')
                    user_datastore.add_role_to_user(current_user, user_role)
                    if current_user.promocodes is None:
                        current_user.promocodes = promocode_attempt
                    else:
                        current_user.promocodes += ';' + promocode_attempt
                    db.session.commit()  
                
            else:
                flash('Invalid Promo Code')
                
    return redirect(url_for('account'))
	
@application.route('/createroles')
@login_required
@roles_required('Admin')
def createroles():
    print "HI ADMIN"		
    print "attempting to create roles"
    flash('Attempting to create roles.')

    #print user_datastore.create_role(name='Admin', description='Administrator')
    #print user_datastore.create_role(name='User', description='User can access basic tests')
    #print user_datastore.create_role(name='Subuser', description='Sub-User not fully registered yet')
    #user_datastore.create_role(name='Expertuser', description='Part of the Expertise data collection user group')
    user_datastore.create_role(name='Mturkuser', description='an MTurk user')
    db.session.commit()
        
    return render_template('account.html')

@application.route('/deleteexpertuserinfo', methods=['GET', 'POST']) 
@login_required
@roles_required('Admin')
def deleteexpertuserinfo():
    if request.method == 'POST':
        submitButton = request.form['submitButton']	
        if submitButton == 'Delete Row':
            row_to_delete = request.form['row_to_delete']
            
            #flash('Deleted row' + row_to_delete)
            
            get_userinfo_expert = userinfo_expert.query.all() 
            
            try:
                userinfo_expert.query.filter(userinfo_expert.id == int(row_to_delete)).delete()
                db.session.commit()
            except:
                "delete didn't work..."
    
    return render_template('account.html')
    
@application.route('/createuser', methods=['GET', 'POST']) 
@login_required
@roles_required('Admin')
def createuser():

    if request.method == 'POST':
        submitButton = request.form['submitButton']	
        if submitButton == 'Create User':
            username_to_create = request.form['username_to_create']
            password_to_create = request.form['password_to_create']
            print "creating user"
            
            if username_to_create and password_to_create:
                db.create_all()
                user_datastore.create_user(email=username_to_create, password=password_to_create, confirmed_at=datetime.datetime.now())
                db.session.commit()
                flash('Created user: ' + username_to_create)
        elif submitButton == 'Delete User':
            username_to_delete = request.form['username_to_create']
            print "deleting user"
            
            if username_to_delete:
                db.create_all()
                user_datastore.delete_user(user_datastore.get_user(username_to_delete))
                db.session.commit()
                flash('Deleted user: ' + username_to_delete)
                
    
    return redirect(url_for('account'))
    
@application.route('/assignroles', methods=['GET', 'POST']) 
@login_required
@roles_required('Admin')
def assignroles():

    if request.method == 'POST':
        submitButton = request.form['submitButton']	
        if submitButton == 'Assign Role' or submitButton == 'Remove Role':
            username_to_assign = request.form['username_to_assign']
            role_to_assign = request.form['role_to_assign']
            print "HI ADMIN"		
            print "attempting to edit roles"
            print username_to_assign
            print role_to_assign
                    
            admin_role = user_datastore.find_role("Admin")
            fulluser_role = user_datastore.find_role("User")
            expertuser_role = user_datastore.find_role("Expertuser")
            
            if username_to_assign and role_to_assign:
                
                #user_datastore.add_role_to_user(current_user, admin_role)
                #user_datastore.add_role_to_user(current_user, fulluser_role)
            
                if submitButton == 'Assign Role':
                    flash('Attempting to assign role: <' + role_to_assign + '> to user: <' + username_to_assign + '>' )
                    if role_to_assign == "Admin":
                        user_datastore.add_role_to_user(user_datastore.get_user(username_to_assign), admin_role)
                    elif role_to_assign == "User":
                        user_datastore.add_role_to_user(user_datastore.get_user(username_to_assign), fulluser_role)
                    elif role_to_assign == "Expertuser":
                        user_datastore.add_role_to_user(user_datastore.get_user(username_to_assign), expertuser_role)
                    else:
                        print "not a role"
                elif submitButton == 'Remove Role':
                    flash('Attempting to remove role: <' + role_to_assign + '> from user: <' + username_to_assign + '>' )
                    if role_to_assign == "Admin":
                        user_datastore.remove_role_from_user(user_datastore.get_user(username_to_assign), admin_role)
                    elif role_to_assign == "User":
                        user_datastore.remove_role_from_user(user_datastore.get_user(username_to_assign), fulluser_role)
                    elif role_to_assign == "Expertuser":
                        user_datastore.remove_role_from_user(user_datastore.get_user(username_to_assign), expertuser_role)
                    else:
                        print "not a role"
                else:
                    print "not a button"
            
                #user_datastore.add_role_to_user(user_datastore.get_user('bradley.c.love@gmail.com'), admin_role)
                #user_datastore.add_role_to_user(user_datastore.get_user('bradley.c.love@gmail.com'), fulluser_role)
                #user_datastore.add_role_to_user(user_datastore.get_user('playiq.user@gmail.com'), fulluser_role)
            
                db.session.commit()
            
            #print 'Get list of users:'
            
            #userid = 1
            #keeptry = 1
            #while keeptry == 1:
            #	try:
            #		print user_datastore.get_user(str(userid)).email
            #		userid += 1
            #	except:
            #		print "EOL"
            #		keeptry = 0
                
            return redirect(url_for('account'))

@application.route('/'+application.config['UCHASH'])
def ucallowthru():
	print "allowing thru..."
	session['counter']=0
	#application.config['UCALLOW'] = True
	return render_template('index.html')

@application.route('/devlogout')
def devlogout():
	application.config['UCALLOW'] = False
	return render_template('comingsoon.html')
	
@application.route('/')
def home():
    session['flowmessage'] = 'restart'
    session['newscore'] = 0
    session['newscore_name'] = ''
    session['newscore_score'] = ''
	#if application.config['UCALLOW'] == True:
    try:
		session['counter'] += 1
    except KeyError:
		session['counter'] = 1
    now_tmp = datetime.datetime.now()
    
    if datetime.time(12, 00) <= now_tmp.time() <= datetime.time(13, 00):
        if random.random() < .05:
            print('doing DB backup................!')
            do_DBbackup()
    
    return render_template('index.html',session=session, showsidebar=1)
	#else:
	#	session['counter'] = 0
	#	return render_template('comingsoon.html')

@application.route('/testflow_mturk', methods = ['GET', 'POST'])
@login_required
@roles_accepted('Mturkuser','Admin')    
def testflow_mturk():
    expert_info_completed = current_user.userinfo_expert_completed

    return render_template('testflow_mturk.html',expert_info_completed=expert_info_completed)

@application.route('/testflow', methods = ['GET', 'POST'])
@login_required
@roles_accepted('Mturkuser','Expertuser','Admin')
#@roles_accepted('Expertuser','Admin')
def testflow():

    userAgentString = request.headers.get('User-Agent')
    user_agent = request.user_agent
    #open comparison data file 
    #print "trying to open Amateurdata.csv"
    #Amateurdata_ANT = []
    #Amateurdata_PRC = []
    #Amateurdata_LRN = []
    #Amateurdata_SYM = []
    
    #with open('static\\analysis_resources\\Amateurdata.csv', 'rb') as csvfile:
    #   spamreader = csv.reader(csvfile)
    #    i = 0
    #    for row in spamreader:
    #        i += 1
    #        if i > 1: #skip header
    #            Amateurdata_ANT.append(float(row[0]))
    #            Amateurdata_PRC.append(float(row[1]))
    #            Amateurdata_LRN.append(float(row[2]))
    #            Amateurdata_SYM.append(float(row[3]))

    Amateurdata_ANT,Amateurdata_PRC,Amateurdata_LRN,Amateurdata_SYM = load_amateurdata()
    
    c_user = User.query.get(current_user.id) #current user
    user_ANT = c_user.user_tasktable_ANT.all()
    user_LRN = c_user.user_tasktable_LRN.all()
    user_PRC = c_user.user_tasktable_PRC.all()
    user_SYM = c_user.user_tasktable_SYM.all()

    user_ANT_prct = None
    user_LRN_prct = None
    user_PRC_prct = None
    user_SYM_prct = None

    expert_info_completed = current_user.userinfo_expert_completed

    test_missing = False
    if not user_ANT:
        user_ANT = []
        test_missing = True
    else:
        if user_ANT[0].rawdata:
            user_ANT_rawdata = user_ANT[0].rawdata
            user_ANT_rawscore = user_ANT_rawdata.split(',')[-1]
            user_ANT_prct = int(percentileofscore(Amateurdata_ANT,float(user_ANT_rawscore)))
    if not user_LRN:
        user_LRN = []
        test_missing = True
    else:
        if user_LRN[0].rawdata:
            user_LRN_rawdata = user_LRN[0].rawdata
            user_LRN_rawscore = user_LRN_rawdata.split(',')[-1]
            user_LRN_prct = int(percentileofscore(Amateurdata_LRN,float(user_LRN_rawscore)))
    if not user_PRC:
        user_PRC = []	
        test_missing = True
    else:
        if user_PRC[0].rawdata:
            user_PRC_rawdata = user_PRC[0].rawdata
            user_PRC_rawscore = user_PRC_rawdata.split(',')[-1]            
            user_PRC_prct = int(percentileofscore(Amateurdata_PRC,float(user_PRC_rawscore)))
    if not user_SYM:
        user_SYM = []
        test_missing = True
    else:
        if user_SYM[0].rawdata:
            user_SYM_rawdata = user_SYM[0].rawdata
            user_SYM_rawscore = user_SYM_rawdata.split(',')[-2]            
            user_SYM_prct = int(percentileofscore(Amateurdata_SYM,float(user_SYM_rawscore)))

    mturk_code = None
    if test_missing == False:
        if current_user.mturkcompletioncode == None:
            mturk_code = str(int(math.floor(100000 + random.random()*(999999 - 100000 + 1))))
            current_user.mturkcompletioncode = mturk_code
            db.session.commit()
        else:
            mturk_code = current_user.mturkcompletioncode
        print mturk_code
        
    UsingQupZilla = 0
    if 'QupZilla' in user_agent.string:
        UsingQupZilla = 1
    
    return render_template('testflow.html',mturk_code=mturk_code,expert_info_completed=expert_info_completed,user_ANT=user_ANT,user_LRN=user_LRN,user_PRC=user_PRC,user_SYM=user_SYM,user_ANT_prct=user_ANT_prct,user_LRN_prct=user_LRN_prct,user_PRC_prct=user_PRC_prct,user_SYM_prct=user_SYM_prct,user_agent=user_agent,UsingQupZilla=UsingQupZilla)

def percentileofscore(scorelist, score):
    
    cnt_LT = 0
    cnt_EQ = 0
    cnt = 0
    for s in scorelist:
        cnt += 1
        if s < score:
            cnt_LT += 1
        elif score == s:
            cnt_EQ += 1
        
        percentile = ((cnt_LT + (0.5 * cnt_EQ)) / cnt) * 100
    print percentile
    return percentile
        
        
@application.route('/testflow_userinfo', methods = ['GET', 'POST'])
@login_required
@roles_accepted('Mturkuser', 'Expertuser','Admin')
def testflow_userinfo():

    c_user = User.query.get(current_user.id) #current user
    c_userinfo_expert = c_user.userinfo_expert.all()
    
    if request.method == 'POST':
        print "HIIIIIIIIIIII"
        format_problem = False
        required_missing_problem = False
        submitButton = request.form['submitButton']	
        if submitButton == 'Submit Information':
            print "submitted"
            
            game_secondary_id = None
            
            age_raw = request.form['age']
            age = None
            if age_raw:
                try:
                    age = float(age_raw)
                except:
                    print "fp01"
                    format_problem = True
                
            gender_raw = request.form['gender']
            gender = 0
            if gender_raw == 'female':
                gender = 2
            elif gender_raw == 'male':
                gender = 1
            
            primarygame_raw =  request.form.get('primarygame')
                
            if primarygame_raw:
                game_primary_id = int(application.config['EXPERTGAMECODES'].index(primarygame_raw))
            else:
                primarygame_raw = None
                game_primary_id = None
            
            game_primary_other = None
            game_primary_other_level = None
            game_primary_other_reason = None

            if primarygame_raw == 'OTHER': #OTHER
                primarygame_raw = request.form.get('game_primary_other')
                game_primary_other = primarygame_raw
                
                game_primary_other_level = request.form.get('game_primary_other_level')
                if game_primary_other_level == "": game_primary_other_level = None
                game_primary_other_reason = request.form.get('game_primary_other_reason')
                if game_primary_other_reason == "": game_primary_other_reason = None

            
            year_pro_play = request.form['year_pro_play']
            if year_pro_play:
                try:
                    year_pro_play = float(year_pro_play)
                except:
                    print "fp02"
                    format_problem = True
            else:
                year_pro_play = None
                
            game_primary_hoursweek = request.form['game_primary_hoursweek']
            if game_primary_hoursweek:
                try:
                    game_primary_hoursweek = float(game_primary_hoursweek)
                except:
                    print "fp03"
                    format_problem = True
            else:
                game_primary_hoursweek = None
                
            game_primary_yearsplayed = request.form['game_primary_yearsplayed']
            if game_primary_yearsplayed:
                try:
                    game_primary_yearsplayed = float(game_primary_yearsplayed)
                except:
                    print "fp04"
                    format_problem = True
            else:
                game_primary_yearsplayed = None
                
            game_secondary = request.form['game_secondary']    
            if game_secondary == "":
                game_secondary = None
            
            game_secondary_hoursweek = request.form['game_secondary_hoursweek']
            if game_secondary_hoursweek:
                try:
                    game_secondary_hoursweek = float(game_secondary_hoursweek)
                except:
                    format_problem = True
            else:
                game_secondary_hoursweek = None
                
            game_secondary_yearsplayed = request.form['game_secondary_yearsplayed']
            if game_secondary_yearsplayed:
                try:
                    game_secondary_yearsplayed = float(game_secondary_yearsplayed)
                except:
                    format_problem = True
            else:
                game_secondary_yearsplayed = None
             
                        
            # specific_starcraft2_wcspoitns = request.form['specific_starcraft2_wcspoitns']
            
            # if specific_starcraft2_wcspoitns:
                # try:
                    # specific_starcraft2_wcspoitns = float(specific_starcraft2_wcspoitns)
                # except:
                    # format_problem = True
            # else:
                # specific_starcraft2_wcspoitns = None
                
            # specific_counterstrike_teamrating = request.form['specific_counterstrike_teamrating']
            # if specific_counterstrike_teamrating:
                # try:
                    # specific_counterstrike_teamrating = float(specific_counterstrike_teamrating)
                # except:
                    # format_problem = True
            # else:
                # specific_counterstrike_teamrating = None
            
            #DOTA
            specific_dota2_mmr = request.form['specific_dota2_mmr']
            if specific_dota2_mmr:
                try:
                    specific_dota2_mmr = float(specific_dota2_mmr)
                except:
                    format_problem = True
            else:
                specific_dota2_mmr = None
            
            specific_dota_hero = None
            if current_user.has_role('Mturkuser'):
                specific_dota_hero =  request.form.get('specific_dota_hero')
                if specific_dota_hero == "": specific_dota_hero = None 
                    
            #STARCRAFT
            specific_starcraft2_battlenetleague =  request.form.get('specific_starcraft2_battlenetleague')
            if specific_starcraft2_battlenetleague:
                specific_starcraft2_battlenetleague_id = int(application.config['BATTLENETLEAGUES'].index(specific_starcraft2_battlenetleague))
                if specific_starcraft2_battlenetleague_id == 0: #OTHER
                    specific_starcraft2_battlenetleague = request.form.get('specific_starcraft2_battlenetleague_other')            
            else:
                specific_starcraft2_battlenetleague = None
                specific_starcraft2_battlenetleague_id = None

            specific_starcraft2_battlenetdivision = request.form['specific_starcraft2_battlenetdivision']
            if specific_starcraft2_battlenetdivision == "": specific_starcraft2_battlenetdivision = None
            
            specific_starcraft_races = None
            if current_user.has_role('Mturkuser'):
                specific_starcraft_races =  request.form.get('specific_starcraft_races')
                if specific_starcraft_races == "": specific_starcraft_races = None 
                
            #COUNTER-STRIKE
            specific_counterstrike_skillgroup =  request.form.get('specific_counterstrike_skillgroup')                
            if specific_counterstrike_skillgroup:
                specific_counterstrike_skillgroup_id = int(application.config['COUNTERSTRIKESKILLGROUP'].index(specific_counterstrike_skillgroup))
                if specific_counterstrike_skillgroup_id == 0: #OTHER
                    specific_counterstrike_skillgroup = request.form.get('specific_counterstrike_skillgroup_other')                    
            else:
                specific_counterstrike_skillgroup = None
                specific_counterstrike_skillgroup_id = None                
            
            specific_counterstrike_weapon = None
            if current_user.has_role('Mturkuser'):
                specific_counterstrike_weapon =  request.form.get('specific_counterstrike_weapon')
                if specific_counterstrike_weapon == "": specific_counterstrike_weapon = None 
                
            #Test if missing info for Mturker
            
            if current_user.has_role('Mturkuser'):
                #Other
                print "game_primary_id"
                print game_primary_id
                if game_primary_id == 11:    
                    if game_primary_other == "" or game_primary_other_level is None or game_primary_other_reason is None:
                        required_missing_problem = True
                
                #Dota2
                if game_primary_id == 0 and specific_dota_hero is None: required_missing_problem = True
                
                #StarCraft
                if game_primary_id == 2:
                    if specific_starcraft_races is None: required_missing_problem = True
                
                #C-S
                if game_primary_id in (3, 5, 8):
                    if specific_counterstrike_weapon is None: required_missing_problem = True 
                
                
            print "NEW EXPERT INFO **************"
            print specific_starcraft2_battlenetleague
            print specific_starcraft2_battlenetleague_id            
            print specific_counterstrike_skillgroup
            print specific_counterstrike_skillgroup_id
            
            
            if game_primary_id == None or year_pro_play == None or game_primary_hoursweek == None or game_primary_yearsplayed == None:
                required_missing_problem = True
            #elif game_secondary == True and (game_secondary_hoursweek == None and game_secondary_yearsplayed == None):
                required_missing_problem = True

            if game_secondary == None or game_secondary_hoursweek == None and game_secondary_yearsplayed == None:
                required_missing_problem = True
            
            print "required_missing_problem = "
            print required_missing_problem
            if format_problem == True:
                #issue with converting from floats
                flash('There was a formatting issue -- make sure numbers contain only numeric characters and decimal point')
                # return render_template('testflow_userinfo.html',age_raw=age_raw,gender=gender,game_primary_id=game_primary_id, year_pro_play=year_pro_play, game_primary_hoursweek=game_primary_hoursweek, game_primary_yearsplayed=game_primary_yearsplayed, game_secondary=game_secondary, game_secondary_hoursweek=game_secondary_hoursweek, game_secondary_yearsplayed=game_secondary_yearsplayed, specific_dota2_mmr=specific_dota2_mmr, specific_starcraft2_wcspoitns=specific_starcraft2_wcspoitns, specific_counterstrike_teamrating=specific_counterstrike_teamrating)
                return render_template('testflow_userinfo.html',age_raw=age_raw,gender=gender,game_primary_id=game_primary_id, year_pro_play=year_pro_play, game_primary_hoursweek=game_primary_hoursweek, game_primary_yearsplayed=game_primary_yearsplayed, game_secondary=game_secondary, game_secondary_hoursweek=game_secondary_hoursweek, game_secondary_yearsplayed=game_secondary_yearsplayed, specific_dota2_mmr=specific_dota2_mmr, specific_starcraft2_battlenetleague=specific_starcraft2_battlenetleague, specific_starcraft2_battlenetleague_id=specific_starcraft2_battlenetleague_id, specific_counterstrike_skillgroup=specific_counterstrike_skillgroup, specific_counterstrike_skillgroup_id=specific_counterstrike_skillgroup_id, specific_starcraft2_battlenetdivision=specific_starcraft2_battlenetdivision, specific_dota_hero=specific_dota_hero,specific_starcraft_races=specific_starcraft_races,specific_counterstrike_weapon=specific_counterstrike_weapon,game_primary_other=game_primary_other,game_primary_other_level=game_primary_other_level,game_primary_other_reason=game_primary_other_reason)
            elif required_missing_problem == True:
                #not all fields filled in
                flash('Please fill in all required fields')
                # return render_template('testflow_userinfo.html',age_raw=age_raw,gender=gender,game_primary_id=game_primary_id, year_pro_play=year_pro_play, game_primary_hoursweek=game_primary_hoursweek, game_primary_yearsplayed=game_primary_yearsplayed, game_secondary=game_secondary, game_secondary_hoursweek=game_secondary_hoursweek, game_secondary_yearsplayed=game_secondary_yearsplayed, specific_dota2_mmr=specific_dota2_mmr, specific_starcraft2_wcspoitns=specific_starcraft2_wcspoitns, specific_counterstrike_teamrating=specific_counterstrike_teamrating)
                return render_template('testflow_userinfo.html',age_raw=age_raw,gender=gender,game_primary_id=game_primary_id, year_pro_play=year_pro_play, game_primary_hoursweek=game_primary_hoursweek, game_primary_yearsplayed=game_primary_yearsplayed, game_secondary=game_secondary, game_secondary_hoursweek=game_secondary_hoursweek, game_secondary_yearsplayed=game_secondary_yearsplayed, specific_dota2_mmr=specific_dota2_mmr, specific_starcraft2_battlenetleague=specific_starcraft2_battlenetleague, specific_starcraft2_battlenetleague_id=specific_starcraft2_battlenetleague_id, specific_counterstrike_skillgroup=specific_counterstrike_skillgroup, specific_counterstrike_skillgroup_id=specific_counterstrike_skillgroup_id, specific_starcraft2_battlenetdivision=specific_starcraft2_battlenetdivision,specific_dota_hero=specific_dota_hero,specific_starcraft_races=specific_starcraft_races,specific_counterstrike_weapon=specific_counterstrike_weapon,game_primary_other=game_primary_other,game_primary_other_level=game_primary_other_level,game_primary_other_reason=game_primary_other_reason)
            else:
                #all is good, save data
                current_user.userinfo_expert_completed = True
                db.session.commit()
                
                # instance_userinfo_expert = userinfo_expert(age = age, gender = gender, year_pro_play = year_pro_play, game_primary = primarygame_raw, game_primary_id = game_primary_id, game_primary_hoursweek = game_primary_hoursweek, game_primary_yearsplayed = game_primary_yearsplayed, game_secondary = game_secondary, game_secondary_id = game_secondary_id, game_secondary_hoursweek = game_secondary_hoursweek, game_secondary_yearsplayed = game_secondary_yearsplayed, specific_dota2_mmr = specific_dota2_mmr, specific_starcraft2_wcspoitns = specific_starcraft2_wcspoitns, specific_counterstrike_teamrating = specific_counterstrike_teamrating, datetime = datetime.datetime.now(), user_id = current_user.id)
                instance_userinfo_expert = userinfo_expert(age = age, gender = gender, year_pro_play = year_pro_play, game_primary = primarygame_raw, game_primary_id = game_primary_id, game_primary_hoursweek = game_primary_hoursweek, game_primary_yearsplayed = game_primary_yearsplayed, game_secondary = game_secondary, game_secondary_id = game_secondary_id, game_secondary_hoursweek = game_secondary_hoursweek, game_secondary_yearsplayed = game_secondary_yearsplayed, specific_dota2_mmr = specific_dota2_mmr, specific_starcraft2_battlenetleague=specific_starcraft2_battlenetleague, specific_starcraft2_battlenetleague_id=specific_starcraft2_battlenetleague_id, specific_counterstrike_skillgroup=specific_counterstrike_skillgroup, specific_counterstrike_skillgroup_id=specific_counterstrike_skillgroup_id, specific_starcraft2_battlenetdivision=specific_starcraft2_battlenetdivision, specific_dota_hero=specific_dota_hero,specific_starcraft_races=specific_starcraft_races,specific_counterstrike_weapon=specific_counterstrike_weapon,game_primary_other=game_primary_other,game_primary_other_level=game_primary_other_level,game_primary_other_reason=game_primary_other_reason, datetime = datetime.datetime.now(), user_id = current_user.id)

                db.session.add(instance_userinfo_expert)
                db.session.commit()
            
                c_user = User.query.get(current_user.id) #current user
                c_userinfo_expert = c_user.userinfo_expert.all() 
                
                
                if current_user.has_role('Mturkuser'):
                    return redirect(url_for('testflow_mturk'))
                else:
                    return redirect(url_for('testflow'))

    else:
        print "NOOOOOOOOO"
        
        if c_user.userinfo_expert_completed == True:   
            print "already completed testflow_userinfo"
            user_expertinfo = c_user.userinfo_expert.all()
            user_expertinfo[-1].age
            # [-1] because we are taking the last (most recent) entry in the expert user table, and using that one to get previous responses
            age_raw=user_expertinfo[-1].age
            gender=user_expertinfo[-1].gender
            game_primary_id=user_expertinfo[-1].game_primary_id
            year_pro_play=user_expertinfo[-1].year_pro_play
            game_primary_hoursweek=user_expertinfo[-1].game_primary_hoursweek
            game_primary_yearsplayed=user_expertinfo[-1].game_primary_yearsplayed
            
            game_primary_other=user_expertinfo[-1].game_primary_other
            game_primary_other_level=user_expertinfo[-1].game_primary_other_level
            game_primary_other_reason=user_expertinfo[-1].game_primary_other_reason
            
            game_secondary=user_expertinfo[-1].game_secondary
            game_secondary_hoursweek=user_expertinfo[-1].game_secondary_hoursweek
            game_secondary_yearsplayed=user_expertinfo[-1].game_secondary_yearsplayed
            specific_dota2_mmr=user_expertinfo[-1].specific_dota2_mmr            
            # specific_starcraft2_wcspoitns=user_expertinfo[-1].specific_starcraft2_wcspoitns
            # specific_counterstrike_teamrating=user_expertinfo[-1].specific_counterstrike_teamrating
            specific_starcraft2_battlenetleague=user_expertinfo[-1].specific_starcraft2_battlenetleague
            specific_starcraft2_battlenetleague_id=user_expertinfo[-1].specific_starcraft2_battlenetleague_id
            specific_counterstrike_skillgroup=user_expertinfo[-1].specific_counterstrike_skillgroup
            specific_counterstrike_skillgroup_id=user_expertinfo[-1].specific_counterstrike_skillgroup_id
            specific_starcraft2_battlenetdivision=user_expertinfo[-1].specific_starcraft2_battlenetdivision
            
            specific_dota_hero=user_expertinfo[-1].specific_dota_hero
            specific_starcraft_races=user_expertinfo[-1].specific_starcraft_races
            specific_counterstrike_weapon=user_expertinfo[-1].specific_counterstrike_weapon
            
            
        else:       
            age_raw=None
            gender=0
            game_primary_id=0
            year_pro_play=None
            game_primary_hoursweek=None
            game_primary_yearsplayed=None
            
            game_primary_other=None
            game_primary_other_level=None
            game_primary_other_reason=None

            game_secondary=None
            game_secondary_hoursweek=None
            game_secondary_yearsplayed=None
            specific_dota2_mmr=None
            # specific_starcraft2_wcspoitns=None
            # specific_counterstrike_teamrating=None
            specific_starcraft2_battlenetleague=None
            specific_starcraft2_battlenetleague_id=None
            specific_counterstrike_skillgroup=None
            specific_counterstrike_skillgroup_id=None
            specific_starcraft2_battlenetdivision=None
            
            specific_dota_hero=None
            specific_starcraft_races=None
            specific_counterstrike_weapon=None

        # return render_template('testflow_userinfo.html',age_raw=age_raw,gender=gender,game_primary_id=game_primary_id, year_pro_play=year_pro_play, game_primary_hoursweek=game_primary_hoursweek, game_primary_yearsplayed=game_primary_yearsplayed, game_secondary=game_secondary, game_secondary_hoursweek=game_secondary_hoursweek, game_secondary_yearsplayed=game_secondary_yearsplayed, specific_dota2_mmr=specific_dota2_mmr, specific_starcraft2_wcspoitns=specific_starcraft2_wcspoitns, specific_counterstrike_teamrating=specific_counterstrike_teamrating)
        return render_template('testflow_userinfo.html',age_raw=age_raw,gender=gender,game_primary_id=game_primary_id, year_pro_play=year_pro_play, game_primary_hoursweek=game_primary_hoursweek, game_primary_yearsplayed=game_primary_yearsplayed, game_secondary=game_secondary, game_secondary_hoursweek=game_secondary_hoursweek, game_secondary_yearsplayed=game_secondary_yearsplayed, specific_dota2_mmr=specific_dota2_mmr, specific_starcraft2_battlenetleague=specific_starcraft2_battlenetleague, specific_starcraft2_battlenetleague_id=specific_starcraft2_battlenetleague_id, specific_counterstrike_skillgroup=specific_counterstrike_skillgroup, specific_counterstrike_skillgroup_id=specific_counterstrike_skillgroup_id, specific_starcraft2_battlenetdivision=specific_starcraft2_battlenetdivision, specific_dota_hero=specific_dota_hero,specific_starcraft_races=specific_starcraft_races,specific_counterstrike_weapon=specific_counterstrike_weapon,game_primary_other=game_primary_other,game_primary_other_level=game_primary_other_level,game_primary_other_reason=game_primary_other_reason)


@application.route('/account')
@login_required
def account():
    print "account:"
    userlist = []
    userlist_userid = []
    userlist_datetime = []
    userlist_roles = []
    userlist_promocodes = []
    userlist_expertinfo = []
    userlist_mturkcompletioncodes = []
    
    get_userinfo_expert = []
    
    if current_user.has_role('Expertuser'):
        print "***USER IS AN EXPERTUSER***"
    if current_user.has_role('Admin'):
        print "***USER IS AN ADMIN***"
        
        get_userinfo_expert = userinfo_expert.query.all() 
        #get list of users, populate userlist
        userid = 1
        keeptry = 1		
        print "number of users ==" + str(User.query.count())
        while keeptry == 1:
            try:
                tmp_usr = user_datastore.get_user(str(userid)).email
                tmp_usr_dt = user_datastore.get_user(str(userid)).confirmed_at
                
                tmp_usr_expertinfo = user_datastore.get_user(str(userid)).userinfo_expert_completed
                if tmp_usr_expertinfo is None:
                    tmp_usr_expertinfo = ""
                    
                tmp_usr_promocodes = user_datastore.get_user(str(userid)).promocodes
                if tmp_usr_promocodes is None:
                    tmp_usr_promocodes = ""
                    
                tmp_userlist_mturkcompletioncodes = user_datastore.get_user(str(userid)).mturkcompletioncode
                if tmp_userlist_mturkcompletioncodes is None:
                    tmp_userlist_mturkcompletioncodes = ""
                    
                tmp_usr_r = ''
                if user_datastore.get_user(str(userid)).has_role('Admin'):
                    tmp_usr_r += 'Admin '
                if user_datastore.get_user(str(userid)).has_role('User'):
                    tmp_usr_r += 'User '
                if user_datastore.get_user(str(userid)).has_role('Subuser'):
                    tmp_usr_r += 'Subuser '
                if user_datastore.get_user(str(userid)).has_role('Expertuser'):
                    tmp_usr_r += 'Expertuser '
                if user_datastore.get_user(str(userid)).has_role('Mturkuser'):
                    tmp_usr_r += 'Mturkuser '
                    
                userlist.append(tmp_usr)
                userlist_userid.append(userid)
                userlist_datetime.append(tmp_usr_dt)
                userlist_roles.append(tmp_usr_r)
                userlist_expertinfo.append(tmp_usr_expertinfo)
                userlist_promocodes.append(tmp_usr_promocodes)
                userlist_mturkcompletioncodes.append(tmp_userlist_mturkcompletioncodes)
                
                
                userid += 1
            except:
                userid += 1
                if userid > User.query.count() + 1:
				    keeptry = 0
			
    return render_template('account.html', userlist=userlist, userlist_userid=userlist_userid, userlist_datetime=userlist_datetime, userlist_roles=userlist_roles,userlist_promocodes=userlist_promocodes,userlist_expertinfo=userlist_expertinfo, userlist_mturkcompletioncodes=userlist_mturkcompletioncodes, get_userinfo_expert=get_userinfo_expert)
		
@application.route('/user_edit', methods = ['GET', 'POST'])
@login_required
def user_edit():
	
	form = UserEditForm()
		
	if form.validate():
		print "valid"
	print form.errors
	if form.validate_on_submit():
		print "A"
		current_user.nickname = form.nickname.data
		current_user.email = form.email.data
		current_user.favcolor= form.favcolor.data
		db.session.add(current_user)
		db.session.commit()
		flash('Your changes have been saved.')
		return redirect(url_for('user_edit'))
	else:
		print "B"
		form.nickname.data = current_user.nickname
		form.email.data = current_user.email
		form.favcolor.data = current_user.favcolor
	return render_template('user_edit.html',
		form = form)
		
@application.route('/feature_playiq')
def feature_playiq():
	return render_template('feature_playiq.html', title = 'Feature: PlayIQ Score')
		
@application.route('/science_blog')
def science_blog():
	return render_template('science_blog.html', title = 'Science Blog',)
	#return render_template('science_blog.html', title = 'Science Blog', stories = stories)
	
@application.route('/tabtest')
def tabtest():
	return render_template('tabtest.html', title = 'tabtest',)
	
@application.route('/demo1', methods = ['GET', 'POST'])
#@login_required
#@roles_required('User')
def demo1():

	return render_template('index.html', title = 'PLAyIQ', demo=1, showsidebar=1)
	
@application.route('/task_ant', methods = ['GET', 'POST'])
@login_required
@roles_required('User')
def task_ant():
    return render_template('task_ant.html',
        title = 'Task: Attention')

@application.route('/user_profile', methods = ['GET', 'POST'])
@login_required
@roles_required('Admin')
def user_profile():
    
    do_user = 1
    
    if do_user == 1:
        userp = {'Nickname': 'ballerbob', 'Email': 'test@test.com', 'Avatar': '1', 'Badge': 'gold', \
            'Quote': 'Recently have been playing lots of FIFA... used to play WoW, but not much recently. Still dabble.', 'MemberSince': 'May 6, 2015', \
            'Pav': '110', 'Phi': '118', 'Plo': '85', \
            'Lav': '106', 'Lhi': '112', 'Llo': '92', \
            'Aav': '95', 'Ahi': '98', 'Alo': '76', \
            'Pcertainty': '85', 'Lcertainty': '91', 'Acertainty': '68', \
            }
    elif do_user == 2:
        userp = {'Nickname': 'TheChosen99', 'Email': 'test@test.com', 'Avatar': '2', 'Badge': 'silver', \
            'Quote': 'Recently have been playing lots of FIFA... used to play WoW, but not much recently. Still dabble.', 'MemberSince': 'May 7, 2015', \
            'Pav': '154', 'Phi': '165', 'Plo': '124', \
            'Lav': '98', 'Lhi': '101', 'Llo': '95', \
            'Aav': '76', 'Ahi': '86', 'Alo': '65', \
            'Pcertainty': '95', 'Lcertainty': '86', 'Acertainty': '78', \
            }
    elif do_user == 3:
        userp = {'Nickname': 'WolfSmash', 'Email': 'test@test.com', 'Avatar': '3', 'Badge': 'bronze', \
            'Quote': 'Recently have been playing lots of FIFA... used to play WoW, but not much recently. Still dabble.', 'MemberSince': 'May 12, 2015', \
            'Pav': '95', 'Phi': '112', 'Plo': '92', \
            'Lav': '124', 'Lhi': '136', 'Llo': '108', \
            'Aav': '87', 'Ahi': '91', 'Alo': '68', \
            'Pcertainty': '77', 'Lcertainty': '98', 'Acertainty': '89', \
            }
    #userg_title.append('Eve Online')
    #userg_date.append('2
    return render_template('user_profile.html',userp=userp)
		
@application.route('/taskinput', methods = ['GET', 'POST'])
@login_required
@roles_accepted('User','Expertuser','Mturkuser')
@crossdomain(origin='*')
def taskinput():
    try:
        flow = 'A'
        print "YOU HAVE JUST TAKEN A TASK, WAS I RIGHT?"
        newscore = 0
        newscore_name = ''
        newscore_score = ''
        session['newscore'] = newscore
        session['newscore_name'] = newscore_name
        session['newscore_score'] = newscore_score
        if request.method == 'POST':
            newscore = 1
            flow += 'B'
            print "I HAVE RECEIVED DATA!"
            taskName = request.form['data']
            taskData = request.form['data1']
            flow += 'C_'
            flow += taskName 
            print "The task completed was = " + taskName
            print "the data are = " + taskData
            if taskName == 'ANT':
                flow += '_ANT_'
                #analyze ANT data
                print "analyzing ANT"
                driftrate = analyze_ANT(taskData)
                newscore_score = driftrate
                newscore_name = 'Attention'
                print "your drift rate = " + str(driftrate)            
                flow += 'D11'
                instance_ANT = tasktable_ANT(rawdata=taskData, driftrate=driftrate, datetime=datetime.datetime.utcnow(),user_id=current_user.id)
                flow += 'D12'
                db.session.add(instance_ANT)
                db.session.commit()
                flow += 'D13'
            elif taskName == 'Learn':
                flow += '_Learn_'
                print "analyzing Learning"
                accuracy = analyze_LRN(taskData)
                newscore_score = accuracy
                newscore_name = 'Learning'
                print "your Learning accuracy = " + str(accuracy)
                flow += 'D21'
                instance_LRN = tasktable_LRN(rawdata=taskData, accuracy=accuracy, datetime=datetime.datetime.utcnow(),user_id=current_user.id)
                flow += 'D22'
                db.session.add(instance_LRN)
                db.session.commit()
                flow += 'D23'
            elif taskName == 'Filter':
                flow += '_Filter_'
                print "analyzing Perception (Filter)"
                driftrate = analyze_PRC(taskData)
                newscore_score = driftrate
                newscore_name = 'Perception'
                print "your driftrate = " + str(driftrate)
                flow += 'D31'
                instance_PRC = tasktable_PRC(rawdata=taskData, driftrate=driftrate, datetime=datetime.datetime.utcnow(),user_id=current_user.id)
                flow += 'D32'
                db.session.add(instance_PRC)
                db.session.commit()
                flow += 'D33'
            elif taskName == 'SYM':
                flow += '_SYM_'
                print "analyzing Symmetry"
                accuracy = analyze_SYM(taskData)
                newscore_name = 'Span'
                newscore_score = accuracy
                print "your accuracy = " + str(accuracy)
                flow += 'D41'
                instance_SYM = tasktable_SYM(rawdata=taskData, accuracy=accuracy, datetime=datetime.datetime.utcnow(),user_id=current_user.id)
                flow += 'D42'
                db.session.add(instance_SYM)
                db.session.commit()
                flow += 'D43'			
        #flow += 'E0'
        #get_ANT = tasktable_ANT.query.all()
        #flow += 'E1'
        #get_LRN = tasktable_LRN.query.all()
        #flow += 'E2'
        #get_PRC = tasktable_PRC.query.all()
        #flow += 'E3'
        #get_SYM = tasktable_SYM.query.all()
        #flow += 'E4'

        #c_user = User.query.get(current_user.id)
        #flow += 'E4'
        #user_ANT = c_user.user_tasktable_ANT.all()
        #flow += 'E5'
        #user_LRN = c_user.user_tasktable_LRN.all() 
        #flow += 'E6'
        #user_PRC = c_user.user_tasktable_PRC.all() 
        #flow += 'E7'
        #user_SYM = c_user.user_tasktable_SYM.all() 
        #flow += 'E8'

        flow += str(newscore)
        print flow
        session['flowmessage'] = flow
        session['newscore'] = newscore
        session['newscore_name'] = newscore_name
        session['newscore_score'] = newscore_score
        
        conn = tinys3.Connection('AKIAJ4JQZZAXHPCIWPYQ','C46OJZXhrqdZCKOdx26D1p0vF9ag6JZj4qhlHreN', tls=True, endpoint='s3-eu-west-1.amazonaws.com') #access key, secret key
        
        fileattempt = os.path.join(basedir, 'app.db')
        nowdate = datetime.datetime.strftime(datetime.datetime.now(), '%Y_%m_%d_%H_%M_%S')
        print nowdate
        
        # Uploading a single file
        f = open(fileattempt,'rb')
        
        print conn.upload(nowdate+'_app.db',f,'playiqdbstore')
        print conn.get(nowdate+'_app.db','playiqdbstore')
        
        if newscore == 1:
            print "attempting DBbackup...."
            do_DBbackup
            print "....attempted DBbackup"
        
        
        return render_template('results.html') #, flow=session['flowmessage'],get_ANT=get_ANT, user_ANT=user_ANT, get_LRN=get_LRN, user_LRN=user_LRN, get_PRC=get_PRC, user_PRC=user_PRC, get_SYM=get_SYM, user_SYM=user_SYM)
        
        #return render_template('index.html') #render_template('test.html', get_ANT=get_ANT, user_ANT=user_ANT)
        
    except:
        flash(sys.exc_info())
        return render_template('index.html')
        #return render_template('testpage.html',testmessage=sys.exc_info())
        
@application.route('/results', methods = ['GET', 'POST'])
@login_required
@roles_accepted('User','Expertuser','Mturkuser')
def results():
    print "results:"
    
    #instance_ANT = tasktable_ANT(driftrate=2.5, datetime=datetime.datetime.utcnow(),user_id=current_user.id)
    #db.session.add(instance_ANT)
    #db.session.commit()

            
    #load ANT data
    get_ANT = tasktable_ANT.query.all() #all users    
    get_LRN = tasktable_LRN.query.all() #all users    
    get_PRC = tasktable_PRC.query.all() #all users    
    get_SYM = tasktable_SYM.query.all() #all users 
    #get_ANT = []
    #get_LRN = []
    
    c_user = User.query.get(current_user.id) #current user
    user_ANT = c_user.user_tasktable_ANT.all()
    user_LRN = c_user.user_tasktable_LRN.all()
    user_PRC = c_user.user_tasktable_PRC.all()
    user_SYM = c_user.user_tasktable_SYM.all()
	
    if not user_ANT:
        user_ANT = []
    if not user_LRN:
        user_LRN = []
    if not user_PRC:
        user_PRC = []
    if not user_SYM:
        user_SYM = []
		
    #score_P = random.randrange(0,100)
    #score_L = random.randrange(0,100)
    #score_A = random.randrange(0,100)
    #scores = [score_P, score_L, score_A]
    #score_IQ = sum(scores)/len(scores)
    
    #make PLAyScore image
    #if current_user.nickname is None:
    #    tmp_userName = str(current_user.id)
    #else:
    #    tmp_userName = current_user.nickname
    #PlotPLAyScore(score_P,score_L,score_A,score_IQ,userName=tmp_userName)    
    
    session['flowmessage'] += '_results'
    
    if (current_user.has_role('Expertuser') == True) & (current_user.has_role('Admin') == False):
		print "to testflow as Expertuser..."
		return redirect(url_for('testflow'))
    if (current_user.has_role('Mturkuser') == True) & (current_user.has_role('Admin') == False):
		print "to testflow as Mturkuser..."
		return redirect(url_for('testflow_mturk'))
    else:
        return render_template('results.html', flow=session['flowmessage'], newscore=session['newscore'], newscore_score=session['newscore_score'], newscore_name=session['newscore_name'], get_ANT=get_ANT, user_ANT=user_ANT, get_LRN=get_LRN, user_LRN=user_LRN, get_PRC=get_PRC, user_PRC=user_PRC, get_SYM=get_SYM, user_SYM=user_SYM)
    

@application.route('/get_rawdata')
@login_required
@roles_required('Admin')
def get_rawdata():
    
    print "get_rawdata:"
    get_ANT = tasktable_ANT.query.all() #all users    
    get_LRN = tasktable_LRN.query.all() #all users    
    get_PRC = tasktable_PRC.query.all() #all users    
    get_SYM = tasktable_SYM.query.all() #all users 
    
    for i_ANT in get_ANT:
        
        tmp_line = str(i_ANT.id) + '\t' + str(i_ANT.user_id) + '\t' + str(i_ANT.datetime) + '\t' + str(i_ANT.driftrate)
        if i_ANT.rawdata is not None:
            tmp_line = tmp_line + '\t' + str(i_ANT.rawdata)
        
        print tmp_line
    
    return render_template('rawdata.html', get_ANT=get_ANT, get_LRN=get_LRN, get_PRC=get_PRC, get_SYM=get_SYM)

    
def analyze_ANT(taskData):
    
    data = taskData.split(',')    
    driftrate = float(data[-1])
    
    return driftrate

def analyze_LRN(taskData):
    
    data = taskData.split(',')    
    accuracy = float(data[-1])
    
    return accuracy
    
def analyze_PRC(taskData):
    
    data = taskData.split(',')    
    driftrate = float(data[-1])
    
    return driftrate

def analyze_SYM(taskData):
    
    data = taskData.split(',')    
    accuracy = float(data[-1])
    print 'accuracy score processed'
    
    return accuracy

def load_amateurdata():
    Amateurdata_ANT=[0.294615393,0.322548889,0.271604713,0.262949028,0.298380024,0.226865182,0.303606298,0.249471548,0.197064507,0.346107499,0.253801797,0.171099602,0.324120522,0.316444346,0.259688884,0.342110765,0.170401318,0.299465457,0.269803973,0.25177211,0.336975452,0.28935455,0.30421508,0.274758926,0.31126499,0.279400095,0.22823974,0.265865951,0.365424426,0.342536214,0.291353088,0.372292397,0.268923347,0.134998305,0.260239447,0.212600569,0.337573333,0.336345343,0.406789912,0.291235963,0.213290701,0.305559241,0.274804837,0.307484923,0.254463305,0.29935529,0.06173297,0.303110164,0.216391871,0.27611564,0.159952025,0.319632083,0.391360827,0.1009176,0.288102817,0.259872645,0.292298756,0.29833522,0.360684458,0.426149858,0.390596677,0.26153404,0.365299165,0.28204785,0.214649066,0.224893719,0.219237877,0.277326161,0.036217002,0.230695807,0.190717931,0.260057323,0.319967799,0.255244857,0.334981901,0.255235266,0.320339858,0.275075302,0.265356679,0.282523067,0.311280527,0.361253048,0.290519073,0.32533741,0.298209547,0.172413769,0.251797133,0.324386859,0.269634384,0.274168242,0.32825657,0.231680028,0.273249673,0.24051268,0.297035582,0.2859562,0.327596078,0.333307656,0.269133969,0.400333174,0.243518633,0.363951834,0.324151137,0.0466538,0.28481421,0.243929197,0.382825431,0.25703324,0.379508641,0.353534623,0.329429927,0.395085221,0.349256659,0.335400581,0.332339035,0.182303999,0.304501574,0.354058537,0.301103302,0.252965191,0.370208005,0.346734316,0.227184158,0.250198265,0.271650618,0.211621551,0.264456491,0.237086522,0.319791981,0.137680208,0.360346463,0.347100649,0.259669208,0.342177484,0.26293573,0.243101607,0.231991556,0.256376468,0.228967926,0.188017708,0.352105655,0.338485655,0.316596065,0.254218331,0.293919517,0.264866866,0.376932264,0.184093489,0.252505702,0.192016251,0.343731458,0.289232407,0.206293623,0.263414155,0,0.373404991,0.282256364,0.215464206,0.403877223,0.337492369,0.282173962,0.223187811,0.267675873,0.273765639,0.134551787,0.31005824,0.315161442,0.218124151,0.24727909,0.207055023,0.312038504,0.294858419,0.232173228,0.257146594,0.406646473,0.357145908,0.33020856,0.229790776,0.332415892,0.341468915,0.225206454,0.353823383,0.256961303,0.317069221,0.297420103,0.252339635,0.222470494,0.247906182,0.3265384,0.136766994,0.333333665,0.350959628,0.222993141,0.244843432,0.324342357,0.232505266,0.239369286,0.282618133,0.304490213,0.292698331,0.111291847,0.301186981,0.282181743,0.289749983,0.208957876,0.20977972,0.278563657,0.354245463,0.30713704,0.265862222,0.29146152,0.161659885,0.211793415,0.163390378,0.296529179,0.27341122,0.316440549,0.196491816,0.253305136,0.320836634,0.314367721,0.266576892,0.407909204,0.167117365,0.303620933,0.267500145,0.087455934,0.401657819,0.275044453,0.322505581,0.361472181,0.388306254,-0.032786981,0.239717417,0.266467974,0.271841343,0.290388811,0.331970031,0.270200057,0.092205844,0.230420318,0.351588467,0.145857015,0.294962348,0.22393343,0.319987693,0.299950385,0.297978417,0.24093948,0.345522515,0.38296474,0.293331966,0.189708942,0.3140944,0.295384619,0.052208053,0.248144325,0.087536607,0.250361794,0.390935604,0.317527882,0.245690602,0.21280727,0.237288804,0.284247642,0.173905047,0.247058433,0.333803989,0.277036591,0.282921114,0.256136431,0.245851032,0.409892628,0.213656955,0.30067034,0.288562309,0.15439602,0.301361096,0.166095727,0.338748144,0.279987495,0.22798099,0.250874043,0.30494967,0.357259987,0.276453838,0.209681399,0.304944354,0.332860902,0.178847825,0.312572462,0.336591445,0.292542378,0.325392156,0.245403893,0.322822818,0.27147428,0.338754429,0.21518761,0.28674925,0.337094974,0.314589738,0.329188524,0.299367418,0.244278408,0.018265146,0.342027969,0.282038974,0.212848242,0.235918478,0.101616488,0.348897981,0.31696205,0.241724749,0.257039756,0.268600057,0.297402031,0.290771984,0.287000037,0.242950612,0.189656696,0.275022894,0.231776496,0.288650213,0.270798288,0.147208594,0.245433482,0.305979485,0.119086207,0.272194799,0.260399527,0.363797233,0.253454454,0.31118205,0.257897262,0.288301852,0.335873785,0.27188651,0.228482668,0.235027123,0.219867057,0.197307129,0.289471574,0.205044352,0.229142552,0.24010929,0.327158868,0.254688397,0.236368193,0.2548086,0.255466749,0.17937824,0.265037788,0.311496999,0.264875829,0.267996701,0.287733777,0.269438695,0.33805627,0.168264108,0.298587399,0.284619554,0.241412888,0.240929615,0.207207373,0.298022268,0.28001452,0.246751035,0.253117882,0.219732027,0.32787142,0.30335979,0.366717297,0.184892043,0.257833517,0.266891604,0.339704068,0.315482968,0.256923977,0.126841884,0.28258638,0.308135582,0.222712955,0.08809278,0.323946756,0.269009155,0.307661691,0.238707731,0.177427133,0.251063943,0.216526586,0.29061736,0.316547335,0.31945759,0.220850863,0.324198889,0.226387769,0.187871982,0.296153132,0.272782125,0.381881435,0.252150186,0.372007189,0.356893254,0.297009354,0.440933964,0.362363043,0.283630583,0.282442883,0.227393687,0.081261426,0.196128515,0.186613404,0.291458466,0.255540063,0.323908526,0.295837554,0.141624208,0.038409544,0.205363682,0.277126983,0.225262291,0.334348703,0.167511054,0.236412119,0.254391892,0.373872742,0.43808753,0.364317291,0.309464992,0.260617551,0.360538169,0.310918599,0.194242713,0.244167583,0.311609779,0.314123684,0.168142744,0.303846056,0.263224671,0.333968652,0.307303707,0.177993175,0.223893009,0.264884076,0.309868724,0.272352663,0.377663203,0.166969513,0.32218109,0.292536897,0.21770012,0.245103393,0.286109367,0.351939713,0.217751313,0.226491378,0.408056578,0.290961728,0.199573731,0.166357929,0.247641239,0.052398083,0.284919556,0.235852324,0.331125951,0.20706622,0.339268083,0.27261643,0.253234428,0.332808514,0.320634459,0.354690197,0.244269686,0.229578729,0.250446206,0.214150181,0.276042551,0.343382596,0.196185441,0.254020831,0.319522725,0.22297069,0.334536853,0.228259443,0.251579102,0.264257268,0.274484396,0.191139057,0.324260695,0.254745428,0.277055479,0.175454916,0.264722933,0.292228678,0.311364524,0.287034108,0.254662795,0.268361832,0.147000406,0.392063163,0.33927088,0.008195056,0.376991965,0.290864474,0.26558821,0.27476472,0.383248735,0.326915026,0.22412884,0.260724175,0.209595553,0.232093501,0.111877506,0.245720896,0.391732261,0.249413865,0.283727514,0.445083198,0.273561779,0.350430381,0.165169158,0.152157191,0.384789434,0.212210393,0.34023944,0.36348704,0.237166563,0.210708124,0.25304458,0.35333857,0.189481643,0.260432024,0.237488806,0.141715313,0.285013442,0.338669889,0.288026385,0.37897986,0.255534374,0.25263932,0.292224696,0.245198002,0.38486842,0.214654036,0.372348578,0.276038471,0.331905043,0.204603116,0.217244483,0.190960743,0.32219051,0.169125445,0.224830074,0.306377551,0.340666002,0.254270796,0.285372249,0.299430214,0.372644434,0.277185163,0.207259162,0.274165308,0.287168044,0.231545831,0.272202614,0.01623434,0.239875664,0.26134355,0.246530219,0.068881623,0.334102233,0.240476873,0.261068061,0.340740903,0.335553256,0.268943984,0.216297573,0.28263873,0.277157859,0.31551798,0.275690362,0.275603485,0.354255548,0.222533429,0.370302328,0.283743056,0.323363843,0.333745983,0.311555425,0.302567887,0.234334932,0.302055222,0.291714219,0.3158766,0.295087604,0.326251728,0.164925609,0.387540262,0.39491598,0.245867984,0.266296417,0.306985181,0.380984893,0.160143536,0.328420567,0.267063272,0.313670222,0.232314419,0.201085741,0.229431784,0.313354551,0.16124731,0.203908756,0.321729897,0.227831752,0.295950407,0.287481356,0.288341401,0.295938567,0.225947589,0.261699599,0.272882981,0.228608901,0.374541041,0.408217437,0.220871062,0.348222192,0.319954207,0.258614845,0.228331515,0.216948755,0.298850737,0.428038268,0.339962556,0.31673579,0.315665271,0.326898512,0.274729681,0.327975313,0.277495251,0.313688001,0.244446656,0.279841877,0.340741138,0.3132791,0.29662451,0.252494883,0.339500682,0.275598899,0.246453013,0.188376596]
    Amateurdata_PRC=[0.05055464,0.145643352,0.058832562,0.129799305,0.129850815,0.10208596,0.075440483,0.034638495,0.112717446,0.145428469,0.226980152,-0.016712259,0.081276709,0.134980254,0.054396638,0.09308429,0.026076426,0.115998868,0.122273899,0.105834934,0.120070567,0.120211075,0.061986552,0.150923094,0.099090033,0.116279901,0.130932977,0.055855549,0.097340838,0.090687946,0.056227261,0.133806079,0.121122079,0.024225926,0.123522251,0.121917093,0.115243014,0.183572887,0.181101961,0.039329153,0.120678532,0.101922474,0.111852485,0.047494581,0.079703018,0.102332005,0.082811629,0.095330887,0.118359744,0.068527078,0.033468537,0.159437172,0.130348686,0.076075397,0.16546908,0.161551309,0.111095429,0.084900323,0.104689562,0.131894006,0.158046121,0.165797483,0.145740704,0.113222676,-0.017357814,0.006660774,0.078175999,0.112665888,-0.013981555,0.092928331,0.107595554,0.067865311,0.071990935,0.050184964,0.143601245,0.037417514,0.066907674,0.104466952,0.130422148,0.101201246,0.177644412,0.120598112,0.172734705,0.076897426,0.102583218,0.010274705,0.174785252,0.132031981,0.02178223,0.096883002,0.116928144,0.077820754,0.105404387,0.109136066,0.148941289,0.157953378,0.083314491,0.102802108,0.034610316,0.089168652,0.093391991,0.190894798,0.132466605,0.053523865,0.087251791,0.076705526,0.153025183,0.109814352,0.137054461,0.110399037,0.139322149,0.061609664,0.116599078,0.11660171,0.093805609,0.013151673,0.142322146,0.074840752,0.11775016,0.097011801,0.06694237,0.102965829,0.067641908,0.098592648,0.121143822,0.123048027,0.124770534,0.058465725,0.027672194,0.053798045,0.097168345,0.099637823,0.112124594,0.083724359,0.041293184,0.155223538,0.103089269,0.065657392,0.089101038,-0.002597955,0.115385719,0.140620686,0.134362881,0.14106764,0.051276243,0.084573851,0.116632543,0.03512044,0.152759229,0.102779236,0.12412211,0.069339063,0.153671509,0.132914457,0.052943791,0.13274985,0.101457287,0.075256786,0.071715326,0.104272884,0.168911505,0.074499267,0.070583718,0.147182763,0.02575115,0.119390069,0.128328883,0.117971177,0.155600033,0.062410101,0.124956339,0.121395171,0.094724019,0.124169649,0.133627244,0.099343835,0.108475087,0.09614713,0.066388208,0.162383456,0.133110318,0.110599358,0.061846158,0.111312447,0.143455349,0.084045636,0.076828331,0.161203454,0.069379974,0.014201829,0.104753484,0.146395512,0.131345699,0.151372115,0.15271407,0.112519442,0.059264149,0.137802507,0.160748031,0.104870789,0.021186338,0.036458309,0.105514191,0.146260099,0.1012414,0.135937509,0.1006252,0.044554904,0.162520295,0.094954027,0.107536408,0.081829166,0.069678603,0.120007764,0.046526432,0.104119914,0.148844255,0.047794065,0.075713341,0.112528195,0.129979948,0.116263727,0.125868943,0.09598055,0.083195842,0.068660399,-0.003107162,0.14874693,0.12419234,0.107089666,0.134355381,0.123134407,0.089885366,0.069663568,0.100998506,0,0.130047283,0.118387659,0.083074302,0.073668578,0.048549657,0.106152318,0.117844019,0.077008682,0.100295719,0.251733421,0.101236455,0.144509673,0.136129719,0.058217669,0.144631779,0.068573312,-0.003137038,0.118863252,0.073933514,-0.012335024,0.107581069,0.058189443,0.115271572,0.163587199,0.171529921,0.124634071,0.105673097,0.080678191,0.140713334,0.074222135,0.042270044,0.114406919,0.026311553,0.1689355,0.181485536,0.128104242,0.100476099,0.168533363,0.159244217,0.128113461,0.103049444,0.075762957,0.031791589,0.127172578,0.092094018,0.095486617,0.105286496,0.152851411,0.159049384,0.084169166,0.085847587,0.095195276,0.124037707,0.035710211,0.128930021,0.09159194,0.088033557,0.159588183,0.114414436,0.160262563,0.136414339,0.134652673,0.062797675,0.119679462,0.094634838,0.062046074,0,0.189211671,0.087241925,0.125150983,0.222784479,0.041344167,0.012522997,0.111530105,0.119853135,0.146823834,0.117228206,0.118154043,0.049014437,0.076910484,0.108064894,0.165070874,0.101708551,0.012946266,0.012857731,0.064562932,0.127035911,0.044476257,0.074738591,0.091493261,0.11302052,0.130633633,0.093573954,0.111730407,0.101764217,0.141632346,0.114093414,0.04561416,0.116607035,0.096303254,0.109206451,0.065250519,0.121484816,0.051307219,0.103895954,0.055353289,0.127708928,0.132514339,0.0963938,0.115279284,0.104345145,0.07332314,0.191054569,0.078662625,-0.005615021,0.062977374,0.129843224,0.094992109,0.153362185,0.030229287,0.149624038,0.074972228,0.136840553,0.037673063,0.108985904,0.130449348,0.076283598,0.047374331,0.065246647,0.124433191,0.059613637,0.102520287,0.080796413,0.069114525,0.11464255,0.151575984,0.216819404,0.087029095,0.035307962,0.161027702,0.096480339,0.072074946,0.099586781,0.098992867,0.096982209,0.103626773,0.09106998,0.069434561,0.135736386,0.043611155,0.108695216,0.089229301,0.069750596,0.086250186,0.098337193,0.06912724,0.115668141,0.091423792,0.151458239,0.161418196,0.107324429,0.006164291,0.140993648,0.110841931,0.175521252,0.065114879,0.05565625,0.059049761,0.040574463,0.127329652,0.119329641,0.107156919,0.116208826,0.083141978,-0.014267121,0.07007256,0.063559988,0.136262527,0.067658534,0.170312285,0.042561188,0.077993154,-0.012380553,0.131679546,0.109150022,0.105338841,0.039488474,0.05375095,0.098732748,0.119008075,0.115070284,0.116327169,0.136299304,0.133060994,0.097183196,0.178085063,0.158221006,0.022720403,0.126975705,0.150570638,0.073510488,0.08631777,0.024224277,0.092274807,0.148583122,0.145637507,0.065360772,0.142912487,0.15275216,0.103500919,0.080037239,0.168109442,0.053845044,0.102303454,0.075540923,0.071672878,0.086828991,0.151426659,0.120345145,0.123763098,0.002611328,0.106302918,0.119841614,0.121976832,0.021337687,0.157014659,0.023010574,0.141190093,0.073404048,0.111903983,0.023734959,0.096660059,0.079740152,0.084529603,0.129487703,0.079138298,0.116761451,0.034689651,0.097407413,0.081353436,0.121287734,0.091626127,0.016079055,0.090707395,0.141497069,0.185795806,0.110852312,0.089934767,0.148603177,0.099168595,0.112253192,0.155871921,0.065546529,0.162300024,0.093564345,0.109099045,0.101467261,0.207935397,0.078830278,0.081271705,0.061941871,0.126632349,0.114358514,0.020330054,0.176274707,0.032512004,0.095150479,0.100304354,0.05955119,0.132696219,0.090449628,0.170695589,0.101249073,0.091504269,0.095031183,0.061493912,-0.006569791,0.119076884,0.079489022,0.126311979,0.089721862,0.164613991,0.197326499,0.090657239,0.138894345,0.109854756,0.015318548,0.126185951,0.065401181,0.072264689,0.157056576,0.148353486,0.119414298,0.046619268,0.047924037,0.069286364,0.024662194,0.107818481,0.172541156,0.116373187,0.052119042,0.055529704,0.179713999,0.083441456,0.110929199,0.124193649,0.098257004,0.093447774,0.17351802,0.106565942,0.062612042,0.14334211,0.077949842,0.061256527,0.049670559,0.14811448,0.055455868,0.123740612,0.114542643,0.119828178,0.133251737,0.18526526,0.130154979,0.180187641,0.136885119,0.048729944,0.11669661,0.144220231,0.145764356,0.082412553,0.067201261,0.111126638,0.092936969,0.059643867,0.070036544,0.186660093,0.106135042,0.198520199,0.139976695,0.145709535,0.106002731,0.159835357,0.085890172,0.002480541,0.131690662,0.097281526,0.076677686,0.045487701,0.095992025,0.061958982,0.158558475,0.105259711,0.126477174,0.110128706,0.114032771,0.12837747,0.066754213,0.052340223,0.136438939,0.151077467,0.097304129,0.039152038,0.113429409,0.159925863,0.108149538,0.065854977,0.119401638,0.15902444,0.118838558,0.15056632,0.08255333,0.214177202,0.135981688,0.128824128,0.137943203,0.122517033,0.042262759,0.103087011,0.067267874,0.069928449,0.098287325,0.131741872,0.062204708,0.07421707,0.07738409,0.110548494,0.075555227,0.022016609,0.04731913,0.08232946,0.088784651,0.071983629,0.142764821,0.128283054,-0.006523077,0.082518599,0.064992914,0.086242389,0.08641731,0.073462336,0.138280762,0.141616192,0.122153933,0.104000165,0.085350239,0.12229736,-0.025314169,0.131095218,0.073921188,0.095736147,0.120039202,0.140379725,0.128254369,0.128864936,0.067122186,0.120242645]
    Amateurdata_LRN=[30,78.75,73.75,83.75,78.75,83.75,90,45,68.75,81.25,73.75,13.75,70,85,73.75,87.5,35,85,71.25,83.75,76.25,67.5,77.5,76.25,78.75,78.75,68.75,66.25,68.75,71.25,63.75,81.25,55,80,73.75,78.75,58.75,50,56.25,52.5,41.25,81.25,60,51.25,72.5,35,62.5,67.5,63.75,72.5,65,75,71.25,43.75,52.5,80,68.75,72.5,68.75,67.5,80,68.75,85,41.25,53.75,37.5,62.5,67.5,33.75,88.75,67.5,57.5,66.25,72.5,60,67.5,16.25,78.75,45,70,68.75,18.75,73.75,50,78.75,60,77.5,70,65,53.75,75,75,78.75,87.5,93.75,78.75,66.25,47.5,21.25,90,36.25,60,82.5,73.75,43.75,71.25,81.25,72.5,82.5,71.25,82.5,81.25,73.75,78.75,73.75,42.5,86.25,85,40,76.25,60,55,71.25,76.25,92.5,67.5,67.5,78.75,62.5,65,76.25,85,81.25,51.25,81.25,70,88.75,51.25,53.75,62.5,87.5,62.5,86.25,75,80,31.25,57.5,60,80,72.5,75,71.25,81.25,68.75,56.25,66.25,73.75,31.25,70,76.25,51.25,71.25,70,77.5,42.5,81.25,83.75,85,68.75,86.25,82.5,72.5,72.5,40,92.5,67.5,78.75,71.25,82.5,70,70,76.25,88.75,61.25,83.75,78.75,83.75,58.75,51.25,62.5,86.25,77.5,76.25,53.75,76.25,62.5,63.75,70,63.75,57.5,56.25,62.5,88.75,70,56.25,76.25,80,85,86.25,46.25,81.25,80,72.5,76.25,65,83.75,58.75,37.5,57.5,93.75,66.25,78.75,83.75,85,66.25,87.5,75,73.75,72.5,75,86.25,82.5,43.75,56.25,50,56.25,88.75,67.5,83.75,33.75,70,82.5,82.5,47.5,78.75,85,76.25,81.25,63.75,52.5,70,72.5,21.25,77.5,63.75,38.75,85,68.75,51.25,68.75,76.25,77.5,73.75,41.25,81.25,72.5,83.75,92.5,75,62.5,77.5,77.5,73.75,86.25,68.75,73.75,56.25,36.25,32.5,81.25,77.5,82.5,73.75,68.75,78.75,46.25,61.25,87.5,72.5,86.25,82.5,72.5,71.25,71.25,80,85,65,83.75,73.75,86.25,66.25,65,37.5,60,55,78.75,73.75,70,36.25,72.5,85,48.75,51.25,73.75,73.75,78.75,85,91.25,78.75,55,66.25,70,71.25,48.75,57.5,58.75,81.25,80,68.75,63.75,71.25,82.5,80,43.75,71.25,60,77.5,68.75,60,83.75,70,83.75,76.25,73.75,40,62.5,75,60,66.25,72.5,43.75,45,77.5,85,78.75,55,87.5,52.5,88.75,35,76.25,47.5,83.75,47.5,85,80,83.75,78.75,47.5,55,72.5,40,83.75,78.75,86.25,72.5,86.25,80,53.75,80,77.5,46.25,16.25,68.75,62.5,76.25,56.25,85,47.5,76.25,76.25,76.25,77.5,83.75,73.75,73.75,68.75,61.25,80,85,78.75,67.5,67.5,62.5,47.5,73.75,63.75,67.5,80,52.5,57.5,66.25,55,78.75,37.5,72.5,75,50,18.75,83.75,51.25,53.75,22.5,78.75,57.5,78.75,82.5,47.5,68.75,63.75,66.25,88.75,81.25,41.25,87.5,35,72.5,80,48.75,81.25,83.75,83.75,85,81.25,62.5,76.25,80,83.75,76.25,66.25,65,70,80,50,78.75,83.75,77.5,76.25,71.25,62.5,32.5,88.75,80,88.75,82.5,60,65,67.5,75,68.75,70,88.75,81.25,46.25,75,83.75,55,72.5,20,60,83.75,77.5,67.5,57.5,70,60,67.5,80,76.25,80,70,51.25,11.25,66.25,60,62.5,53.75,57.5,65,60,85,70,80,55,77.5,62.5,78.75,86.25,62.5,80,42.5,50,23.75,77.5,50,77.5,66.25,77.5,88.75,78.75,81.25,60,72.5,65,67.5,42.5,81.25,81.25,83.75,56.25,85,63.75,58.75,66.25,82.5,51.25,51.25,75,57.5,53.75,45,68.75,77.5,66.25,53.75,65,43.75,81.25,66.25,51.25,76.25,67.5,83.75,65,81.25,61.25,76.25,78.75,80,76.25,53.75,73.75,48.75,68.75,91.25,61.25,81.25,47.5,56.25,71.25,58.75,62.5,67.5,78.75,71.25,55,63.75,67.5,72.5,55,67.5,77.5,50,75,71.25,67.5,73.75,63.75,86.25,58.75,70,83.75,68.75,72.5,88.75,83.75,62.5,62.5,72.5,85,61.25,87.5,67.5,76.25,66.25,68.75,66.25,82.5,63.75,83.75,72.5,48.75,55,32.5,40,63.75,60,77.5,47.5,83.75,78.75,82.5,76.25,65,83.75,85,55,70,78.75,77.5,78.75,82.5,46.25,68.75,75,76.25,73.75,67.5,81.25,85,72.5,73.75,67.5,80,78.75,83.75,82.5,67.5,80,78.75,73.75,38.75]
    Amateurdata_SYM=[30,19,37,42,40,22,24,29,26,6,34,23,29,29,17,29,13,32,20,30,20,21,22,15,40,36,38,24,34,40,10,27,22,26,19,18,22,39,25,23,15,15,27,31,31,23,24,17,14,24,28,34,21,21,16,37,30,35,39,34,15,19,17,14,37,39,42,40,27,19,21,25,30,21,30,27,32,26,29,38,20,15,19,30,35,30,20,42,21,27,25,31,42,31,25,28,20,23,23,35,19,27,21,14,20,34,26,32,17,35,28,26,23,34,35,24,23,13,21,42,33,22,33,10,24,30,22,30,26,25,28,21,36,41,41,11,38,36,42,16,16,21,23,18,19,11,25,29,29,23,13,24,18,16,22,39,20,42,22,14,30,27,26,23,30,16,41,22,28,28,24,42,40,30,32,40,39,40,10,27,26,30,35,25,34,26,32,22,24,29,38,29,30,35,42,30,26,18,23,30,36,22,10,31,42,21,22,7,20,30,23,18,27,20,37,24,24,25,14,33,29,11,4,30,21,18,35,21,23,23,27,27,21,21,36,22,39,42,29,42,25,35,25,26,21,39,32,31,16,28,19,18,13,22,36,27,42,42,22,33,30,38,17,27,35,28,19,32,27,33,14,35,20,7,21,21,23,34,27,33,30,22,21,23,21,17,16,29,28,20,31,33,14,40,20,36,24,26,21,20,29,42,24,35,28,39,16,17,27,34,33,26,42,8,30,37,18,24,20,14,25,23,30,19,27,27,24,34,34,24,21,23,25,26,28,33,27,39,28,23,36,23,32,23,42,32,28,20,19,14,42,15,36,28,34,24,37,37,23,20,15,27,39,32,14,31,32,15,40,29,42,25,34,15,16,19,40,42,17,19,32,42,29,22,30,22,42,31,32,32,23,42,33,30,25,28,18,31,19,34,21,42,34,42,27,12,39,20,42,31,28,30,29,23,28,28,42,24,35,6,36,22,36,29,25,29,39,39,23,28,27,18,20,25,31,8,34,25,31,25,31,34,36,42,27,26,42,29,36,29,23,19,29,27,28,26,22,13,28,16,38,18,23,24,35,42,32,19,21,19,29,42,22,26,25,24,8,42,34,23,30,15,30,35,28,32,31,10,29,26,18,24,22,42,32,25,24,34,38,20,16,17,24,37,39,20,17,26,41,34,29,30,27,17,38,35,29,10,22,25,36,31,19,27,13,39,29,42,26,21,26,32,30,42,7,33,26,26,25,28,18,36,10,36,24,32,29,36,27,22,27,28,30,13,27,11,28,35,42,22,25,15,23,42,42,17,10,42,19,21,21,24,24,34,34,41,38,39,25,27,30,26,22,11,29,20,34,22,27,12,25,19,23,33,22,32,31,11,37,27,20,36,27,22,22,37,17,36,9,30,36,35,19,19,24,22,21,36,16,39,25,29,16,36,35,23,18,26,31,26,25,30,22,27,24,13,21,16,10,41,30,5,31,29,36,17,36,29,26,35,27,38]
    return (Amateurdata_ANT,Amateurdata_PRC,Amateurdata_LRN,Amateurdata_SYM)
    
if __name__ == '__main__':
    if len(sys.argv) == 1: #uncomment when updated database!!
    #if str(sys.argv[1]) == 'run': 
        application.run(debug=True) #(host='0.0.0.0', debug=True)
    else:
        manager.run() #1) db migrate, 2) db upgrade (perform these in order when updating database!!)