import tensorflow as tf

# print tf.__version__
hello = tf.constant("Hello")
space = tf.constant(", ")
world = tf.constant("World!")
hello_world = hello + space + world
with tf.Session() as sess:
    ans = sess.run(hello_world)

print ans
