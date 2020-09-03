import tensorflow as tf


message = tf.constant('welcome to tensorflow')
with tf.Session() as sess:
    print(sess.run(message))


v_1 = tf.constant([1,2,3,4])
v_2 = tf.constant([2,1,5,3])
v_add = v_1 + v_2
with tf.Session() as sess:
    print(sess.run(v_add, feed_dict=None))
