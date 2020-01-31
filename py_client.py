#-*- coding:utf-8 -*-
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from py.thrift.generated import PersonService
from py.thrift.generated import ttypes

try:
    tSocket = TSocket.TSocket("localhost",8899)
    tSocket.setTimeout(600)

    transport = TTransport.TFramedTransport(tSocket)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = PersonService.Client(protocol)

    transport.open();

    person = client.getPersonByUsername("test");
    print person.age
    print person.married
    print person.username

    print "----------------"

    person2 = ttypes.Person();
    person2.username = "test002"
    person2.age = 90
    person2.married = True
    client.savePerson(person2)

    transport.close()

except Thrift.TException,tx:
    print '%s' % tx.message