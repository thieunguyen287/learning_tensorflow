import tensorflow as tf

default_graph = tf.get_default_graph()
print default_graph

new_graph = tf.Graph()
print new_graph
