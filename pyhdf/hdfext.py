# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.1.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _hdfext
else:
    import _hdfext

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


DFNT_NONE = _hdfext.DFNT_NONE
DFNT_QUERY = _hdfext.DFNT_QUERY
DFNT_VERSION = _hdfext.DFNT_VERSION
DFNT_FLOAT32 = _hdfext.DFNT_FLOAT32
DFNT_FLOAT = _hdfext.DFNT_FLOAT
DFNT_FLOAT64 = _hdfext.DFNT_FLOAT64
DFNT_DOUBLE = _hdfext.DFNT_DOUBLE
DFNT_FLOAT128 = _hdfext.DFNT_FLOAT128
DFNT_INT8 = _hdfext.DFNT_INT8
DFNT_UINT8 = _hdfext.DFNT_UINT8
DFNT_INT16 = _hdfext.DFNT_INT16
DFNT_UINT16 = _hdfext.DFNT_UINT16
DFNT_INT32 = _hdfext.DFNT_INT32
DFNT_UINT32 = _hdfext.DFNT_UINT32
DFNT_INT64 = _hdfext.DFNT_INT64
DFNT_UINT64 = _hdfext.DFNT_UINT64
DFNT_INT128 = _hdfext.DFNT_INT128
DFNT_UINT128 = _hdfext.DFNT_UINT128
DFNT_UCHAR8 = _hdfext.DFNT_UCHAR8
DFNT_UCHAR = _hdfext.DFNT_UCHAR
DFNT_CHAR8 = _hdfext.DFNT_CHAR8
DFNT_CHAR = _hdfext.DFNT_CHAR
DFNT_CHAR16 = _hdfext.DFNT_CHAR16
DFNT_UCHAR16 = _hdfext.DFNT_UCHAR16
SD_UNLIMITED = _hdfext.SD_UNLIMITED
SD_FILL = _hdfext.SD_FILL
SD_NOFILL = _hdfext.SD_NOFILL
CHAR_BUFFER_SIZE = _hdfext.CHAR_BUFFER_SIZE
ATTRIB_BUFFER_SIZE = _hdfext.ATTRIB_BUFFER_SIZE
DFACC_READ = _hdfext.DFACC_READ
DFACC_WRITE = _hdfext.DFACC_WRITE
DFACC_CREATE = _hdfext.DFACC_CREATE
DFACC_ALL = _hdfext.DFACC_ALL
DFACC_RDONLY = _hdfext.DFACC_RDONLY
DFACC_RDWR = _hdfext.DFACC_RDWR
DFACC_CLOBBER = _hdfext.DFACC_CLOBBER
DFACC_BUFFER = _hdfext.DFACC_BUFFER
DFACC_APPENDABLE = _hdfext.DFACC_APPENDABLE
DFACC_CURRENT = _hdfext.DFACC_CURRENT
DFACC_OLD = _hdfext.DFACC_OLD
COMP_CODE_NONE = _hdfext.COMP_CODE_NONE
COMP_CODE_RLE = _hdfext.COMP_CODE_RLE
COMP_CODE_NBIT = _hdfext.COMP_CODE_NBIT
COMP_CODE_SKPHUFF = _hdfext.COMP_CODE_SKPHUFF
COMP_CODE_DEFLATE = _hdfext.COMP_CODE_DEFLATE
COMP_CODE_SZIP = _hdfext.COMP_CODE_SZIP
DFTAG_NDG = _hdfext.DFTAG_NDG
DFTAG_VH = _hdfext.DFTAG_VH
DFTAG_VG = _hdfext.DFTAG_VG
H4_MAX_VAR_DIMS = _hdfext.H4_MAX_VAR_DIMS
class array_byte(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, nelements):
        _hdfext.array_byte_swiginit(self, _hdfext.new_array_byte(nelements))
    __swig_destroy__ = _hdfext.delete_array_byte

    def __getitem__(self, index):
        return _hdfext.array_byte___getitem__(self, index)

    def __setitem__(self, index, value):
        return _hdfext.array_byte___setitem__(self, index, value)

    def cast(self):
        return _hdfext.array_byte_cast(self)

    @staticmethod
    def frompointer(t):
        return _hdfext.array_byte_frompointer(t)

# Register array_byte in _hdfext:
_hdfext.array_byte_swigregister(array_byte)
class array_int8(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, nelements):
        _hdfext.array_int8_swiginit(self, _hdfext.new_array_int8(nelements))
    __swig_destroy__ = _hdfext.delete_array_int8

    def __getitem__(self, index):
        return _hdfext.array_int8___getitem__(self, index)

    def __setitem__(self, index, value):
        return _hdfext.array_int8___setitem__(self, index, value)

    def cast(self):
        return _hdfext.array_int8_cast(self)

    @staticmethod
    def frompointer(t):
        return _hdfext.array_int8_frompointer(t)

