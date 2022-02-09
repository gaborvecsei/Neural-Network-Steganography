from typing import List, Union


def str_to_bits(s: str, as_list: bool = False) -> Union[List[int], List[List[int]]]:
    tmp = []
    for b in bytes(s, "ascii"):
        s_bin = bin(b)[2:].rjust(8, "0")
        tmp.append(s_bin)
    if as_list:
        return [list(map(int, list(x))) for x in tmp]
    return [int(x) for x in "".join(tmp)]


def bits_to_str(b: List[int]) -> str:
    tmp = []
    for i in range(0, len(b), 8):
        c = chr(int("".join(map(str, b[i:i + 8])), 2))
        tmp.append(c)
    return "".join(tmp)
