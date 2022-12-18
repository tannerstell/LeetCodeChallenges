class Solution:
    def romanToInt(self, s: str) -> int:

        numerals = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10,
                    "XL": 40, "L": 50
            , "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}
        numeral = s
        number = 0
        j = 0
        while numeral != '':
            sub_numeral, sub_number = self.numeralFinder(numeral, numerals)
            numeral = numeral.rsplit(sub_numeral, 1)[0]
            number += sub_number
        return number
    def numeralFinder(self, numeral, numerals):
        s = numeral
        sub_numeral, sub_number = [[s[-i:], numerals[s[-i:]]] for i in range(4, 0, -1) if s[-i:] in numerals.keys()][0]
        return sub_numeral, sub_number
