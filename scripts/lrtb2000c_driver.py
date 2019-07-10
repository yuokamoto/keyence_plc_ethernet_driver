#!/usr/bin/env python
# Keyence LR-TB2000c driver
import rospy
from std_msgs.msg import Float32
from keyence_plc_ethernet_driver.ethernet_driver import PLCSocket


class LRTB2000(object):
	def __init__(self, socket, device, topic_name='lrtb2000c'):
		self._socket = socket
		self._pub = rospy.Publisher(topic_name, Float32, queue_size=10)
		self._rate = rospy.Rate(10) # 10hz
		self._device = device

	def spin(self):
		while not rospy.is_shutdown():
			data = self._socket.send('RD '+self._device+'.U')
			self._pub.publish(Float32(float(data)*0.001)) #convert to m
			self._rate.sleep()

if __name__ == '__main__':
	rospy.init_node('lrtb200c_driver')
	
	host = rospy.get_param('~host', 'localhost')
	port = rospy.get_param('~port', 8501)
	udp = rospy.get_param('~udp', True)
	
	socket = PLCSocket(host=host, port=port, udp=udp)
	socket.connect()
	lrtb = LRTB2000(socket, 'W05')
	lrtb.spin()
