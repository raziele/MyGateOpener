#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Jun 14 20:22:40 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import ConfigParser
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self._variable_config_LowCO_config = ConfigParser.ConfigParser()
        self._variable_config_LowCO_config.read("/home/maayan4/MyReps/MyGateOpener/LiveSession/Parking_RC_config.ini")
        try: variable_config_LowCO = self._variable_config_LowCO_config.getfloat("BPF", "Low_CO")
        except: variable_config_LowCO = 150e3
        self.variable_config_LowCO = variable_config_LowCO
        self._variable_config_HighCO_config = ConfigParser.ConfigParser()
        self._variable_config_HighCO_config.read("/home/maayan4/MyReps/MyGateOpener/LiveSession/Parking_RC_config.ini")
        try: variable_config_HighCO = self._variable_config_HighCO_config.getfloat("BPF", "High_CO")
        except: variable_config_HighCO = 300e3
        self.variable_config_HighCO = variable_config_HighCO
        self.samp_rate = samp_rate = 2E6
        self.fc = fc = 433.5E6
        self.Low_CO = Low_CO = variable_config_LowCO
        self.High_CO = High_CO = variable_config_HighCO
        self.Decim_value = Decim_value = 4

        ##################################################
        # Blocks
        ##################################################
        self.nb = self.nb = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "RF")
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "filtered")
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "BB")
        self.Add(self.nb)
        _Low_CO_sizer = wx.BoxSizer(wx.VERTICAL)
        self._Low_CO_text_box = forms.text_box(
        	parent=self.nb.GetPage(1).GetWin(),
        	sizer=_Low_CO_sizer,
        	value=self.Low_CO,
        	callback=self.set_Low_CO,
        	label="Low_CO",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._Low_CO_slider = forms.slider(
        	parent=self.nb.GetPage(1).GetWin(),
        	sizer=_Low_CO_sizer,
        	value=self.Low_CO,
        	callback=self.set_Low_CO,
        	minimum=0,
        	maximum=500e3,
        	num_steps=200,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb.GetPage(1).Add(_Low_CO_sizer)
        _High_CO_sizer = wx.BoxSizer(wx.VERTICAL)
        self._High_CO_text_box = forms.text_box(
        	parent=self.nb.GetPage(1).GetWin(),
        	sizer=_High_CO_sizer,
        	value=self.High_CO,
        	callback=self.set_High_CO,
        	label="High_CO",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._High_CO_slider = forms.slider(
        	parent=self.nb.GetPage(1).GetWin(),
        	sizer=_High_CO_sizer,
        	value=self.High_CO,
        	callback=self.set_High_CO,
        	minimum=150e3,
        	maximum=500e3,
        	num_steps=200,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb.GetPage(1).Add(_High_CO_sizer)
        self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_c(
        	self.nb.GetPage(0).GetWin(),
        	baseband_freq=fc,
        	dynamic_range=100,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=512,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="RF",
        )
        self.nb.GetPage(0).Add(self.wxgui_waterfallsink2_0.win)
        self.wxgui_scopesink2_0_0 = scopesink2.scope_sink_f(
        	self.nb.GetPage(2).GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate/Decim_value,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.nb.GetPage(2).Add(self.wxgui_scopesink2_0_0.win)
        self.wxgui_fftsink2_0_0 = fftsink2.fft_sink_c(
        	self.nb.GetPage(1).GetWin(),
        	baseband_freq=fc,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="Filtered",
        	peak_hold=False,
        )
        self.nb.GetPage(1).Add(self.wxgui_fftsink2_0_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.nb.GetPage(0).GetWin(),
        	baseband_freq=fc,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="RF",
        	peak_hold=False,
        	win=window.flattop,
        )
        self.nb.GetPage(0).Add(self.wxgui_fftsink2_0.win)
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(250*(1+0.0), 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.digital_binary_slicer_fb_1 = digital.binary_slicer_fb()
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((100, ))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/maayan4/MyReps/MyGateOpener/Samples/ParkingRC-f4.335000e+08-s2.000000e+06-t20160513215_trimmed.cfile", False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, "/home/maayan4/MyReps/MyGateOpener/LiveSession/output_code", False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_add_const_vxx_0_0 = blocks.add_const_vff((-0.3, ))
        self.band_pass_filter_0_0 = filter.fir_filter_ccc(Decim_value, firdes.complex_band_pass(
        	1, samp_rate, Low_CO, High_CO, High_CO-Low_CO, firdes.WIN_HAMMING, 6.76))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_complex_to_mag_0, 0))    
        self.connect((self.band_pass_filter_0_0, 0), (self.wxgui_fftsink2_0_0, 0))    
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_const_vxx_0_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.band_pass_filter_0_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_waterfallsink2_0, 0))    
        self.connect((self.digital_binary_slicer_fb_1, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_1, 0))    
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.wxgui_scopesink2_0_0, 0))    

    def get_variable_config_LowCO(self):
        return self.variable_config_LowCO

    def set_variable_config_LowCO(self, variable_config_LowCO):
        self.variable_config_LowCO = variable_config_LowCO
        self.set_Low_CO(self.variable_config_LowCO)

    def get_variable_config_HighCO(self):
        return self.variable_config_HighCO

    def set_variable_config_HighCO(self, variable_config_HighCO):
        self.variable_config_HighCO = variable_config_HighCO
        self.set_High_CO(self.variable_config_HighCO)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate, self.Low_CO, self.High_CO, self.High_CO-self.Low_CO, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0_0.set_sample_rate(self.samp_rate/self.Decim_value)
        self.wxgui_waterfallsink2_0.set_sample_rate(self.samp_rate)

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.wxgui_fftsink2_0.set_baseband_freq(self.fc)
        self.wxgui_fftsink2_0_0.set_baseband_freq(self.fc)
        self.wxgui_waterfallsink2_0.set_baseband_freq(self.fc)

    def get_Low_CO(self):
        return self.Low_CO

    def set_Low_CO(self, Low_CO):
        self.Low_CO = Low_CO
        self._Low_CO_slider.set_value(self.Low_CO)
        self._Low_CO_text_box.set_value(self.Low_CO)
        self._variable_config_LowCO_config = ConfigParser.ConfigParser()
        self._variable_config_LowCO_config.read("/home/maayan4/MyReps/MyGateOpener/LiveSession/Parking_RC_config.ini")
        if not self._variable_config_LowCO_config.has_section("BPF"):
        	self._variable_config_LowCO_config.add_section("BPF")
        self._variable_config_LowCO_config.set("BPF", "Low_CO", str(self.Low_CO))
        self._variable_config_LowCO_config.write(open("/home/maayan4/MyReps/MyGateOpener/LiveSession/Parking_RC_config.ini", 'w'))
        self.band_pass_filter_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate, self.Low_CO, self.High_CO, self.High_CO-self.Low_CO, firdes.WIN_HAMMING, 6.76))

    def get_High_CO(self):
        return self.High_CO

    def set_High_CO(self, High_CO):
        self.High_CO = High_CO
        self._High_CO_slider.set_value(self.High_CO)
        self._High_CO_text_box.set_value(self.High_CO)
        self._variable_config_HighCO_config = ConfigParser.ConfigParser()
        self._variable_config_HighCO_config.read("/home/maayan4/MyReps/MyGateOpener/LiveSession/Parking_RC_config.ini")
        if not self._variable_config_HighCO_config.has_section("BPF"):
        	self._variable_config_HighCO_config.add_section("BPF")
        self._variable_config_HighCO_config.set("BPF", "High_CO", str(self.High_CO))
        self._variable_config_HighCO_config.write(open("/home/maayan4/MyReps/MyGateOpener/LiveSession/Parking_RC_config.ini", 'w'))
        self.band_pass_filter_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate, self.Low_CO, self.High_CO, self.High_CO-self.Low_CO, firdes.WIN_HAMMING, 6.76))

    def get_Decim_value(self):
        return self.Decim_value

    def set_Decim_value(self, Decim_value):
        self.Decim_value = Decim_value
        self.wxgui_scopesink2_0_0.set_sample_rate(self.samp_rate/self.Decim_value)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
