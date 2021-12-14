from . import db
from app.filter import format_datetime

class Keyword_dict(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tech_lv1 = db.Column(db.String(20), nullable=False)
    tech_lv2 = db.Column(db.String(20), nullable=False)
    tech_lv3 = db.Column(db.String(20), nullable=False)
    keywords = db.Column(db.String(500), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

    @property
    def html_table(self):
        html = f"""<tr class="text-center" data-bs-toggle="modal" data-bs-target="#staticBackdrop{self.id}">
                <td class="col-1">{self.tech_lv1}</td>
                <td class="col-1">{self.tech_lv2}</td>
                <td class="col-1">{self.tech_lv3}</td>
                <td class="col-7">{self.keywords}</td>
                <td class="col-2">{format_datetime(self.create_date)}</td></tr>"""
        return html

    @property
    def html_modal(self):
        html = f"""<div class="modal fade" id="staticBackdrop{self.id}" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog modal-lg">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="staticBackdropLabel">{self.tech_lv1} / {self.tech_lv2} / {self.tech_lv3}</h5>
                        <button type="button" class="btn-close x-btn" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <textarea name="keywords" id="revised_kwds" cols="100" rows="5">{self.keywords}</textarea> 
                    </div>
                    <div class="modal-footer">
                        <button id="delBtn" type="button" class="btn btn-danger" onclick="deleteKwd({self.id})">삭제</button>
                        <button type="button" class="btn btn-primary" onclick="updateKwd({self.id});">변경</button>
                    </div>
                </div>
            </div>
        </div>
        """
        return html
                