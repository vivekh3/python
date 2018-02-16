import tensorflow as tf

x = tf.placeholder("float32", None)
x = [ 18.27762222 -3.28520679 2.48342848 -4.64049053 -6.00347185 -4.08683825 -1.80674195 -2.16284728 -4.48559856 1.90175676]
softmaxx=tf.nn.softmax(x)
with tf.Session() as session:
    result = session.run(softmaxx)
    print(result)
