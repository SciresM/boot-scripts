import sys

def decompile_func(ea):
    if not idaapi.init_hexrays_plugin():
        return False

    f = idaapi.get_func(ea)
    if f is None:
        return False

    cfunc = idaapi.decompile(f, flags=idaapi.DECOMP_NO_CACHE);
    if cfunc is None:
        # Failed to decompile
        return False

    lines = []
    sv = cfunc.get_pseudocode();
    for sline in sv:
        line = idaapi.tag_remove(sline.line);
        lines.append(line)
    return lines

ADDRESS = 0x7100005380

lines = decompile_func(ADDRESS)
assert lines[0].startswith('void __fastcall') and lines[0].endswith('()')
assert lines[ 1] == '{'
assert lines[-1] == '}'

lines = lines[2:-1]

def empty_rule():
    return [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

def empty_param():
    return [None, None, None, None, None, None, None, None, None, None, None, None]

g_battery_limits = [[], [], [], []]
g_battery_params = [empty_param(), empty_param(), empty_param(), empty_param()]

for i in xrange(32):
    g_battery_limits[0].append(empty_rule())
    g_battery_limits[1].append(empty_rule())
    g_battery_limits[2].append(empty_rule())
    g_battery_limits[3].append(empty_rule())

def get_field_index(field):
    '''
    struct BatteryLimits
    {
        _DWORD temperature_type;
        _DWORD min_avg_v_cell;
        _DWORD max_avg_v_cell;
        _DWORD min_battery_done_current;
        _DWORD max_battery_done_current;
        float min_unknown_14;
        float max_unknown_18;
        float min_voltage_fuel_gauge_percentage;
        float max_voltage_fuel_gauge_percentage;
        _DWORD *acceptable_power_states;
        _QWORD num_acceptable_power_states;
        _DWORD check_battery_current;
        bool reinitialize_charger;
        _DWORD charge_voltage_limit;
        _DWORD fast_charge_current_limit;
        _DWORD battery_compensation;
        _DWORD voltage_clamp;
    };
    '''
    if field == 'temperature_type':
        return 0
    if field == 'min_avg_v_cell':
        return 1
    if field == 'max_avg_v_cell':
        return 2
    if field == 'min_battery_done_current':
        return 3
    if field == 'max_battery_done_current':
        return 4
    if field == 'min_unknown_14':
        return 5
    if field == 'max_unknown_18':
        return 6
    if field == 'min_voltage_fuel_gauge_percentage':
        return 7
    if field == 'max_voltage_fuel_gauge_percentage':
        return 8
    if field == 'acceptable_power_states':
        return 9
    if field == 'num_acceptable_power_states':
        return 10
    if field == 'check_battery_current':
        return 11
    if field == 'reinitialize_charger':
        return 12
    if field == 'charge_voltage_limit':
        return 13
    if field == 'fast_charge_current_limit':
        return 14
    if field == 'battery_compensation':
        return 15
    if field == 'voltage_clamp':
        return 16

def get_cp_field_index(field):
    '''
    struct BatterySomethingX
    {
        _DWORD _00;
        _DWORD _04;
        double _08;
        double _10;
    };

    struct BatteryChargeParameters
    {
        _DWORD temp_min;
        _DWORD temp_low;
        _DWORD temp_high;
        _DWORD temp_max;
        _DWORD fast_charge_current_limit_low_voltage;
        _DWORD charge_voltage_limit_default;
        BatterySomethingX *battery_x_table;
        _DWORD battery_x_count;
        double _28;
        double _30;
        BatteryLimits *rules;
        _QWORD num_rules;
    };
    '''
    if field == 'temp_min':
        return 0
    if field == 'temp_low':
        return 1
    if field == 'temp_high':
        return 2
    if field == 'temp_max':
        return 3
    if field == 'fast_charge_current_limit_low_voltage':
        return 4
    if field == 'charge_voltage_limit_default':
        return 5
    if field == 'battery_x_table':
        return 6
    if field == 'battery_x_count':
        return 7
    if field == '_28':
        return 8
    if field == '_30':
        return 9
    if field == 'rules':
        return 10
    if field == 'num_rules':
        return 11

def set_entry(limits, index, fi, value):
    if type(value) is int or type(value) is long:
        limits[index][fi] = (value & 0xFFFFFFFF)
    else:
        limits[index][fi] = value

def set_qword(limits, index, fi, value):
    assert fi <= 15
    assert type(value) is long
    limits[index][fi]     = (value & 0xFFFFFFFF)
    limits[index][fi + 1] = ((value >> 32) & 0xFFFFFFFF)

def parse_line(line):
    global g_battery_limits
    global g_battery_params
    spl = [s.replace(';','').lstrip().rstrip() for s in line.split('=')]
    #print spl
    qword = spl[0].startswith('*(_QWORD *)&')
    if qword:
        spl[0] = spl[0][len('*(_QWORD *)&'):]
    #print spl
    if spl[0].startswith('g_BatteryLimits'):
        limits_ind = '012A'.index(spl[0][len('g_BatteryLimits')])
        spl[0] = spl[0][spl[0].index('[')+1:]
        rule_ind = int(spl[0][:spl[0].index(']')])
        spl[0] = spl[0][spl[0].index(']')+2:]
        field = spl[0]
        value = spl[1]
        if value[0] in '0123456789':
            value = int(spl[1].replace('LL',''), 0) & 0xFFFFFFFFFFFFFFFF
        #print limits_ind, rule_ind, field, value
        if qword:
            set_qword(g_battery_limits[limits_ind], rule_ind, get_field_index(field), value)
        else:
            set_entry(g_battery_limits[limits_ind], rule_ind, get_field_index(field), value)
        return True
    if spl[0].startswith('g_BatteryChargeParameters'):
        params_ind = '012A'.index(spl[0][len('g_BatteryChargeParameters')])
        spl[0] = spl[0][spl[0].index('.')+1:]
        field = spl[0]
        value = spl[1]
        if value[0] in '0123456789':
            if '.' in value:
                value = float(value)
            else:
                value = int(spl[1].replace('LL',''), 0) & 0xFFFFFFFFFFFFFFFF
        if qword:
            set_qword(g_battery_params, params_ind, get_cp_field_index(field), value)
        else:
            set_entry(g_battery_params, params_ind, get_cp_field_index(field), value)
        return True
    if spl[0] in ('g_LowBatteryDataSize', 'g_ChargingRedDataSize', 'g_ChargingDataSize'):
        return True
    return False

good = True
for line in lines:
    if not parse_line(line):
        good = False
        break

def s32(n):
    if n & 0x80000000:
        assert n == 0x80000000
        return ' Min'
    else:
        assert n <= 0x7FFFFFFF
        if n == 0x7FFFFFFF:
            return ' Max'
        else:
            return '%4d' % n

def f32(n):
    if n == 0x40400000:
        return '     3.0'
    if n == 0x41b80000:
        return '    23.0'
    elif n == 0x7F7FFFFF:
        return 'FloatMax'
    elif n == 0xFF7FFFFF:
        return 'FloatMin'
    else:
        print 'ERR! %x' % n
        assert False

def b(x):
    return ['false,', 'true, '][x]

def g(x):
    return '%2.1f' % x

def print_rule(f, rule):
    TEMPS = [
                'BatteryTemperatureLevel::TooLow,  ',
                'BatteryTemperatureLevel::Low,     ',
                'BatteryTemperatureLevel::Medium,  ',
                'BatteryTemperatureLevel::High,    ',
                'BatteryTemperatureLevel::TooHigh, ',
            ]
    print rule
    print >> f, '    { %s%s, %s, %s, %s, %s, %s, %s, %s, %-39s %-51s %s %s %s, %s, %s, %s },' % (TEMPS[rule[0]], s32(rule[1]), s32(rule[2]), s32(rule[3]), s32(rule[4]), f32(rule[5]), f32(rule[6]), f32(rule[7]), f32(rule[8]), rule[9]+',', ('util::size(%s),' % rule[9]), b(rule[11]), b(rule[12]), s32(rule[13]), s32(rule[14]), s32(rule[15]), s32(rule[16]))

def print_params(f, p, n, r):
    print >> f, ('    %%2d, %%2d, %%2d, %%2d, %%s, %%s, %%%ds %%%ds %%5s, %%5s, %%46s, util::size(%%s)' % (n+1, n+1+12)) % (p[0], p[1], p[2], p[3], s32(p[4]), s32(p[5]), p[6]+',', (('util::size(%s)' % p[6]) if p[6] != 'nullptr' else '0')+',', g(p[8]), g(p[9]), r, r)

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

/* NOTE: This file is auto-generated by boot_charger_params.py, do not edit manually. */
'''

lim_names = ['0', '1', '2', '0ForAula']

if not good:
    print 'Failed to parse parameters!'
else:
    for i in xrange(len(g_battery_limits)):
        for j in xrange(len(g_battery_limits[i])):
            if g_battery_limits[i][j] == empty_rule():
                g_battery_limits[i] = g_battery_limits[i][:j]
                break
    for i,limits in enumerate(g_battery_limits):
        for j,rule in enumerate(limits):
            for k,value in enumerate(rule):
                if value is None:
                    print i,j,k
                    assert value is not None
    for i,params in enumerate(g_battery_params):
        for j,value in enumerate(params):
            if value is None:
                print i,j
                assert value is not None
    for i in xrange(len(g_battery_params)):
        if g_battery_params[i][6] == 0:
            g_battery_params[i][6] = 'nullptr'
    with open('powctl_charger_parameters.board.nintendo_nx.inc', 'w') as f:
        print >> f, COPYRIGHT_HEADER
        for i,limit in enumerate(g_battery_limits):
            print >> f, 'constexpr inline const ChargeParametersRule ChargeParametersRulesForBatteryVersion%s[] = {' % lim_names[i]
            for rule in limit:
                print_rule(f, rule)
            print >> f, '};'
            print >> f, ''
        for i,param in enumerate(g_battery_params):
            rule = 'ChargeParametersRulesForBatteryVersion%s' % lim_names[i]
            print >> f, 'constexpr inline const ChargeParameters ChargeParametersForBatteryVersion%s = {' % lim_names[i]
            print_params(f, param, max([len(p[6]) for p in g_battery_params]), rule)
            print >> f, '};'
            print >> f, ''
