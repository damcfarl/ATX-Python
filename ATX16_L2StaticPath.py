from acitoolkit.acitoolkit import *
import acitoolkit.acitoolkit as ACI
#import credentials
import csv

# Define static values for VLAN encapsulation type
VLAN = {'encap_type': 'vlan'}

# Define Tenant, AppProfile, and EPG classes
tenant = ACI.Tenant('ATX16')
app = ACI.AppProfile('myapp', tenant)
epg = ACI.EPG('APP', app)

# Get the APIC login credentials
description = 'acitoolkit tutorial application'
creds = Credentials('apic', description)
creds.add_argument('--delete', action='store_true',
                   help='Delete the configuration from the APIC')
args = creds.get()

# Delete the configuration if desired
if args.delete:
    tenant.mark_as_deleted()

# Login to APIC and push the config
session = Session(args.url, args.login, args.password)
session.login()
resp = tenant.push_to_apic(session)
if resp.ok:
    print ('Success')



# While loop to attach EPGs to interfaces based on csv file
with open('server-list.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # print all valuse as for loop works through csv file
        print ('Adding the following to APIC')
        print ('Server: ' + str(row['Hostname']))
        print ('Port: ' + str(row['Node']) + '/' + str(row['Module']) + '/' + str(row['Port']))
        print ('EPG: ' + str(row['EPG']))
        print ('VLAN: ' + str(row['VLAN']))
        print ('\r')
        # assign csv contents to each variable based on the column type
        # (e.g. VLAN column is assigned to csv_vlan variable)
        csv_vlan = row['VLAN']
        csv_node = row['Node']
        csv_module = row['Module']
        csv_port = row['Port']
        csv_epg = row['EPG']
        # if statements to assign the appropriate EPG to the EPG class
        # depedning on the contents of the EPG value in the csv file
        if csv_epg == 'APP':
            epg = ACI.EPG('APP', app)
        elif csv_epg == 'WEB':
            epg = ACI.EPG('WEB', app)
        elif csv_epg == 'DB':
            epg = ACI.EPG('DB', app)
        # Create interface dictionary with all the appropriate values
        INTERFACE = {'type': 'eth', 'pod': '1', 'node': csv_node, 'module': csv_module, 'port': csv_port}
        # Create the physical interface object
        intf = ACI.Interface(INTERFACE['type'],
                             INTERFACE['pod'],
                             INTERFACE['node'],
                             INTERFACE['module'],
                             INTERFACE['port'])
        # Create a VLAN Interface and attach to the physical interface
        vlan_intf = ACI.L2Interface(csv_vlan, VLAN['encap_type'], csv_vlan)
        vlan_intf.attach(intf)

        # Attach the EPG to the VLAN interface
        epg.attach(vlan_intf)

        # Push it all to the APIC
        resp = session.push_to_apic(tenant.get_url(),
                                    tenant.get_json())
        print (resp)
        print ('\r')

        if not resp.ok:
            print

