from __future__ import print_function
from datetime import datetime
from pefile import PE


def get_file_info(file, verbose: bool = False) -> str:
    out = str()

    pe = PE(name=file)
    ped = pe.dump_dict()

    file_info = {}
    for structure in pe.FileInfo[0]:
        if structure.Key == b'StringFileInfo':
            for s_table in structure.StringTable:
                for key, value in s_table.entries.items():
                    if value is None or len(value) == 0:
                        value = "Unknown"
                    file_info[key] = value
    out += "File Information:"
    out += "=================="

    for k, v in file_info.items():
        if isinstance(k, bytes):
            k = k.decode()
        if isinstance(v, bytes):
            v = v.decode()
    comp_time = ped['FILE_HEADER']['TimeDateStamp']['Value']
    comp_time = comp_time.split("[")[-1].strip("]")
    time_stamp, timezone = comp_time.rsplit(" ", 1)
    comp_time = datetime.strptime(time_stamp, "%a %b %d %H:%M:%S %Y")

    out += "Compiled on {} {}".format(comp_time, timezone.strip())

    ##
    for section in ped['PE Sections']:
        out += "Section '{}' at {}: {}/{} {}".format(
            section['Name']['Value'], hex(section['VirtualAddress']['Value']),
            section['Misc_VirtualSize']['Value'],
            section['SizeOfRawData']['Value'], section['MD5'])

    if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
        out += "\nImports: "
        out += "========="

        for dir_entry in pe.DIRECTORY_ENTRY_IMPORT:
            dll = dir_entry.dll

            if not verbose:
                out += dll.decode()
                continue
            name_list = []

            for imports in dir_entry.imports:
                if getattr(imports, "name", b"Unknown") is None:
                    name = b"Unknown"
                else:
                    name = getattr(imports, "name", b"Unknown")
                    name_list.append([name.decode(), hex(imports.address)])
            name_fmt = ["{} ({})".format(x[0], x[1]) for x in name_list]
            out += '- {}: {}'.format(dll.decode(), ", ".join(name_fmt))
    if not verbose:
        print()

    if hasattr(pe, 'DIRECTORY_ENTRY_EXPORT'):
        out += "\nExports: "
        out += "========="

        for sym in pe.DIRECTORY_ENTRY_EXPORT.symbols:
            out += '- {}: {}'.format(sym.name.decode(), hex(sym.address))
    return out
