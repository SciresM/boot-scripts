TYPES = ['0A', '0R', '0M', '1', '2A', '2R', '2M']

ADDRESSES = [0x710009D762, 0x710009D6E4, 0x710009D666, 0x710009D5E8, 0x710009D56A, 0x710009D4EC, 0x710009D46E]

COPYRIGHT_HEADER = '''/*
 * Copyright (c) Atmosphère-NX
 *
 * This program is free software; you can redistribute it and/or modify it
 * under the terms and conditions of the GNU General Public License,
 * version 2, as published by the Free Software Foundation.
 *
 * This program is distributed in the hope it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
 * more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

/* NOTE: This file is auto-generated by max17050_parameters_gen.py, do not edit manually. */
'''

r8  = lambda x, y: ida_bytes.get_32bit(x + y) & 0xFF
r16 = lambda x, y: ida_bytes.get_32bit(x + y) & 0xFFFF
r32 = lambda x, y: ida_bytes.get_32bit(x + y)
r64 = lambda x, y: ida_bytes.get_64bit(x + y)

PARSED_PARAMS = []

for i in xrange(len(TYPES)):
    params = []
    addr = ADDRESSES[i]
    for i in xrange(13):
        params.append(r16(addr, i * 2))
    model_table = []
    for i in xrange(13, 0x3D):
        model_table.append(r16(addr, i * 2))
    params.append(model_table)
    for i in xrange(0x3D, 0x3F):
        params.append(r16(addr, i * 2))
    PARSED_PARAMS.append(params)

def print_params(f, p):
    print >> f, '    .relaxcfg    = 0x%04X,' % p[ 0]
    print >> f, '    .rcomp0      = 0x%04X,' % p[ 1]
    print >> f, '    .tempco      = 0x%04X,' % p[ 2]
    print >> f, '    .ichgterm    = 0x%04X,' % p[ 3]
    print >> f, '    .tgain       = 0x%04X,' % p[ 4]
    print >> f, '    .toff        = 0x%04X,' % p[ 5]
    print >> f, '    .vempty      = 0x%04X,' % p[ 6]
    print >> f, '    .qresidual00 = 0x%04X,' % p[ 7]
    print >> f, '    .qresidual10 = 0x%04X,' % p[ 8]
    print >> f, '    .qresidual20 = 0x%04X,' % p[ 9]
    print >> f, '    .qresidual30 = 0x%04X,' % p[10]
    print >> f, '    .fullcap     = 0x%04X,' % p[11]
    print >> f, '    .vffullcap   = 0x%04X,' % p[12]
    print >> f, '    .modeltbl    = {'
    m = p[13]
    for i in xrange(0, len(m), 8):
        print >> f, '        0x%04X, 0x%04X, 0x%04X, 0x%04X, 0x%04X, 0x%04X, 0x%04X, 0x%04X,' % (m[i+0], m[i+1], m[i+2], m[i+3], m[i+4], m[i+5], m[i+6], m[i+7])
    print >> f, '    },'
    print >> f, '    .fullsocthr  = 0x%04X,' % p[14]
    print >> f, '    .iavgempty   = 0x%04X,' % p[15]


with open('powctl_max17050_custom_parameters.inc', 'w') as f:
    print >> f, COPYRIGHT_HEADER
    for i, tp in enumerate(TYPES):
        print >> f, 'constexpr inline const CustomParameters CustomParameters%s = {' % tp
        print_params(f, PARSED_PARAMS[i])
        print >> f, '};'
        print >> f, ''
