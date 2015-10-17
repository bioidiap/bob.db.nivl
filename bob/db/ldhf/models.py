#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# @author: Tiago de Freitas Pereira<tiago.pereira@idiap.ch>
# @date:   Mon Oct  15 17:41:51 CEST 2015
#
# Copyright (C) 2011-2013 Idiap Research Institute, Martigny, Switzerland
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Table models and functionality for the Long Distance Heterogeneous Face Database (LDHF-DB)

"""

import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey, or_, and_, not_
from bob.db.base.sqlalchemy_migration import Enum, relationship
from sqlalchemy.orm import backref
from sqlalchemy.ext.declarative import declarative_base

import bob.db.verification.utils

import os

Base = declarative_base()

""" Defining protocols. Yes, they are static """
PROTOCOLS = ('split1','split2','split3','split4','split5','split6','split7','split8','split9','split10')

GROUPS    = ('world', 'dev')

PURPOSES   = ('train', 'enroll', 'probe')


class Protocol_File_Association(Base):
  """
  Describe the protocols
  """
  __tablename__ = 'protocol_file_association'

  protocol = Column('protocol', Enum(*PROTOCOLS), primary_key=True)
  group    = Column('group', Enum(*GROUPS), primary_key=True)
  purpose  = Column('purpose', Enum(*PURPOSES), primary_key=True)

  file_id   = Column('file_id',  Integer, ForeignKey('file.id'), primary_key=True)
  client_id  = Column('client_id',  Integer, ForeignKey('client.id'), primary_key=True)

  def __init__(self, protocol, group, purpose, file_id, client_id):
    self.protocol  = protocol
    self.group     = group
    self.purpose   = purpose
    self.file_id   = file_id
    self.client_id = client_id



class Client(Base):
  """
  Information about the clients (identities) of the LDHF.

  """
  __tablename__ = 'client'

  id          = Column(Integer, primary_key=True)
  name        = Column(String(4))  

  def __init__(self, id, name):
    self.id = id
    self.name = name

  def __repr__(self):
    return "<Client({0} {1})>".format(self.id, self.name)


class Annotation(Base):
  """
    - Annotation.id
    - x
    - y

  """  
  __tablename__ = 'annotation'

  file_id = Column(Integer, ForeignKey('file.id'), primary_key=True)
  le_x     = Column(Integer)
  le_y     = Column(Integer)  
  re_x     = Column(Integer)
  re_y     = Column(Integer)  


  def __init__(self, file_id, le_x, le_y, re_x, re_y):
    self.file_id = file_id
    self.le_x          = le_x
    self.le_y          = le_y
    self.re_x          = re_x
    self.re_y          = re_y


  def __repr__(self):
    return "<Annotation(file_id:{0}, le_x={1}, le_y={2}), re_x={3}, re_y={4})>".format(self.file_id, self.le_x, self.le_y, self.re_x, self.re_y)



class File(Base, bob.db.verification.utils.File):
  """
  Information about the files of the LDHF database.

  Each file includes
  * the client id
  """
  __tablename__ = 'file'

  modality_choices = ('VIS', 'NIR')

  id        = Column(Integer, primary_key=True, autoincrement=True)
  path      = Column(String(100), unique=True)
  client_id = Column(Integer, ForeignKey('client.id'))
  modality  = Column(Enum(*modality_choices))
  distance  = Column(String(4))  

  # a back-reference from the client class to a list of files
  client      = relationship("Client", backref=backref("files", order_by=id))
  all_annotations = relationship("Annotation", backref=backref("file"), uselist=True)

  def __init__(self, file_id, image_name, client_id, modality, distance):
    # call base class constructor
    bob.db.verification.utils.File.__init__(self, file_id=file_id, client_id = client_id, path = image_name)
    self.modality = modality
    self.distance = distance

  
  def annotations(self, annotation_type="eyes_center"):
    assert len(self.all_annotations)==1
  
    if annotation_type=="eyes_center":
      return {'reye' : (self.all_annotations[0].re_y, self.all_annotations[0].re_x ), 'leye' : (self.all_annotations[0].le_y, self.all_annotations[0].le_x) }
    else:
      raise ValueError("Annotations type {0} invalid. Only 'eyes_center' is allowed".format(annotation_type))
      
    return data

    



