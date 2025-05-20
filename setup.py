from setuptools import setup, find_packages

setup(
    name='trading_utils',
    version='0.1',
    packages=find_packages(include=['Utils', 'Utils.*']),
    description='Полезные утилиты для парсинга трейдинговых данных',
    python_requires='>=3.7',
)
