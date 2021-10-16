import string

EVENTS = {
    -1   : 'WakeEvent_None               ',
    0x00 : 'WakeEvent_PexWakeN           ',
    0x01 : 'WakeEvent_GpioPortA6         ',
    0x02 : 'WakeEvent_QspiCsN            ',
    0x03 : 'WakeEvent_Spi2Mosi           ',
    0x04 : 'WakeEvent_ExtconDetS         ',
    0x05 : 'WakeEvent_McuIrq             ',
    0x06 : 'WakeEvent_Uart2Cts           ',
    0x07 : 'WakeEvent_Uart3Cts           ',
    0x08 : 'WakeEvent_WifiWakeAp         ',
    0x09 : 'WakeEvent_AoTag2Pmc          ',
    0x0A : 'WakeEvent_ExtconDetU         ',
    0x0B : 'WakeEvent_NfcInt             ',
    0x0C : 'WakeEvent_Gen1I2cSda         ',
    0x0D : 'WakeEvent_Gen2I2cSda         ',
    0x0E : 'WakeEvent_CradleIrq          ',
    0x0F : 'WakeEvent_GpioPortK6         ',
    0x10 : 'WakeEvent_RtcIrq             ',
    0x11 : 'WakeEvent_Sdmmc1Dat1         ',
    0x12 : 'WakeEvent_Sdmmc2Dat1         ',
    0x13 : 'WakeEvent_HdmiCec            ',
    0x14 : 'WakeEvent_Gen3I2cSda         ',
    0x15 : 'WakeEvent_GpioPortL1         ',
    0x16 : 'WakeEvent_Clk_32kOut         ',
    0x17 : 'WakeEvent_PwrI2cSda          ',
    0x18 : 'WakeEvent_ButtonPowerOn      ',
    0x19 : 'WakeEvent_ButtonVolUp        ',
    0x1A : 'WakeEvent_ButtonVolDown      ',
    0x1B : 'WakeEvent_ButtonSlideSw      ',
    0x1C : 'WakeEvent_ButtonHome         ',

    0x20 : 'WakeEvent_AlsProxInt         ',
    0x21 : 'WakeEvent_TempAlert          ',
    0x22 : 'WakeEvent_Bq24190Irq         ',
    0x23 : 'WakeEvent_SdCd               ',
    0x24 : 'WakeEvent_GpioPortZ2         ',

    0x27 : 'WakeEvent_Utmip0             ',
    0x28 : 'WakeEvent_Utmip1             ',
    0x29 : 'WakeEvent_Utmip2             ',
    0x2A : 'WakeEvent_Utmip3             ',
    0x2B : 'WakeEvent_Uhsic              ',
    0x2C : 'WakeEvent_Wake2PmcXusbSystem ',
    0x2D : 'WakeEvent_Sdmmc3Dat1         ',
    0x2E : 'WakeEvent_Sdmmc4Dat1         ',
    0x2F : 'WakeEvent_CamI2cScl          ',
    0x30 : 'WakeEvent_CamI2cSda          ',
    0x31 : 'WakeEvent_GpioPortZ5         ',
    0x32 : 'WakeEvent_DpHpd0             ',
    0x33 : 'WakeEvent_PwrIntN            ',
    0x34 : 'WakeEvent_BtWakeAp           ',
    0x35 : 'WakeEvent_HdmiIntDpHpd       ',
    0x36 : 'WakeEvent_UsbVbusEn0         ',
    0x37 : 'WakeEvent_UsbVbusEn1         ',
    0x38 : 'WakeEvent_LcdRst             ',
    0x39 : 'WakeEvent_LcdGpio1           ',
    0x3A : 'WakeEvent_LcdGpio2           ',
    0x3B : 'WakeEvent_Uart4Cts           ',
    0x3D : 'WakeEvent_ModemWakeAp        ',
    0x3E : 'WakeEvent_TouchInt           ',
    0x3F : 'WakeEvent_MotionInt          ',
}

