import re


def dna_complement(DNA_str):
    if len(DNA_str) == 0 or re.search('[^atgc]', DNA_str, re.IGNORECASE):
        return None
    else:
        DNA_str = DNA_str.upper()
        result = DNA_str.translate(str.maketrans("ATGC", "TACG"))
        return result


print("Input String is : atATCGGCTAccgg")
result_str1 = dna_complement('atATCGGCTAccgg')
print("Output String is : " + result_str1)
print("Input Invalid String is : amATCGGCTAccgg")
result_str2 = dna_complement('amATCGGCTAccgg')
print(result_str2)