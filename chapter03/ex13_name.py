import tensorflow as tf

with tf.Graph().as_default():
    c1 = tf.constant(4, dtype=tf.float64, name='c')
    c2 = tf.constant(4, dtype=tf.float64, name='c')
print c1.name
print c2.name
print c1.graph
print tf.get_default_graph() is c1.graph
