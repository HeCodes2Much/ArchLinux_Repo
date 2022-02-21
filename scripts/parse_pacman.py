"""
Pacman -Si to JSON parser
Copyright (C) 2022  Mathias Klug

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import json

def parse_pacman(src):
    res = {}

    k = ""
    for l in src.splitlines():
        if len(l) == 0: continue
        if l[0] != ' ':
            r = l.split(':')
        else:
            r = []
            r.append(k)
            r.extend(l.split(':'))
        if len(r) == 2:
            vr = r[1].strip().split("  ")
            if len(vr) == 1: vr = vr[0]
        else:
            if r[2][0] != ' ':
                vr = ':'.join(r[1:]).strip().split("  ")
                if len(vr) == 1: vr = vr[0]
            else:
                v = r[2].strip().split("  ")
                if len(v) == 1: v = v[0]
                vr = {}
                vr[r[1].strip()] = v
        k = r[0].strip()
        if k in res:
            res[k][list(vr.keys())[0]] = list(vr.values())[0]
        else:
            res[k] = vr
    return res

