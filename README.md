Intercom
--------

A daemon and it's minions used for managing you Home. They communicate using ZeroMQ and are built in Python 3.

Components
----------

Intercom is made out of five different kinds of components :
* relay : central communication node, relays messages between other components
* minions : execute instructions
* controllers : send instructions from user interactions
* monitors : read sensors and publish their values
* logic nodes : transform information into instructions