# Register array_int8 in _hdfext:
_hdfext.array_int8_swigregister(array_int8)
class array_int16(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, nelements):
        _hdfext.array_int16_swiginit(self, _hdfext.new_array_int16(nelements))
    __swig_destroy__ = _hdfext.delete_array_int16

    def __getitem__(self, index):
        return _hdfext.array_int16___getitem__(self, index)

    def __setitem__(self, index, value):
        return _hdfext.array_int16___setitem__(self, index, value)

    def cast(self):
        return _hdfext.array_int16_cast(self)

    @staticmethod
    def frompointer(t):
        return _hdfext.array_int16_frompointer(t)

# Register array_int16 in _hdfext:
_hdfext.array_int16_swigregister(array_int16)
class array_uint16(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, nelements):
        _hdfext.array_uint16_swiginit(self, _hdfext.new_array_uint16(nelements))
    __swig_destroy__ = _hdfext.delete_array_uint16

    def __getitem__(self, index):
        return _hdfext.array_uint16___getitem__(self, index)

    def __setitem__(self, index, value):
        return _hdfext.array_uint16___setitem__(self, index, value)

    def cast(self):
        return _hdfext.array_uint16_cast(self)

    @staticmethod
    def frompointer(t):
        return _hdfext.array_uint16_frompointer(t)

# Register array_uint16 in _hdfext:
_hdfext.array_uint16_swigregister(array_uint16)
class array_int32(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, nelements):
        _hdfext.array_int32_swiginit(self, _hdfext.new_array_int32(nelements))
    __swig_destroy__ = _hdfext.delete_array_int32

    def __getitem__(self, index):
        return _hdfext.array_int32___getitem__(self, index)

    def __setitem__(self, index, value):
        return _hdfext.array_int32___setitem__(self, index, value)

    def cast(self):
        return _hdfext.array_int32_cast(self)

    @staticmethod
    def frompointer(t):
        return _hdfext.array_int32_frompointer(t)

# Register array_int32 in _hdfext:
_hdfext.array_int32_swigregister(array_int32)
class array_uint32(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, nelements):
        _hdfext.array_uint32_swiginit(self, _hdfext.new_array_uint32(nelements))
    __swig_destroy__ = _hdfext.delete_array_uint32

    def __getitem__(self, index):
        return _hdfext.array_uint32___getitem__(self, index)

    def __setitem__(self, index, value):
        return _hdfext.array_uint32___setitem__(self, index, value)

    def cast(self):
        return _hdfext.array_uint32_cast(self)

    @staticmethod
    def frompointer(t):
        return _hdfext.array_uint32_frompointer(t)

# Register array_uint32 in _hdfext:
_hdfext.array_uint32_swigregister(array_uint32)
class array_float32(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, nelements):
        _hdfext.array_float32_swiginit(self, _hdfext.new_array_float32(nelements))
    __swig_destroy__ = _hdfext.delete_array_float32

    def __getitem__(self, index):
        return _hdfext.array_float32___getitem__(self, index)

    def __setitem__(self, index, value):
        return _hdfext.array_float32___setitem__(self, index, value)

    def cast(self):
        return _hdfext.array_float32_cast(self)

    @staticmethod
    def frompointer(t):
        return _hdfext.array_float32_frompointer(t)

# Register array_float32 in _hdfext:
_hdfext.array_float32_swigregister(array_float32)
class array_float64(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, nelements):
        _hdfext.array_float64_swiginit(self, _hdfext.new_array_float64(nelements))
    __swig_destroy__ = _hdfext.delete_array_float64

    def __getitem__(self, index):
        return _hdfext.array_float64___getitem__(self, index)

    def __setitem__(self, index, value):
        return _hdfext.array_float64___setitem__(self, index, value)

    def cast(self):
        return _hdfext.array_float64_cast(self)

    @staticmethod
    def frompointer(t):
        return _hdfext.array_float64_frompointer(t)

# Register array_float64 in _hdfext:
_hdfext.array_float64_swigregister(array_float64)

def new_array_voidp(nelements):
    return _hdfext.new_array_voidp(nelements)

def delete_array_voidp(ary):
    return _hdfext.delete_array_voidp(ary)

def array_voidp_getitem(ary, index):
    return _hdfext.array_voidp_getitem(ary, index)

def array_voidp_setitem(ary, index, value):
    return _hdfext.array_voidp_setitem(ary, index, value)

