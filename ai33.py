# import torch
import tensorflow as tf
import numpy as np

# print("Số lượng GPU khả dụng: ", len(tf.config.list_physical_devices('GPU')))
# t1 = tf.ones([3,4])*5
# print(t1)
# t2 = tf.random.uniform(shape=(2,2,2), minval=0, maxval=1)
# print(t2)
# l = tf.constant([1,2,3,4])
# print(tf.linalg.diag(l))


# tensor = tf.constant([[1,2,3,4],
#                       [5,6,7,8],
#                       [9,10,11,12]])
# print(tensor[0], tensor[-1])
# print(tensor[:,1:2])
## small = tensor[0:2]
# small = tensor[0:2, 2:]
# print(small)
# tensor = tf.reshape(tensor,(4,3))
# print(tensor)


# a = tf.constant([[1, 2], [3, 4]])
# b = tf.constant([[5, 6], [7, 8]])
# print((2*a + tf.multiply(b,b)))
# print(tf.matmul(a,b))
# print(tf.linalg.det(tf.cast(a,float)))
# print(tf.transpose(b))


image = tf.random.uniform([256, 256, 3], maxval=255, dtype=tf.int32)
# r = image[:,:,0]
# g = image[:,:,1]
# b = image[:,:,2]

# print(tf.reduce_mean(r))
# print(tf.reduce_mean(g))
# print(tf.reduce_mean(b))

# new = tf.stack([0.299*tf.cast(r,float), 0.587*tf.cast(g,float), 0.114*tf.cast(b,float)],axis=-1)
# print(new)

# new = tf.concat([0.299*tf.cast(r,float), 0.587*tf.cast(g,float), 0.114*tf.cast(b,float)],axis=-1)
r = image[:,:,0:1]
g = image[:,:,1:2]
b = image[:,:,2:]
gray = 0.299*tf.cast(r,float)+ 0.587*tf.cast(g,float)+ 0.114*tf.cast(b,float)
print(gray)
# print('\n', tf.image.rgb_to_grayscale(image))

l, r = tf.split(gray, num_or_size_splits=2, axis=1)
p1,p2=tf.split(l, num_or_size_splits=2, axis=0)
p3,p4=tf.split(r, num_or_size_splits=2, axis=0)
print(p1,p2,p3,p4,sep='\n')