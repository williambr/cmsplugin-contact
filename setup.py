from setuptools import setup, find_packages

setup(
    name='cmsplugin-contact',
    version='0.2',
    description='Contact form plugin for Django CMS with spam protection and i18n',
    author='Maccesch',
    author_email='maccesch@gmail.com',
    url='http://github.com/maccesch/cmsplugin_contact',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)
