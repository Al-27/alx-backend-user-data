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