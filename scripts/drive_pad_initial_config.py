import sys

DRIVE_PAD_NAMES = [
    'PinmuxDrivePadIndex_AlsProxInt,   ',
    'PinmuxDrivePadIndex_ApReady,      ',
    'PinmuxDrivePadIndex_ApWakeBt,     ',
    'PinmuxDrivePadIndex_ApWakeNfc,    ',
    'PinmuxDrivePadIndex_AudMclk,      ',
    'PinmuxDrivePadIndex_BattBcl,      ',
    'PinmuxDrivePadIndex_BtRst,        ',
    'PinmuxDrivePadIndex_BtWakeAp,     ',
    'PinmuxDrivePadIndex_ButtonHome,   ',
    'PinmuxDrivePadIndex_ButtonPowerOn,',
    'PinmuxDrivePadIndex_ButtonSlideSw,',
    'PinmuxDrivePadIndex_ButtonVolDown,',
    'PinmuxDrivePadIndex_ButtonVolUp,  ',
    'PinmuxDrivePadIndex_Cam1Mclk,     ',
    'PinmuxDrivePadIndex_Cam1Pwdn,     ',
    'PinmuxDrivePadIndex_Cam1Strobe,   ',
    'PinmuxDrivePadIndex_Cam2Mclk,     ',
    'PinmuxDrivePadIndex_Cam2Pwdn,     ',
    'PinmuxDrivePadIndex_CamAfEn,      ',
    'PinmuxDrivePadIndex_CamFlashEn,   ',
    'PinmuxDrivePadIndex_CamI2cScl,    ',
    'PinmuxDrivePadIndex_CamI2cSda,    ',
    'PinmuxDrivePadIndex_CamRst,       ',
    'PinmuxDrivePadIndex_Clk32kIn,     ',
    'PinmuxDrivePadIndex_Clk32kOut,    ',
    'PinmuxDrivePadIndex_ClkReq,       ',
    'PinmuxDrivePadIndex_CorePwrReq,   ',
    'PinmuxDrivePadIndex_CpuPwrReq,    ',
    'PinmuxDrivePadIndex_Dap1Din,      ',
    'PinmuxDrivePadIndex_Dap1Dout,     ',
    'PinmuxDrivePadIndex_Dap1Fs,       ',
    'PinmuxDrivePadIndex_Dap1Sclk,     ',
    'PinmuxDrivePadIndex_Dap2Din,      ',
    'PinmuxDrivePadIndex_Dap2Dout,     ',
    'PinmuxDrivePadIndex_Dap2Fs,       ',
    'PinmuxDrivePadIndex_Dap2Sclk,     ',
    'PinmuxDrivePadIndex_Dap4Din,      ',
    'PinmuxDrivePadIndex_Dap4Dout,     ',
    'PinmuxDrivePadIndex_Dap4Fs,       ',
    'PinmuxDrivePadIndex_Dap4Sclk,     ',
    'PinmuxDrivePadIndex_Dmic1Clk,     ',
    'PinmuxDrivePadIndex_Dmic1Dat,     ',
    'PinmuxDrivePadIndex_Dmic2Clk,     ',
    'PinmuxDrivePadIndex_Dmic2Dat,     ',
    'PinmuxDrivePadIndex_Dmic3Clk,     ',
    'PinmuxDrivePadIndex_Dmic3Dat,     ',
    'PinmuxDrivePadIndex_DpHpd,        ',
    'PinmuxDrivePadIndex_DvfsClk,      ',
    'PinmuxDrivePadIndex_DvfsPwm,      ',
    'PinmuxDrivePadIndex_Gen1I2cScl,   ',
    'PinmuxDrivePadIndex_Gen1I2cSda,   ',
    'PinmuxDrivePadIndex_Gen2I2cScl,   ',
    'PinmuxDrivePadIndex_Gen2I2cSda,   ',
    'PinmuxDrivePadIndex_Gen3I2cScl,   ',
    'PinmuxDrivePadIndex_Gen3I2cSda,   ',
    'PinmuxDrivePadIndex_GpioPa6,      ',
    'PinmuxDrivePadIndex_GpioPcc7,     ',
    'PinmuxDrivePadIndex_GpioPe6,      ',
    'PinmuxDrivePadIndex_GpioPe7,      ',
    'PinmuxDrivePadIndex_GpioPh6,      ',
    'PinmuxDrivePadIndex_GpioPk0,      ',
    'PinmuxDrivePadIndex_GpioPk1,      ',
    'PinmuxDrivePadIndex_GpioPk2,      ',
    'PinmuxDrivePadIndex_GpioPk3,      ',
    'PinmuxDrivePadIndex_GpioPk4,      ',
    'PinmuxDrivePadIndex_GpioPk5,      ',
    'PinmuxDrivePadIndex_GpioPk6,      ',
    'PinmuxDrivePadIndex_GpioPk7,      ',
    'PinmuxDrivePadIndex_GpioPl0,      ',
    'PinmuxDrivePadIndex_GpioPl1,      ',
    'PinmuxDrivePadIndex_GpioPz0,      ',
    'PinmuxDrivePadIndex_GpioPz1,      ',
    'PinmuxDrivePadIndex_GpioPz2,      ',
    'PinmuxDrivePadIndex_GpioPz3,      ',
    'PinmuxDrivePadIndex_GpioPz4,      ',
    'PinmuxDrivePadIndex_GpioPz5,      ',
    'PinmuxDrivePadIndex_GpioX1Aud,    ',
    'PinmuxDrivePadIndex_GpioX3Aud,    ',
    'PinmuxDrivePadIndex_GpsEn,        ',
    'PinmuxDrivePadIndex_GpsRst,       ',
    'PinmuxDrivePadIndex_HdmiCec,      ',
    'PinmuxDrivePadIndex_HdmiIntDpHpd, ',
    'PinmuxDrivePadIndex_JtagRtck,     ',
    'PinmuxDrivePadIndex_LcdBlEn,      ',
    'PinmuxDrivePadIndex_LcdBlPwm,     ',
    'PinmuxDrivePadIndex_LcdGpio1,     ',
    'PinmuxDrivePadIndex_LcdGpio2,     ',
    'PinmuxDrivePadIndex_LcdRst,       ',
    'PinmuxDrivePadIndex_LcdTe,        ',
    'PinmuxDrivePadIndex_ModemWakeAp,  ',
    'PinmuxDrivePadIndex_MotionInt,    ',
    'PinmuxDrivePadIndex_NfcEn,        ',
    'PinmuxDrivePadIndex_NfcInt,       ',
    'PinmuxDrivePadIndex_PexL0ClkReqN, ',
    'PinmuxDrivePadIndex_PexL0RstN,    ',
    'PinmuxDrivePadIndex_PexL1ClkreqN, ',
    'PinmuxDrivePadIndex_PexL1RstN,    ',
    'PinmuxDrivePadIndex_PexWakeN,     ',
    'PinmuxDrivePadIndex_PwrI2cScl,    ',
    'PinmuxDrivePadIndex_PwrI2cSda,    ',
    'PinmuxDrivePadIndex_PwrIntN,      ',
    'PinmuxDrivePadIndex_QspiComp,     ',
    'PinmuxDrivePadIndex_QspiSck,      ',
    'PinmuxDrivePadIndex_SataLedActive,',
    'PinmuxDrivePadIndex_Sdmmc1Pad,    ',
    'PinmuxDrivePadIndex_Sdmmc3Pad,    ',
    'PinmuxDrivePadIndex_Shutdown,     ',
    'PinmuxDrivePadIndex_SpdifIn,      ',
    'PinmuxDrivePadIndex_SpdifOut,     ',
    'PinmuxDrivePadIndex_Spi1Cs0,      ',
    'PinmuxDrivePadIndex_Spi1Cs1,      ',
    'PinmuxDrivePadIndex_Spi1Miso,     ',
    'PinmuxDrivePadIndex_Spi1Mosi,     ',
    'PinmuxDrivePadIndex_Spi1Sck,      ',
    'PinmuxDrivePadIndex_Spi2Cs0,      ',
    'PinmuxDrivePadIndex_Spi2Cs1,      ',
    'PinmuxDrivePadIndex_Spi2Miso,     ',
    'PinmuxDrivePadIndex_Spi2Mosi,     ',
    'PinmuxDrivePadIndex_Spi2Sck,      ',
    'PinmuxDrivePadIndex_Spi4Cs0,      ',
    'PinmuxDrivePadIndex_Spi4Miso,     ',
    'PinmuxDrivePadIndex_Spi4Mosi,     ',
    'PinmuxDrivePadIndex_Spi4Sck,      ',
    'PinmuxDrivePadIndex_TempAlert,    ',
    'PinmuxDrivePadIndex_TouchClk,     ',
    'PinmuxDrivePadIndex_TouchInt,     ',
    'PinmuxDrivePadIndex_TouchRst,     ',
    'PinmuxDrivePadIndex_Uart1Cts,     ',
    'PinmuxDrivePadIndex_Uart1Rts,     ',
    'PinmuxDrivePadIndex_Uart1Rx,      ',
    'PinmuxDrivePadIndex_Uart1Tx,      ',
    'PinmuxDrivePadIndex_Uart2Cts,     ',
    'PinmuxDrivePadIndex_Uart2Rts,     ',
    'PinmuxDrivePadIndex_Uart2Rx,      ',
    'PinmuxDrivePadIndex_Uart2Tx,      ',
    'PinmuxDrivePadIndex_Uart3Cts,     ',
    'PinmuxDrivePadIndex_Uart3Rts,     ',
    'PinmuxDrivePadIndex_Uart3Rx,      ',
    'PinmuxDrivePadIndex_Uart3Tx,      ',
    'PinmuxDrivePadIndex_Uart4Cts,     ',
    'PinmuxDrivePadIndex_Uart4Rts,     ',
    'PinmuxDrivePadIndex_Uart4Rx,      ',
    'PinmuxDrivePadIndex_Uart4Tx,      ',
    'PinmuxDrivePadIndex_UsbVbusEn0,   ',
    'PinmuxDrivePadIndex_UsbVbusEn1,   ',
    'PinmuxDrivePadIndex_WifiEn,       ',
    'PinmuxDrivePadIndex_WifiRst,      ',
    'PinmuxDrivePadIndex_WifiWakeAp,   ',
]

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

