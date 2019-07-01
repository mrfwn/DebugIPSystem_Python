import requests
import json
import random

class Topology():

    fabricId = 0
    urlNameSDNO = "http://10.175.254.33:8930/Ipvr/Diagnostics/QueryLogicalIOs"
    urlFlowSDNO = "http://10.175.254.33:8930/Ipvr/Diagnostics/QueryDeviceChannelByUriJson?uri="
    valueSDNOname = None
    valueSDNOflow = None
    searchIP = None
    searchName = None
    
    devices = {
        "0":"10.175.254.11",
        "2":"10.175.254.13",
        "4":"10.175.254.15",
        "6":"10.175.254.17",
        "8":"10.175.254.19"       
    }

    gateways = {
        "10.175.254.41":"DC1CTRS1",
        "10.175.254.43":"DC1CTRS2",
        "10.175.254.45":"DC1MST3",
        "10.175.254.47":"DC1MST4",
        "10.175.254.51":"DC2ACV",
        "10.175.254.61":"RF1",
        "10.175.254.63":"RF2",
        "10.175.254.71":"SLH1",
        "10.175.254.73":"SLH2",
        "10.175.254.81":"PVWTEC1",
        "10.175.254.83":"PVWTEC2",
        "10.175.254.91":"CTL1SLA1",
        "10.175.254.93":"CTL1SLA2",
        "10.175.254.95":"CTL1SLA3",
        "10.175.254.97":"CTL1SLA4",
        "10.175.254.103":"DC1EPIC1",
        "10.175.254.109":"DC1EPIC2",
        "10.175.254.115":"DC1EPIC3",
        "10.175.254.121":"DC1EPIC4",
        "10.175.254.127":"DC1EPIC5",
        "10.175.254.133":"DC1EPIC6",
        "10.175.254.139":"DC1EPIC7",
        "10.175.254.145":"DC1EPIC8",
        "10.175.254.151":"DC1EPIC9",
        "10.175.254.157":"DC1EPIC10",
        "10.175.254.163":"DC1EPIC11",
        "10.175.254.169":"DC1EPIC12"
    }  
    
    switchPortName = {
        "0":{
            "1":{
                "gateway":"",
                "slot":""
            },
            "2":{
                "gateway":"",
                "slot":""
            },
            "3":{
                "gateway":"",
                "slot":""
            },
            "4":{
                "gateway":"",
                "slot":""
            },
            "5":{
                "gateway":"",
                "slot":""
            },
            "6":{
                "gateway":"",
                "slot":""
            },
            "7":{
                "gateway":"",
                "slot":""
            },
            "8":{
                "gateway":"",
                "slot":""
            },
            "9":{
                "gateway":"",
                "slot":""
            },
            "10":{
                "gateway":"",
                "slot":""
            },
            "11":{
                "gateway":"",
                "slot":""
            },
            "12":{
                "gateway":"",
                "slot":""
            },
            "13":{
                "gateway":"",
                "slot":""
            },
            "14":{
                "gateway":"",
                "slot":""
            },
            "15":{
                "gateway":"",
                "slot":""
            },
            "16":{
                "gateway":"",
                "slot":""
            },
            "17":{
                "gateway":"",
                "slot":""
            },
            "18":{
                "gateway":"",
                "slot":""
            },
            "19":{
                "gateway":"",
                "slot":""
            },
            "20":{
                "gateway":"",
                "slot":""
            },
            "21":{
                "gateway":"",
                "slot":""
            },
            "22":{
                "gateway":"",
                "slot":""
            },
            "23":{
                "gateway":"",
                "slot":""
            },
            "24":{
                "gateway":"",
                "slot":""
            },
            "25":{
                "gateway":"",
                "slot":""
            },
            "26":{
                "gateway":"",
                "slot":""
            },
            "27":{
                "gateway":"",
                "slot":""
            },
            "28":{
                "gateway":"",
                "slot":""
            },
            "29":{
                "gateway":"",
                "slot":""
            },
            "30":{
                "gateway":"",
                "slot":""
            },
            "31":{
                "gateway":"",
                "slot":""
            },
            "32":{
                "gateway":"",
                "slot":""
            },
            "33":{
                "gateway":"",
                "slot":""
            },
            "34":{
                "gateway":"",
                "slot":""
            },
            "35":{
                "gateway":"",
                "slot":""
            },
            "36":{
                "gateway":"",
                "slot":""
            },
            "37":{
                "gateway":"",
                "slot":""
            },
            "38":{
                "gateway":"",
                "slot":""
            },
            "39":{
                "gateway":"",
                "slot":""
            },
            "40":{
                "gateway":"",
                "slot":""
            },
            "41":{
                "gateway":"",
                "slot":""
            },
            "42":{
                "gateway":"",
                "slot":""
            },
            "43":{
                "gateway":"",
                "slot":""
            },
            "44":{
                "gateway":"",
                "slot":""
            },
            "45":{
                "gateway":"",
                "slot":""
            },
            "46":{
                "gateway":"",
                "slot":""
            },
            "47":{
                "gateway":"",
                "slot":""
            },
            "48":{
                "gateway":"",
                "slot":""
            },
            "49":{
                "gateway":"",
                "slot":""
            },
            "50":{
                "gateway":"",
                "slot":""
            },
            "51":{
                "gateway":"",
                "slot":""
            },
            "52":{
                "gateway":"",
                "slot":""
            }
        },
        "1":{
            "1":{
                "gateway":"",
                "slot":""
            },
            "2":{
                "gateway":"",
                "slot":""
            },
            "3":{
                "gateway":"",
                "slot":""
            },
            "4":{
                "gateway":"",
                "slot":""
            },
            "5":{
                "gateway":"",
                "slot":""
            },
            "6":{
                "gateway":"",
                "slot":""
            },
            "7":{
                "gateway":"",
                "slot":""
            },
            "8":{
                "gateway":"",
                "slot":""
            },
            "9":{
                "gateway":"",
                "slot":""
            },
            "10":{
                "gateway":"",
                "slot":""
            },
            "11":{
                "gateway":"",
                "slot":""
            },
            "12":{
                "gateway":"",
                "slot":""
            },
            "13":{
                "gateway":"",
                "slot":""
            },
            "14":{
                "gateway":"",
                "slot":""
            },
            "15":{
                "gateway":"",
                "slot":""
            },
            "16":{
                "gateway":"",
                "slot":""
            },
            "17":{
                "gateway":"",
                "slot":""
            },
            "18":{
                "gateway":"",
                "slot":""
            },
            "19":{
                "gateway":"",
                "slot":""
            },
            "20":{
                "gateway":"",
                "slot":""
            },
            "21":{
                "gateway":"",
                "slot":""
            },
            "22":{
                "gateway":"",
                "slot":""
            },
            "23":{
                "gateway":"",
                "slot":""
            },
            "24":{
                "gateway":"",
                "slot":""
            },
            "25":{
                "gateway":"",
                "slot":""
            },
            "26":{
                "gateway":"",
                "slot":""
            },
            "27":{
                "gateway":"",
                "slot":""
            },
            "28":{
                "gateway":"",
                "slot":""
            },
            "29":{
                "gateway":"",
                "slot":""
            },
            "30":{
                "gateway":"",
                "slot":""
            },
            "31":{
                "gateway":"",
                "slot":""
            },
            "32":{
                "gateway":"",
                "slot":""
            },
            "33":{
                "gateway":"",
                "slot":""
            },
            "34":{
                "gateway":"",
                "slot":""
            },
            "35":{
                "gateway":"",
                "slot":""
            },
            "36":{
                "gateway":"",
                "slot":""
            },
            "37":{
                "gateway":"",
                "slot":""
            },
            "38":{
                "gateway":"",
                "slot":""
            },
            "39":{
                "gateway":"",
                "slot":""
            },
            "40":{
                "gateway":"",
                "slot":""
            },
            "41":{
                "gateway":"",
                "slot":""
            },
            "42":{
                "gateway":"",
                "slot":""
            },
            "43":{
                "gateway":"",
                "slot":""
            },
            "44":{
                "gateway":"",
                "slot":""
            },
            "45":{
                "gateway":"",
                "slot":""
            },
            "46":{
                "gateway":"",
                "slot":""
            },
            "47":{
                "gateway":"",
                "slot":""
            },
            "48":{
                "gateway":"",
                "slot":""
            },
            "49":{
                "gateway":"",
                "slot":""
            },
            "50":{
                "gateway":"",
                "slot":""
            },
            "51":{
                "gateway":"",
                "slot":""
            },
            "52":{
                "gateway":"",
                "slot":""
            }
        },
        "2":{
            "1":{
                "gateway":"DC1CTRS1",
                "slot":"1"
            },
            "2":{
                "gateway":"DC1CTRS1",
                "slot":"2"
            },
            "3":{
                "gateway":"DC1CTRS1",
                "slot":"3"
            },
            "4":{
                "gateway":"DC1CTRS1",
                "slot":"4"
            },
            "5":{
                "gateway":"DC1CTRS1",
                "slot":"5"
            },
            "6":{
                "gateway":"DC1CTRS1",
                "slot":"6"
            },
            "7":{
                "gateway":"DC1CTRS1",
                "slot":"7"
            },
            "8":{
                "gateway":"DC1CTRS1",
                "slot":"8"
            },
            "9":{
                "gateway":"DC1CTRS1",
                "slot":"9"
            },
            "10":{
                "gateway":"DC1CTRS1",
                "slot":"10"
            },
            "11":{
                "gateway":"DC1CTRS1",
                "slot":"11"
            },
            "12":{
                "gateway":"DC1CTRS1",
                "slot":"12"
            },
            "13":{
                "gateway":"DC1CTRS1",
                "slot":"13"
            },
            "14":{
                "gateway":"DC1CTRS1",
                "slot":"14"
            },
            "15":{
                "gateway":"RF1",
                "slot":"1"
            },
            "16":{
                "gateway":"RF1",
                "slot":"2"
            },
            "17":{
                "gateway":"RF1",
                "slot":"3"
            },
            "18":{
                "gateway":"RF1",
                "slot":"4"
            },
            "19":{
                "gateway":"RF1",
                "slot":"5"
            },
            "20":{
                "gateway":"RF1",
                "slot":"6"
            },
            "21":{
                "gateway":"RF1",
                "slot":"7"
            },
            "22":{
                "gateway":"RF1",
                "slot":"8"
            },
            "23":{
                "gateway":"",
                "slot":""
            },
            "24":{
                "gateway":"",
                "slot":""
            },
            "25":{
                "gateway":"PVWTEC1",
                "slot":"1"
            },
            "26":{
                "gateway":"PVWTEC1",
                "slot":"4"
            },
            "27":{
                "gateway":"PVWTEC1",
                "slot":"5"
            },
            "28":{
                "gateway":"PVWTEC1",
                "slot":"8"
            },
            "29":{
                "gateway":"PVWTEC1",
                "slot":"9"
            },
            "30":{
                "gateway":"",
                "slot":""
            },
            "31":{
                "gateway":"CTL1SLA1",
                "slot":"1"
            },
            "32":{
                "gateway":"CTL1SLA1",
                "slot":"2"
            },
            "33":{
                "gateway":"CTL1SLA1",
                "slot":"3"
            },
            "34":{
                "gateway":"CTL1SLA1",
                "slot":"4"
            },
            "35":{
                "gateway":"CTL1SLA1",
                "slot":"5"
            },
            "36":{
                "gateway":"",
                "slot":""
            },
            "37":{
                "gateway":"CTL1SLA3",
                "slot":"1"
            },
            "38":{
                "gateway":"CTL1SLA3",
                "slot":"2"
            },
            "39":{
                "gateway":"",
                "slot":""
            },
            "40":{
                "gateway":"",
                "slot":""
            },
            "41":{
                "gateway":"",
                "slot":""
            },
            "42":{
                "gateway":"",
                "slot":""
            },
            "43":{
                "gateway":"",
                "slot":""
            },
            "44":{
                "gateway":"",
                "slot":""
            },
            "45":{
                "gateway":"",
                "slot":""
            },
            "46":{
                "gateway":"",
                "slot":""
            },
            "47":{
                "gateway":"",
                "slot":""
            },
            "48":{
                "gateway":"",
                "slot":""
            },
            "49":{
                "gateway":"",
                "slot":""
            },
            "50":{
                "gateway":"",
                "slot":""
            },
            "51":{
                "gateway":"",
                "slot":""
            },
            "52":{
                "gateway":"",
                "slot":""
            }
        },
        "3":{
            "1":{
                "gateway":"DC1CTRS1",
                "slot":"1"
            },
            "2":{
                "gateway":"DC1CTRS1",
                "slot":"2"
            },
            "3":{
                "gateway":"DC1CTRS1",
                "slot":"3"
            },
            "4":{
                "gateway":"DC1CTRS1",
                "slot":"4"
            },
            "5":{
                "gateway":"DC1CTRS1",
                "slot":"5"
            },
            "6":{
                "gateway":"DC1CTRS1",
                "slot":"6"
            },
            "7":{
                "gateway":"DC1CTRS1",
                "slot":"7"
            },
            "8":{
                "gateway":"DC1CTRS1",
                "slot":"8"
            },
            "9":{
                "gateway":"DC1CTRS1",
                "slot":"9"
            },
            "10":{
                "gateway":"DC1CTRS1",
                "slot":"10"
            },
            "11":{
                "gateway":"DC1CTRS1",
                "slot":"11"
            },
            "12":{
                "gateway":"DC1CTRS1",
                "slot":"12"
            },
            "13":{
                "gateway":"DC1CTRS1",
                "slot":"13"
            },
            "14":{
                "gateway":"DC1CTRS1",
                "slot":"14"
            },
            "15":{
                "gateway":"RF1",
                "slot":"1"
            },
            "16":{
                "gateway":"RF1",
                "slot":"2"
            },
            "17":{
                "gateway":"RF1",
                "slot":"3"
            },
            "18":{
                "gateway":"RF1",
                "slot":"4"
            },
            "19":{
                "gateway":"RF1",
                "slot":"5"
            },
            "20":{
                "gateway":"RF1",
                "slot":"6"
            },
            "21":{
                "gateway":"RF1",
                "slot":"7"
            },
            "22":{
                "gateway":"RF1",
                "slot":"8"
            },
            "23":{
                "gateway":"",
                "slot":""
            },
            "24":{
                "gateway":"",
                "slot":""
            },
            "25":{
                "gateway":"PVWTEC1",
                "slot":"1"
            },
            "26":{
                "gateway":"PVWTEC1",
                "slot":"4"
            },
            "27":{
                "gateway":"PVWTEC1",
                "slot":"5"
            },
            "28":{
                "gateway":"PVWTEC1",
                "slot":"8"
            },
            "29":{
                "gateway":"PVWTEC1",
                "slot":"9"
            },
            "30":{
                "gateway":"",
                "slot":""
            },
            "31":{
                "gateway":"CTL1SLA1",
                "slot":"1"
            },
            "32":{
                "gateway":"CTL1SLA1",
                "slot":"2"
            },
            "33":{
                "gateway":"CTL1SLA1",
                "slot":"3"
            },
            "34":{
                "gateway":"CTL1SLA1",
                "slot":"4"
            },
            "35":{
                "gateway":"CTL1SLA1",
                "slot":"5"
            },
            "36":{
                "gateway":"",
                "slot":""
            },
            "37":{
                "gateway":"CTL1SLA3",
                "slot":"1"
            },
            "38":{
                "gateway":"CTL1SLA3",
                "slot":"2"
            },
            "39":{
                "gateway":"",
                "slot":""
            },
            "40":{
                "gateway":"",
                "slot":""
            },
            "41":{
                "gateway":"",
                "slot":""
            },
            "42":{
                "gateway":"",
                "slot":""
            },
            "43":{
                "gateway":"",
                "slot":""
            },
            "44":{
                "gateway":"",
                "slot":""
            },
            "45":{
                "gateway":"",
                "slot":""
            },
            "46":{
                "gateway":"",
                "slot":""
            },
            "47":{
                "gateway":"",
                "slot":""
            },
            "48":{
                "gateway":"",
                "slot":""
            },
            "49":{
                "gateway":"",
                "slot":""
            },
            "50":{
                "gateway":"",
                "slot":""
            },
            "51":{
                "gateway":"",
                "slot":""
            },
            "52":{
                "gateway":"",
                "slot":""
            }
        },
        "4":{
            "1":{
                "gateway":"DC1CTRS2",
                "slot":"1"
            },
            "2":{
                "gateway":"DC1CTRS2",
                "slot":"2"
            },
            "3":{
                "gateway":"DC1CTRS2",
                "slot":"3"
            },
            "4":{
                "gateway":"DC1CTRS2",
                "slot":"4"
            },
            "5":{
                "gateway":"DC1CTRS2",
                "slot":"5"
            },
            "6":{
                "gateway":"DC1CTRS2",
                "slot":"6"
            },
            "7":{
                "gateway":"DC1CTRS2",
                "slot":"7"
            },
            "8":{
                "gateway":"DC1CTRS2",
                "slot":"8"
            },
            "9":{
                "gateway":"DC1CTRS2",
                "slot":"9"
            },
            "10":{
                "gateway":"DC1CTRS2",
                "slot":"10"
            },
            "11":{
                "gateway":"DC1CTRS2",
                "slot":"11"
            },
            "12":{
                "gateway":"DC1CTRS2",
                "slot":"12"
            },
            "13":{
                "gateway":"DC1CTRS2",
                "slot":"13"
            },
            "14":{
                "gateway":"DC1CTRS2",
                "slot":"14"
            },
            "15":{
                "gateway":"RF2",
                "slot":"1"
            },
            "16":{
                "gateway":"RF2",
                "slot":"2"
            },
            "17":{
                "gateway":"RF2",
                "slot":"3"
            },
            "18":{
                "gateway":"RF2",
                "slot":"4"
            },
            "19":{
                "gateway":"RF2",
                "slot":"5"
            },
            "20":{
                "gateway":"RF2",
                "slot":"6"
            },
            "21":{
                "gateway":"RF2",
                "slot":"7"
            },
            "22":{
                "gateway":"RF2",
                "slot":"8"
            },
            "23":{
                "gateway":"",
                "slot":""
            },
            "24":{
                "gateway":"",
                "slot":""
            },
            "25":{
                "gateway":"PVWTEC2",
                "slot":"1"
            },
            "26":{
                "gateway":"PVWTEC2",
                "slot":"4"
            },
            "27":{
                "gateway":"PVWTEC2",
                "slot":"8"
            },
            "28":{
                "gateway":"PVWTEC2",
                "slot":"9"
            },
            "29":{
                "gateway":"DC2ACV",
                "slot":"1"
            },
            "30":{
                "gateway":"DC2ACV",
                "slot":"2"
            },
            "31":{
                "gateway":"CTL1SLA2",
                "slot":"1"
            },
            "32":{
                "gateway":"CTL1SLA2",
                "slot":"2"
            },
            "33":{
                "gateway":"CTL1SLA2",
                "slot":"3"
            },
            "34":{
                "gateway":"CTL1SLA2",
                "slot":"4"
            },
            "35":{
                "gateway":"CTL1SLA4",
                "slot":"1"
            },
            "36":{
                "gateway":"",
                "slot":""
            },
            "37":{
                "gateway":"SLH1",
                "slot":"1"
            },
            "38":{
                "gateway":"SLH1",
                "slot":"2"
            },
            "39":{
                "gateway":"",
                "slot":""
            },
            "40":{
                "gateway":"",
                "slot":""
            },
            "41":{
                "gateway":"",
                "slot":""
            },
            "42":{
                "gateway":"",
                "slot":""
            },
            "43":{
                "gateway":"",
                "slot":""
            },
            "44":{
                "gateway":"",
                "slot":""
            },
            "45":{
                "gateway":"",
                "slot":""
            },
            "46":{
                "gateway":"",
                "slot":""
            },
            "47":{
                "gateway":"",
                "slot":""
            },
            "48":{
                "gateway":"",
                "slot":""
            },
            "49":{
                "gateway":"",
                "slot":""
            },
            "50":{
                "gateway":"",
                "slot":""
            },
            "51":{
                "gateway":"",
                "slot":""
            },
            "52":{
                "gateway":"",
                "slot":""
            }
        },
        "5":{
           "1":{
                "gateway":"DC1CTRS2",
                "slot":"1"
            },
            "2":{
                "gateway":"DC1CTRS2",
                "slot":"2"
            },
            "3":{
                "gateway":"DC1CTRS2",
                "slot":"3"
            },
            "4":{
                "gateway":"DC1CTRS2",
                "slot":"4"
            },
            "5":{
                "gateway":"DC1CTRS2",
                "slot":"5"
            },
            "6":{
                "gateway":"DC1CTRS2",
                "slot":"6"
            },
            "7":{
                "gateway":"DC1CTRS2",
                "slot":"7"
            },
            "8":{
                "gateway":"DC1CTRS2",
                "slot":"8"
            },
            "9":{
                "gateway":"DC1CTRS2",
                "slot":"9"
            },
            "10":{
                "gateway":"DC1CTRS2",
                "slot":"10"
            },
            "11":{
                "gateway":"DC1CTRS2",
                "slot":"11"
            },
            "12":{
                "gateway":"DC1CTRS2",
                "slot":"12"
            },
            "13":{
                "gateway":"DC1CTRS2",
                "slot":"13"
            },
            "14":{
                "gateway":"DC1CTRS2",
                "slot":"14"
            },
            "15":{
                "gateway":"RF2",
                "slot":"1"
            },
            "16":{
                "gateway":"RF2",
                "slot":"2"
            },
            "17":{
                "gateway":"RF2",
                "slot":"3"
            },
            "18":{
                "gateway":"RF2",
                "slot":"4"
            },
            "19":{
                "gateway":"RF2",
                "slot":"5"
            },
            "20":{
                "gateway":"RF2",
                "slot":"6"
            },
            "21":{
                "gateway":"RF2",
                "slot":"7"
            },
            "22":{
                "gateway":"RF2",
                "slot":"8"
            },
            "23":{
                "gateway":"",
                "slot":""
            },
            "24":{
                "gateway":"",
                "slot":""
            },
            "25":{
                "gateway":"PVWTEC2",
                "slot":"1"
            },
            "26":{
                "gateway":"PVWTEC2",
                "slot":"4"
            },
            "27":{
                "gateway":"PVWTEC2",
                "slot":"8"
            },
            "28":{
                "gateway":"PVWTEC2",
                "slot":"9"
            },
            "29":{
                "gateway":"DC2ACV",
                "slot":"1"
            },
            "30":{
                "gateway":"DC2ACV",
                "slot":"2"
            },
            "31":{
                "gateway":"CTL1SLA2",
                "slot":"1"
            },
            "32":{
                "gateway":"CTL1SLA2",
                "slot":"2"
            },
            "33":{
                "gateway":"CTL1SLA2",
                "slot":"3"
            },
            "34":{
                "gateway":"CTL1SLA2",
                "slot":"4"
            },
            "35":{
                "gateway":"CTL1SLA4",
                "slot":"1"
            },
            "36":{
                "gateway":"",
                "slot":""
            },
            "37":{
                "gateway":"SLH1",
                "slot":"1"
            },
            "38":{
                "gateway":"SLH1",
                "slot":"2"
            },
            "39":{
                "gateway":"",
                "slot":""
            },
            "40":{
                "gateway":"",
                "slot":""
            },
            "41":{
                "gateway":"",
                "slot":""
            },
            "42":{
                "gateway":"",
                "slot":""
            },
            "43":{
                "gateway":"",
                "slot":""
            },
            "44":{
                "gateway":"",
                "slot":""
            },
            "45":{
                "gateway":"",
                "slot":""
            },
            "46":{
                "gateway":"",
                "slot":""
            },
            "47":{
                "gateway":"",
                "slot":""
            },
            "48":{
                "gateway":"",
                "slot":""
            },
            "49":{
                "gateway":"",
                "slot":""
            },
            "50":{
                "gateway":"",
                "slot":""
            },
            "51":{
                "gateway":"",
                "slot":""
            },
            "52":{
                "gateway":"",
                "slot":""
            } 
        },
        "6":{
            "1":{
                "gateway":"DC1MST3",
                "slot":"1"
            },
            "2":{
                "gateway":"DC1MST3",
                "slot":"2"
            },
            "3":{
                "gateway":"DC1MST3",
                "slot":"3"
            },
            "4":{
                "gateway":"DC1MST3",
                "slot":"4"
            },
            "5":{
                "gateway":"DC1MST3",
                "slot":"5"
            },
            "6":{
                "gateway":"DC1MST3",
                "slot":"6"
            },
            "7":{
                "gateway":"DC1MST3",
                "slot":"7"
            },
            "8":{
                "gateway":"DC1MST3",
                "slot":"8"
            },
            "9":{
                "gateway":"DC1MST3",
                "slot":"9"
            },
            "10":{
                "gateway":"DC1MST3",
                "slot":"10"
            },
            "11":{
                "gateway":"",
                "slot":""
            },
            "12":{
                "gateway":"",
                "slot":""
            },
            "13":{
                "gateway":"",
                "slot":""
            },
            "14":{
                "gateway":"",
                "slot":""
            },
            "15":{
                "gateway":"",
                "slot":""
            },
            "16":{
                "gateway":"",
                "slot":""
            },
            "17":{
                "gateway":"DC1EPIC1",
                "slot":"1"
            },
            "18":{
                "gateway":"DC1EPIC1",
                "slot":"1"
            },
            "19":{
                "gateway":"DC1EPIC1",
                "slot":"2"
            },
            "20":{
                "gateway":"DC1EPIC1",
                "slot":"2"
            },
            "21":{
                "gateway":"DC1EPIC7",
                "slot":"1"
            },
            "22":{
                "gateway":"DC1EPIC7",
                "slot":"1"
            },
            "23":{
                "gateway":"DC1EPIC9",
                "slot":"1"
            },
            "24":{
                "gateway":"DC1EPIC9",
                "slot":"1"
            },
            "25":{
                "gateway":"DC1EPIC3",
                "slot":"1"
            },
            "26":{
                "gateway":"DC1EPIC3",
                "slot":"1"
            },
            "27":{
                "gateway":"DC1EPIC3",
                "slot":"2"
            },
            "28":{
                "gateway":"DC1EPIC3",
                "slot":"2"
            },
            "29":{
                "gateway":"DC1EPIC11",
                "slot":"1"
            },
            "30":{
                "gateway":"DC1EPIC11",
                "slot":"1"
            },
            "31":{
                "gateway":"DC1EPIC11",
                "slot":"2"
            },
            "32":{
                "gateway":"DC1EPIC11",
                "slot":"2"
            },
            "33":{
                "gateway":"DC1EPIC5",
                "slot":"1"
            },
            "34":{
                "gateway":"DC1EPIC5",
                "slot":"1"
            },
            "35":{
                "gateway":"",
                "slot":""
            },
            "36":{
                "gateway":"",
                "slot":""
            },
            "37":{
                "gateway":"",
                "slot":""
            },
            "38":{
                "gateway":"",
                "slot":""
            },
            "39":{
                "gateway":"",
                "slot":""
            },
            "40":{
                "gateway":"",
                "slot":""
            },
            "41":{
                "gateway":"",
                "slot":""
            },
            "42":{
                "gateway":"",
                "slot":""
            },
            "43":{
                "gateway":"",
                "slot":""
            },
            "44":{
                "gateway":"",
                "slot":""
            },
            "45":{
                "gateway":"",
                "slot":""
            },
            "46":{
                "gateway":"",
                "slot":""
            },
            "47":{
                "gateway":"",
                "slot":""
            },
            "48":{
                "gateway":"",
                "slot":""
            },
            "49":{
                "gateway":"",
                "slot":""
            },
            "50":{
                "gateway":"",
                "slot":""
            },
            "51":{
                "gateway":"",
                "slot":""
            },
            "52":{
                "gateway":"",
                "slot":""
            }
        },
        "7":{
            "1":{
                "gateway":"DC1MST3",
                "slot":"1"
            },
            "2":{
                "gateway":"DC1MST3",
                "slot":"2"
            },
            "3":{
                "gateway":"DC1MST3",
                "slot":"3"
            },
            "4":{
                "gateway":"DC1MST3",
                "slot":"4"
            },
            "5":{
                "gateway":"DC1MST3",
                "slot":"5"
            },
            "6":{
                "gateway":"DC1MST3",
                "slot":"6"
            },
            "7":{
                "gateway":"DC1MST3",
                "slot":"7"
            },
            "8":{
                "gateway":"DC1MST3",
                "slot":"8"
            },
            "9":{
                "gateway":"DC1MST3",
                "slot":"9"
            },
            "10":{
                "gateway":"DC1MST3",
                "slot":"10"
            },
            "11":{
                "gateway":"",
                "slot":""
            },
            "12":{
                "gateway":"",
                "slot":""
            },
            "13":{
                "gateway":"",
                "slot":""
            },
            "14":{
                "gateway":"",
                "slot":""
            },
            "15":{
                "gateway":"",
                "slot":""
            },
            "16":{
                "gateway":"",
                "slot":""
            },
            "17":{
                "gateway":"DC1EPIC1",
                "slot":"1"
            },
            "18":{
                "gateway":"DC1EPIC1",
                "slot":"1"
            },
            "19":{
                "gateway":"DC1EPIC1",
                "slot":"2"
            },
            "20":{
                "gateway":"DC1EPIC1",
                "slot":"2"
            },
            "21":{
                "gateway":"DC1EPIC7",
                "slot":"1"
            },
            "22":{
                "gateway":"DC1EPIC7",
                "slot":"1"
            },
            "23":{
                "gateway":"DC1EPIC9",
                "slot":"1"
            },
            "24":{
                "gateway":"DC1EPIC9",
                "slot":"1"
            },
            "25":{
                "gateway":"DC1EPIC3",
                "slot":"1"
            },
            "26":{
                "gateway":"DC1EPIC3",
                "slot":"1"
            },
            "27":{
                "gateway":"DC1EPIC3",
                "slot":"2"
            },
            "28":{
                "gateway":"DC1EPIC3",
                "slot":"2"
            },
            "29":{
                "gateway":"DC1EPIC11",
                "slot":"1"
            },
            "30":{
                "gateway":"DC1EPIC11",
                "slot":"1"
            },
            "31":{
                "gateway":"DC1EPIC11",
                "slot":"2"
            },
            "32":{
                "gateway":"DC1EPIC11",
                "slot":"2"
            },
            "33":{
                "gateway":"DC1EPIC5",
                "slot":"1"
            },
            "34":{
                "gateway":"DC1EPIC5",
                "slot":"1"
            },
            "35":{
                "gateway":"",
                "slot":""
            },
            "36":{
                "gateway":"",
                "slot":""
            },
            "37":{
                "gateway":"",
                "slot":""
            },
            "38":{
                "gateway":"",
                "slot":""
            },
            "39":{
                "gateway":"",
                "slot":""
            },
            "40":{
                "gateway":"",
                "slot":""
            },
            "41":{
                "gateway":"",
                "slot":""
            },
            "42":{
                "gateway":"",
                "slot":""
            },
            "43":{
                "gateway":"",
                "slot":""
            },
            "44":{
                "gateway":"",
                "slot":""
            },
            "45":{
                "gateway":"",
                "slot":""
            },
            "46":{
                "gateway":"",
                "slot":""
            },
            "47":{
                "gateway":"",
                "slot":""
            },
            "48":{
                "gateway":"",
                "slot":""
            },
            "49":{
                "gateway":"",
                "slot":""
            },
            "50":{
                "gateway":"",
                "slot":""
            },
            "51":{
                "gateway":"",
                "slot":""
            },
            "52":{
                "gateway":"",
                "slot":""
            }
        },
        "8":{
            "1":{
                "gateway":"DC1MST4",
                "slot":"1"
            },
            "2":{
                "gateway":"DC1MST4",
                "slot":"2"
            },
            "3":{
                "gateway":"DC1MST4",
                "slot":"3"
            },
            "4":{
                "gateway":"DC1MST4",
                "slot":"4"
            },
            "5":{
                "gateway":"DC1MST4",
                "slot":"5"
            },
            "6":{
                "gateway":"DC1MST4",
                "slot":"6"
            },
            "7":{
                "gateway":"DC1MST4",
                "slot":"7"
            },
            "8":{
                "gateway":"DC1MST4",
                "slot":"8"
            },
            "9":{
                "gateway":"DC1MST4",
                "slot":"9"
            },
            "10":{
                "gateway":"DC1MST4",
                "slot":"10"
            },
            "11":{
                "gateway":"",
                "slot":""
            },
            "12":{
                "gateway":"",
                "slot":""
            },
            "13":{
                "gateway":"",
                "slot":""
            },
            "14":{
                "gateway":"",
                "slot":""
            },
            "15":{
                "gateway":"",
                "slot":""
            },
            "16":{
                "gateway":"",
                "slot":""
            },
            "17":{
                "gateway":"DC1EPIC2",
                "slot":"1"
            },
            "18":{
                "gateway":"DC1EPIC2",
                "slot":"1"
            },
            "19":{
                "gateway":"DC1EPIC2",
                "slot":"2"
            },
            "20":{
                "gateway":"DC1EPIC2",
                "slot":"2"
            },
            "21":{
                "gateway":"DC1EPIC8",
                "slot":"1"
            },
            "22":{
                "gateway":"DC1EPIC8",
                "slot":"1"
            },
            "23":{
                "gateway":"DC1EPIC8",
                "slot":"2"
            },
            "24":{
                "gateway":"DC1EPIC8",
                "slot":"2"
            },
            "25":{
                "gateway":"DC1EPIC4",
                "slot":"1"
            },
            "26":{
                "gateway":"DC1EPIC4",
                "slot":"1"
            },
            "27":{
                "gateway":"DC1EPIC10",
                "slot":"1"
            },
            "28":{
                "gateway":"DC1EPIC10",
                "slot":"1"
            },
            "29":{
                "gateway":"DC1EPIC10",
                "slot":"2"
            },
            "30":{
                "gateway":"DC1EPIC10",
                "slot":"2"
            },
            "31":{
                "gateway":"DC1EPIC12",
                "slot":"1"
            },
            "32":{
                "gateway":"DC1EPIC12",
                "slot":"1"
            },
            "33":{
                "gateway":"DC1EPIC6",
                "slot":"1"
            },
            "34":{
                "gateway":"DC1EPIC6",
                "slot":"1"
            },
            "35":{
                "gateway":"",
                "slot":""
            },
            "36":{
                "gateway":"",
                "slot":""
            },
            "37":{
                "gateway":"",
                "slot":""
            },
            "38":{
                "gateway":"",
                "slot":""
            },
            "39":{
                "gateway":"",
                "slot":""
            },
            "40":{
                "gateway":"",
                "slot":""
            },
            "41":{
                "gateway":"",
                "slot":""
            },
            "42":{
                "gateway":"",
                "slot":""
            },
            "43":{
                "gateway":"",
                "slot":""
            },
            "44":{
                "gateway":"",
                "slot":""
            },
            "45":{
                "gateway":"",
                "slot":""
            },
            "46":{
                "gateway":"",
                "slot":""
            },
            "47":{
                "gateway":"",
                "slot":""
            },
            "48":{
                "gateway":"",
                "slot":""
            },
            "49":{
                "gateway":"",
                "slot":""
            },
            "50":{
                "gateway":"",
                "slot":""
            },
            "51":{
                "gateway":"",
                "slot":""
            },
            "52":{
                "gateway":"",
                "slot":""
            }
        },
        "9":{
            "1":{
                "gateway":"DC1MST4",
                "slot":"1"
            },
            "2":{
                "gateway":"DC1MST4",
                "slot":"2"
            },
            "3":{
                "gateway":"DC1MST4",
                "slot":"3"
            },
            "4":{
                "gateway":"DC1MST4",
                "slot":"4"
            },
            "5":{
                "gateway":"DC1MST4",
                "slot":"5"
            },
            "6":{
                "gateway":"DC1MST4",
                "slot":"6"
            },
            "7":{
                "gateway":"DC1MST4",
                "slot":"7"
            },
            "8":{
                "gateway":"DC1MST4",
                "slot":"8"
            },
            "9":{
                "gateway":"DC1MST4",
                "slot":"9"
            },
            "10":{
                "gateway":"DC1MST4",
                "slot":"10"
            },
            "11":{
                "gateway":"",
                "slot":""
            },
            "12":{
                "gateway":"",
                "slot":""
            },
            "13":{
                "gateway":"",
                "slot":""
            },
            "14":{
                "gateway":"",
                "slot":""
            },
            "15":{
                "gateway":"",
                "slot":""
            },
            "16":{
                "gateway":"",
                "slot":""
            },
            "17":{
                "gateway":"DC1EPIC2",
                "slot":"1"
            },
            "18":{
                "gateway":"DC1EPIC2",
                "slot":"1"
            },
            "19":{
                "gateway":"DC1EPIC2",
                "slot":"2"
            },
            "20":{
                "gateway":"DC1EPIC2",
                "slot":"2"
            },
            "21":{
                "gateway":"DC1EPIC8",
                "slot":"1"
            },
            "22":{
                "gateway":"DC1EPIC8",
                "slot":"1"
            },
            "23":{
                "gateway":"DC1EPIC8",
                "slot":"2"
            },
            "24":{
                "gateway":"DC1EPIC8",
                "slot":"2"
            },
            "25":{
                "gateway":"DC1EPIC4",
                "slot":"1"
            },
            "26":{
                "gateway":"DC1EPIC4",
                "slot":"1"
            },
            "27":{
                "gateway":"DC1EPIC10",
                "slot":"1"
            },
            "28":{
                "gateway":"DC1EPIC10",
                "slot":"1"
            },
            "29":{
                "gateway":"DC1EPIC10",
                "slot":"2"
            },
            "30":{
                "gateway":"DC1EPIC10",
                "slot":"2"
            },
            "31":{
                "gateway":"DC1EPIC12",
                "slot":"1"
            },
            "32":{
                "gateway":"DC1EPIC12",
                "slot":"1"
            },
            "33":{
                "gateway":"DC1EPIC6",
                "slot":"1"
            },
            "34":{
                "gateway":"DC1EPIC6",
                "slot":"1"
            },
            "35":{
                "gateway":"",
                "slot":""
            },
            "36":{
                "gateway":"",
                "slot":""
            },
            "37":{
                "gateway":"",
                "slot":""
            },
            "38":{
                "gateway":"",
                "slot":""
            },
            "39":{
                "gateway":"",
                "slot":""
            },
            "40":{
                "gateway":"",
                "slot":""
            },
            "41":{
                "gateway":"",
                "slot":""
            },
            "42":{
                "gateway":"",
                "slot":""
            },
            "43":{
                "gateway":"",
                "slot":""
            },
            "44":{
                "gateway":"",
                "slot":""
            },
            "45":{
                "gateway":"",
                "slot":""
            },
            "46":{
                "gateway":"",
                "slot":""
            },
            "47":{
                "gateway":"",
                "slot":""
            },
            "48":{
                "gateway":"",
                "slot":""
            },
            "49":{
                "gateway":"",
                "slot":""
            },
            "50":{
                "gateway":"",
                "slot":""
            },
            "51":{
                "gateway":"",
                "slot":""
            },
            "52":{
                "gateway":"",
                "slot":""
            }
        } 
    }
    
    routesSW = []

    routesPim = []

    routesIgmp = []

    flowTransmiter = []

    flowReceiver = []

    resultFlows = []

    ultimateIP = ""
    
    totalRotas = {
        "total": 0,
        "video": 0,
        "audio": 0
    }

    def __init__(self,searchIP,searchName):
        self.searchIP = searchIP
        self.searchName = searchName.upper()

    def idGen(self):
        hash = random.getrandbits(16)
        return hash

    def nxapi_call(self,hostname, payload, username, password, content_type="json"):
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

    def cli_show(self,show_command, hostname, username, password):
        payload = [
            {
                "ins_api": {
                    "version": "1.0",
                    "type": "cli_show",
                    "chunk": "0",
                    "sid": "1",
                    "input": show_command,
                    "output_format": "json"
                }
            }
        ]
        return self.nxapi_call(hostname, payload, username, password, "json")

    def get_network(self,ip):
        self.ultimateIP = ip
        self.routesSW = []
        for i in self.devices:
            command_pim = "show ip pim route " + ip
            command_igmp = "show ip igmp route " + ip
            routesPim = []
            routesIgmp = []
            auxPim  = self.cli_show(command_pim,self.devices[i],"admin","1234QWer")  
            if "TABLE_addr" in auxPim["ins_api"]["outputs"]["output"]["body"]["TABLE_vrf"]["ROW_vrf"]:
                if len(auxPim["ins_api"]["outputs"]["output"]["body"]["TABLE_vrf"]["ROW_vrf"]["TABLE_addr"]["ROW_addr"]) == 2:            
                    routesPim = []
                    for j in auxPim["ins_api"]["outputs"]["output"]["body"]["TABLE_vrf"]["ROW_vrf"]["TABLE_addr"]["ROW_addr"]:
                        if j["TABLE_rpf"]["ROW_rpf"]["intf-name"]!= "Null":
                            routePim = {
                                "ipMulticast":"",
                                "intName":"",
                                "rpfNbr":"",
                                "ipRp":"" 
                            }
                            if "rp-addr" in j:
                                routePim["ipMulticast"] =  j["mcast-addrs"]
                                routePim["intName"] =  j["TABLE_rpf"]["ROW_rpf"]["intf-name"]
                                routePim["rpfNbr"] =  j["TABLE_rpf"]["ROW_rpf"]["rpf-nbr-addr"]
                                routePim["ipRp"] =  j["rp-addr"]
                                routesPim.append(routePim)
                            else:
                                routePim["ipMulticast"] =  j["mcast-addrs"]
                                routePim["intName"] =  j["TABLE_rpf"]["ROW_rpf"]["intf-name"]
                                routePim["rpfNbr"] =  j["TABLE_rpf"]["ROW_rpf"]["rpf-nbr-addr"]
                                routesPim.append(routePim)
                elif len(auxPim["ins_api"]["outputs"]["output"]["body"]["TABLE_vrf"]["ROW_vrf"]["TABLE_addr"]["ROW_addr"]) == 11:
                    a = auxPim["ins_api"]["outputs"]["output"]["body"]["TABLE_vrf"]["ROW_vrf"]["TABLE_addr"]["ROW_addr"]
                    if a["TABLE_rpf"]["ROW_rpf"]["intf-name"]!= "Null":
                            routePim = {
                                "ipMulticast":"",
                                "intName":"",
                                "rpfNbr":"",
                                "ipRp":"" 
                            }
                            if "rp-addr" in a:
                                routePim["ipMulticast"] =  a["mcast-addrs"]
                                routePim["intName"] =  a["TABLE_rpf"]["ROW_rpf"]["intf-name"]
                                routePim["rpfNbr"] =  a["TABLE_rpf"]["ROW_rpf"]["rpf-nbr-addr"]
                                routePim["ipRp"] =  a["rp-addr"]
                                routesPim.append(routePim)
                            else:
                                routePim["ipMulticast"] =  a["mcast-addrs"]
                                routePim["intName"] =  a["TABLE_rpf"]["ROW_rpf"]["intf-name"]
                                routePim["rpfNbr"] =  a["TABLE_rpf"]["ROW_rpf"]["rpf-nbr-addr"]
                                routesPim.append(routePim)  
            if int(i)>1:                
                auxIgmp  = self.cli_show(command_igmp,self.devices[i],"admin","1234QWer")
                aux = auxIgmp["ins_api"]["outputs"]["output"]["body"]["TABLE_vrf"]["ROW_vrf"]["TABLE_group"]["ROW_group"]
                routesIgmp = []
                for k in range(len(aux)):
                   routeIgmp = {
                        "ipMulticast":"",
                        "intName":"",
                        "reporter":"" 
                    } 
                   if len(aux) > 1 and k > 0:
                        routeIgmp["ipMulticast"] = aux[k]["group-addr"]
                        routeIgmp["intName"] = aux[k]["TABLE_source"]["ROW_source"]["if-name"]
                        routeIgmp["reporter"] = aux[k]["TABLE_source"]["ROW_source"]["reporter"]
                        routesIgmp.append(routeIgmp)
            self.routesSW.append([routesPim,routesIgmp])
        

    def get_src(self,source):
        for i in self.valueSDNOname:
            if (source == i['Uri'] and i['SrcUri'] == '' and i["DeviceChannelStatus"] == "Online"):
                return i


    def split_string(self,string):
        string = string[6:]
        string = string.split('/',6)
        string[1] = string[1][string[1].index(":")+1:]
        string[2] = string[2][string[2].index(":")+1:]
        string[3] = string[3][string[3].index(":")+1:]
        return string

    def validate_name_SDNO(self,name):
        self.searchName = name
        self.valueSDNOname = json.loads(requests.get(self.urlNameSDNO).content)
        validResults = []
        nameResults = []
        flows = []
        for i in self.valueSDNOname:
            if ((name in i['SrcUri'] or name in i['Uri']) and (i["DeviceChannelStatus"] == "Online")):
                   validResults.append(i)
                   if name in i['SrcUri']:
                        if i['SrcUri'] not in nameResults:
                            nameResults.append(i['SrcUri'])
                   else:
                        if i['Uri'] not in nameResults:
                            nameResults.append(i['Uri'])

        for j in nameResults:
            srcFlow = []
            dstFlow = []
            for k in validResults:
                if j in k['Uri'] and k['SrcUri'] == '': 
                    srcFlow.append(k)
                elif j in k['Uri']:
                    dstFlow.append(k)
                elif j in k['SrcUri']:                    
                    srcFlow.append(k)   
            flows.append([srcFlow,dstFlow]) 
        for i in range(len(flows)):
            vetAux = []
            for j in range(len(flows[i])):
                if len(flows[i][0]) != 0 and len(flows[i][1]) != 0:
                    for k in range(len(flows[i][j])):
                        if j == 0:
                            flow = {
                                "mcastFabricTit":"",
                                "mcastFabricBy":"",
                                "directionFlow":"",
                                "nameSrc":"",
                                "nameDst":"",
                                "typeFlow":"",
                                "ipCtrlGWsrc":"",
                                "ipCtrlGWdst":"",
                                "nameGWsrc":"",
                                "nameGWdst":"",
                                "slotGWsrc":"",
                                "slotGWdst":"",
                                "portGWsrc":"",
                                "portGWdst":"",
                                "channelGWsrc":"",
                                "channelGWdst":"",
                                "ipUniGWFabricTit":"",
                                "ipUniGWFabricBy":"",
                                "nameSwSrcTit":"",
                                "nameSwRPTit":"",
                                "namePortRPTit":"",
                                "nameSwDstTit":"",
                                "namePortSrcTit":"",
                                "namePortDstTit":"",
                                "nameSwSrcSby":"",
                                "nameSwRPSby":"",
                                "namePortRPSby":"",
                                "nameSwDstSby":"",
                                "namePortSrcSby":"",
                                "namePortDstSby":""
                            }
                            if k < (len(flows[i][j])-1):
                                flow["nameSrc"] = flows[i][j][k]["SrcUri"][:flows[i][j][k]["SrcUri"].index(".")]
                                flow["nameDst"] = flows[i][j][k]["Uri"][:flows[i][j][k]["Uri"].index(".")]
                                flow["mcastFabricTit"] = flows[i][j][k]["MulticastPrimary"][:flows[i][j][k]["MulticastPrimary"].index(":")]
                                flow["mcastFabricBy"] = flows[i][j][k]["MulticastSecondary"][:flows[i][j][k]["MulticastSecondary"].index(":")]
                                vetor_value = self.split_string(flows[i][j][k]["DeviceChannel"])
                                flow["ipCtrlGWdst"] = vetor_value[0]
                                flow["nameGWdst"] = self.gateways[flow["ipCtrlGWdst"]]
                                flow["slotGWdst"] = vetor_value[1]
                                flow["portGWdst"] = vetor_value[2]
                                flow["channelGWdst"] = vetor_value[3]
                                flow["typeFlow"] = vetor_value[5]
                                vetor_value = self.split_string(flows[i][j][len(flows[i][j])-1]["DeviceChannel"])
                                flow["ipCtrlGWsrc"] = vetor_value[0]
                                flow["nameGWsrc"] = self.gateways[flow["ipCtrlGWsrc"]]
                                flow["slotGWsrc"] = vetor_value[1]
                                flow["portGWsrc"] = vetor_value[2]
                                flow["channelGWsrc"] = vetor_value[3]
                                vetAux.append(flow)
                            else:
                                flow = {
                                    "mcastFabricTit":"",
                                    "mcastFabricBy":"",
                                    "directionFlow":"",
                                    "nameSrc":"",
                                    "nameDst":"",
                                    "typeFlow":"",
                                    "ipCtrlGWsrc":"",
                                    "ipCtrlGWdst":"",
                                    "nameGWsrc":"",
                                    "nameGWdst":"",
                                    "slotGWsrc":"",
                                    "slotGWdst":"",
                                    "portGWsrc":"",
                                    "portGWdst":"",
                                    "channelGWsrc":"",
                                    "channelGWdst":"",
                                    "ipUniGWFabricTit":"",
                                    "ipUniGWFabricBy":"",
                                    "nameSwSrcTit":"",
                                    "nameSwRPTit":"",
                                    "namePortRPTit":"",
                                    "nameSwDstTit":"",
                                    "namePortSrcTit":"",
                                    "namePortDstTit":"",
                                    "nameSwSrcSby":"",
                                    "nameSwRPSby":"",
                                    "namePortRPSby":"",
                                    "nameSwDstSby":"",
                                    "namePortSrcSby":"",
                                    "namePortDstSby":""
                                }
                                '''
                                flow["nameSrc"] = flows[i][j][k]["Uri"][:flows[i][j][k]["Uri"].index(".")]
                                flow["mcastFabricTit"] = flows[i][j][k]["MulticastPrimary"][:flows[i][j][k]["MulticastPrimary"].index(":")]
                                flow["mcastFabricBy"] = flows[i][j][k]["MulticastSecondary"][:flows[i][j][k]["MulticastSecondary"].index(":")]
                                vetor_value = self.split_string(flows[i][j][k]["DeviceChannel"])
                                flow["ipCtrlGWsrc"] = vetor_value[0]
                                flow["nameGWsrc"] = self.gateways[flow["ipCtrlGWsrc"]]
                                flow["slotGWsrc"] = vetor_value[1]
                                flow["portGWsrc"] = vetor_value[2]
                                flow["channelGWsrc"] = vetor_value[3]
                                flow["typeFlow"] = vetor_value[5]
                                vetAux.append(flow)
                                '''
                        else:
                            flow = {
                                "mcastFabricTit":"",
                                "mcastFabricBy":"",
                                "directionFlow":"",
                                "nameSrc":"",
                                "nameDst":"",
                                "typeFlow":"",
                                "ipCtrlGWsrc":"",
                                "ipCtrlGWdst":"",
                                "nameGWsrc":"",
                                "nameGWdst":"",
                                "slotGWsrc":"",
                                "slotGWdst":"",
                                "portGWsrc":"",
                                "portGWdst":"",
                                "channelGWsrc":"",
                                "channelGWdst":"",
                                "ipUniGWFabricTit":"",
                                "ipUniGWFabricBy":"",
                                "nameSwSrcTit":"",
                                "nameSwRPTit":"",
                                "namePortRPTit":"",
                                "nameSwDstTit":"",
                                "namePortSrcTit":"",
                                "namePortDstTit":"",
                                "nameSwSrcSby":"",
                                "nameSwRPSby":"",
                                "namePortRPSby":"",
                                "nameSwDstSby":"",
                                "namePortSrcSby":"",
                                "namePortDstSby":""
                            }
                            flow["nameSrc"] = flows[i][j][0]["SrcUri"][:flows[i][j][0]["SrcUri"].index(".")]
                            flow["nameDst"] = flows[i][j][0]["Uri"][:flows[i][j][0]["Uri"].index(".")]
                            flow["mcastFabricTit"] = flows[i][j][0]["MulticastPrimary"][:flows[i][j][0]["MulticastPrimary"].index(":")]
                            flow["mcastFabricBy"] = flows[i][j][0]["MulticastSecondary"][:flows[i][j][0]["MulticastSecondary"].index(":")]
                            vetor_value = self.split_string(flows[i][j][0]["DeviceChannel"])
                            flow["ipCtrlGWdst"] = vetor_value[0]
                            flow["nameGWdst"] = self.gateways[flow["ipCtrlGWdst"]]
                            flow["slotGWdst"] = vetor_value[1]
                            flow["portGWdst"] = vetor_value[2]
                            flow["channelGWdst"] = vetor_value[3]
                            flow["typeFlow"] = vetor_value[5]
                            srcVet = self.get_src(flows[i][j][0]["SrcUri"])
                            if srcVet != None:
                                vetor_value = self.split_string(srcVet["DeviceChannel"])
                                flow["ipCtrlGWsrc"] = vetor_value[0]
                                flow["nameGWsrc"] = self.gateways[flow["ipCtrlGWsrc"]]
                                flow["slotGWsrc"] = vetor_value[1]
                                flow["portGWsrc"] = vetor_value[2]
                                flow["channelGWsrc"] = vetor_value[3]
                                vetAux.append(flow)
                elif len(flows[i][1]) == 0 and j==0:
                    if len(flows[i][0])>1:
                        for k in range(len(flows[i][j])):
                            flow = {
                                "mcastFabricTit":"",
                                "mcastFabricBy":"",
                                "directionFlow":"",
                                "nameSrc":"",
                                "nameDst":"",
                                "typeFlow":"",
                                "ipCtrlGWsrc":"",
                                "ipCtrlGWdst":"",
                                "nameGWsrc":"",
                                "nameGWdst":"",
                                "slotGWsrc":"",
                                "slotGWdst":"",
                                "portGWsrc":"",
                                "portGWdst":"",
                                "channelGWsrc":"",
                                "channelGWdst":"",
                                "ipUniGWFabricTit":"",
                                "ipUniGWFabricBy":"",
                                "nameSwSrcTit":"",
                                "nameSwRPTit":"",
                                "namePortRPTit":"",
                                "nameSwDstTit":"",
                                "namePortSrcTit":"",
                                "namePortDstTit":"",
                                "nameSwSrcSby":"",
                                "nameSwRPSby":"",
                                "namePortRPSby":"",
                                "nameSwDstSby":"",
                                "namePortSrcSby":"",
                                "namePortDstSby":""
                            }
                            if k < (len(flows[i][j])-1):
                                flow["nameSrc"] = flows[i][j][k]["SrcUri"][:flows[i][j][k]["SrcUri"].index(".")]
                                flow["nameDst"] = flows[i][j][k]["Uri"][:flows[i][j][k]["Uri"].index(".")]
                                flow["mcastFabricTit"] = flows[i][j][k]["MulticastPrimary"][:flows[i][j][k]["MulticastPrimary"].index(":")]
                                flow["mcastFabricBy"] = flows[i][j][k]["MulticastSecondary"][:flows[i][j][k]["MulticastSecondary"].index(":")]
                                vetor_value = self.split_string(flows[i][j][k]["DeviceChannel"])
                                flow["ipCtrlGWdst"] = vetor_value[0]
                                flow["nameGWdst"] = self.gateways[flow["ipCtrlGWdst"]]
                                flow["slotGWdst"] = vetor_value[1]
                                flow["portGWdst"] = vetor_value[2]
                                flow["channelGWdst"] = vetor_value[3]
                                flow["typeFlow"] = vetor_value[5]
                                vetor_value = self.split_string(flows[i][j][len(flows[i][j])-1]["DeviceChannel"])
                                flow["ipCtrlGWsrc"] = vetor_value[0]
                                flow["nameGWsrc"] = self.gateways[flow["ipCtrlGWsrc"]]
                                flow["slotGWsrc"] = vetor_value[1]
                                flow["portGWsrc"] = vetor_value[2]
                                flow["channelGWsrc"] = vetor_value[3]
                                vetAux.append(flow)
                            else:
                                flow = {
                                    "mcastFabricTit":"",
                                    "mcastFabricBy":"",
                                    "directionFlow":"",
                                    "nameSrc":"",
                                    "nameDst":"",
                                    "typeFlow":"",
                                    "ipCtrlGWsrc":"",
                                    "ipCtrlGWdst":"",
                                    "nameGWsrc":"",
                                    "nameGWdst":"",
                                    "slotGWsrc":"",
                                    "slotGWdst":"",
                                    "portGWsrc":"",
                                    "portGWdst":"",
                                    "channelGWsrc":"",
                                    "channelGWdst":"",
                                    "ipUniGWFabricTit":"",
                                    "ipUniGWFabricBy":"",
                                    "nameSwSrcTit":"",
                                    "nameSwRPTit":"",
                                    "namePortRPTit":"",
                                    "nameSwDstTit":"",
                                    "namePortSrcTit":"",
                                    "namePortDstTit":"",
                                    "nameSwSrcSby":"",
                                    "nameSwRPSby":"",
                                    "namePortRPSby":"",
                                    "nameSwDstSby":"",
                                    "namePortSrcSby":"",
                                    "namePortDstSby": ""
                                }
                                '''
                                flow["nameSrc"] = flows[i][j][k]["Uri"][:flows[i][j][k]["Uri"].index(".")]
                                flow["mcastFabricTit"] = flows[i][j][k]["MulticastPrimary"][:flows[i][j][k]["MulticastPrimary"].index(":")]
                                flow["mcastFabricBy"] = flows[i][j][k]["MulticastSecondary"][:flows[i][j][k]["MulticastSecondary"].index(":")]
                                vetor_value = self.split_string(flows[i][j][k]["DeviceChannel"])
                                flow["ipCtrlGWsrc"] = vetor_value[0]
                                flow["nameGWsrc"] = self.gateways[flow["ipCtrlGWsrc"]]
                                flow["slotGWsrc"] = vetor_value[1]
                                flow["portGWsrc"] = vetor_value[2]
                                flow["channelGWsrc"] = vetor_value[3]
                                flow["typeFlow"] = vetor_value[5]
                                vetAux.append(flow)
                                '''
                    else:
                        flow = {
                            "mcastFabricTit":"",
                            "mcastFabricBy":"",
                            "directionFlow":"",
                            "nameSrc":"",
                            "nameDst":"",
                            "typeFlow":"",
                            "ipCtrlGWsrc":"",
                            "ipCtrlGWdst":"",
                            "nameGWsrc":"",
                            "nameGWdst":"",
                            "slotGWsrc":"",
                            "slotGWdst":"",
                            "portGWsrc":"",
                            "portGWdst":"",
                            "channelGWsrc":"",
                            "channelGWdst":"",
                            "ipUniGWFabricTit":"",
                            "ipUniGWFabricBy":"",
                            "nameSwSrcTit":"",
                            "nameSwRPTit":"",
                            "namePortRPTit":"",
                            "nameSwDstTit":"",
                            "namePortSrcTit":"",
                            "namePortDstTit":"",
                            "nameSwSrcSby":"",
                            "nameSwRPSby":"",
                            "namePortRPSby":"",
                            "nameSwDstSby":"",
                            "namePortSrcSby":"",
                            "namePortDstSby":""
                        }
                        '''
                        flow["nameSrc"] = flows[i][j][0]["Uri"][:flows[i][j][0]["Uri"].index(".")]
                        flow["mcastFabricTit"] = flows[i][j][0]["MulticastPrimary"][:flows[i][j][0]["MulticastPrimary"].index(":")]
                        flow["mcastFabricBy"] = flows[i][j][0]["MulticastSecondary"][:flows[i][j][0]["MulticastSecondary"].index(":")]
                        vetor_value = self.split_string(flows[i][j][0]["DeviceChannel"])
                        flow["ipCtrlGWsrc"] = vetor_value[0]
                        flow["nameGWsrc"] = self.gateways[flow["ipCtrlGWsrc"]]
                        flow["slotGWsrc"] = vetor_value[1]
                        flow["portGWsrc"] = vetor_value[2]
                        flow["channelGWsrc"] = vetor_value[3]
                        flow["typeFlow"] = vetor_value[5]
                        vetAux.append(flow)
                        '''
                
                elif len(flows[i][0]) == 0 and j==1:
                    flow = {
                        "mcastFabricTit":"",
                        "mcastFabricBy":"",
                        "directionFlow":"",
                        "nameSrc":"",
                        "nameDst":"",
                        "typeFlow":"",
                        "ipCtrlGWsrc":"",
                        "ipCtrlGWdst":"",
                        "nameGWsrc":"",
                        "nameGWdst":"",
                        "slotGWsrc":"",
                        "slotGWdst":"",
                        "portGWsrc":"",
                        "portGWdst":"",
                        "channelGWsrc":"",
                        "channelGWdst":"",
                        "ipUniGWFabricTit":"",
                        "ipUniGWFabricBy":"",
                        "nameSwSrcTit":"",
                        "nameSwRPTit":"",
                        "namePortRPTit":"",
                        "nameSwDstTit":"",
                        "namePortSrcTit":"",
                        "namePortDstTit":"",
                        "nameSwSrcSby":"",
                        "nameSwRPSby":"",
                        "namePortRPSby":"",
                        "nameSwDstSby":"",
                        "namePortSrcSby":"",
                        "namePortDstSby":""
                    }
                    flow["nameSrc"] = flows[i][j][0]["SrcUri"][:flows[i][j][0]["SrcUri"].index(".")]
                    flow["nameDst"] = flows[i][j][0]["Uri"][:flows[i][j][0]["Uri"].index(".")]
                    flow["mcastFabricTit"] = flows[i][j][0]["MulticastPrimary"][:flows[i][j][0]["MulticastPrimary"].index(":")]
                    flow["mcastFabricBy"] = flows[i][j][0]["MulticastSecondary"][:flows[i][j][0]["MulticastSecondary"].index(":")]
                    vetor_value = self.split_string(flows[i][j][0]["DeviceChannel"])
                    flow["ipCtrlGWdst"] = vetor_value[0]
                    flow["nameGWdst"] = self.gateways[flow["ipCtrlGWdst"]]
                    flow["slotGWdst"] = vetor_value[1]
                    flow["portGWdst"] = vetor_value[2]
                    flow["channelGWdst"] = vetor_value[3]
                    flow["typeFlow"] = vetor_value[5]
                    srcVet = self.get_src(flows[i][j][0]["SrcUri"])
                    if srcVet != None:
                        vetor_value = self.split_string(srcVet["DeviceChannel"])
                        flow["ipCtrlGWsrc"] = vetor_value[0]
                        flow["nameGWsrc"] = self.gateways[flow["ipCtrlGWsrc"]]
                        flow["slotGWsrc"] = vetor_value[1]
                        flow["portGWsrc"] = vetor_value[2]
                        flow["channelGWsrc"] = vetor_value[3]
                        vetAux.append(flow)                    
            self.resultFlows.append([vetAux])
        return 1 
    
    def writeNet(self,flow):
        for i in range(len(self.routesSW)):
            for j in range(len(self.routesSW[i])):
                for k in range(len(self.routesSW[i][j])):
                    if j == 0:
                        if i == 0 :
                            if flow["nameSwRPTit"] == "" and k == 1:
                                flow["nameSwRPTit"] = "SPINE 1"
                                flow["namePortRPTit"] = self.routesSW[i][j][k]["intName"]
                        elif i == 20:
                            if flow["nameSwRPSby"] == "" and k == 1:
                                flow["nameSwRPSby"] = "SPINE 2"
                        elif len(self.routesSW[i][j])==2:
                            if k == 1:
                                if flow["nameSwSrcTit"] == "":
                                    flow["nameSwSrcTit"] = "LEAF " + str(i)
                                    flow["namePortSrcTit"] = self.routesSW[i][j][k]["intName"]
                    
                    else:
                        for m in range(len(self.switchPortName)):
                            for n in range(len(self.switchPortName[str(m)])):                   
                                if self.switchPortName[str(m)][str(n+1)]["gateway"] == flow["nameGWdst"] and self.switchPortName[str(m)][str(n+1)]["slot"] == flow["slotGWdst"]:
                                    flow["nameSwDstTit"] = "LEAF " + str(m)
                                    flow["namePortDstTit"] = "Ethernet1/" + str(n+1)
                                          
        return flow
        



    def load_flow_NET(self):
        self.totalRotas = {
            "total": 0,
            "video": 0,
            "audio": 0
        }
        for i in self.resultFlows:
            for j in i:
                for k in j:
                    self.totalRotas["total"] = self.totalRotas["total"] + 1
                    if k["typeFlow"] == "Video":
                        self.totalRotas["video"] = self.totalRotas["video"] + 1
                    else:
                        self.totalRotas["audio"] = self.totalRotas["audio"] + 1
                    if self.ultimateIP != k["mcastFabricTit"]:
                        self.get_network(k["mcastFabricTit"])
                    k = self.writeNet(k)             

    def validate_request(self):
        if self.searchIP and self.searchName:
            if self.validate_name_SDNO():
                self.load_flow_SDNO()
                if self.validate_ip_NET():
                    self.load_flow_NET()
                else:
                    return 0
            elif self.validate_ip_SDNO():
                self.load_flow_SDNO()
                if self.validate_ip_NET():
                    self.load_flow_NET()
                else:
                    return 0
            else:
                if self.validate_ip_NET():
                    self.load_flow_NET()
                else:
                    return 0
        elif self.searchIP:
            if self.validate_ip_SDNO():
                self.load_flow_SDNO()
                if self.validate_ip_NET():
                    self.load_flow_NET()
                else:
                    return 0
            else:
                if self.validate_ip_NET():
                    self.load_flow_NET()
                else:
                    return 0
        else:
            self.resultFlows = []
            self.routesSW = []
            if self.validate_name_SDNO(self.searchName):
                self.load_flow_NET()
                return 1
                if self.validate_ip_NET():
                    self.load_flow_NET()
                else:
                    return 0
            else:       
                return 0

    



    

        