from flask import Blueprint, render_template, request, jsonify, url_for
from werkzeug.utils import redirect
from app.models import Keyword_dict
from datetime import datetime
from app import db

bp = Blueprint("main", __name__, "/")

@bp.route('/')
def index():
    data = Keyword_dict.query.all()
    return render_template('main.html', data=data)

@bp.route('/save', methods=['POST'])
def save():
    if request.method == 'POST':
        data = request.get_json()
        tech_lv1 = data.get('tech_lv1')
        tech_lv2 = data.get('tech_lv2')
        tech_lv3 = data.get('tech_lv3')
        keywords = data.get('tech_kwds')
        create_date = datetime.now()
        
        kd = Keyword_dict()
        kd.tech_lv1 = tech_lv1
        kd.tech_lv2 = tech_lv2
        kd.tech_lv3 = tech_lv3
        kd.keywords = keywords
        kd.create_date = create_date

        db.session.add(kd)
        db.session.commit()

        return jsonify(), 201

@bp.route('/delete', methods=['DELETE'])
def delete():
    data = request.get_json()
    id = data.get('id')
    kd = Keyword_dict.query.get_or_404(id)
    db.session.delete(kd)
    db.session.commit()
    return jsonify(), 200
    
@bp.route('/update', methods=['POST'])
def update():
    data = request.get_json()
    id = data.get('id')
    keywords = data.get('tech_kwds')
    kd = Keyword_dict.query.get_or_404(id)
    
    kd.keywords = keywords
    kd.create_date = datetime.now()
    db.session.commit()
    # 여기서 로그를 기록해야함 (어떤 키워드 값이 어떻게 달라졌는지 검사 필요)
    return jsonify(), 201
