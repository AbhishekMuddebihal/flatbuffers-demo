
import flatbuffers
import sys

import Person
import Group
import Client
import ClientList
from ClientUnion import ClientUnion 


builder = flatbuffers.Builder(1024)

# creating person 'Ram'
male_str = builder.CreateString("Male")
female_str = builder.CreateString("Female")

person1_name = builder.CreateString("Ram")

Person.Start(builder)
Person.AddName(builder,person1_name)
Person.AddAge(builder,21)
Person.AddWeight(builder,76.5)
Person.AddGender(builder,male_str)
person1_ram = Person.End(builder)

# Creating group 'FightClub'
person2_name = builder.CreateString("Shyam")
person3_name = builder.CreateString("Raghuveer")

Group.StartNamesVector(builder,3)
builder.PrependUOffsetTRelative(person1_name)
builder.PrependUOffsetTRelative(person2_name)
builder.PrependUOffsetTRelative(person3_name)
person_names_in_group = builder.EndVector()

group1_name = builder.CreateString("FightClub")
Group.Start(builder)
Group.AddNames(builder,person_names_in_group)
Group.AddAverageAge(builder,24.5)
Group.AddAverageWeight(builder,66.0)
Group.AddGroupname(builder,group1_name)
group1 = Group.End(builder)

# Add Person as Client
Client.Start(builder)
Client.AddClientType(builder,ClientUnion.Person)
Client.AddClient(builder,person1_ram)
client1 = Client.End(builder)

# Add Group as Client
Client.Start(builder)
Client.AddClientType(builder,ClientUnion.Group)
Client.AddClient(builder,group1)
client2 = Client.End(builder)

# Create Vector of Clients
ClientList.StartClientsVector(builder,2)
builder.PrependUOffsetTRelative(client2)
builder.PrependUOffsetTRelative(client1)
client_list = builder.EndVector()

ClientList.Start(builder)
ClientList.AddClients(builder,client_list)
clients = ClientList.End(builder)

builder.Finish(clients)

buf = builder.Output()

# Write as bin file
open(sys.argv[1],'wb').write(buf);