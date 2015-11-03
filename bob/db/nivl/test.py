#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Tiago de Freitas Pereira <tiago.pereira@idiap.ch>
# Thu Oct 09 11:27:27 CEST 2014
#
# Copyright (C) 2011-2014 Idiap Research Institute, Martigny, Switzerland
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""A few checks on the protocols of the Near-Infrared and Visible-Light (NIVL) Dataset
"""

import bob.db.nivl

""" Defining protocols. Yes, they are static """
PROTOCOLS = ( 'idiap-comparison_2011-VIS-NIR', \
              'idiap-comparison_2012-VIS-NIR', \
              'idiap-search_2011-VIS-NIR_split1', \
              'idiap-search_2011-VIS-NIR_split2', \
              'idiap-search_2011-VIS-NIR_split3', \
              'idiap-search_2011-VIS-NIR_split4', \
              'idiap-search_2011-VIS-NIR_split5', \
              'idiap-search_2012-VIS-NIR_split1', \
              'idiap-search_2012-VIS-NIR_split2', \
              'idiap-search_2012-VIS-NIR_split3', \
              'idiap-search_2012-VIS-NIR_split4', \
              'idiap-search_2012-VIS-NIR_split5', \
              'original_2011-2012', \
              'original_2012-2011')

GROUPS    = ('world', 'dev', 'eval')

PURPOSES   = ('train', 'enroll', 'probe')




def test01_protocols_purposes_groups():

  #testing protocols

  #possible_protocols = bob.db.nivl.Database().protocols()
  #for p in possible_protocols:
    #assert p  in PROTOCOLS

  #testing purposes
  possible_purposes = bob.db.nivl.Database().purposes()
  for p in possible_purposes:
    assert p  in PURPOSES

  #testing GROUPS
  possible_groups = bob.db.nivl.Database().groups()
  for p in possible_groups:
    assert p  in GROUPS


def test02_original_protocols():

  original_2011_2012 = {'world':0, 'enroll-eval':1281, 'probe-eval':8987}
  original_2012_2011 = {'world':0, 'enroll-eval':1051, 'probe-eval':13166}

  #First protocol
  assert len(bob.db.nivl.Database().objects(protocol='original_2011-2012', groups='world'))                  == original_2011_2012['world']
  assert len(bob.db.nivl.Database().objects(protocol='original_2011-2012', groups='eval', purposes="enroll")) == original_2011_2012['enroll-eval']
  assert len(bob.db.nivl.Database().objects(protocol='original_2011-2012', groups='eval', purposes="probe"))  == original_2011_2012['probe-eval']    

  #Second protocol
  assert len(bob.db.nivl.Database().objects(protocol='original_2012-2011', groups='world'))                  == original_2012_2011['world']
  assert len(bob.db.nivl.Database().objects(protocol='original_2012-2011', groups='eval', purposes="enroll")) == original_2012_2011['enroll-eval']
  assert len(bob.db.nivl.Database().objects(protocol='original_2012-2011', groups='eval', purposes="probe"))  == original_2012_2011['probe-eval']    


def test03_idiap_comparison_protocols():

  idiap_comparison_2011_VIS_NIR = {'world':13780, 'dev-enroll':404, 'dev-probe':6532, 'eval-enroll':62, 'eval-probe':3143}
  idiap_comparison_2012_VIS_NIR = {'world':13780, 'dev-enroll':276, 'dev-probe':6532, 'eval-enroll':288, 'eval-probe':3143}

  #First protocol
  assert len(bob.db.nivl.Database().objects(protocol='idiap-comparison_2011-VIS-NIR', groups='world'))                   == idiap_comparison_2011_VIS_NIR['world']
  assert len(bob.db.nivl.Database().objects(protocol='idiap-comparison_2011-VIS-NIR', groups='dev', purposes="enroll"))  == idiap_comparison_2011_VIS_NIR['dev-enroll']
  assert len(bob.db.nivl.Database().objects(protocol='idiap-comparison_2011-VIS-NIR', groups='dev', purposes="probe"))   == idiap_comparison_2011_VIS_NIR['dev-probe']    
  assert len(bob.db.nivl.Database().objects(protocol='idiap-comparison_2011-VIS-NIR', groups='eval', purposes="enroll")) == idiap_comparison_2011_VIS_NIR['eval-enroll']
  assert len(bob.db.nivl.Database().objects(protocol='idiap-comparison_2011-VIS-NIR', groups='eval', purposes="probe"))  == idiap_comparison_2011_VIS_NIR['eval-probe']    

  #Second protocol
  assert len(bob.db.nivl.Database().objects(protocol='idiap-comparison_2012-VIS-NIR', groups='world'))                   == idiap_comparison_2012_VIS_NIR['world']
  assert len(bob.db.nivl.Database().objects(protocol='idiap-comparison_2012-VIS-NIR', groups='dev', purposes="enroll"))  == idiap_comparison_2012_VIS_NIR['dev-enroll']
  assert len(bob.db.nivl.Database().objects(protocol='idiap-comparison_2012-VIS-NIR', groups='dev', purposes="probe"))   == idiap_comparison_2012_VIS_NIR['dev-probe']    
  assert len(bob.db.nivl.Database().objects(protocol='idiap-comparison_2012-VIS-NIR', groups='eval', purposes="enroll")) == idiap_comparison_2012_VIS_NIR['eval-enroll']
  assert len(bob.db.nivl.Database().objects(protocol='idiap-comparison_2012-VIS-NIR', groups='eval', purposes="probe"))  == idiap_comparison_2012_VIS_NIR['eval-probe']    



def test04_idiap_search_protocols():

  idiap_search_2011_VIS_NIR_splitn = {'world':10658, 'dev-enroll':816, 'dev-probe':12521}
  idiap_search_2012_VIS_NIR_splitn = {'world':10658, 'dev-enroll':490, 'dev-probe':12521}
  
  #Testing first protocol
  for i in range(1,6):
    protocol = "idiap-search_2011-VIS-NIR_split%s"%i

    assert len(bob.db.nivl.Database().objects(protocol=protocol, groups='world'))                   == idiap_search_2011_VIS_NIR_splitn['world']
    assert len(bob.db.nivl.Database().objects(protocol=protocol, groups='dev', purposes="enroll"))  == idiap_search_2011_VIS_NIR_splitn['dev-enroll']
    assert len(bob.db.nivl.Database().objects(protocol=protocol, groups='dev', purposes="probe"))   == idiap_search_2011_VIS_NIR_splitn['dev-probe']    

  for i in range(1,6):
    protocol = "idiap-search_2012-VIS-NIR_split%s"%i

    assert len(bob.db.nivl.Database().objects(protocol=protocol, groups='world'))                   == idiap_search_2012_VIS_NIR_splitn['world']
    assert len(bob.db.nivl.Database().objects(protocol=protocol, groups='dev', purposes="enroll"))  == idiap_search_2012_VIS_NIR_splitn['dev-enroll']
    assert len(bob.db.nivl.Database().objects(protocol=protocol, groups='dev', purposes="probe"))   == idiap_search_2012_VIS_NIR_splitn['dev-probe']    



def test05_annotations():

  db = bob.db.nivl.Database()

  for p in PROTOCOLS:
    for f in db.objects(protocol=p):
      assert f.annotations()["reye"][0] > 0
      assert f.annotations()["reye"][1] > 0

      assert f.annotations()["leye"][0] > 0
      assert f.annotations()["leye"][1] > 0



def test06_strings():
  
  db = bob.db.nivl.Database()

  for p in PROTOCOLS:
    for g in GROUPS:
      for u in PURPOSES:
        files = db.objects(purposes=u, groups=g, protocol=p)
        import ipdb; ipdb.set_trace();
        for f in files:
          #Checking if the strings are correct 
          assert f.purpose  == u
          assert f.protocol == p
          assert f.group    == g



