#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import pandas as pd


def k26_som_xdc_to_csv(xdc_fname, csv_fname):
    # 読み込む
    with open(xdc_fname) as f:
        src = f.readlines()

    col_port = 'Port Name'
    col_bank = 'Bank'
    col_type = 'Device Pin Type'
    col_name = "Name"
    col_vcco = 'VCCO'

    pin_dict = {}

    # 先頭2行捨てる
    for line in src[2:]:
        # pin
        result = re.match('.*PACKAGE_PIN (\S+) ', line)
        if result is None: assert(0)
        pin = result.group(1)
        pin_dict[pin] = {}

        # SOM connector 1
        result = re.match('set_property\s+PACKAGE_PIN\s+([A-Z]+[0-9]+)\s+\[get_ports\s+\"(.*)\".*Bank\s+([0-9]+)\s+VCCO\s+-\s(\S+)\s+-\s(\S+)', line)
        if result:
            pin = result.group(1)
            pin_dict[pin][col_port] = result.group(2)
            pin_dict[pin][col_bank] = result.group(3)
            pin_dict[pin][col_vcco] = result.group(4)
            pin_dict[pin][col_type] = result.group(5)
            continue

        # SOM connector 2
        result = re.match('set_property\s+PACKAGE_PIN\s+([A-Z]+[0-9]+)\s+\[get_ports\s+\"(.*)\".*Bank\s+([0-9]+)\s+-\s(\S+)', line)
        if result:
            pin = result.group(1)
            pin_dict[pin][col_port] = result.group(2)
            pin_dict[pin][col_bank] = result.group(3)
            pin_dict[pin][col_type] = result.group(4)
            continue

        # Other 1
        result = re.match('#Other\s+net\s+PACKAGE_PIN\s+([A-Z]+[0-9]+)\s+-\s(\S+)\s+Bank\s+([0-9]+)\s+-\s+(\S+)', line)
        if result:
            pin = result.group(1)
            pin_dict[pin][col_name] = result.group(2)
            pin_dict[pin][col_bank] = result.group(3)
            pin_dict[pin][col_type] = result.group(4)
            continue

        # Other 2
        result = re.match('#Other\s+net\s+PACKAGE_PIN\s+([A-Z]+[0-9]+)\s+-\s+(No Connect)\s+Bank\s+([0-9]+)\s+-\s+(\S+)', line)
        if result:
            pin = result.group(1)
            pin_dict[pin][col_name] = result.group(2)
            pin_dict[pin][col_bank] = result.group(3)
            pin_dict[pin][col_type] = result.group(4)
            continue
        print(line)

    # pandas を使って CSV に変換
    df = pd.DataFrame.from_dict(pin_dict, orient="index", columns=[col_port, col_bank, col_type, col_name, col_vcco])
    df.index.name = "Device Pin Number"
    df.to_csv(csv_fname)


if __name__ == '__main__':
    k26_som_xdc_to_csv('Kria_K26_SOM_Rev1.xdc', 'k26-som-xck26-sfvc784-pin.csv')
