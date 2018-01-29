import tensorflow as tf

a = tf.constant([[1, 2], [3, 4]])
b = tf.fill([3, 2], 5)
c = tf.zeros([2, 3])
d = tf.zeros_like(b)
e = tf.ones([2, 3])
f = tf.ones_like(b)
g = tf.random_normal([2, 3])
h = tf.truncated_normal([2, 3])
i = tf.random_uniform([2, 3], minval=-1.0, maxval=1.0)
j = tf.random_shuffle([[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 10, 11, 12]])

with tf.Session() as sess:
    print sess.run(a)
    print sess.run(b)
    print sess.run(c)
    print sess.run(d)
    print sess.run(e)
    print sess.run(f)
    print sess.run(g)
    print sess.run(h)
    print sess.run(i)
    print sess.run(j)
