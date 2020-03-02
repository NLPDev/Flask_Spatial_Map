from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import PostForm
from app.models import Post

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = PostForm()
    map_data = Post.query.order_by('id')
    filter_data = form.select_tag.data
    lat_list = []
    lon_list = []
    for each_data in map_data:
        lat_list.append(each_data.lat)
        lon_list.append(each_data.lon)

    if form.validate_on_submit():        
        flash('You can find the place on the map')
        filter_data = form.select_tag.data

        if filter_data != 'all':
            map_data = Post.query.filter_by(primary_tag=form.select_tag.data)
        
        lat_list = []
        lon_list = []
        for each_data in map_data:
            lat_list.append(each_data.lat)
            lon_list.append(each_data.lon)
    
    return render_template('index.html', title='Home', form=form, lat_list=lat_list, lon_list=lon_list)



