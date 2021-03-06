from models import *


model_zoo = ['DCGAN', 'LSGAN', 'WGAN', 'WGAN-GP', 'EBGAN', 'BEGAN', 'DRAGAN', 'CoulombGAN']

def get_model(mtype, name, training,image_shape=[64,64,3]):
    model = None
    if mtype == 'DCGAN':
        model = dcgan.DCGAN
    elif mtype == 'LSGAN':
        model = lsgan.LSGAN
    elif mtype == 'WGAN':
        model = wgan.WGAN
    elif mtype == 'WGAN-GP':
        model = wgan_gp.WGAN_GP
    elif mtype == 'EBGAN':
        model = ebgan.EBGAN
    elif mtype == 'BEGAN':
        model = began.BEGAN
    elif mtype == 'DRAGAN':
        model = dragan.DRAGAN
    elif mtype == 'COULOMBGAN':
        model = coulombgan.CoulombGAN
    elif mtype == 'DCGAN-GP':
        model = dcgan_gp.DCGAN_GP
    elif mtype == 'WGAN-DRAGAN':
        model = wgan_dragan.WGAN_DRAGAN
    elif mtype == 'DCGAN-CONS':
        model = dcgan_consensus.DCGAN_CONS
    elif mtype == 'DCGAN-LOCAL':
        model = dcgan_local.DCGAN_LOCAL
    else:
        assert False, mtype + ' is not in the model zoo'

    assert model, mtype + ' is work in progress'

    return model(name=name, training=training,image_shape=image_shape)


def get_dataset(dataset_name):
    celebA_64 = './data/celebA_tfrecords/*.tfrecord'
    lsun_bedroom_128 = './data/lsun/bedroom_128_tfrecords/*.tfrecord'
    lsun_bedroom_64 = './data/lsun/bedroom_64_tfrecords/*.tfrecord'

    if dataset_name == 'celeba':
        path = celebA_64
        n_examples = 201599 #1000 images held out for testing
    elif dataset_name == 'lsun':
        path = lsun_bedroom_64
        n_examples = 3033042
    else:
        raise ValueError('{} is does not supported. dataset must be celeba or lsun.'.format(dataset_name))

    return path, n_examples


def pprint_args(FLAGS):
    print("\nParameters:")
    for attr, value in sorted(vars(FLAGS).items()):
        print("{}={}".format(attr.upper(), value))
    print("")

