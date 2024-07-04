#!/usr/bin/env python3
"""
Mod Doc
"""
import logging
import re


def filter_datum(fields: list, redaction: str, message: list, separator: str) -> str:
    new_mess = "\n".join(map(str,message))
    for f in fields:
        new_mess = re.sub(f"(?<={f}=)[^{separator}]+",redaction, new_mess)
    return new_mess