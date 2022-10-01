import os
import secrets
import urllib
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, jsonify, session
from se_hackethon_project.forms import RegistrationForm, LoginForm, AccountUpdateForm, RequestResetForm, ResetPasswordForm, SuggestionForm, PostForm, HelpForm
from se_hackethon_project import app, db, bcrypt, mail, oauth, google
from se_hackethon_project.models import User, Post, Feedback
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message
from requests import get


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home Page')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(
            f"Your account has been successfully been created for {form.username.data}. Now you can LogIN!!!", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title="User Registration")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                print(next_page)
                list1 = next_page.split("/")
                print(list1)
                return redirect(url_for(list1[1]))
            flash("You have been logged in successfully", 'success')
            return redirect(url_for('home'))
        else:
            flash("You cannot be logged in!!!!", "danger")
    return render_template('login.html', form=form, title='Login Page')


@app.route("/google")
def google_login():
    google = oauth.create_client('google')
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    userinfo = resp.json()
    print(userinfo)
    session['email'] = userinfo['email']
    # do something with the token and profile
    user = User.query.filter_by(email=userinfo['email']).first()
    if user:
        login_user(user)
        next_page = request.args.get('next')
        if next_page:
            print(next_page)
            list1 = next_page.split("/")
            print(list1)
            return redirect(url_for(list1[1]))
        flash("You have been logged in successfully", 'success')
        return redirect(url_for('home'))
    else:
        user = User(name=userinfo['name'], email=userinfo['email'], password=secrets.token_hex(16))
        db.session.add(user)
        db.session.commit()
        login_user(user)
        next_page = request.args.get('next')
        if next_page:
            print(next_page)
            list1 = next_page.split("/")
            print(list1)
            return redirect(url_for(list1[1]))
        flash("You have been logged in successfully", 'success')
        return redirect(url_for('home'))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out successfully!!!!", "success")
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    image_file = url_for('static', filename='profile_pics/'+current_user.image_file)
    form = AccountUpdateForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.name = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your account has been updated successfully!!!", 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.name
        form.email.data = current_user.email
    return render_template("account.html", title="Profile Page", image_file=image_file, form=form)


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message("Password Reset Email", sender="noreply@demo.com", recipients=[user.email])
    msg.body = f'''
        To reset your password visit the following link.
        {url_for('reset_token',token=token,_external=True)}
        If you did not make the change request please ignore it.
        Nothing will be changed!!!
    '''
    mail.send(msg)


@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with the instructions to reset password!', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verified_reset_token(token)
    if user is None:
        flash("The token is invalid or expired", "warning")
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash(f"Your password has been changed! Now You will be able to login!!! ", "success")
        return redirect(url_for('login'))
    return render_template('reset_token.html', title='Reset Password', form=form)


def send_suggestion_email(user, form):
    msg = Message(form.title.data, sender=user.email, recipients=['vedantjolly2001@gmail.com'])
    msg.body = f'The suggestion by the user is that {form.content.data}'
    mail.send(msg)


@app.route("/suggestions", methods=['GET', 'POST'])
@login_required
def suggestions():
    form = SuggestionForm()
    if form.validate_on_submit():
        send_suggestion_email(current_user, form)
        flash('Thank you for your valuable feedback !!! We will surely try to improve', 'info')
        return redirect(url_for('home'))
    return render_template('suggestion.html', title='Suggestion Page', form=form)


@app.route("/detect")
@login_required
def detect_posture():
    return render_template('index.html')


@app.route("/inspect", methods=['GET', 'POST'])
@login_required
def analyze_posture():
    f1 = 0
    f2 = 0
    f3 = 0
    f4 = 0
    data = []
    sum2 = 1
    if request.method == "POST":
        # getting input with name = fname in HTML form
        f1 = int(request.form.get("fname1"))
        f2 = int(request.form.get("fname2"))
        f3 = int(request.form.get("fname3"))
        f4 = int(request.form.get("fname4"))
        print(f1, f2, f3, f4)
        sum2 = f1 + f2 + f3 + f4
        f1 = ((f1)/(sum2))*100
        f2 = ((f2)/(sum2))*100
        f3 = ((f3)/(sum2))*100
        f4 = ((f4)/(sum2))*100
        f1 = format(f1, ".2f")
        f2 = format(f2, ".2f")
        f3 = format(f3, ".2f")
        f4 = format(f4, ".2f")
        print(f1, f2, f3, f4)
        data.append(f1)
        data.append(f2)
        data.append(f3)
        data.append(f4)
        # # getting input with name = lname in HTML form
        # last_name = request.form.get("lname")
        # return "Your name is "+first_name + last_name
    return render_template('graph.html', x1=f1, x2=f2, x3=f3, x4=f4, data=data)


@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            print(picture_file)
            post = Post(title=form.title.data, content=form.content.data,
                        author=current_user, image_file=picture_file)
            db.session.add(post)
            db.session.commit()
        else:
            print("yess")
            post = Post(title=form.title.data, content=form.content.data, author=current_user)
            db.session.add(post)
            db.session.commit()
        flash("Your post has been successfully created!!!", 'success')
        return redirect(url_for('all_posts'))
    return render_template('create_post.html', title='New Post', form=form, legend="New Post")


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash("Your post has been updated!!", 'success')
        return redirect(url_for('post', post_id=post.id))
    if request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, legend="Update Post")


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted", "success")
    return redirect(url_for("all_posts"))


@app.route("/posts")
@login_required
def all_posts():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
    return render_template('allPosts.html', posts=posts)


@app.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(name=username).first_or_404()
    posts = Post.query.filter_by(author=user).order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=2)
    return render_template('user_posts.html', posts=posts, user=user)
