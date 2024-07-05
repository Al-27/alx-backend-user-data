#!/usr/bin/env python3
"""
Mod Doc
"""
import typing
import logging
import re


def filter_datum(fields: typing.List[str], redaction: str, message: str, separator: str) -> str:
    """    Mod Doc    """
    for f in fields:
        message = re.sub(f"(?<={f}=)[^{separator}]+",redaction, message)
    return message
    
    
class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: typing.List[str]):
        self.fields = list(fields)
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ Redacting Formatter class
        """
        record.msg = filter_datum(self.fields,self.REDACTION, record.msg, self.SEPARATOR) 
        
        return super().format(record)
