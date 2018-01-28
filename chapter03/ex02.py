import tensorflow as tf

a = tf.constant(3)
b = tf.constant(9)

c = tf.multiply(a, b)
d = tf.add(a, b)
e = tf.subtract(d, c)
f = tf.add(d, c)
g = tf.divide(f, e)

sess = tf.Session()
outs = sess.run(g)

print "outs = {}".format(outs)
