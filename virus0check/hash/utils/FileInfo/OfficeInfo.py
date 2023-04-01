import zipfile
import xml.dom.minidom


def file_office_info(file) -> str:
    out = str()
    out += "File Information:\n"

    myFile = zipfile.ZipFile(file, 'r')
    doc = xml.dom.minidom.parseString(myFile.read('docProps/core.xml'))
    xml.dom.minidom.parseString(myFile.read('docProps/core.xml')).toprettyxml()

    docInfo = {}
    docInfo['File name'] = file
    try:
        docInfo['Title'] = doc.getElementsByTagName('dc:title')[0].childNodes[0].data
    except:
        docInfo['Title'] = ''
    try:
        docInfo['Description'] = doc.getElementsByTagName('dc:description')[0].childNodes[0].data
    except:
        docInfo['Description'] = ''
    try:
        docInfo['Creator'] = doc.getElementsByTagName('dc:creator')[0].childNodes[0].data
    except:
        docInfo['Creator'] = ''
    try:
        docInfo['LastModifiedBy'] = doc.getElementsByTagName('cp:lastModifiedBy')[0].childNodes[0].data
    except:
        docInfo['LastModifiedBy'] = ''
    try:
        docInfo['DateCreated'] = doc.getElementsByTagName('dcterms:created')[0].childNodes[0].data
    except:
        docInfo['DateCreated'] = ''
    try:
        docInfo['DateModified'] = doc.getElementsByTagName('dcterms:modified')[0].childNodes[0].data
    except:
        docInfo['DateModified'] = ''

    for label, value in docInfo.items():
        out += f"{label:25}: {value}\n"

    return out
