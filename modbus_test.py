#%% Test
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian

client = ModbusClient('10.18.80.10', port = '502')
registers_set = 1

address = 0x4008

count = registers_set * 2

unit = 1

result = client.read_holding_registers(address, count, unit = unit)
print(result.registers)

decoder = BinaryPayloadDecoder.fromRegisters(result.registers, 
byteorder=Endian.Big,
wordorder=Endian.Big)
decoded = {
    'float': decoder.decode_32bit_float(),
}

for name, value in decoded.items():
    print(value)