from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship
from flask_appbuilder.models.decorators import renders
from flask import Markup, render_template
import json


class Tick(Model):
    sequence = Column(Integer, primary_key=True)
    raw = Column(String(255), nullable=True)
    pdump = Column(String(255), nullable=True)
    bpipe = Column(String(255), nullable=True)

    def __repr__(self):
        return self.sequence

    @renders('custom')
    def bpipe_render(self):
        parsed = json.loads(self.bpipe)

        return render_template('collapsed-list.html',
                               preview_text='{} ticks'.format(len(parsed)),
                               items=parsed)
