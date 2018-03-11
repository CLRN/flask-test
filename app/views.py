from flask import render_template, flash
from flask_appbuilder import BaseView, expose, has_access, SimpleFormView, ModelView, IndexView
from app import appbuilder, db
from .forms import MyForm
from flask_babel import lazy_gettext as _
from .models import Tick
from flask_appbuilder.models.sqla.interface import SQLAInterface


class MyView(BaseView):

    default_view = 'method1'

    @expose('/method1/')
    @has_access
    def method1(self):
            # do something with param1
            # and return to previous page or index
        return 'Hello'

    @expose('/method2/<string:param1>')
    @has_access
    def method2(self, param1):
        # do something with param1
        # and render template with param
        param1 = 'Goodbye %s' % (param1)
        return param1


class MyFormView(SimpleFormView):
    form = MyForm
    form_title = 'This is my first form view'
    message = 'My form was submitted'

    def form_get(self, form):
        form.field1.data = 'This was prefilled'

    def form_post(self, form):
        # post process form
        flash(form.field1.data, 'info')


class TickModelView(ModelView):
    datamodel = SQLAInterface(Tick)
    related_views = []
    list_columns = ['sequence', 'raw', 'pdump', 'bpipe_render']

    base_order = ('sequence', 'desc')


db.create_all()
appbuilder.add_view(MyFormView, "My form View", icon="fa-group", label=_('My form View'),
                    category="My Forms", category_icon="fa-cogs")
appbuilder.add_view(MyView(), "Method1", category='My View')
appbuilder.add_link("Method2", href='/myview/method2/jonh', category='My View')

appbuilder.add_view(TickModelView,
                    "List Ticks",
                    icon="fa-envelope",
                    category="Ticks")
