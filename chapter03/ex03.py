import tensorflow as tf

a = tf.constant(21, dtype=tf.float32)
b = tf.constant(314, dtype=tf.float32)
c = tf.multiply(b, a)
d = tf.sin(c)
e = tf.divide(b, d)

sess = tf.Session()
outs = sess.run(e)
print "outs = {}".format(outs)
