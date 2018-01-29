import tensorflow as tf

a = tf.constant(4.0)
print a
print a.dtype
b = tf.constant(4.0, dtype=tf.float64)
print b
print b.dtype
