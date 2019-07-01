from flask import render_template
from app.services import flows_services
from app.forms import flow_form
from app import app


@app.route("/flows", methods=["GET" , "POST"])
def flows():
    
    form = flow_form.FlowForm()
    if form.validate_on_submit():
        try:
            searchIP = form.searchIP.data
            searchName = form.searchName.data
            topology = None
            topology = flows_services.Topology(searchIP,searchName)
            topology.validate_request()                       
            return render_template('flow_menu/flows_exib_template.html',rotas = topology.totalRotas , form=form,topology=topology.resultFlows,idGen = topology.idGen)
            
        except:
            print('ERRO')
    rotas = {"total": 0,"video": 0,"audio": 0}       
    return render_template('flow_menu/flows_exib_template.html',rotas = rotas ,form=form)





