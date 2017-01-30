from setup import setup

setup(name="systeminfo",
      version="0.1",
      url="",
      author="Wei lan",
      author_email="lan.wei@ucdconnect.ie",
      licence="GPL3",
      packages=['systeminfo'],
      entry_points={
          'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
          }
      )