from protos import a_pb2,b_pb2
import time 
def test_a(name,message):
    hello=a_pb2.HelloMessage()
    hello.name=name
    hello.message=message
    return hello

def test_b(id):
    person=b_pb2.MsgPerson()
    person.id=id
    return person

for i in range(10):
    print(test_a('mike', 'hello world'))
    print(test_b(i))
    time.sleep(1)
