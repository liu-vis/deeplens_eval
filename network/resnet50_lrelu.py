from network import Network
import tensorflow as tf

class ResNet50(Network):
    def __init__(self, input, is_training, trainable=True):
        self.is_training = is_training
        super(ResNet50, self).__init__(input, trainable)
    def setup(self):
        (self.feed('data')
             .padding(padding=3, name='data_pad')
             .conv(7, 7, 64, 2, 2, 1, relu=False, name='conv1', padding='VALID')
             .batch_normalization(relu=True, name='bn_conv1')
             .max_pool(3, 3, 2, 2, name='pool1')
             .conv(1, 1, 256, 1, 1, 1, biased=False, relu=False, name='res2a_branch1')
             .batch_normalization(name='bn2a_branch1'))

        (self.feed('pool1')
             .conv(1, 1, 64, 1, 1, 1, biased=False, relu=False, name='res2a_branch2a')
             .batch_normalization(relu=True, name='bn2a_branch2a')
             .conv(3, 3, 64, 1, 1, 1, biased=False, relu=False, name='res2a_branch2b')
             .batch_normalization(relu=True, name='bn2a_branch2b')
             .conv(1, 1, 256, 1, 1, 1, biased=False, relu=False, name='res2a_branch2c')
             .batch_normalization(name='bn2a_branch2c'))

        (self.feed('bn2a_branch1', 
                   'bn2a_branch2c')
             .add(name='res2a')
             .relu(name='res2a_relu')
             .conv(1, 1, 64, 1, 1, 1, biased=False, relu=False, name='res2b_branch2a')
             .batch_normalization(relu=True, name='bn2b_branch2a')
             .conv(3, 3, 64, 1, 1, 1, biased=False, relu=False, name='res2b_branch2b')
             .batch_normalization(relu=True, name='bn2b_branch2b')
             .conv(1, 1, 256, 1, 1, 1, biased=False, relu=False, name='res2b_branch2c')
             .batch_normalization(name='bn2b_branch2c'))

        (self.feed('res2a_relu', 
                   'bn2b_branch2c')
             .add(name='res2b')
             .relu(name='res2b_relu')
             .conv(1, 1, 64, 1, 1, 1, biased=False, relu=False, name='res2c_branch2a')
             .batch_normalization(relu=True, name='bn2c_branch2a')
             .conv(3, 3, 64, 1, 1, 1, biased=False, relu=False, name='res2c_branch2b')
             .batch_normalization(relu=True, name='bn2c_branch2b')
             .conv(1, 1, 256, 1, 1, 1, biased=False, relu=False, name='res2c_branch2c')
             .batch_normalization(name='bn2c_branch2c'))

        (self.feed('res2b_relu', 
                   'bn2c_branch2c')
             .add(name='res2c')
             .relu(name='res2c_relu')
             .conv(1, 1, 512, 2, 2, 1, biased=False, relu=False, name='res3a_branch1')
             .batch_normalization(name='bn3a_branch1'))

        (self.feed('res2c_relu')
             .conv(1, 1, 128, 2, 2, 1, biased=False, relu=False, name='res3a_branch2a')
             .batch_normalization(relu=True, name='bn3a_branch2a')
             .conv(3, 3, 128, 1, 1, 1, biased=False, relu=False, name='res3a_branch2b')
             .batch_normalization(relu=True, name='bn3a_branch2b')
             .conv(1, 1, 512, 1, 1, 1, biased=False, relu=False, name='res3a_branch2c')
             .batch_normalization(name='bn3a_branch2c'))

        (self.feed('bn3a_branch1', 
                   'bn3a_branch2c')
             .add(name='res3a')
             .relu(name='res3a_relu')
             .conv(1, 1, 128, 1, 1, 1, biased=False, relu=False, name='res3b_branch2a')
             .batch_normalization(relu=True, name='bn3b_branch2a')
             .conv(3, 3, 128, 1, 1, 1, biased=False, relu=False, name='res3b_branch2b')
             .batch_normalization(relu=True, name='bn3b_branch2b')
             .conv(1, 1, 512, 1, 1, 1, biased=False, relu=False, name='res3b_branch2c')
             .batch_normalization(name='bn3b_branch2c'))

        (self.feed('res3a_relu', 
                   'bn3b_branch2c')
             .add(name='res3b')
             .relu(name='res3b_relu')
             .conv(1, 1, 128, 1, 1, 1, biased=False, relu=False, name='res3c_branch2a')
             .batch_normalization(relu=True, name='bn3c_branch2a')
             .conv(3, 3, 128, 1, 1, 1, biased=False, relu=False, name='res3c_branch2b')
             .batch_normalization(relu=True, name='bn3c_branch2b')
             .conv(1, 1, 512, 1, 1, 1, biased=False, relu=False, name='res3c_branch2c')
             .batch_normalization(name='bn3c_branch2c'))

        (self.feed('res3b_relu', 
                   'bn3c_branch2c')
             .add(name='res3c')
             .relu(name='res3c_relu')
             .conv(1, 1, 128, 1, 1, 1, biased=False, relu=False, name='res3d_branch2a')
             .batch_normalization(relu=True, name='bn3d_branch2a')
             .conv(3, 3, 128, 1, 1, 1, biased=False, relu=False, name='res3d_branch2b')
             .batch_normalization(relu=True, name='bn3d_branch2b')
             .conv(1, 1, 512, 1, 1, 1, biased=False, relu=False, name='res3d_branch2c')
             .batch_normalization(name='bn3d_branch2c'))

        (self.feed('res3c_relu', 
                   'bn3d_branch2c')
             .add(name='res3d')
             .relu(name='res3d_relu')
             .conv(1, 1, 1024, 1, 1, 1, biased=False, relu=False, name='res4a_branch1')
             .batch_normalization(name='bn4a_branch1'))

        (self.feed('res3d_relu')
             .conv(1, 1, 256, 1, 1, 1, biased=False, relu=False, name='res4a_branch2a')
             .batch_normalization(relu=True, name='bn4a_branch2a')
             .conv(3, 3, 256, 1, 1, 2, biased=False, relu=False, name='res4a_branch2b')
             .batch_normalization(relu=True, name='bn4a_branch2b')
             .conv(1, 1, 1024, 1, 1, 1, biased=False, relu=False, name='res4a_branch2c')
             .batch_normalization(name='bn4a_branch2c'))

        (self.feed('bn4a_branch1', 
                   'bn4a_branch2c')
             .add(name='res4a')
             .relu(name='res4a_relu')
             .conv(1, 1, 256, 1, 1, 1, biased=False, relu=False, name='res4b_branch2a')
             .batch_normalization(relu=True, name='bn4b_branch2a')
             .conv(3, 3, 256, 1, 1, 2, biased=False, relu=False, name='res4b_branch2b')
             .batch_normalization(relu=True, name='bn4b_branch2b')
             .conv(1, 1, 1024, 1, 1, 1, biased=False, relu=False, name='res4b_branch2c')
             .batch_normalization(name='bn4b_branch2c'))

        (self.feed('res4a_relu', 
                   'bn4b_branch2c')
             .add(name='res4b')
             .relu(name='res4b_relu')
             .conv(1, 1, 256, 1, 1, 1, biased=False, relu=False, name='res4c_branch2a')
             .batch_normalization(relu=True, name='bn4c_branch2a')
             .conv(3, 3, 256, 1, 1, 2, biased=False, relu=False, name='res4c_branch2b')
             .batch_normalization(relu=True, name='bn4c_branch2b')
             .conv(1, 1, 1024, 1, 1, 1, biased=False, relu=False, name='res4c_branch2c')
             .batch_normalization(name='bn4c_branch2c'))

        (self.feed('res4b_relu', 
                   'bn4c_branch2c')
             .add(name='res4c')
             .relu(name='res4c_relu')
             .conv(1, 1, 256, 1, 1, 1, biased=False, relu=False, name='res4d_branch2a')
             .batch_normalization(relu=True, name='bn4d_branch2a')
             .conv(3, 3, 256, 1, 1, 2, biased=False, relu=False, name='res4d_branch2b')
             .batch_normalization(relu=True, name='bn4d_branch2b')
             .conv(1, 1, 1024, 1, 1, 1, biased=False, relu=False, name='res4d_branch2c')
             .batch_normalization(name='bn4d_branch2c'))

        (self.feed('res4c_relu', 
                   'bn4d_branch2c')
             .add(name='res4d')
             .relu(name='res4d_relu')
             .conv(1, 1, 256, 1, 1, 1, biased=False, relu=False, name='res4e_branch2a')
             .batch_normalization(relu=True, name='bn4e_branch2a')
             .conv(3, 3, 256, 1, 1, 2, biased=False, relu=False, name='res4e_branch2b')
             .batch_normalization(relu=True, name='bn4e_branch2b')
             .conv(1, 1, 1024, 1, 1, 1, biased=False, relu=False, name='res4e_branch2c')
             .batch_normalization(name='bn4e_branch2c'))

        (self.feed('res4d_relu', 
                   'bn4e_branch2c')
             .add(name='res4e')
             .relu(name='res4e_relu')
             .conv(1, 1, 256, 1, 1, 1, biased=False, relu=False, name='res4f_branch2a')
             .batch_normalization(relu=True, name='bn4f_branch2a')
             .conv(3, 3, 256, 1, 1, 2, biased=False, relu=False, name='res4f_branch2b')
             .batch_normalization(relu=True, name='bn4f_branch2b')
             .conv(1, 1, 1024, 1, 1, 1, biased=False, relu=False, name='res4f_branch2c')
             .batch_normalization(name='bn4f_branch2c'))
        (self.feed('res4e_relu', 
                   'bn4f_branch2c')
             .add(name='res4f')
             .relu(name='res4f_relu'))
        (self.conv(1, 1, 256, 1, 1, 1, biased=False, relu=False, name='spp_conv1')
             .batch_normalization(lrelu=True, name='spp_bn1'))
        (self.avg_pool(40, 40, 40, 40, name='spp_pool_a')
             .conv(1, 1, 32, 1, 1, 1, biased=False, relu=False, name='spp_conv_a')
             .batch_normalization(lrelu=True, name='spp_bn_a')
             .resize(40, name='spp_up_a', method=tf.image.ResizeMethod.BILINEAR))
        (self.feed('spp_bn1')
             .avg_pool(20, 20, 20, 20, name='spp_pool_b')
             .conv(1, 1, 32, 1, 1, 1, biased=False, relu=False, name='spp_conv_b')
             .batch_normalization(lrelu=True, name='spp_bn_b')
             .resize(20, name='spp_up_b', method=tf.image.ResizeMethod.BILINEAR))
        (self.feed('spp_bn1')
             .avg_pool(10, 10, 10, 10, name='spp_pool_c')
             .conv(1, 1, 32, 1, 1, 1, biased=False, relu=False, name='spp_conv_c')
             .batch_normalization(lrelu=True, name='spp_bn_c')
             .resize(10, name='spp_up_c', method=tf.image.ResizeMethod.BILINEAR))
        (self.feed('spp_bn1')
             .avg_pool(5, 5, 5, 5, name='spp_pool_d')
             .conv(1, 1, 32, 1, 1, 1, biased=False, relu=False, name='spp_conv_d')
             .batch_normalization(lrelu=True, name='spp_bn_d')
             .resize(5, name='spp_up_d', method=tf.image.ResizeMethod.BILINEAR))

        (self.feed('spp_bn1', 'spp_up_a', 'spp_up_b', 'spp_up_c', 'spp_up_d')
             .concat(axis=3, name='spp_concat')
             .conv(3, 3, 64, 1, 1, 1, biased=False, relu=False, name='spp_conv2')
             .batch_normalization(lrelu=True, name='spp_bn2')
             .resize(2, name='spp_up2', method=tf.image.ResizeMethod.BILINEAR))
        (self.feed('res2c_relu')
             .conv(3, 3, 64, 1, 1, 1, biased=False, relu=False, name='spp_conv3_1')
             .batch_normalization(lrelu=True, name='spp_bn3_1')
             .feed('spp_up2', 'spp_bn3_1')
             .concat(axis=3, name='spp_concat3')
             .conv(3, 3, 64, 1, 1, 1, biased=False, relu=False, name='spp_conv3_2')
             .batch_normalization(lrelu=True, name='spp_bn3_2')
             .resize(2, name='spp_up3', method=tf.image.ResizeMethod.BILINEAR))
        (self.feed('bn_conv1')
             .conv(3, 3, 64, 1, 1, 1, biased=False, relu=False, name='spp_conv4_1')
             .batch_normalization(lrelu=True, name='spp_bn4_1')
             .feed('spp_up3', 'spp_bn4_1')
             .concat(axis=3, name='spp_concat4')
             .conv(3, 3, 64, 1, 1, 1, biased=False, relu=False, name='spp_conv4_2')
             .batch_normalization(lrelu=True, name='spp_bn4_2')
             .resize(2, name='spp_up4', method=tf.image.ResizeMethod.BILINEAR)
             .conv(3, 3, 64, 1, 1, 1, biased=False, relu=False, name='depth_conv1')
             .batch_normalization(lrelu=True, name='depth_bn1')
             .conv(3, 3, 64, 1, 1, 1, biased=False, relu=False, name='depth_conv2')
             .batch_normalization(relu=False, name='depth_bn2')
             .feed('depth_bn1', 'depth_bn2')
             .add(name='depth_add2')
             .leaky_relu(name='depth_relu2')
             .dropout(rate=0.05, name='depth_drop2')
             .conv(1, 1, 1, 1, 1, 1, biased=True, relu=False, name='depth_pre'))