ADDRESS = 0x710003D050

lines = decompile_func(ADDRESS)
assert lines[0].startswith('void __fastcall') and lines[0].endswith('()')
assert lines[ 1] == '{'
assert lines[-1] == '}'

lines = lines[2:-1]

def empty_config():
    return [None, None, None]

g_configs = [[], []]

for i in xrange(0x2F):
    g_configs[0].append(empty_config())
    g_configs[1].append(empty_config())




def get_field_index(field):
    '''
    struct PinmuxDrivePadConfig
    {
        _DWORD index;
        _DWORD option;
        _DWORD option_mask;
    };
    '''
    if field == 'index':
        return 0
    if field == 'option':
        return 1
    if field == 'option_mask':
        return 2

def set_entry(cfg, index, fi, value):
    if type(value) is int or type(value) is long:
        cfg[index][fi] = (value & 0xFFFFFFFF)
    else:
        cfg[index][fi] = value

def set_qword(cfg, index, fi, value):
    assert type(value) is long
    if fi <= 1:
        cfg[index][fi]     = (value & 0xFFFFFFFF)
        cfg[index][fi + 1] = ((value >> 32) & 0xFFFFFFFF)
    else:
        cfg[index][fi]    = (value & 0xFFFFFFFF)
        cfg[index + 1][0] = ((value >> 32) & 0xFFFFFFFF)

