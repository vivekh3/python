import tensorflow as tf
sess=tf.InteractiveSession()
t = tf.constant(42.0)
u = tf.constant(37.0)
tu = tf.multiply(t, u)
ut = tf.multiply(u, t)
with sess.as_default():
   tu.eval()  # runs one step
   ut.eval()  # runs one step
   sess.run([tu, ut])  # evaluates both tensors in a single step
   print(sess.run(tu))

   
