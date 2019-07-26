from UserDict import UserDict
import os
import sys
import traceback

class Mp3FileInfoError(Exception): pass
class HeaderCorruptError(Mp3FileInfoError): pass
class FreeBitrateError(Mp3FileInfoError): pass

def stripnulls(data):
    'strip whitespace and nulls'
    return data.replace('\00', '').strip()

class Mp3FileInfo(UserDict):
    'store ID3v1.0 MP3 tags'
    tagDataMap = {
        'title' : (3, 33, stripnulls),
        'artist' : (33, 63, stripnulls),
        'album' : (63, 93, stripnulls),
        'year' : (93, 97, stripnulls),
        'comment' : (97, 126, stripnulls),
        'genre' : (127, 128, ord)
    }

    def __init__(self, path):
        UserDict.__init__(self)
        file_data = {}
        file_data['path'] = path
        file_data['size'] = os.stat(path).st_size
        self['file'] = file_data
        try:
            fd = open(path, 'rb', 0)
            self.read_ID3v1(fd)
            self.read_audio(fd)
        finally:
            fd.close()

    def __str__(self):
        sections = ['[Mp3FileInfo]' ]
        for s in sorted(self.keys()):
            items = [s]
            for k in sorted(self[s].keys()):
                items.append('%s: %s' % (k, self[s][k]))
                
            sections.append('\n    '.join(items))
        return '\n  '.join(sections)
    
    ID3V1_TAGS_SIZE = 128
    ID3V2_HEADER_SIZE = 10
  
    def read_ID3v1(self, file):
        file.seek(-self.ID3V1_TAGS_SIZE, 2)
        tag_data = file.read(self.ID3V1_TAGS_SIZE)
        if len(tag_data) < self.ID3V1_TAGS_SIZE: return
        tags = {}
        if tag_data[:3] == 'TAG':
            for tag, (start, end, parseFunc) in self.tagDataMap.items():
                tags[tag] = parseFunc(tag_data[start:end])

        self['ID3v1'] = tags
  
    def read_audio(self, file):
        frame = self.find_frame(file)
        if frame:
            audio = {}
            audio['encoding'] = frame.version_desc() + ' ' + frame.layer_desc()
            audio['bitrate'] = frame.bitrate
            audio['bitrate_mode'] = frame.bitrate_mode
            audio['sampling_rate'] = frame.sampling_rate
            audio['emphasis'] = frame.emphasis_desc()
            audio['channel_mode'] = frame.channel_mode_desc()
            audio['copyright'] = frame.copyright
            audio['original'] = frame.original
            audio['crc'] = frame.crc
            audio['length'] = frame.length
            audio['frames'] = frame.frames
            self['audio'] = audio

    def find_frame(self, file):
        file.seek(0)
        header = file.read(self.ID3V2_HEADER_SIZE)
        if len(header) < self.ID3V2_HEADER_SIZE : return None
        file.seek(self.skip_id3v2_tags(header))
        file_data = file.read(16384)
        offset = 0
        end_offset = len(file_data) - MPAHeader.MPA_HEADER_SIZE
        while offset < end_offset:
            # look for sync bytes: first 11 bits should be 1
            try:
                if ord(file_data[offset]) == 0xff and (ord(file_data[offset + 1]) & 0xe0) == 0xe0:
                    return MPAHeader(file_data, offset, self['file']['size'])
            except Exception, e:
                # continue search
                type, value, stack = sys.exc_info()
                traceback.print_exception(type, value, stack)
                pass
            offset += 1
        return None
  
    def skip_id3v2_tags(self, header):
        if header[0:3] != 'ID3': return 0
        if ord(header[3]) > 4: return 0
        if ord(header[4]) == 0xff: return 0
        total_size = (ord(header[5]) & 0x10) and 20 or 10
        size = (ord(header[6]) << 21) + (ord(header[7]) << 14) + (ord(header[8]) << 7) + ord(header[9])
        return total_size + size

class MPAHeader:
    # Audio versions
    MPEG25 = 0
    MPEGReserved = 1
    MPEG2 = 2
    MPEG1 = 3

    # Layers
    Layer1 = 0
    Layer2 = 1
    Layer3 = 2
    LayerReserved = 3
    
    # Emphasis
    EmphNone = 0
    Emph5015 = 1
    EmphReserved = 2
    EmphCCITJ17 = 3

    # Channel modes
    Stereo = 0
    JointStereo = 1
    DualChannel = 2
    SingleChannel = 3

    Layers =    ['Layer I', 'Layer II', 'Layer III']
    MPEGVersions = ['MPEG 2.5', '', 'MPEG 2', 'MPEG 1']
    ChannelModes = ['Stereo', 'Joint Stereo', 'Dual Channel', 'Single Channel' ]
    Emphasis = ['None', '50/15ms', '', 'CCIT J.17' ]

    MPA_HEADER_SIZE = 4

