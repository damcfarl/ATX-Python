#!/usr/local/bin/python3.7
# import sys
import requests
import json
#python3
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#python2
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

apic = '10.122.143.36'
tenant = 'ATX16-Postman'
aci_user = 'apic:ACI_TOA\\damcfarl'
aci_pwd = 'cisco!123'

headers = {'content-type': "application/json"}

s = (requests.Session())
print('\n')

# Login to ACI fabric
print("login to ACI fabric: " " "+ apic + "")
url = 'https://' + apic + '/api/mo/aaaLogin.json'
payload = {'aaaUser': {'attributes': {'name': aci_user, 'pwd': aci_pwd}}}
r = s.post(url, data=json.dumps(payload), verify=False)
cookies = r.cookies
print(r.status_code)
print('\n')

url = "https://"+apic+"/api/node/mo/uni/tn-"+tenant+".json"
payload =    {
      "fvTenant": {
        "attributes": {
          "annotation": "",
          "descr": "",
          "dn": "uni/tn-"+tenant+"",
          "name": ""+tenant+"",
          "nameAlias": "",
          "ownerKey": "",
          "ownerTag": ""
        },
        "children": [
          {
            "vnsSvcCont": {
              "attributes": {
                "annotation": ""
              }
            }
          },
          {
            "fvCtx": {
              "attributes": {
                "annotation": "",
                "bdEnforcedEnable": "no",
                "descr": "",
                "ipDataPlaneLearning": "enabled",
                "knwMcastAct": "permit",
                "name": "vrf",
                "nameAlias": "",
                "ownerKey": "",
                "ownerTag": "",
                "pcEnfDir": "ingress",
                "pcEnfPref": "enforced"
              },
              "children": [
                {
                  "fvRsVrfValidationPol": {
                    "attributes": {
                      "annotation": "",
                      "tnL3extVrfValidationPolName": ""
                    }
                  }
                },
                {
                  "vzAny": {
                    "attributes": {
                      "annotation": "",
                      "descr": "",
                      "matchT": "AtleastOne",
                      "name": "",
                      "nameAlias": "",
                      "prefGrMemb": "disabled"
                    }
                  }
                },
                {
                  "fvRsOspfCtxPol": {
                    "attributes": {
                      "annotation": "",
                      "tnOspfCtxPolName": ""
                    }
                  }
                },
                {
                  "fvRsCtxToEpRet": {
                    "attributes": {
                      "annotation": "",
                      "tnFvEpRetPolName": ""
                    }
                  }
                },
                {
                  "fvRsCtxToExtRouteTagPol": {
                    "attributes": {
                      "annotation": "",
                      "tnL3extRouteTagPolName": ""
                    }
                  }
                },
                {
                  "fvRsBgpCtxPol": {
                    "attributes": {
                      "annotation": "",
                      "tnBgpCtxPolName": ""
                    }
                  }
                }
              ]
            }
          },
          {
            "fvBD": {
              "attributes": {
                "OptimizeWanBandwidth": "no",
                "annotation": "",
                "arpFlood": "no",
                "descr": "",
                "epClear": "no",
                "epMoveDetectMode": "",
                "hostBasedRouting": "no",
                "intersiteBumTrafficAllow": "no",
                "intersiteL2Stretch": "no",
                "ipLearning": "yes",
                "limitIpLearnToSubnets": "yes",
                "llAddr": "::",
                "mac": "00:22:BD:F8:19:FF",
                "mcastAllow": "no",
                "multiDstPktAct": "bd-flood",
                "name": "APP",
                "nameAlias": "",
                "ownerKey": "",
                "ownerTag": "",
                "type": "regular",
                "unicastRoute": "yes",
                "unkMacUcastAct": "proxy",
                "unkMcastAct": "flood",
                "v6unkMcastAct": "flood",
                "vmac": "not-applicable"
              },
              "children": [
                {
                  "fvRsMldsn": {
                    "attributes": {
                      "annotation": "",
                      "tnMldSnoopPolName": ""
                    }
                  }
                },
                {
                  "fvRsIgmpsn": {
                    "attributes": {
                      "annotation": "",
                      "tnIgmpSnoopPolName": ""
                    }
                  }
                },
                {
                  "fvRsCtx": {
                    "attributes": {
                      "annotation": "",
                      "tnFvCtxName": "vrf"
                    }
                  }
                },
                {
                  "fvRsBdToEpRet": {
                    "attributes": {
                      "annotation": "",
                      "resolveAct": "resolve",
                      "tnFvEpRetPolName": ""
                    }
                  }
                },
                {
                  "fvRsBDToNdP": {
                    "attributes": {
                      "annotation": "",
                      "tnNdIfPolName": ""
                    }
                  }
                }
              ]
            }
          },
          {
            "fvBD": {
              "attributes": {
                "OptimizeWanBandwidth": "no",
                "annotation": "",
                "arpFlood": "no",
                "descr": "",
                "epClear": "no",
                "epMoveDetectMode": "",
                "hostBasedRouting": "no",
                "intersiteBumTrafficAllow": "no",
                "intersiteL2Stretch": "no",
                "ipLearning": "yes",
                "limitIpLearnToSubnets": "yes",
                "llAddr": "::",
                "mac": "00:22:BD:F8:19:FF",
                "mcastAllow": "no",
                "multiDstPktAct": "bd-flood",
                "name": "DB",
                "nameAlias": "",
                "ownerKey": "",
                "ownerTag": "",
                "type": "regular",
                "unicastRoute": "yes",
                "unkMacUcastAct": "proxy",
                "unkMcastAct": "flood",
                "v6unkMcastAct": "flood",
                "vmac": "not-applicable"
              },
              "children": [
                {
                  "fvRsMldsn": {
                    "attributes": {
                      "annotation": "",
                      "tnMldSnoopPolName": ""
                    }
                  }
                },
                {
                  "fvRsIgmpsn": {
                    "attributes": {
                      "annotation": "",
                      "tnIgmpSnoopPolName": ""
                    }
                  }
                },
                {
                  "fvRsCtx": {
                    "attributes": {
                      "annotation": "",
                      "tnFvCtxName": "vrf"
                    }
                  }
                },
                {
                  "fvRsBdToEpRet": {
                    "attributes": {
                      "annotation": "",
                      "resolveAct": "resolve",
                      "tnFvEpRetPolName": ""
                    }
                  }
                },
                {
                  "fvRsBDToNdP": {
                    "attributes": {
                      "annotation": "",
                      "tnNdIfPolName": ""
                    }
                  }
                }
              ]
            }
          },
          {
            "fvBD": {
              "attributes": {
                "OptimizeWanBandwidth": "no",
                "annotation": "",
                "arpFlood": "no",
                "descr": "",
                "epClear": "no",
                "epMoveDetectMode": "",
                "hostBasedRouting": "no",
                "intersiteBumTrafficAllow": "no",
                "intersiteL2Stretch": "no",
                "ipLearning": "yes",
                "limitIpLearnToSubnets": "yes",
                "llAddr": "::",
                "mac": "00:22:BD:F8:19:FF",
                "mcastAllow": "no",
                "multiDstPktAct": "bd-flood",
                "name": "WEB",
                "nameAlias": "",
                "ownerKey": "",
                "ownerTag": "",
                "type": "regular",
                "unicastRoute": "yes",
                "unkMacUcastAct": "proxy",
                "unkMcastAct": "flood",
                "v6unkMcastAct": "flood",
                "vmac": "not-applicable"
              },
              "children": [
                {
                  "fvRsMldsn": {
                    "attributes": {
                      "annotation": "",
                      "tnMldSnoopPolName": ""
                    }
                  }
                },
                {
                  "fvRsIgmpsn": {
                    "attributes": {
                      "annotation": "",
                      "tnIgmpSnoopPolName": ""
                    }
                  }
                },
                {
                  "fvRsCtx": {
                    "attributes": {
                      "annotation": "",
                      "tnFvCtxName": "vrf"
                    }
                  }
                },
                {
                  "fvRsBdToEpRet": {
                    "attributes": {
                      "annotation": "",
                      "resolveAct": "resolve",
                      "tnFvEpRetPolName": ""
                    }
                  }
                },
                {
                  "fvRsBDToNdP": {
                    "attributes": {
                      "annotation": "",
                      "tnNdIfPolName": ""
                    }
                  }
                }
              ]
            }
          },
          {
            "fvRsTenantMonPol": {
              "attributes": {
                "annotation": "",
                "tnMonEPGPolName": ""
              }
            }
          },
          {
            "fvAp": {
              "attributes": {
                "annotation": "",
                "descr": "",
                "name": "myapp",
                "nameAlias": "",
                "ownerKey": "",
                "ownerTag": "",
                "prio": "unspecified"
              },
              "children": [
                {
                  "fvAEPg": {
                    "attributes": {
                      "annotation": "",
                      "descr": "",
                      "exceptionTag": "",
                      "floodOnEncap": "disabled",
                      "fwdCtrl": "",
                      "hasMcastSource": "no",
                      "isAttrBasedEPg": "no",
                      "matchT": "AtleastOne",
                      "name": "APP",
                      "nameAlias": "",
                      "pcEnfPref": "unenforced",
                      "prefGrMemb": "exclude",
                      "prio": "unspecified",
                      "shutdown": "no"
                    },
                    "children": [
                      {
                        "fvRsCustQosPol": {
                          "attributes": {
                            "annotation": "",
                            "tnQosCustomPolName": ""
                          }
                        }
                      },
                      {
                        "fvRsBd": {
                          "attributes": {
                            "annotation": "",
                            "tnFvBDName": "APP"
                          }
                        }
                      }
                    ]
                  }
                },
                {
                  "fvAEPg": {
                    "attributes": {
                      "annotation": "",
                      "descr": "",
                      "exceptionTag": "",
                      "floodOnEncap": "disabled",
                      "fwdCtrl": "",
                      "hasMcastSource": "no",
                      "isAttrBasedEPg": "no",
                      "matchT": "AtleastOne",
                      "name": "WEB",
                      "nameAlias": "",
                      "pcEnfPref": "unenforced",
                      "prefGrMemb": "exclude",
                      "prio": "unspecified",
                      "shutdown": "no"
                    },
                    "children": [
                      {
                        "fvRsCustQosPol": {
                          "attributes": {
                            "annotation": "",
                            "tnQosCustomPolName": ""
                          }
                        }
                      },
                      {
                        "fvRsBd": {
                          "attributes": {
                            "annotation": "",
                            "tnFvBDName": "WEB"
                          }
                        }
                      }
                    ]
                  }
                },
                {
                  "fvAEPg": {
                    "attributes": {
                      "annotation": "",
                      "descr": "",
                      "exceptionTag": "",
                      "floodOnEncap": "disabled",
                      "fwdCtrl": "",
                      "hasMcastSource": "no",
                      "isAttrBasedEPg": "no",
                      "matchT": "AtleastOne",
                      "name": "DB",
                      "nameAlias": "",
                      "pcEnfPref": "unenforced",
                      "prefGrMemb": "exclude",
                      "prio": "unspecified",
                      "shutdown": "no"
                    },
                    "children": [
                      {
                        "fvRsCustQosPol": {
                          "attributes": {
                            "annotation": "",
                            "tnQosCustomPolName": ""
                          }
                        }
                      },
                      {
                        "fvRsBd": {
                          "attributes": {
                            "annotation": "",
                            "tnFvBDName": "DB"
                          }
                        }
                      }
                    ]
                  }
                }
              ]
            }
          }
        ]
      }
    }
r = s.post(url, data=json.dumps(payload), verify=False)
print(payload)
print(r.text)
print(r.status_code)
print('\n')