DESCS = [
    '0x01 CodecLdoEnTemp 0xCC 0x33000002'.split(),
    '0x02 PowSdEn 0x24 0x3C000001'.split(),
    '0x03 BtRst 0x3C 0x37000002'.split(),
    '0x04 RamCode3 0xDA 0xC9000402'.split(),
    '0x05 GameCardReset 0xDB 0x3C000402'.split(),
    '0x06 CodecAlert 0xDC 0x33000003'.split(),
    '0x07 PowGc 0x25 0x3C000401'.split(),
    '0x08 DebugControllerDet 0x90 0x350000CA'.split(),
    '0x09 BattChgStatus 0x91 0x39000407'.split(),
    '0x0A BattChgEnableN 0x96 0x39000003'.split(),
    '0x0B FanTach 0x97 0x3D000002'.split(),
    '0x0C ExtconDetS 0x26 0x3500040B'.split(),
    '0x0D Vdd50AEn 0x05 0x39000401'.split(),
    '0x0E SdevCoaxSel1 0x78 0xCA000406'.split(),
    '0x0F GameCardCd 0x93 0x3C000403'.split(),
    '0x10 ProdType0 0x7D 0xC900040B'.split(),
    '0x11 ProdType1 0x7C 0xC900040C'.split(),
    '0x12 ProdType2 0x7B 0xC900040D'.split(),
    '0x13 ProdType3 0x7A 0xC900040E'.split(),
    '0x14 TempAlert 0xBC 0x3E000002'.split(),
    '0x15 CodecHpDetIrq 0xAE 0x33000004'.split(),
    '0x16 MotionInt 0xBA 0x35000041'.split(),
    '0x17 TpIrq 0xB9 0x35000036'.split(),
    '0x18 ButtonSleep2 0xBD 0x35000001'.split(),
    '0x19 ButtonVolUp 0xBE 0x35000002'.split(),
    '0x1A ButtonVolDn 0xBF 0x35000003'.split(),
    '0x1B BattMgicIrq 0xC0 0x39000034'.split(),
    '0x1C RecoveryKey 0xC1 0x35000004'.split(),
    '0x1D PowLcdBlEn 0xA9 0x3400003E'.split(),
    '0x1E LcdReset 0xAA 0x34000033'.split(),
    '0x1F PdVconnEn 0x55 0x040000CC'.split(),
    '0x20 PdRstN 0xAD 0x040000CA'.split(),
    '0x21 Bq24190Irq 0xC8 0x39000002'.split(),
    '0x22 SdevCoaxSel0 0xCA 0xCA000405'.split(),
    '0x23 SdWp 0xCB 0x3C000003'.split(),
    '0x24 TpReset 0x4F 0x35000035'.split(),
    '0x25 BtGpio2 0x50 0x37000401'.split(),
    '0x26 BtGpio3 0x51 0x37000402'.split(),
    '0x27 BtGpio4 0x52 0x37000403'.split(),
    '0x28 CradleIrq 0x54 0x040000CB'.split(),
    '0x29 PowVcpuInt 0x56 0x3E000003'.split(),
    '0x2A Max77621GpuInt 0x57 0x3E000004'.split(),
    '0x2B ExtconChgU 0x53 0x35000402'.split(),
    '0x2C ExtconChgS 0xE3 0x3500040C'.split(),
    '0x2D WifiRfDisable 0x38 0x38000003'.split(),
    '0x2E WifiReset 0x39 0x38000002'.split(),
    '0x2F ApWakeBt 0x3B 0x37000003'.split(),
    '0x30 BtWakeAp 0x3D 0x37000004'.split(),
    '0x31 BtGpio5 0x3F 0x37000404'.split(),
    '0x32 PowLcdVddPEn 0x40 0x34000034'.split(),
    '0x33 PowLcdVddNEn 0x41 0x34000035'.split(),
    '0x34 ExtconDetU 0x3E 0x35000401'.split(),
    '0x35 RamCode2 0xE2 0xC9000401'.split(),
    '0x36 Vdd50BEn 0xE4 0x39000402'.split(),
    '0x37 WifiWakeHost 0x3A 0x38000004'.split(),
    '0x38 SdCd 0xC9 0x3C000002'.split(),
    '0x39 OtgFet1ForSdev 0x4D 0x39000404'.split(),
    '0x3A OtgFet2ForSdev 0x58 0x39000405'.split(),
    '0x3B ExtConWakeU 0x3E 0x35000403'.split(),
    '0x3C ExtConWakeS 0x26 0x3500040D'.split(),
    '0x3D PmuIrq -1 0x39000406'.split(),
    '0x3E ExtUart2Cts 0x33 0x35000404'.split(),
    '0x3F ExtUart3Cts 0x1C 0x3500040E'.split(),
    '0x40 5VStepDownEn 0xD9 0x39000408'.split(),
    '0x41 UsbSwitchB2Oc 0x0C 0x04000401'.split(),
    '0x42 5VStepDownPg 0x0D 0x39000409'.split(),
    '0x43 UsbSwitchAEn 0x21 0x04000402'.split(),
    '0x44 UsbSwitchAFlag 0x27 0x04000403'.split(),
    '0x45 UsbSwitchB3Oc 0x92 0x04000404'.split(),
    '0x46 UsbSwitchB3En 0x95 0x04000405'.split(),
    '0x47 UsbSwitchB2En 0x98 0x04000406'.split(),
    '0x48 Hdmi5VEn 0x10 0x34000004'.split(),
    '0x49 UsbSwitchB1En 0x11 0x04000407'.split(),
    '0x4A HdmiPdTrEn 0x12 0x34000005'.split(),
    '0x4B FanEn 0x42 0x3D000003'.split(),
    '0x4C UsbSwitchB1Oc 0xE6 0x04000408'.split(),
    '0x4D PwmFan 0xAC 0x3D000001'.split(),
    '0x4E HdmiHpd 0xE1 0x34000006'.split(),
    '0x4F Max77812Irq 0x56 0x3E000003'.split(),
    '0x50 Debug0 0x20 0xCA000001'.split(),
    '0x51 Debug1 0x21 0xCA000002'.split(),
    '0x52 Debug2 0x22 0xCA000003'.split(),
    '0x53 Debug3 0x23 0xCA000004'.split(),
    '0x54 NfcIrq 0x4C 0x36000004'.split(),
    '0x55 NfcRst 0x57 0x36000003'.split(),
    '0x56 McuIrq 0x27 0x35000415'.split(),
    '0x57 McuBoot 0x98 0x35000416'.split(),
    '0x58 McuRst 0x99 0x35000417'.split(),
    '0x59 Vdd5V3En 0xBB 0x39000403'.split(),
    '0x5A McuPor 0xE5 0x35000418'.split(),
    '0x5B LcdGpio1 0xAB 0x35000005'.split(),
    '0x5C NfcEn 0x4E 0x36000002'.split(),
    '-1 ExtUart2Rts 0x32 0x35000406'.split(),
    '-1 ExtUart3Rts 0x1B 0x35000410'.split(),
    '-1 GpioPortC7 0x17 0x3500041B'.split(),
    '-1 GpioPortD0 0x18 0x3500041C'.split(),
    '-1 GpioPortC5 0x15 0x3500041D'.split(),
    '-1 GpioPortC6 0x16 0x3500041E'.split(),
    '-1 GpioPortY7 0xC5 0x35000065'.split(),
    '-1 GpioPortF1 0x29 0x04000409'.split(),
    '-1 GpioPortH0 0x38 0x34000401'.split(),
    '-1 GpioPortI6 0x46 0x37000405'.split(),
]

