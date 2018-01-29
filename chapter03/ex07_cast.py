import tensorflow as tf

x = tf.constant([1, 2, 3], name='x', dtype=tf.float32)
print x
print x.dtype
y = tf.cast(x, tf.int64)
print x
print x.dtype
print y
print y.dtype
