#!/usr/bin/env node

/* The number, 197, is called a circular prime because all
   rotations of the digits: 197, 971, and 719, are themselves prime.

   How many circular primes are there below one million? */

var fns = require('../functions.js'),
    operator = require('../operator.js'),
    timer = require('../timer.js');

// from python_code.functions import sieve

// def contains_only_digits(n, digits):
//     n_digits = [int(dig) for dig in str(n)]
//     return set(n_digits) <= set(digits)

// def all_circular_perms(list_):
//     n = len(list_)
//     result = []
//     for lead in range(n):
//         indices = [index % n for index in range(lead, lead + n)]
//         result.append([list_[index] for index in indices])
//     return result

// def all_circular_perms_int(n):
//     digs = [dig for dig in str(n)]
//     return [int(''.join(perm)) for perm in all_circular_perms(digs)]

// def all_circular_perm_in(prime, primes):
//     perms = all_circular_perms_int(prime)
//     return set(perms) <= set(primes)

// def all_circular(n):
//     # the number of digits limits the size of all permutations
//     digs = len(str(n))
//     possible_primes = [2, 5] + \
//         [prime for prime in sieve(10**digs - 1)
//          if contains_only_digits(prime, [1, 3, 7, 9])]
//     return [prime for prime in possible_primes if prime <= n
//              and all_circular_perm_in(prime, possible_primes)]

exports.main = function() {
    //    print len(all_circular(10**6 - 1))
    return 1;
};

if (require.main === module) {
    timer.timer(35, exports.main);
}
