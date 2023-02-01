from setuptools import setup

setup(
    name='zktunnel',
    version='0.2',
    py_modules=['zktunnel','Instance'],
    install_requires=[
        'Click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        zktunnel=zktunnel:cli
    '''
)
