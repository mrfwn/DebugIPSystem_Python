from app import app
from flask import render_template
from app.services import shows_services

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

@app.route("/index")
@app.route("/")
@app.route("/home")
def home():
    return render_template('home_template.html')

@app.route("/show")
def show():
    return render_template('show_template.html')

@app.route("/configure")
def configure():
    return render_template('configure_template.html')

@app.route("/dashboard")
def dashboard():
    #resp = shows_services.cli_show('show logging last 10','10.175.254.13','mwessen','mrfwn@2019')       
    #variavel = resp['ins_api']['outputs']['output']['body'].replace( '\n','<br />')
    selection = [1,2,3,4,5,6,7,8,11,12]
    results = shows_services.selection_device(selection,'show logging last 10')
    return render_template('home_menu/dashboard_template.html',selection = selection, results=results)