def Hopen(filename, access_mode, num_dds_blocks):
    return _hdfext.Hopen(filename, access_mode, num_dds_blocks)

def Hclose(file_id):
    return _hdfext.Hclose(file_id)

def Hgetlibversion():
    return _hdfext.Hgetlibversion()

def Hgetfileversion(file_id):
    return _hdfext.Hgetfileversion(file_id)

def Hishdf(filename):
    return _hdfext.Hishdf(filename)

def HEvalue(error_stack_offset):
    return _hdfext.HEvalue(error_stack_offset)

def HEstring(error_code):
    return _hdfext.HEstring(error_code)

def _HEprint():
    return _hdfext._HEprint()

def _SDreaddata_0(sds_id, data_type, start, edges, stride):
    return _hdfext._SDreaddata_0(sds_id, data_type, start, edges, stride)

def _SDwritedata_0(sds_id, data_type, start, edges, data, stride):
    return _hdfext._SDwritedata_0(sds_id, data_type, start, edges, data, stride)

def SDstart(filename, access_mode):
    return _hdfext.SDstart(filename, access_mode)

def SDcreate(sd_id, sds_name, data_type, rank, dim_sizes):
    return _hdfext.SDcreate(sd_id, sds_name, data_type, rank, dim_sizes)

def SDselect(sd_id, sds_index):
    return _hdfext.SDselect(sd_id, sds_index)

def SDendaccess(sds_id):
    return _hdfext.SDendaccess(sds_id)

def SDend(sd_id):
    return _hdfext.SDend(sd_id)

def SDfileinfo(sd_id):
    return _hdfext.SDfileinfo(sd_id)

def SDgetinfo(sds_id, buf):
    return _hdfext.SDgetinfo(sds_id, buf)

def SDcheckempty(sds_id):
    return _hdfext.SDcheckempty(sds_id)

def SDidtoref(sds_id):
    return _hdfext.SDidtoref(sds_id)

def SDiscoordvar(sds_id):
    return _hdfext.SDiscoordvar(sds_id)

def SDisrecord(sds_id):
    return _hdfext.SDisrecord(sds_id)

def SDnametoindex(sd_id, sds_name):
    return _hdfext.SDnametoindex(sd_id, sds_name)

def SDreftoindex(sd_id, sds_ref):
    return _hdfext.SDreftoindex(sd_id, sds_ref)

def SDdiminfo(dim_id):
    return _hdfext.SDdiminfo(dim_id)

def SDgetdimid(sds_id, dim_index):
    return _hdfext.SDgetdimid(sds_id, dim_index)

def SDsetdimname(dim_id, dim_name):
    return _hdfext.SDsetdimname(dim_id, dim_name)

def SDgetdimscale(dim_id, buf):
    return _hdfext.SDgetdimscale(dim_id, buf)

def SDsetdimscale(dim_id, n_values, data_type, buf):
    return _hdfext.SDsetdimscale(dim_id, n_values, data_type, buf)

def SDattrinfo(obj_id, attr_index):
    return _hdfext.SDattrinfo(obj_id, attr_index)

def SDfindattr(obj_id, attr_name):
    return _hdfext.SDfindattr(obj_id, attr_name)

def SDreadattr(obj_id, attr_index, buf):
    return _hdfext.SDreadattr(obj_id, attr_index, buf)

def SDsetattr(obj_id, attr_name, data_type, n_values, values):
    return _hdfext.SDsetattr(obj_id, attr_name, data_type, n_values, values)

def SDgetcal(sds_id):
    return _hdfext.SDgetcal(sds_id)

def SDgetdatastrs(sds_id, len):
    return _hdfext.SDgetdatastrs(sds_id, len)

def SDgetdimstrs(sds_id, len):
    return _hdfext.SDgetdimstrs(sds_id, len)

def SDgetfillvalue(sds_id, buf):
    return _hdfext.SDgetfillvalue(sds_id, buf)

def SDgetrange(sds_id, buf1, buf2):
    return _hdfext.SDgetrange(sds_id, buf1, buf2)

def SDsetcal(sds_id, cal, cal_error, offset, offset_err, data_type):
    return _hdfext.SDsetcal(sds_id, cal, cal_error, offset, offset_err, data_type)

def SDsetdatastrs(sds_id, label, unit, format, coord_system):
    return _hdfext.SDsetdatastrs(sds_id, label, unit, format, coord_system)

def SDsetdimstrs(sds_id, label, unit, format):
    return _hdfext.SDsetdimstrs(sds_id, label, unit, format)

def SDsetfillmode(sd_id, fill_mode):
    return _hdfext.SDsetfillmode(sd_id, fill_mode)

