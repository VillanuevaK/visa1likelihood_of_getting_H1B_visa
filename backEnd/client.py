import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from kevin import kevin
#print (kevin(10, 1, 1,500000,1,-83.1,42.2))

# Use a service account
cred = credentials.Certificate('C:/Users/X007X/Downloads/visa1-a0886e894e54.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

users_ref = db.collection(u'users')
docs = users_ref.get()

#for doc in docs:
#    print(u'{} => {}'.format(doc.id, doc.to_dict()))
l = []
i = 0

for doc in docs:
    l.append(doc.to_dict())
    print(l[i])
    i+=1
    if doc.id!='back':
        db.collection(u'users').document(doc.id).delete()

#print(l)
for i in range(len(l)):
   if(list(l[i].keys())[0]=='data'):
       #print(list(l[i].keys())[0])
       s = l[i]['data']#we're going to upload data back up, so we're going to try and keep the first value as the data we recieve here

print(s)
#most of above recieves the data

###delete data that we recieved from doc###

#db.collection(u'users').document(u'DC').delete()
    

###########################################

string_parameters = s.split(":")
num_parameters = [0,0,0,0,0,0]
for i in range(len(string_parameters)):
    num_parameters[i] = float(string_parameters[i])
    print(num_parameters[i])
    
acceptedOrRejected = 0
acceptedOrRejected = kevin(10, num_parameters[0], num_parameters[1],num_parameters[2],num_parameters[3],num_parameters[4], num_parameters[5])
acceptedOrRejected_stringForm = str(acceptedOrRejected)

#below sends calculated data back
doc_ref = db.collection(u'users').document(u'back')
doc_ref.set({
    u'backend_data': acceptedOrRejected_stringForm,
    #add percent here, remember to tell hirish to make it an int tho
})

