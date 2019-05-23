import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='QChatterPyClient',  
     version='1.5',
     scripts=['qchatterpy', 'constants.py', 'settings.py'] ,
     data_files=["notification.mp3"],
     author="Polis Flatt",
     author_email="polisflatt@gmail.com",
     description="A client which interfaces with the QChatterServer.",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/polisflatt/QChatterPyClient/",
     packages=setuptools.find_packages(),
     
)
