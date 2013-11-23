FROM okso/7.2

RUN apt-get -y install python3-zmq git
RUN cd /root && git clone https://github.com/oksome/Intercom.git


CMD ["/usr/bin/python3", "/root/Intercom/intercom/minion.py", "ra:5559"]
