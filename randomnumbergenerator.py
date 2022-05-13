#!/usr/bin/env python3

import dearpygui.dearpygui as dpg
import random

range1 = 0
range2 = 0

def rand_gen(s=None, data=None):
	r = 0
	try:
		r = random.randint(range1, range2)
	except Exception:
		dpg.set_value("rand", "(invalid)")
		return
	dpg.set_value("rand", str(r))

def rand_cb(s, data):
	if not s in globals():
		raise ValueError("invalid sender " + s)
	globals()[s] = data
	rand_gen()

dpg.create_context()

with dpg.window(tag="rng", label="Random Generator"):
	with dpg.group(tag="rgroup", width=200, horizontal=True):
		dpg.add_text("Range:")
		dpg.add_input_int(tag="range1", callback=rand_cb)
		dpg.add_text("-")
		dpg.add_input_int(tag="range2", callback=rand_cb)
	with dpg.group(tag="result", horizontal=True):
		dpg.add_text("Output:")
		dpg.add_text(tag="rand", default_value="(uninitialized)")
	dpg.add_button(label="Regenerate", callback=rand_gen)

dpg.create_viewport(width=640, height=480)
dpg.setup_dearpygui()
dpg.set_primary_window("rng", True)
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
