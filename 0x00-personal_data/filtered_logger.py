#!/usr/bin/env python3
"""
Mod Doc
"""
import logging
import re


def filter_datum(fields, redaction, message: list, separator):
    new_mess = message.copy()
    for i in range(len(new_mess)):
        for f in fields:
            new_mess[i] = re.sub(f"(?<={f}=)[^{separator}]+",redaction, new_mess[i])
    return new_mess