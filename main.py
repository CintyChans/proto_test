from protos import a_pb2
import sys,os
sys.path.append('./protos') #把protos路径添加到环境变量中，否则b_pb2导入会报错
from protos import b_pb2
import time
def test_a(name,message):
    hello=a_pb2.HelloMessage()
    hello.name=name
    hello.message=message
    return hello

def test_b(id,hello):
    person=b_pb2.MsgPerson()
    person.id=id
    person.hellomessage.name=hello.name
    person.hellomessage.message=hello.message
    return person

for i in range(10):
    hello=test_a('mike', 'hello world')
    print(hello)
    person=test_b(i,hello)
    print(person)
    time.sleep(1)
