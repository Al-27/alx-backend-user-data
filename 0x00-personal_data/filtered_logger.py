#!/usr/bin/env python3
"""
Mod Doc
"""
import typing
import logging
import re


def filter_datum(fields: typing.List[str], redaction: str, message: str, separator: str) -> str:
    new_mess = message.copy()
    for f in fields:
        new_mess = re.sub(f"(?<={f}=)[^{separator}]+",redaction, new_mess)
    return new_mess