def parse_line(line):
    global g_battery_limits
    global g_battery_params
    spl = [s.replace(';','').lstrip().rstrip() for s in line.split('=')]
    #print spl
    qword = spl[0].startswith('*(_QWORD *)&')
    if qword:
        spl[0] = spl[0][len('*(_QWORD *)&'):]
    #print spl
    if spl[0].startswith('g_DrivePadConfigs'):
        cfg_ind = 0 if spl[0].startswith('g_DrivePadConfigsHoag') else 1
        spl[0] = spl[0][spl[0].index('[')+1:]
        index = int(spl[0][:spl[0].index(']')], 0)
        spl[0] = spl[0][spl[0].index(']')+2:]
        field = spl[0]
        value = spl[1]
        if value[0] in '0123456789':
            value = int(spl[1].replace('LL',''), 0) & 0xFFFFFFFFFFFFFFFF
        #print limits_ind, rule_ind, field, value
        if qword:
            set_qword(g_configs[cfg_ind], index, get_field_index(field), value)
        else:
            set_entry(g_configs[cfg_ind], index, get_field_index(field), value)
        return True
    if spl[0].startswith('nn::os::SdkMutex::SdkMutex'):
        return True
    return False

good = True
for line in lines:
    if not parse_line(line):
        good = False
        break

def print_config(f, cfg):
    print >> f, '    { %s 0x%08X, 0x%08X },' % (DRIVE_PAD_NAMES[cfg[0]], cfg[1], cfg[2])

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

/* NOTE: This file is auto-generated by drive_pad_initial_config.py, do not edit manually. */
'''

lim_fns   = ['_hoag', '']
lim_names = ['Hoag', '']

if not good:
    print 'Failed to parse parameters!'
else:
    #print g_configs
    for i,cfgs in enumerate(g_configs):
        for j,cfg in enumerate(cfgs):
            for k,value in enumerate(cfg):
                if value is None:
                    print i,j,k
                    assert value is not None
    for i,cfgs in enumerate(g_configs):
        with open('pinmux_initial_drive_pad_config%s.inc' % lim_fns[i], 'w') as f:
            print >> f, COPYRIGHT_HEADER
            print >> f, 'constexpr inline const PinmuxDrivePadConfig PinmuxDrivePadConfigs%s[] = {' % lim_names[i]
            for cfg in cfgs:
                print_config(f, cfg)
            print >> f, '};'
            print >> f, ''
            print >> f, 'constexpr inline const size_t NumPinmuxDrivePadConfigs%s = util::size(PinmuxDrivePadConfigs%s);' % (lim_names[i], lim_names[i])
