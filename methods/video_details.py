from hachoir_core.cmd_line import unicodeFilename
from hachoir_core.error import HachoirError
from hachoir_core.i18n import getTerminalCharset
from hachoir_core.tools import makePrintable
from hachoir_metadata import extractMetadata
from hachoir_parser import createParser


# Get metadata for video file
def metadata_for(filename):
    filename, realname = unicodeFilename(filename), filename
    parser = createParser(filename, realname)
    if not parser:
        print "Unable to parse file"
        exit(1)
    try:
        metadata = extractMetadata(parser)
    except HachoirError, err:
        print "Metadata extraction error: %s" % unicode(err)
        metadata = None
    if not metadata:
        print "Unable to extract metadata"
        exit(1)

    text = metadata.exportPlaintext()
    charset = getTerminalCharset()
    for line in text:
        print makePrintable(line, charset)

    return metadata


def extract_data(metadata):
    for data in sorted(metadata):
        if len(data.values) > 0:
            print data.key, data.values[0].value
