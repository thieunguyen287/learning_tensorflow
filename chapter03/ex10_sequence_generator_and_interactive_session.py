import tensorflow as tf

sess = tf.InteractiveSession()
c = tf.linspace(0.0, 4.0, 5)
print "The content of 'c': {}".format(c.eval())
sess.close()
