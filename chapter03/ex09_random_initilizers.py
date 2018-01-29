import tensorflow as tf

a = tf.random_normal([2, 3])
b = tf.truncated_normal([2, 3])
c = tf.random_uniform([2, 3], minval=-1, maxval=1)
with tf.Session() as sess:
    print sess.run(a)
    print sess.run(b)
    print sess.run(c)
