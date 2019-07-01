from flask_wtf import FlaskForm
from wtforms import Form,StringField,RadioField,SubmitField,validators,SelectMultipleField,widgets
from wtforms.validators import DataRequired,Required
from wtforms.widgets import ListWidget, CheckboxInput

class FlowForm(FlaskForm):
    searchIP = StringField("searchIP",[
        validators.Regexp("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", message="IP invalido"),
        validators.Optional()
    ])
    searchName = StringField("searchName",[validators.Optional()])
    submit = SubmitField("Search")

class ShowForm(FlaskForm):
    check1 = CheckboxInput()
    submit = SubmitField("Run")
    
class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class SimpleForm(FlaskForm):
    example = MultiCheckboxField('Label', coerce=int,choices=[
        (1,'LEAF 1'),
        (2,'LEAF 2'),
        (3,'LEAF 3'),
        (4,'LEAF 4'),
        (5,'LEAF 5'),
        (6,'LEAF 6'),
        (7,'LEAF 7'),
        (8,'LEAF 8'),
        (11,'SPINE 1'),
        (12,'SPINE 2')        
        ])
    submit = SubmitField("Run")