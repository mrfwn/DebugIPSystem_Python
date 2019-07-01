from flask import render_template
from flask import render_template,request
import json
from jinja2 import Template
from app.services import shows_services
from app.services import flows_services
from app.forms import flow_form
from app import app

commands = {
        "token":{
            "token":"show system internal nbm info shm table token"
        },
        "igmp":{
            "groups":"show ip igmp groups", "snooping":"show ip igmp snooping", "route":"show ip igmp route", "interface":"show ip igmp interface"
        },
        "pim":{
            "route":"show ip pim route", "neighbor":"show ip pim neighbor", "rp":"show ip pim rp", "interface":"show ip pim interface"
        },
        "routes":{
            "mroute":"show ip mroute", "route":"show ip route"
        },
        "interface":{
            "information":"show interface brief", "status":"show interface status", "transceiver":"show interface transceiver details", "counters":"show interface counters"
        },
        "nbm":{
            "all":"show nbm flows all", "active":"show nbm flows active"
        }
    }

@app.context_processor
def inject_enumerate():
    return dict(enumerate=enumerate)

@app.route('/token',defaults ={'show': None,'sub_show':None})
@app.route('/token/<string:show>/<string:sub_show>', methods=['POST','GET'])
def token(show,sub_show):
    selection = []
    results = []
    form = flow_form.SimpleForm()
    print(form.example.data)
    
    if form.validate_on_submit():
        try:
            
            '''
            token = request.form
            for key, value in token.items():
                selection.append(value)
            selection.sort()
            '''
            selection = form.example.data
            results = shows_services.selection_device(selection,commands[show][sub_show])
            
            
        except:
            print('ERRO')
    
    return render_template('show_menu/tokens_template.html',form=form,results=results,selection=selection,show=show,sub_show=sub_show) 
    