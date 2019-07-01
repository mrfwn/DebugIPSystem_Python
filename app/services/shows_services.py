import requests
import json

devices = {
        "1":"SW1",
        "2":"SW2",
        "3":"SW3",
        "4":"SW4",
        "5":"SW5",
        "6":"SW6",
        "7":"SW7",
        "8":"SW8",
        "11":"SW9",
        "12":"SW10"
    }


def nxapi_call(hostname, payload, username, password, content_type="json"):
    headers={'content-type':'application/%s' % content_type}
    response = requests.post("http://%s/ins" % (hostname),
                             auth=(username, password),
                             headers=headers,
                             data=json.dumps(payload),
                             verify=False,
                             timeout=4)
    if response.status_code == 200:
        if "ins_api" in payload:
            if "type" in payload['ins_api'].keys():
                if "cli_conf" in payload['ins_api']['type']:
                    for result in response.json()['ins_api']['outputs']['output']:
                        if result['code'] != "200":
                            print("--&gt; partial configuration failed, please verify your configuration!")
                            break
        return response.json()
    else:
        msg = "call to failed, status code %d (%s)" % (response.status_code,response.content.decode("utf-8"))
        print(msg)
        raise Exception(msg)

def cli_show(show_command, hostname, username, password):
    payload = [
        {
            "ins_api": {
                "version": "1.0",
                "type": "cli_show_ascii",
                "chunk": "0",
                "sid": "1",
                "input": show_command,
                "output_format": "json"
            }
        }
    ]
    return nxapi_call(hostname, payload, username, password, "json")
    

def selection_device(selection,command):
    results = []
    for device in selection:
        aux = cli_show(command,devices[str(device)],'login','password')
        results.append(aux['ins_api']['outputs']['output']['body'].replace( '\n','<br />'))
        
    return results

