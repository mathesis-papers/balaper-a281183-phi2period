import json
from fractions import Fraction
from math import comb, factorial
from math import gcd


PREFIX = [
    1, 2, 32, 1376, 114176, 15519488, 3132551168,
    879422726144, 327670676455424, 156439068819587072,
    93116847688811282432, 67602541384815095054336,
    58796336342280763841970176, 60351125684887424790500999168,
    72187248798124538021926003539968,
    99529442030183464236437157900713984,
    156697512616609083360755035696397287424,
]


def factor(modulus):
    result = []
    prime = 2
    while prime * prime <= modulus:
        exponent = 0
        while modulus % prime == 0:
            modulus //= prime
            exponent += 1
        if exponent:
            result.append((prime, exponent))
        prime += 1
    if modulus > 1:
        result.append((modulus, 1))
    return result


def onset(modulus):
    return max([0] + [exponent if prime == 2 else (exponent + 1) // 2
                     for prime, exponent in factor(modulus)])


def totient(modulus):
    return sum(gcd(value, modulus) == 1 for value in range(1, modulus + 1))


def manyama(maximum, exponent=2, modulus=None, flow_exponent=4):
    width = flow_exponent - 1
    previous = [1] * (width * maximum + 1)
    result = [1 % modulus if modulus else 1]
    for index in range(1, maximum + 1):
        current = []
        for offset in range(width * (maximum - index) + 1):
            power = exponent + 2 * offset
            value = power * ((power + width) * previous[offset + width]
                             - (power + width - 1) * previous[offset + width - 1])
            current.append(value % modulus if modulus else value)
        previous = current
        result.append(current[0])
    return result


def differential(maximum, polynomial, modulus=None):
    values = ([value % modulus for value in polynomial]
              if modulus else list(polynomial))
    result = [values[0]]
    for derivative in range(1, 2 * maximum + 1):
        updated = [0] * (len(values) + 3)
        for degree in range(1, len(values)):
            value = degree * values[degree]
            updated[degree - 1] += value
            updated[degree + 1] += 2 * value
            updated[degree + 3] += value
        values = ([value % modulus for value in updated]
                  if modulus else updated)
        if derivative % 2 == 0:
            result.append(values[0])
    return result


def nested(maximum, modulus):
    values = [1 % modulus]
    result = [1 % modulus]
    for index in range(1, 2 * maximum + 1):
        product = [0] * (len(values) + 2)
        for degree, value in enumerate(values):
            product[degree] += value
            product[degree + 2] += value
        derivative = [degree * product[degree]
                      for degree in range(1, len(product))]
        updated = [0] * (len(derivative) + 2)
        for degree, value in enumerate(derivative):
            updated[degree] += value
            updated[degree + 2] += value
        values = [value % modulus for value in updated]
        if index % 2 == 0:
            result.append(values[0])
    return result


def multiply(left, right, size, modulus):
    result = [0] * size
    for left_degree, left_value in enumerate(left):
        for right_degree, right_value in enumerate(right):
            degree = left_degree + right_degree
            if degree < size:
                result[degree] += left_value * right_value
    return [value % modulus for value in result]


def derivative(values):
    return [(degree + 1) * value for degree, value in enumerate(values[1:])] + [0]


def matrix_step(values, parameter, parity, modulus):
    size = len(values)
    auxiliary = multiply([2, 2], derivative(values), size, modulus)
    auxiliary = [(value + parity * original) % modulus
                 for value, original in zip(auxiliary, values)]
    first = multiply([1, parity + 2 * parameter - 1], auxiliary, size, modulus)
    second = multiply([0, 2, 2], derivative(auxiliary), size, modulus)
    result = [(left + right) % modulus for left, right in zip(first, second)]
    for unused in range(2 * parameter - 2):
        result = multiply(result, [1, 1], size, modulus)
    return result


