import ctypes
from typing import Tuple


class FloatBinary:

    def __init__(self, v: float) -> None:
        self.v: float = float(v)

        # Binary representation of the float value LSB
        self._bin: Tuple[bool] = self.float_to_binary(self.v)

        # Binary representation splitted to sign, exponent, fraction/mantissa
        self._splitted_bin: dict = self.split_binary(self._bin)

        # 1 bit for sign
        self.sign: bool = self._splitted_bin["sign"]

        # 8 bits for exponent
        self.exponent: Tuple[bool] = self._splitted_bin["exponent"]

        # Full 23 bits for fraction/mantissa - 3 parts: first 7 bits, middle 8 bits, last 8 bits
        self.fraction: Tuple[bool] = self._splitted_bin["fraction"]

    def float_to_binary(self, num: float) -> Tuple[bool]:
        """
        Convert float value to a binary representation - 1s and 0s
        (True is 1 and False is 0)

        Args:
            num: float value

        Returns:
            Tuple[bool]: tuple of bools
        """

        bin_num = bin(ctypes.c_uint.from_buffer(ctypes.c_float(num)).value)[2:]
        bin_num = bin_num.rjust(32, "0")
        return tuple([False if x == "0" else True for x in list(bin_num)])

    @staticmethod
    def split_binary(binary_float: Tuple[bool]) -> dict:
        """
        Structures (splits) the binary representation to sign, exponent, fraction

        Args:
            binary_float: binary representation of the float value

        Returns:
            dict: part name and binary representation
        """

        if len(binary_float) != 32:
            raise ValueError("You need 32 bits")

        sign = binary_float[0]
        exponent = binary_float[1:9]
        fraction = binary_float[9:32]
        d = {"sign": sign, "exponent": exponent, "fraction": fraction}
        return d

    @staticmethod
    def _reconstruct_float_value(sign: bool, exponent: Tuple[bool], fraction: Tuple[bool]) -> float:
        """
        From the binary float representation "reconstruct" (calculate) the float value

        Args:
            sign: sign value as a bool
            exponent: exponent as a tuple of bools
            fraction: fraction as a tuple of bools

        Returns:
            float: calculated float value
        """

        if len(fraction) != 23:
            raise ValueError("Fraction should be 23 values bits")
        if len(exponent) != 8:
            raise ValueError("Exponent should be 8 bits")
        if not isinstance(sign, bool):
            raise ValueError("Sign is a single bit")

        fraction = (True,) + fraction
        fraction_as_int = int(FloatBinary.bool_to_str_representation(fraction), 2) / 2**23
        exponent_as_int = int(FloatBinary.bool_to_str_representation(exponent), 2) - 127
        sign_as_int: int = -1 if sign else 1
        return sign_as_int * fraction_as_int * (2**exponent_as_int)

    def reconstruct_float_value(self) -> float:
        """
        From the binary float representation "reconstruct" (calculate) the float value

        Returns:
            float: calculated float value
        """

        return self._reconstruct_float_value(self.sign, self.exponent, self.fraction)

    @staticmethod
    def bool_to_str_representation(vals) -> str:
        # 0 = False; 1 = True
        return "".join(["1" if x else "0" for x in vals])

    def modify_clone(self,
                     sign: bool = None,
                     exponent: Tuple[bool] = None,
                     fraction: Tuple[bool] = None) -> "FloatBinary":
        sign = sign if sign is not None else self.sign
        exponent = exponent if exponent is not None else self.exponent
        fraction = fraction if fraction is not None else self.fraction
        
        new_float_value = FloatBinary._reconstruct_float_value(sign=sign, exponent=exponent, fraction=fraction)
        return FloatBinary(new_float_value)

    def as_bit_str(self) -> str:
        return self.bool_to_str_representation(self._bin)
