import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
x = tf.placeholder(tf.float32, shape=[None, 28 * 28])
w = tf.Variable(tf.zeros([28 * 28, 10]))
logits = tf.matmul(x, w)
y = tf.placeholder(tf.float32, shape=[None, 10])
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=logits))
train_op = tf.train.GradientDescentOptimizer(learning_rate=0.5).minimize(loss)
acc = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(logits, 1), tf.argmax(y, 1)), tf.float32))
train_dir = '/tmp/mnist'
epochs = 1000
batch_size = 100
data = input_data.read_data_sets(train_dir=train_dir, one_hot=True)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(epochs):
        batch_x, batch_y = data.train.next_batch(batch_size=batch_size)
        sess.run(train_op, feed_dict={x: batch_x, y: batch_y})
    print "Accuracy: {:.4%}".format(sess.run(acc, feed_dict={x: data.test.images, y: data.test.labels}))
    w_value = sess.run(w)
    with open('w.txt', 'w') as f:
        for d, wi in enumerate(w_value.transpose()):
            wi_t = wi.reshape(-1, 28)
            wi_t = np.round(wi_t, 2)

            f.write('For %d\t\n' % d)
            for i in range(wi_t.shape[0]):
                for j in range(wi_t.shape[1]):
                    f.write('%4.2f  ' % wi_t[i][j])
                f.write('\t\n')
            f.write('\t\n\t\n')
        f.close()



