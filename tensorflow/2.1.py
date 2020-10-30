import tensorflow as tf
import numpy as np

vector = tf.constant([1, 2, 3])
print(tf.rank(vector))
print(np.ndim(vector))