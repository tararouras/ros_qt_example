import threading

import rospy
from std_msgs.msg import String

class RosNode(object):
    def __init__(self):
	self._stop = False
        self._lock = threading.RLock()
        self._callback = None
        self._thread = None
        self._publisher = None
        self._subscriber = None

    def active(self):
        return self._thread is not None and self._thread.is_alive()

    def start(self, callback):
        self._callback = callback
        self._thread = threading.Thread(target=self._work, name='RosNode')
        self._thread.start()

    def stop(self):
        with self._lock:
            self._stop = True
        self._thread.join()

    def _work(self):
        print('%s thread execution starting' % threading.current_thread().name)
	rospy.init_node('example_node', disable_signals=True)
        self._publisher = rospy.Publisher('notifier', String, queue_size=10)
        self._subscriber = rospy.Subscriber('notifiee', String, self._order_arrived)
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            with self._lock:
                if self._stop:
                    break
            rate.sleep()
        print('%s thread execution finished' % threading.current_thread().name)

    def notify(self):
        if not self._publisher:
            return False
        self._publisher.publish('My order please!')
        return True

    def _order_arrived(self, data):
        if self._callback:
            self._callback()