def SDsetfillvalue(sds_id, fill_val):
    return _hdfext.SDsetfillvalue(sds_id, fill_val)

def SDsetrange(sds_id, max, min):
    return _hdfext.SDsetrange(sds_id, max, min)

def _SDgetcompress(sds_id):
    return _hdfext._SDgetcompress(sds_id)

def _SDsetcompress(sds_id, comp_type, value, v2):
    return _hdfext._SDsetcompress(sds_id, comp_type, value, v2)

def SDsetexternalfile(sds_id, filename, offset):
    return _hdfext.SDsetexternalfile(sds_id, filename, offset)

def Vinitialize(file_id):
    return _hdfext.Vinitialize(file_id)

def VSattach(file_id, vdata_ref, vdata_access_mode):
    return _hdfext.VSattach(file_id, vdata_ref, vdata_access_mode)

def VSdetach(vdata_id):
    return _hdfext.VSdetach(vdata_id)

def Vfinish(file_id):
    return _hdfext.Vfinish(file_id)

def VHstoredata(file_id, fieldname, buf, n_records, data_type, vdata_name, vdata_class):
    return _hdfext.VHstoredata(file_id, fieldname, buf, n_records, data_type, vdata_name, vdata_class)

def VHstoredatam(file_id, fieldname, buf, n_records, data_type, vdata_name, vdata_class, order):
    return _hdfext.VHstoredatam(file_id, fieldname, buf, n_records, data_type, vdata_name, vdata_class, order)

def VSfdefine(vdata_id, fieldname, data_type, order):
    return _hdfext.VSfdefine(vdata_id, fieldname, data_type, order)

def VSsetfields(vdata_id, fieldname_list):
    return _hdfext.VSsetfields(vdata_id, fieldname_list)

def VSseek(vdata_id, record_index):
    return _hdfext.VSseek(vdata_id, record_index)

def VSread(vdata_id, databuf, n_records, interlace_mode):
    return _hdfext.VSread(vdata_id, databuf, n_records, interlace_mode)

def VSwrite(vdata_id, databuf, n_records, interlace_mode):
    return _hdfext.VSwrite(vdata_id, databuf, n_records, interlace_mode)

def VSfpack(vdata_id, action, fields_in_buf, buf, buf_size, n_records, fieldname_list, bufptrs):
    return _hdfext.VSfpack(vdata_id, action, fields_in_buf, buf, buf_size, n_records, fieldname_list, bufptrs)

def VSelts(vdata_id):
    return _hdfext.VSelts(vdata_id)

def VSgetclass(vdata_id):
    return _hdfext.VSgetclass(vdata_id)

def VSgetfields(vdata_id):
    return _hdfext.VSgetfields(vdata_id)

def VSgetinterlace(vdata_id):
    return _hdfext.VSgetinterlace(vdata_id)

def VSgetname(vdata_id):
    return _hdfext.VSgetname(vdata_id)

def VSsizeof(vdata_id, fieldname_list):
    return _hdfext.VSsizeof(vdata_id, fieldname_list)

def VSinquire(vdata_id):
    return _hdfext.VSinquire(vdata_id)

def VSQuerytag(vdata_id):
    return _hdfext.VSQuerytag(vdata_id)

def VSQueryref(vdata_id):
    return _hdfext.VSQueryref(vdata_id)

def VSfindex(vdata_id, field_name):
    return _hdfext.VSfindex(vdata_id, field_name)

def VSisattr(vdta_id):
    return _hdfext.VSisattr(vdta_id)

def VFnfields(vdata_id):
    return _hdfext.VFnfields(vdata_id)

def VFfieldtype(vdata_id, field_index):
    return _hdfext.VFfieldtype(vdata_id, field_index)

def VFfieldname(vdata_id, field_index):
    return _hdfext.VFfieldname(vdata_id, field_index)

def VFfieldesize(vdata_id, field_index):
    return _hdfext.VFfieldesize(vdata_id, field_index)

def VFfieldisize(vdata_id, field_index):
    return _hdfext.VFfieldisize(vdata_id, field_index)

def VFfieldorder(vdata_id, field_index):
    return _hdfext.VFfieldorder(vdata_id, field_index)

def VSfind(file_id, vdata_name):
    return _hdfext.VSfind(file_id, vdata_name)

def VSgetid(file_id, vdata_ref):
    return _hdfext.VSgetid(file_id, vdata_ref)

def VSfexist(vdata_id, fieldname_list):
    return _hdfext.VSfexist(vdata_id, fieldname_list)

