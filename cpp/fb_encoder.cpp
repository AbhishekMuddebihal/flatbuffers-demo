
#include "schema_generated.h"
#include <fstream>
#include <iostream>

int main(int argc, const char *argv[]) {
    // Build up a serialized buffer algorithmically:
    flatbuffers::FlatBufferBuilder builder;

    // creating person 'Ram'
    auto male_str = builder.CreateString("Male");
    auto female_str = builder.CreateString("Female");

    auto person1_name = builder.CreateString("Ram");

    auto person1_ram = CreatePerson(builder,person1_name,21,76.5,male_str);
    
    // Creating group 'FightClub'
    auto person2_name = builder.CreateString("Shyam");
    auto person3_name = builder.CreateString("Raghuveer");

    std::vector<flatbuffers::Offset<flatbuffers::String>> names_vector; 
    names_vector.push_back(person1_name);
    names_vector.push_back(person2_name);
    names_vector.push_back(person3_name);
    auto person_names_in_group = builder.CreateVector(names_vector);

    auto group1_name = builder.CreateString("FightClub");

    auto group1 = CreateGroup(builder,group1_name,24.5, 66.0,person_names_in_group);
    
    // Add Person as Client
    auto client1 = CreateClient(builder,ClientUnion_Person,person1_ram.Union());


    // Add Group as Client
    auto client2 = CreateClient(builder,ClientUnion_Group,group1.Union());

    // Create Vector of Clients
    std::vector<flatbuffers::Offset<Client>> clients_vector;
    clients_vector.push_back(client1);
    clients_vector.push_back(client2);
    auto client_list = builder.CreateVector(clients_vector);

    auto clients = CreateClientList(builder,client_list);
    
    builder.Finish(clients);

    uint8_t *buf = builder.GetBufferPointer();
    int buf_size = builder.GetSize();

    std::ofstream fout;
    fout.open("../fb_bytes.bin", std::ios_base::binary | std::ios_base::out);

    if(fout.is_open()){
        fout.write((char*)buf, buf_size);
        fout.close();
    }else{
        std::cout<<"ERROR: not able to open bin file."<<std::endl;
    }
    return 0;
}