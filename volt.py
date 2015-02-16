__author__ = 'msullivan'

from volt_modules import vagrant

vagrant.status('virtualbox')
vagrant.up('virtualbox')
vagrant.destroy('virtualbox')