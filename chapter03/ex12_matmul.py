import tensorflow as tf

a = tf.constant([[1, 2, 3],
                 [4, 5, 6]])
print a.get_shape()
x = tf.constant([1, 0, 1])
print x.get_shape()
x = tf.expand_dims(x, 1)
print x.get_shape()

b = tf.matmul(a, x)
sess = tf.InteractiveSession()
print 'matmul result: \n{}'.format(b.eval())
sess.close()
