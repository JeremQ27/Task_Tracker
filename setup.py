from setuptools import setup
from setuptools.config.expand import entry_points

setup(
    name='task_tracker',
    version='1.0.0',
    description='CLI application to manage tasks.',
    author='Jeremiah',
    author_email='jeremiahquinto0627@gmail.com',
    url='https://github.com/JeremQ27/Task_Tracker',
    py_modules=['app', 'task_processes'],
    entry_points={
        'console_scripts': [
            'task_tracker=app:main'
        ]
    },
    tests_require=[
        'pytest',
    ],
)