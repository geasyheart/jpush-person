from distutils.core import setup


def read(fn):
    """

    :param fn:
    :return:
    """
    with open(fn, 'rb') as f:
        content = f.read()
    return content


setup(
    name='jpush-person',
    version='0.0.1',
    packages=['jpush', 'jpush.push'],
    url='https://github.com/geasyheart/jpush-person.git',
    license='MIT License',
    platforms='any',
    author='zhangyu',
    author_email='',
    description='依照jpush官方sdk,实现个人版.',
    long_description=read('README.md').decode('utf-8'),
    install_requires=[
        'requests>=2.18.4',
    ]
)
