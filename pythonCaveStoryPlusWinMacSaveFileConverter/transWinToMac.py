# coding=utf-8

INPUT_FILE_WIN = 'saveFiles/Profile.dat'
INPUT_FILE_MAC = 'saveFiles/Profile2.dat'
OUTPUT_FILE_MAC = 'saveFiles/Cave Story+Profile.dat'
import struct


def getWhatFromBytes(offset, num, type, bytes):
    return struct.unpack(str(num) + type, bytes[offset: offset + 4 * num])


def getIntsFromBytes(offset, num, bytes):
    return getWhatFromBytes(offset, num, 'i', bytes);


if __name__ == '__main__':
    winFile = open(INPUT_FILE_WIN, 'rb')
    realMac = open(INPUT_FILE_MAC, 'rb')
    outputMacFile = open(OUTPUT_FILE_MAC, 'wb')
    bytes = winFile.read()
    bytesMac = realMac.read()

    # firstPoint
    print "==========FIRST STEP============"
    i, = struct.unpack('i', bytes[1536:1540]);
    firstPoint = struct.unpack('4i', bytes[1536:1552]);
    firstPointMac = struct.unpack('4i', bytesMac[1536:1552]);
    print "1536 4byte win&mac:\n", firstPoint, "\n", firstPointMac
    bytes = bytes[:1540] + bytes[1544:]
    print "after del 1540:1544 byte :\n", struct.unpack('4i', bytes[1536:1552]);

    # secondPoint:
    print "==========SECOND STEP============"
    secondPoint = getIntsFromBytes(127004, 50, bytes);
    secondPointMac = getIntsFromBytes(126360, 50, bytesMac);
    print "win 127008, mac126360:\n", secondPoint, "\n", secondPointMac

    st = 127004 - (127004 - 126360)
    ed = 127004
    bytes = bytes[:st] + bytes[ed:]
    print "after del " + str(st) + ":" + str(ed) + " byte :\n", getIntsFromBytes(126360, 50, bytes)

    #thirdPoint:
    print "==========THIRD STEP============"
    print "byte length of win and mac:"
    print len(bytes)
    print len(bytesMac)
    bytes = bytes[:len(bytes)-4]
    print "after del last 4bytes:", len(bytes)

    outputMacFile.write(bytes)
    winFile.close()
    outputMacFile.close()
