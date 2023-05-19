#  Copyright (c) 2018 Phil Birkelbach
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

import pyavtools.fix as fix

# Set a value in the FIX database.  arg should be "key,value"
def setValue(arg):
    args = arg.split(',')
    fix.db.set_value(args[0].strip(), args[1].strip())

# Change a value in the FIX database by a certain value.  arg should be "key,value"
def changeValue(arg):
    args = arg.split(',')
    i = fix.db.get_item(args[0])
    i.value += i.dtype(args[1])

def toggleBool(arg):
    bit = fix.db.get_item(arg)
    bit.value = not bit.value

def setAoA0g(arg):
    _aoa = fix.db.get_item('AOA')
    print(_aoa._value)
    _aoa.set_aux_value('0g', _aoa._value)

def setAoAWarn(arg):
    _aoa = fix.db.get_item('AOA')
    print(_aoa._value)
    _aoa.set_aux_value('Warn', _aoa._value)

def setAoAStall(arg):
    _aoa = fix.db.get_item('AOA')
    print(_aoa._value)
    _aoa.set_aux_value('Stall', _aoa._value)

