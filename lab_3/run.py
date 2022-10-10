class Encoder():
    def __init__(self, input_encode: str = 'YYYYggkeeeAAABV', input_decode: str = 'Y4g2ke3A3BV') -> None:
        self._alphabet_encode = 'abcdefghijklmnopqrstuvwxyz'
        self._alphabet_encode = self._alphabet_encode.upper() + self._alphabet_encode
        self._alphabet_decode = self._alphabet_encode + '1234567890'
        self._input_encode = input_encode.strip()
        self._input_decode = input_decode.strip()

    def encode_string(self) -> str:
        # task 1 encode input str 'YYYYggkeeeAAABV' -> 'Y4g2ke3A3BV'

        output_str = str()
        if set(self._input_encode).issubset(set(self._alphabet_encode)):
            temp_string = self._input_encode
            while (len(temp_string) > 0):
                # count letter in string
                count = temp_string.count(temp_string[0])
                # if count > 1 -> add letter and count to output_str
                output_str += temp_string[0] + \
                    str(count) if count > 1 else temp_string[0]
                temp_string = temp_string.replace(temp_string[0], '')
        else:
            raise ValueError('Wrong input string')
        return output_str

    def decode_string(self):
        # task 1.1 decode input str 'Y4g2ke3A3BV' -> 'YYYYggkeeeAAABV'

        output_str = str()
        if set(self._input_decode).issubset(set(self._alphabet_decode)):
            for char in range(len(self._input_decode)):
                if self._input_decode[char].isdigit():
                    # if char is digit -> add previous char*digit to output_str
                    output_str += self._input_decode[char-1] * \
                        (int(self._input_decode[char])-1)
                else:
                    output_str += self._input_decode[char]

        else:
            raise ValueError('Wrong input string')
        return output_str

    def most_common(self) -> str:
        # task 2 find 3 most common letters in string
        output_str = str()
        temp_string = self._input_encode
        for _ in range(3):
            # find max letter in string
            max_letter = max(set(temp_string), key=temp_string.count)
            # add max letter to output_str
            output_str += f'{max_letter}:{str(temp_string.count(max_letter))}\n'
            # delete max letter from string
            temp_string = temp_string.replace(max_letter, '')
        return output_str


class Num_to_string():
    def __init__(self, number):
        self._number = number if number < 1000 and number > 0 else None

    def units(self, number: int) -> str:
        units = ('один', 'два', 'три', 'четыре',
                 'пять', 'шесть', 'семь', 'восемь', 'девять')
        return units[number]

    def tens(self, number: int) -> str:
        tens = ('десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят',
                'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто')
        return tens[number]

    def tens_eleven_to_nineteen(self, number: int) -> str:
        tens_11_to_19 = ('одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать',
                         'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать')
        return tens_11_to_19[number]

    def hundreds(self, number: int) -> str:
        hundreds = ('сто', 'двести', 'триста', 'четыреста',
                    'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот')
        return hundreds[number]

    def to_string(self) -> str:
        output_string = str()
        if self._number is not None:

            if self._number > 99:
                if self._number % 100 not in range(11, 20):
                    output_string += self.hundreds(self._number //
                                                   100 - 1) + ' '
                    output_string += self.tens(self._number %
                                               100 // 10 - 1) + ' '
                    output_string += self.units(self._number % 10 - 1)
                else:
                    output_string += self.hundreds(self._number //
                                                   100 - 1) + ' '
                    output_string += self.tens_eleven_to_nineteen(
                        self._number % 100-11)

            elif self._number > 9:
                if self._number % 100 not in range(11, 20):
                    output_string += self.tens(self._number // 10 - 1) + ' '
                    output_string += self.units(self._number % 10 - 1)
                else:
                    output_string += self.tens_eleven_to_nineteen(
                        self._number % 10 - 1)
            else:
                output_string += self.units(self._number - 1)
        else:
            raise ValueError('Wrong number')

        return f'{str(self._number)}:{output_string}'


if __name__ == '__main__':
    # _ = Encoder(input('Enter string to encode: '),
    #             input('Enter string to decode: '))
    _ = Encoder()
    print(
        f'Кодирование строки:\n{_._input_encode} -> {_.encode_string()}', end='\n\n')
    print(
        f'Раскодирование строки:\n{_._input_decode} -> {_.decode_string()}', end='\n\n')
    print(
        f'Три самых частовстречаемых символа в строке:\n{_.most_common()}', end='\n\n')

    # _ = Num_to_string(int(input('Enter number: ')))
    _ = Num_to_string(12)
    print(_.to_string())
