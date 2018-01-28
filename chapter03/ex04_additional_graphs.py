import tensorflow as tf

default_graph = tf.get_default_graph()
print default_graph

new_graph = tf.Graph()
print new_graph

a = tf.constant(5)
print a.graph is default_graph
print a.graph is new_graph

with new_graph.as_default():
    print "Now with new_graph as default"
    print "Is initial default graph still default graph? {}".format(default_graph is tf.get_default_graph())
    print "Is new graph default graph? {}".format(new_graph is tf.get_default_graph())
    print "a belongs to default_graph? {}".format(a.graph is default_graph)
    print "a belongs to new_graph? {}".format(a.graph is new_graph)
    print "a belongs to default graph? {}".format(a.graph is tf.get_default_graph())

print "Now we're not in the context of new graph as default anymore"
print "Is initial default graph no default graph again? {}".format(default_graph is tf.get_default_graph())
print "Is new graph still default graph? {}".format(new_graph is tf.get_default_graph())
print "a belongs to default_graph? {}".format(a.graph is default_graph)
print "a belongs to new_graph? {}".format(a.graph is new_graph)
print "a belongs to default graph? {}".format(a.graph is tf.get_default_graph())