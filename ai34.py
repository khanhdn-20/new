import tensorflow as tf

# a = tf.ones([1,9])
# a = tf.reshape(a, [3,3])
# a = tf.expand_dims(a, axis=0)
# b = tf.zeros([1,3,3])
# print(tf.stack([a,b]))

# a=[[1,2],[3,4]]
# b=[[5,6],[7,8]]
# # print(tf.shape(a))
# print(tf.stack([a,b],axis=-1))
# print(tf.concat([a,b],axis=0))
# print(tf.concat([a,b],axis=1))

# r = tf.ragged.constant([[1,2],[3],[],[4,5,6]])
# print(r[2])
# print(r[3])
# print(tf.reduce_sum(r, axis=1))

# n = tf.SparseTensor(indices=[[0,2],[2,0]],values=[10,5],dense_shape=[3,3])
# # sp = tf.sparse.to_dense(n)
# # print(sp)
# # print(sp[0,2] , sp[2,0], sep='\n')

# print(tf.sparse.to_dense(n))
# print(n.values)

stri = tf.constant('Machine learning is fun!')
w = tf.strings.split(stri)
rep = tf.strings.regex_replace(stri, "fun", "powerful")
print(w)
print(rep)

c = tf.Variable([1.0, 2.0, 3.0])
print(c.assign_add(2.0))