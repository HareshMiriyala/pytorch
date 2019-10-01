#!/usr/bin/env python3
from __future__ import absolute_import, division, print_function, unicode_literals

import sys
from dist_autograd_test import TestDistAutograd
from common_distributed import MultiProcessTestCase
from common_utils import TEST_WITH_ASAN, run_tests

import unittest

@unittest.skipIf(
    sys.version_info < (3, 6),
    "Test is flaky for py35, see https://github.com/pytorch/pytorch/issues/27157",
)
@unittest.skipIf(TEST_WITH_ASAN, "Skip ASAN as torch + multiprocessing spawn have known issues")
class TestDistAutogradWithSpawn(MultiProcessTestCase, TestDistAutograd):

    def setUp(self):
        super(TestDistAutogradWithSpawn, self).setUp()
        self._spawn_processes()

if __name__ == '__main__':
    run_tests()
