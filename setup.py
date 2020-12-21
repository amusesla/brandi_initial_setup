from setuptools import setup

setup(
    name="brandi",
    version="1.0",
    author="14_wecode",
    install_requires=[
        "requests",
        "bcrypt",
        "PyJWT",
        "PyMySQL",
        "certifi",
        "cffi",
        "click",
        "Flask",
        "Flask-Cors",
        "itsdangerous",
        "Jinja2",
        "protobuf",
        "pycparser",
        "six",
        "Werkzeug",
        "nginx",
        "gunicorn"
    ],
    python_requires=">=3.7"
)