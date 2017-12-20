from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):

    def run_tests(self):
        import pytest
        errno = pytest.main([])
        exit(errno)


setup(
    name='Tola',
    version=0.1,
    url='http://www.dongwm.com/',
    author='Dong Weiming',
    license='BSD',
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),  #最后安装的时候需要排除测试相关的文件
    zip_safe=True,        # 出于性能考虑，通常可以把包打包成zip文件。如果包内没有数据文件、C扩展文件等就可以选择压缩
    test_suite='tests',
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