def VSsetclass(vdata_id, vdata_class):
    return _hdfext.VSsetclass(vdata_id, vdata_class)

def VSsetname(vdata_id, vdata_name):
    return _hdfext.VSsetname(vdata_id, vdata_name)

def VSsetinterlace(vdata_id, interlace_mode):
    return _hdfext.VSsetinterlace(vdata_id, interlace_mode)

def VSsetattr(vdata_id, field_index, attr_name, data_type, n_values, values):
    return _hdfext.VSsetattr(vdata_id, field_index, attr_name, data_type, n_values, values)

def VSgetattr(vdata_id, field_index, attr_index, buf):
    return _hdfext.VSgetattr(vdata_id, field_index, attr_index, buf)

def VSfnattrs(vdata_id, field_index):
    return _hdfext.VSfnattrs(vdata_id, field_index)

def VSnattrs(vdata_id):
    return _hdfext.VSnattrs(vdata_id)

def VSattrinfo(vdata_id, field_index, attr_index):
    return _hdfext.VSattrinfo(vdata_id, field_index, attr_index)

def VSfindattr(vdata_id, field_index, attr_name):
    return _hdfext.VSfindattr(vdata_id, field_index, attr_name)

def Vattach(file_id, vgroup_ref, vg_access_mode):
    return _hdfext.Vattach(file_id, vgroup_ref, vg_access_mode)

def Vdetach(vgroup_id):
    return _hdfext.Vdetach(vgroup_id)

def Vgetname(vgroup_id):
    return _hdfext.Vgetname(vgroup_id)

def Vsetname(vgroup_id, vgroup_name):
    return _hdfext.Vsetname(vgroup_id, vgroup_name)

def Vgetclass(vgroup_id):
    return _hdfext.Vgetclass(vgroup_id)

def Vsetclass(vgroup_id, vgroup_class):
    return _hdfext.Vsetclass(vgroup_id, vgroup_class)

def Vfind(file_id, vgroup_name):
    return _hdfext.Vfind(file_id, vgroup_name)

def Vfindclass(file_id, vgroup_class):
    return _hdfext.Vfindclass(file_id, vgroup_class)

def Vinsert(vgroup_id, v_id):
    return _hdfext.Vinsert(vgroup_id, v_id)

def Vaddtagref(vgroup_id, obj_tag, obj_ref):
    return _hdfext.Vaddtagref(vgroup_id, obj_tag, obj_ref)

def Vdeletetagref(vgroup_id, obj_tag, obj_ref):
    return _hdfext.Vdeletetagref(vgroup_id, obj_tag, obj_ref)

def Vdelete(file_id, vgroup_id):
    return _hdfext.Vdelete(file_id, vgroup_id)

def VQueryref(vgroup_id):
    return _hdfext.VQueryref(vgroup_id)

def VQuerytag(vgroup_id):
    return _hdfext.VQuerytag(vgroup_id)

def Vntagrefs(vgroup_id):
    return _hdfext.Vntagrefs(vgroup_id)

def Vgettagref(vgroup_id, index):
    return _hdfext.Vgettagref(vgroup_id, index)

def Vgetversion(vgroup_id):
    return _hdfext.Vgetversion(vgroup_id)

def Vgettagrefs(vgroup_id, tag_attay, ref_array, maxsize):
    return _hdfext.Vgettagrefs(vgroup_id, tag_attay, ref_array, maxsize)

def Vgetid(file_id, vgroup_ref):
    return _hdfext.Vgetid(file_id, vgroup_ref)

def Vinqtagref(vgroup_id, tag, ref):
    return _hdfext.Vinqtagref(vgroup_id, tag, ref)

def Visvg(vgroup_id, obj_ref):
    return _hdfext.Visvg(vgroup_id, obj_ref)

def Visvs(vgroup_id, obj_ref):
    return _hdfext.Visvs(vgroup_id, obj_ref)

def Vnrefs(vgroup_id, tag_type):
    return _hdfext.Vnrefs(vgroup_id, tag_type)

def Vfindattr(vgroup_id, attr_name):
    return _hdfext.Vfindattr(vgroup_id, attr_name)

def Vgetattr(vdata_id, attr_index, buf):
    return _hdfext.Vgetattr(vdata_id, attr_index, buf)

def Vsetattr(vgroup_id, attr_name, data_type, n_values, values):
    return _hdfext.Vsetattr(vgroup_id, attr_name, data_type, n_values, values)

def Vattrinfo(vgroup_id, attr_index):
    return _hdfext.Vattrinfo(vgroup_id, attr_index)

def Vnattrs(vgroup_id):
    return _hdfext.Vnattrs(vgroup_id)

