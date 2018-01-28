import tensorflow as tf

a = tf.constant([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=tf.float32)
b = tf.constant([[5, 6, 7, 8], [9, 10, 11, 12]], dtype=tf.float32)
cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=a, logits=b)
reversed_cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=b, logits=a)
softmax_cross_entropy = -tf.reduce_sum(a * tf.log(tf.nn.softmax(b)), axis=-1)
with tf.Session() as sess:
    print sess.run(tf.multiply(a, b))
    print sess.run(cross_entropy)
    print sess.run(reversed_cross_entropy)
    print sess.run(softmax_cross_entropy)

