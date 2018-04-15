import nep
import time

node = nep.node("publisher_node") # Create a new node
conf = node.conf_pub(transport = "ZMQ", mode = "many2many") # Select the configuration of the publisher
pub = node.new_pub("many2may_test", conf) # Set the topic and the configuration of the publisher

# Publish a message each second
while True: 
    msg = "hello world"
    pub.send_string(msg) 
    time.sleep(1)