ENTRIES = [ (int(x[0], 0), x[1], int(x[2], 0), int(x[3], 0)) for x in DESCS ]

max_name = max([len(x[1]) for x in ENTRIES])


print '    enum GpioPadName : u32 {'
for entry in ENTRIES:
    if entry[0] != -1:
        print ('        GpioPadName_%%-%ds = %%d,' % max_name) % (entry[1], entry[0])
print '    };'
print ''
for entry in ENTRIES:
    print ('    constexpr inline const DeviceCode DeviceCode_%%-%ds = 0x%%08X;' % max_name) % (entry[1], entry[3])
print ''
print '    constexpr inline GpioPadName ConvertToGpioPadName(DeviceCode dc) {'
print '        switch (dc.GetInternalValue()) {'
for entry in ENTRIES:
    if entry[0] != -1:
        print ('            case DeviceCode_%%-%ds.GetInternalValue(): return GpioPadName_%%s;' % max_name) % (entry[1], entry[1])
print '            AMS_UNREACHABLE_DEFAULT_CASE();'
print '        }'
print '    }'
print ''
print '    constexpr inline DeviceCode ConvertToDeviceCode(GpioPadName gpn) {'
print '        switch (gpn) {'
for entry in ENTRIES:
    if entry[0] != -1:
        print ('            case GpioPadName_%%-%ds return DeviceCode_%%s;' % (max_name+1)) % (entry[1]+':', entry[1])
