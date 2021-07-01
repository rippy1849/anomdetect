from py2cfg import CFGBuilder

cfg = CFGBuilder().build_from_file('example', './Test.py')

cfg.build_visual('exampleCFG', 'pdf')