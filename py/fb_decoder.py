
import flatbuffers
import sys

import Person
import Group
import Client
import ClientList
from ClientUnion import ClientUnion

# Read from bin file
buf = open(sys.argv[1],'rb').read()

client_list = ClientList.ClientList.GetRootAs(buf,0)

number_of_clients = client_list.ClientsLength()

#Iterate on Client_list
for i in range(number_of_clients):
    client = client_list.Clients(i)
    clientType = client.ClientType();
    if clientType == ClientUnion.Person:
        person = Person.Person()
        person.Init(client.Client().Bytes,client.Client().Pos)
        person_name = person.Name()
        person_age = person.Age()
        person_weight = person.Weight()
        person_gender = person.Gender()
        print("{",person_name.decode("utf-8"),",",person_age,",",person_weight,",",person_gender.decode("utf-8"),"}")
    elif clientType == ClientUnion.Group:
        group = Group.Group()
        group.Init(client.Client().Bytes,client.Client().Pos)
        groupname = group.Groupname()
        average_age = group.AverageAge()
        average_weight = group.AverageWeight()
        number_of_peoples = group.NamesLength()
        person_names = "{"
        for j in range(number_of_peoples):
            personName = group.Names(j)
            person_names += personName.decode("utf-8") + ","
        person_names = person_names[:-1] + "}"
        print("{",groupname.decode("utf-8"),",",average_age,",",average_weight,",",person_names,"}")
    else:
        print("Client must be either Person or Group")