print '            AMS_UNREACHABLE_DEFAULT_CASE();'
print '        }'
print '    }'
print ''

PORTS = ['%s' % c for c in string.uppercase] + ['AA','BB','CC','DD','EE','FF']

def get_port_name(port):
    if port == -1:
        return 'InternalGpioPadNumber_None'
    else:
        return 'InternalGpioPadNumber_Port_%s_%d' % (PORTS[port / 8], port & 7)

port_len_max = len('InternalGpioPadNumber_Port_XX_X')

def get_entry_by_device_code(dc):
    for entry in ENTRIES:
        if entry[3] == dc:
            return entry
    return None

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

/* NOTE: This file is auto-generated by gpio_pad_gen.py, do not edit manually. */
'''

ADDRESS = 0x7100099F90
COUNT   = 91

with open('gpio_internal_pad_map_combination.inc', 'w') as f:
    print >> f, COPYRIGHT_HEADER
    print >> f, 'constexpr inline const PadMapCombination PadMapCombinationList[] = {'
    for i in xrange(COUNT):
        entry = ADDRESS + 12 * i
        x, y, z = ida_bytes.get_32bit(entry), ida_bytes.get_32bit(entry + 4), ida_bytes.get_32bit(entry + 8)
        if x == 0xFFFFFFFF:
            x = -1
        if y == 0xFFFFFFFF:
            y = -1
        if z == 0xFFFFFFFF:
            z = -1
        e = get_entry_by_device_code(x)
        assert e is not None
        assert y == e[2]
        assert z in EVENTS.keys()
        print >> f, (('    { DeviceCode_%%-%ds %%-%ds ams::wec::%%s},' % (max_name+1, port_len_max+1)) % (e[1]+',', get_port_name(y)+',', EVENTS[z])).replace('0x000000', '      0x')
    print >> f, '};'
    print >> f, ''
    print >> f, 'constexpr inline size_t PadMapCombinationListSize = util::size(PadMapCombinationList);'

TYPES = ['Icosa', 'Copper', 'Hoag', 'Iowa', 'Calcio', 'Aula']
COUNTS = [0x3C, 0x3B, 0x3C, 0x3B, 0x20, 0x30]

ADDRESS = 0x71000BB410

for i,t in enumerate(TYPES):
    if i == 1:
        continue
    with open('gpio_initial_config_%s.inc' % t.lower(), 'w') as f:
        print >> f, COPYRIGHT_HEADER
        print >> f, 'constexpr inline const GpioInitialConfig InitialGpioConfigs%s[] = {' % t
        list_addr = ida_bytes.get_64bit(ADDRESS + 8 * i)
        for n in xrange(COUNTS[i]):
            entry = list_addr + 12 * n
            x, y, z = ida_bytes.get_32bit(entry), ida_bytes.get_32bit(entry + 4), ida_bytes.get_32bit(entry + 8)
            e = get_entry_by_device_code(x)
            print >> f, (('    { DeviceCode_%%-%ds %%s %%s },' % (max_name+1)) % (e[1]+',', ['Direction_Input, ','Direction_Output,'][y], ['GpioValue_Low ','GpioValue_High'][z]))
        print >> f, '};'
        print >> f, ''
        print >> f, 'constexpr inline size_t NumInitialGpioConfigs%s = util::size(InitialGpioConfigs%s);' % (t, t)
