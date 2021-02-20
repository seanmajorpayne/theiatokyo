from flask import render_template
from app.google import google_api
from app.eyexplore.eyexplore import Eyexplore

EYEXPLORE = Eyexplore()

@app.route('/eyexploreCaseStudy')
def eyexplore_case():
    video_count = EYEXPLORE.get_video_count()
    views = EYEXPLORE.get_views()
    subscribers = EYEXPLORE.get_subscribers()
    video_count, views, subscribers
    return render_template(
        'eyexploreCaseStudy.html',
        video_count=video_count,
        views=views,
        subscribers=subscribers,
        year=2020,
    )