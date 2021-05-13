# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from turtlebot_actions/FindFiducialGoal.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class FindFiducialGoal(genpy.Message):
  _md5sum = "8906385fe785bb5733551eb61968fe5b"
  _type = "turtlebot_actions/FindFiducialGoal"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
#goal definition
uint8   CHESSBOARD = 1
uint8   CIRCLES_GRID = 2
uint8   ASYMMETRIC_CIRCLES_GRID =3

string    camera_name       # name of the camera 
uint8     pattern_width     # number of objects across
uint8     pattern_height    # number of objects down
float32   pattern_size      # size the object pattern (square size or circle size)
uint8     pattern_type      # type of pattern (CHESSBOARD, CIRCLES_GRID, ASYMMETRIC_CIRCLES_GRID)
"""
  # Pseudo-constants
  CHESSBOARD = 1
  CIRCLES_GRID = 2
  ASYMMETRIC_CIRCLES_GRID = 3

  __slots__ = ['camera_name','pattern_width','pattern_height','pattern_size','pattern_type']
  _slot_types = ['string','uint8','uint8','float32','uint8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       camera_name,pattern_width,pattern_height,pattern_size,pattern_type

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(FindFiducialGoal, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.camera_name is None:
        self.camera_name = ''
      if self.pattern_width is None:
        self.pattern_width = 0
      if self.pattern_height is None:
        self.pattern_height = 0
      if self.pattern_size is None:
        self.pattern_size = 0.
      if self.pattern_type is None:
        self.pattern_type = 0
    else:
      self.camera_name = ''
      self.pattern_width = 0
      self.pattern_height = 0
      self.pattern_size = 0.
      self.pattern_type = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.camera_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2BfB().pack(_x.pattern_width, _x.pattern_height, _x.pattern_size, _x.pattern_type))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.camera_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.camera_name = str[start:end]
      _x = self
      start = end
      end += 7
      (_x.pattern_width, _x.pattern_height, _x.pattern_size, _x.pattern_type,) = _get_struct_2BfB().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.camera_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2BfB().pack(_x.pattern_width, _x.pattern_height, _x.pattern_size, _x.pattern_type))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.camera_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.camera_name = str[start:end]
      _x = self
      start = end
      end += 7
      (_x.pattern_width, _x.pattern_height, _x.pattern_size, _x.pattern_type,) = _get_struct_2BfB().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2BfB = None
def _get_struct_2BfB():
    global _struct_2BfB
    if _struct_2BfB is None:
        _struct_2BfB = struct.Struct("<2BfB")
    return _struct_2BfB