#  attr_reader :bitrate, :bitrate_mode, :sampling_rate, :copyright, :original, :crc, :frames, :length

    def version_desc(self):
        return self.MPEGVersions[self.version]    
  
    def layer_desc(self):
        return self.Layers[self.layer]
  
    def emphasis_desc(self):
        return self.Emphasis[self.emphasis]
  
    def channel_mode_desc(self):
        return self.ChannelModes[self.channel_mode]
  
    # sampling rates in hertz: 1. index = MPEG Version ID, 2. index = sampling rate index
    SamplingRates = [ 
        [11025, 12000, 8000,  ],    # MPEG 2.5
        [0,     0,     0,     ],    # reserved
        [22050, 24000, 16000, ],    # MPEG 2
        [44100, 48000, 32000  ]        # MPEG 1
    ]

    # bitrates: 1. index = LSF, 2. index = Layer, 3. index = bitrate index
    Bitrates = [
        [    # MPEG 1
            [0,32,64,96,128,160,192,224,256,288,320,352,384,416,448],    # Layer1
            [0,32,48,56, 64, 80, 96,112,128,160,192,224,256,320,384],    # Layer2
            [0,32,40,48, 56, 64, 80, 96,112,128,160,192,224,256,320]    # Layer3
        ],
        [    # MPEG 2, 2.5        
            [0,32,48,56,64,80,96,112,128,144,160,176,192,224,256],        # Layer1
            [0,8,16,24,32,40,48,56,64,80,96,112,128,144,160],            # Layer2
            [0,8,16,24,32,40,48,56,64,80,96,112,128,144,160]            # Layer3
        ]
    ]

    # allowed combination of bitrate (1.index) and mono (2.index)
    AllowedModes = [
        # stereo, intensity stereo, dual channel allowed, single channel allowed
        [True, True],        # free mode
        [False, True],       # 32
        [False, True],       # 48
        [False, True],       # 56
        [True, True],        # 64
        [False, True],       # 80
        [True, True],        # 96
        [True, True],        # 112
        [True, True],        # 128
        [True, True],        # 160
        [True, True],        # 192
        [True, False],       # 224
        [True, False],       # 256
        [True, False],       # 320
        [True, False]        # 384
    ]

    # Samples per Frame: 1. index = LSF, 2. index = Layer
    SamplesPerFrames = [
        [ # MPEG 1
          # Layer1 Layer2 Layer3
            384,   1152,  1152    
        ],
        [ # MPEG 2, 2.5
          # Layer1 Layer2 Layer3
            384,   1152,  576
        ]    
    ]

    # size of side information (only for Layer III)
    # 1. index = LSF, 2. index = mono
    SideInfoSizes = [
        # MPEG 1
        [32, 17],
        # MPEG 2/2.5
        [17, 9]
    ]
  
    # Samples per Frame / 8
    Coefficients = [
        [ # MPEG 1
            12,        # Layer1    (must be multiplied with 4, because of slot size)
            144,       # Layer2
            144        # Layer3
        ],
        [ # MPEG 2, 2.5
            12,        # Layer1    (must be multiplied with 4, because of slot size)
            144,       # Layer2
            72         # Layer3
        ]
    ]
  
    # slot size per layer
    SlotSizes = [
        4,         # Layer1
        1,         # Layer2
        1          # Layer3
    ]

    def __init__(self, header, offset, size):
        self.header, self.offset, self.bytes = header, offset, size
        self.bitrate_mode = 'CBR'

        # get MPEG version [bit 11,12]
        self.version = (ord(header[offset + 1]) >> 3) & 0x03    # mask only the rightmost 2 bits
        if self.version == self.MPEGReserved: raise HeaderCorruptError, 'reserved MPEG version'

        self.bLSF = self.version != self.MPEG1

        # get layer (0 = layer1, 2 = layer2, ...)  [bit 13,14]
        self.layer = 3 - ((ord(header[offset + 1]) >> 1) & 0x03)    
        if self.layer == self.LayerReserved: raise HeaderCorruptError, 'reserved layer' 

        # protection bit (inverted) [bit 15]
        self.crc = not ((ord(header[offset + 1])) & 0x01)

        # bitrate [bit 16..19]
        bitrate_index = (ord(header[offset + 2]) >> 4) & 0x0F
        if bitrate_index == 0x0F: raise HeaderCorruptError, 'all bitrate bits set'
        self.bitrate = self.Bitrates[self.bLSF][self.layer][bitrate_index] # in kbit/sec

        if self.bitrate == 0: raise FreeBitrateError, 'free bitrate is not supported yet'

        # sampling rate [bit 20,21]
        index = (ord(header[offset + 2]) >> 2) & 0x03;
        if index == 0x03: raise HeaderCorrupt, 'all sampling rate bits set'
        self.sampling_rate = self.SamplingRates[self.version][index]
    
        samples_per_frame = self.SamplesPerFrames[self.bLSF][self.layer]

        # channel mode [bit 24,25]
        self.channel_mode = (ord(header[offset + 3]) >> 6) & 0x03

        # copyright bit [bit 28]
        self.copyright = ((ord((header[offset + 3])) >> 3) & 0x01) != 0

        # original bit [bit 29]
        self.original = ((ord(header[offset + 3]) >> 2) & 0x01) != 0

        # emphasis [bit 30,31]
        self.emphasis = ord(header[offset + 3]) & 0x03
        if self.emphasis == self.EmphReserved: raise HeaderCorruptError, 'reserved emphasis value'

        # extended check for Layer II
        if self.layer == self.Layer2:
            if self.version == self.MPEG1:
                if not self.AllowedModes[bitrate_index][self.channel_mode == self.SingleChannel]: 
                    raise HeaderCorrupt
  
        self.frames = 0
        self.find_vbr_header()
  
        if self.frames == 0:
            self.length = self.bytes * 8 / self.bitrate / 1000
            padding_size = (ord(header[offset + 2]) >> 1) & 0x01
            frame_size = int((self.Coefficients[self.bLSF][self.layer] * self.bitrate * 1000.0 / 
                          self.sampling_rate + padding_size) * self.SlotSizes[self.layer])
            self.frames = self.bytes / frame_size
        else:
            self.length = self.frames * samples_per_frame / self.sampling_rate
            #print 'length %d frames %d sampling_rate %d\n' % (self.length, self.frames, self.sampling_rate)
  
    def side_info_size(self):
        return self.SideInfoSizes[self.bLSF][self.channel_mode == self.SingleChannel]
  
    def find_vbr_header(self):
        if self.find_xing_header():
            self.bitrate_mode = 'VBR'; 
        elif self.find_vbri_header():
            self.bitrate_mode = 'VBRI';

    # XING header flags 
    XING_FRAMES_FLAG =    0x0001
    XING_BYTES_FLAG =     0x0002
    XING_TOC_FLAG =       0x0004
    XING_VBR_SCALE_FLAG = 0x0008

    def find_xing_header(self):
        # XING VBR-Header

        # size  description
        # 4     'Xing' or 'Info'
        # 4     flags (indicates which fields are used)
        # 4     frames (optional)
        # 4     bytes (optional)
        # 100   toc (optional)
        # 4     a VBR quality indicator: 0=best 100=worst (optional)


        offset = self.offset + self.MPA_HEADER_SIZE + self.side_info_size()
        tag = self.header[offset:offset + 4]
        if tag !=  'Xing' and tag != 'Info': return False
        
        flags = self.read_be_value(4, offset + 4)
        if flags & self.XING_FRAMES_FLAG:
            self.frames = self.read_be_value(4, offset + 8)
        if flags & self.XING_BYTES_FLAG:
            bytes = self.read_be_value(4, offset + 12)
        if bytes > 0: self.bytes = bytes
        return True
  
    def find_vbri_header(self):
        # FhG VBRI Header

        # size    description
        # 4       'VBRI' (ID)
        # 2       version
        # 2       delay
        # 2       quality
        # 4       # bytes
        # 4       # frames
        # 2       table size (for TOC)
        # 2       table scale (for TOC)
        # 2       size of table entry (max. size = 4 byte (must be stored in an integer))
        # 2       frames per table entry
    
        # ??      dynamic table consisting out of frames with size 1-4
        #         whole length in table size! (for TOC)

        offset = self.offset + self.MPA_HEADER_SIZE + 32
    
        if self.header[offset:offset + 4] != 'VBRI': return False 
        bytes = self.read_be_value(4, offset + 10)
        if bytes > 0: self.bytes = bytes 
        self.frames = self.read_be_value(4, offset + 14)
        return True
  
    def read_be_value(self, len, offset):
        n = 0
        for c in self.header[offset:offset + len]:
            n = (n << 8) + ord(c)
        return n

if __name__ == '__main__':
    total = 0
    
    for root, dirs, files in os.walk('/mp3'):
        for f in files:
            if '.mp3' in f:
                path = os.path.join(root, f)
                fi = Mp3FileInfo(path)
                total += fi['audio']['length']
                #print path + ' ' + str(fi['audio']['length'])
        
    print 'Total length is %d:%02d:%02d\n' % (total / 60 / 60, (total / 60) % 60, total %60)