def matrix_column(maximum, parameter, power, modulus):
    size = (modulus + 1) // 2
    parity = power % 2
    values = [1] + [0] * (size - 1)
    for unused in range((power - parity) // 2):
        values = multiply(values, [1, 1], size, modulus)
    result = [values[0]]
    for unused in range(maximum):
        values = matrix_step(values, parameter, parity, modulus)
        result.append(values[0])
    return result


def certificates():
    rows = [
        ('A281180', 2, 4, 1, 7, 18, 1, 6, 2),
        ('A281181', 2, 1, 0, 10, 8, 0, None, None),
        ('A281181', 2, 1, 0, 9, 3, 1, None, None),
        ('A281181', 2, 1, 0, 13, 72, 0, 6, 7),
        ('A281183', 2, 2, 0, 11, 25, 1, 5, 5),
        ('A281184', 2, 3, 0, 11, 25, 1, 5, 5),
        ('A281440', 4, 1, 0, 13, 72, 0, 6, 6),
    ]
    result = []
    for name, parameter, power, offset, modulus, period, start, row_width, ratio in rows:
        size = (modulus + 1) // 2
        column_start = start - offset
        maximum = column_start + period + size
        values = matrix_column(maximum, parameter, power, modulus)
        independent = manyama(maximum, power, modulus, 2 * parameter)
        assert values == independent
        zero_differences = [(values[index + period] - values[index]) % modulus
                            for index in range(column_start, column_start + size)]
        assert zero_differences == [0] * size
        witnesses = []
        for prime, unused in factor(period):
            reduced = period // prime
            assert values[column_start] != values[column_start + reduced]
            witnesses.append({'prime': prime, 'excluded_shift': reduced,
                              'oeis_index': start, 'values':
                              [values[column_start], values[column_start + reduced]]})
        parity = power % 2
        columns = []
        for degree in range(size):
            basis = [0] * size
            basis[degree] = 1
            columns.append(matrix_step(basis, parameter, parity, modulus))
        row = {'sequence': name, 'd': parameter, 'k': power, 'offset': offset,
               'modulus': modulus, 'dimension': size, 'matrix_columns': columns,
               'period': period, 'oeis_onset': start,
               'one_period_residues': values[column_start:column_start + period],
               'zero_period_differences': zero_differences,
               'minimality_witnesses': witnesses,
               'independent_comparison_count': maximum + 1}
        if row_width is not None:
            geometric = [(values[index + row_width] - ratio * values[index]) % modulus
                         for index in range(column_start, column_start + size)]
            assert geometric == [0] * size
            row['geometric_rows'] = {'width': row_width, 'ratio': ratio,
                                     'zero_differences': geometric}
        result.append(row)
    twelve = matrix_column(6, 2, 1, 12)
    assert twelve == [1] * 7
    assert twelve == manyama(6, 1, 12)
    return {'period_rows': result,
            'a281181_mod12': {'dimension': 6, 'initial_residues': twelve,
                              'zero_successive_differences': [0] * 6},
            'scope': 'Finite matrix identities imply all-index conclusions by Cayley-Hamilton as proved in the note.'}


def source_nested_formulas(maximum):
    size = 2 * maximum + 1

    def product(left, right, bound):
        values = [Fraction(0)] * bound
        for left_degree, left_value in enumerate(left):
            for right_degree, right_value in enumerate(right):
                if left_degree + right_degree < bound:
                    values[left_degree + right_degree] += left_value * right_value
        return values

    cosine = [Fraction(0) if degree % 2 else
              Fraction((-1) ** (degree // 2), factorial(degree))
              for degree in range(size)]
    square = product(cosine, cosine, size)
    secant_square = [Fraction(1)]
    for degree in range(1, size):
        secant_square.append(-sum(square[index] * secant_square[degree - index]
                                  for index in range(1, degree + 1)))
    root_inverse = [Fraction(0) if degree % 2 else
                    Fraction(comb(degree, degree // 2), 2 ** degree)
                    for degree in range(size)]
    columns = []
    for multiplier, initial in [(secant_square, [Fraction(1)] + [Fraction(0)] * (size - 1)),
                                (root_inverse, root_inverse)]:
        values = initial[:]
        column = [values[0]]
        for index in range(1, 2 * maximum + 1):
            values = product(multiplier, values, len(values))
            values = [(degree + 1) * value for degree, value in enumerate(values[1:])]
            if index % 2 == 0:
                column.append(values[0])
        assert column == manyama(maximum)
        columns.append(column)
    return {'indices': [0, maximum], 'formulas': ['f: sec(z)^2', 'h: (1-z^2)^(-1/2)'],
            'exact_comparisons': sum(len(column) for column in columns)}


def main():
    assert manyama(16) == PREFIX
    assert differential(16, [1, 0, 1]) == PREFIX
    comparisons = 0
    sibling_comparisons = 0
    method_comparisons = 0
    nested_comparisons = 0
    periods = []
    for modulus in range(1, 61):
        start = onset(modulus)
        shift = 1 if modulus <= 2 else totient(modulus) ** 2 // 2
        maximum = max(96, start + shift + 63)
        values = manyama(maximum, modulus=modulus)
        for index in range(start, start + 64):
            assert values[index + shift] == values[index]
            comparisons += 1
        sibling = manyama(maximum, exponent=4, modulus=modulus)
        for index in range(start, start + 64):
            assert sibling[index + shift] == sibling[index]
            sibling_comparisons += 1
        if modulus <= 32:
            independent = differential(96, [1, 0, 1], modulus)
            assert independent == values[:97]
            method_comparisons += 97
            alternative = nested(96, modulus)
            assert alternative == independent
            nested_comparisons += 97
        periods.append({'modulus': modulus, 'onset': start, 'shift': shift})
    for exponent in range(1, 13):
        values = differential(48, [1, 0, 1], 2 ** exponent)
        assert all(value == 0 for value in values[exponent:])
    eleven = manyama(100, modulus=11)
    assert all(eleven[index + 5] == 5 * eleven[index] % 11
               for index in range(1, 96))
    assert all(eleven[index + 25] == eleven[index] for index in range(1, 76))
    assert eleven[1] == 2 and eleven[6] == 10
    assert all(pow(5, exponent, 11) != 1 for exponent in range(1, 5))
    assert pow(5, 5, 11) == 1
    inverse = [(-1) ** (degree // 2) if degree % 2 == 0 else 0
               for degree in range(49)]
    assert differential(24, inverse) == manyama(24, exponent=-2)
    assert all(value % (2 ** index) == 0
               for index, value in enumerate(manyama(24, exponent=-2)))
    assert all(value % 2 == 1 for value in manyama(48, exponent=1))
    assert all(value % 2 == 0 for value in manyama(48, exponent=4)[1:])
    report = {
        'status': 'all_checks_passed',
        'prefix_terms': len(PREFIX),
        'prefix_methods': ['Manyama recurrence', 'polynomial differential operator'],
        'a281183_period_comparisons': comparisons,
        'a281180_period_comparisons': sibling_comparisons,
        'period_checks_per_modulus': 64,
        'period_moduli': [1, 60],
        'a281180_index': 'OEIS n equals polynomial-column index plus one',
        'independent_method_comparisons': method_comparisons,
        'independent_method_moduli': [1, 32],
        'independent_method_indices': [0, 96],
        'nested_derivative_comparisons': nested_comparisons,
        'two_adic_checks': {'exponents': [1, 12], 'indices': [0, 48]},
        'modulus_11': {'geometric_step': 5, 'ratio': 5,
                       'least_eventual_period': 25,
                       'a1': eleven[1], 'a6': eleven[6]},
        'scope': 'Finite coefficient and congruence checks; the note contains the arbitrary-modulus proof.',
        'period_parameters': periods,
        'residue_certificates': certificates(),
        'integral_series_example': {'observable': '(1+s^2)^(-1)',
                                   'coefficient_indices': [0, 24],
                                   'independent_comparisons': 25},
        'a281182_mod2': {'eventual_tail': [1, 0], 'least_eventual_period': 2,
                         'independent_parity_indices': [0, 48]},
        'other_source_nested_formulas': source_nested_formulas(12),
    }
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
