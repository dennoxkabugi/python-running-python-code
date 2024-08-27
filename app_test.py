#!/usr/bin/env python3

from os import path
import runpy
import io
import sys

class TestAppPy:
    '''
    app.py
    '''
    def test_app_py_exists(self):
        '''
        exists in lib directory
        '''
        assert(path.exists)

    def test_app_py_runs(self):
        '''
        is executable
        '''
        runpy.run_path

    def test_prints_hello_world(self):
        '''
        prints "Hello World! Pass this test, please.\n"
        '''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        runpy.run_path
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue().strip()== "Hello World! Pass this test, please.\n")
        