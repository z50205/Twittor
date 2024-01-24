from flask import render_template,redirect,url_for,request,abort,current_app,flash
from twittor.forms import Loginform,Registerform,EditProfileform,Tweetform,PasswdResetRequestForm,PasswdResetForm
from twittor.models.user import User
from twittor.models.tweet import Tweet
from flask_login import login_user,current_user,logout_user,login_required
from twittor import db
from twittor.email import send_email

import os



@login_required
def index():
    form=Tweetform()
    if form.validate_on_submit():
        t=Tweet(body=form.tweet.data,author=current_user)
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('index'))
    page_num=int(request.args.get('page') or 1)
    tweets=current_user.own_and_followed_tweets().paginate(page=page_num,per_page=current_app.config['TWEET_PER_PAGE'],error_out=False)
    next_url=url_for('index',page=tweets.next_num) if tweets.has_next else None
    prev_url=url_for('index',page=tweets.prev_num) if tweets.has_prev else None
    return render_template('index.html',tweets=tweets.items,form=form,next_url=next_url,prev_url=prev_url)

def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=Loginform(meta={'csrf': False})
    if form.validate_on_submit():
        u=User.query.filter_by(username=form.username.data).first()
        if u is None or not u.check_password(form.password.data):
            print('Invalid username or password')
            return redirect(url_for('login'))
        login_user(u,remember=form.remember_me.data)
        next_page=request.args.get('next')
        print(next_page)
        if next_page:
            return redirect(url_for(next_page))
        return redirect(url_for('index'))
    return render_template('login.html',title="Sign In",form=form)
def logout():
    logout_user()
    return redirect(url_for('login'))


def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=Registerform(meta={'csrf': False})
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html',title="Register",form=form)

@login_required
def user(username):
    u=User.query.filter_by(username=username).first()
    if u is None:
        abort(404)
    page_num=int(request.args.get('page') or 1)
    tweets=u.tweets.order_by(Tweet.create_time.desc()).paginate(page=page_num,per_page=current_app.config['TWEET_PER_PAGE'],error_out=False)
    next_url=url_for('profile',page=tweets.next_num,username=u.username) if tweets.has_next else None
    prev_url=url_for('profile',page=tweets.prev_num,username=u.username) if tweets.has_prev else None
    if request.method=='POST':
        if request.form['request_button']=='Follow':
            current_user.follow(u)
            db.session.commit()
        elif request.form['request_button']=='Unfollow':
            current_user.unfollow(u)
            db.session.commit()
        else:
            flash("Send an email to your email address, please check!!!!")
            send_email_for_user_activate(u)
    return render_template('user.html',title='profile',tweets=tweets.items,user=u,next_url=next_url,prev_url=prev_url)

def page_not_found(e):
    return render_template('404.html'),404


def send_email_for_user_activate(user):
    token = user.get_jwt()
    url_user_activate = url_for('user_activate',token=token,_external=True)
    print(url_user_activate)
    send_email(
        subject='Twittor-Reset Your Password',
        recipents=[os.environ.get('RECIPENT')],
        text_body=render_template('email/user_activate.txt',username=user.username,url_user_activate=url_user_activate),
        html_body=render_template('email/user_activate.html',username=user.username,url_user_activate=url_user_activate)
        )

@login_required
def edit_profile():
    form=EditProfileform()
    if request.method=='GET':
        form.about_me.data=current_user.about_me
    if request.method=='POST':
        current_user.about_me=form.about_me.data
        db.session.commit()
        return redirect(url_for('profile',username=current_user.username))
    return render_template('edit_profile.html',form=form)


def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form=PasswdResetRequestForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user:
            flash(
                "You should soon receive an email allowing you to reset your \
                password. Please make sure to check your spam and trash \
                if you can't find the email."
            )
            token=user.get_jwt()
            url_password_reset = url_for(
                'password_reset',
                token=token,
                _external=True
            )
            url_password_reset_request = url_for(
                'reset_password_request',
                _external=True
            )
            send_email(
                subject='Twittor-Reset Your Password',
                recipents=[os.environ.get('RECIPENT')],
                text_body=render_template(
                    'email/passwd_reset.txt',
                    url_password_reset=url_password_reset,
                    url_password_reset_request=url_password_reset_request
                ),
                html_body=render_template(
                    'email/passwd_reset.html',
                    url_password_reset=url_password_reset,
                    url_password_reset_request=url_password_reset_request)
                )
        return redirect(url_for('login'))
    return render_template('password_reset_request.html', form=form)

def password_reset(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user=User.verify_jwt(token)
    if not user:
        return redirect(url_for('login'))
    form=PasswdResetForm()
    if form.validate_on_submit():
        user.set_password(form.password1.data)
        db.session.commit()
        flash("You reset Password")
        return redirect(url_for('login'))
    return render_template('password_reset.html',title='Password Reset', form=form)

def explore():
    page_num=int(request.args.get('page') or 1)
    tweets=Tweet.query.order_by(Tweet.create_time.desc()).paginate(page=page_num,per_page=current_app.config['TWEET_PER_PAGE'],error_out=False)
    next_url=url_for('explore',page=tweets.next_num) if tweets.has_next else None
    prev_url=url_for('explore',page=tweets.prev_num) if tweets.has_prev else None
    return render_template('explore.html',title='explore',tweets=tweets.items,next_url=next_url,prev_url=prev_url)

def user_activate(token):
    # if current_user.is_authenticated:
    #     return redirect(url_for('index'))
    user=User.verify_jwt(token)
    print("HI")
    if not user:
        msg = "Token has expired, please try to re-send email"
    else:
        user.is_activated = True
        db.session.commit()
        msg = 'User has been activated!'
    return render_template('user_activate.html',msg=msg)
