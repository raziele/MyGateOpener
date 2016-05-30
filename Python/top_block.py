#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sat May 28 01:43:33 2016
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
        self._variable_config_LowCO_config.read("/home/maayan4/ParkingRC/Parking_RC_config.ini")
        try: variable_config_LowCO = self._variable_config_LowCO_config.getfloat("BPF", "Low_CO")
        except: variable_config_LowCO = 150e3
        self.variable_config_LowCO = variable_config_LowCO
        self._variable_config_HighCO_config = ConfigParser.ConfigParser()
        self._variable_config_HighCO_config.read("/home/maayan4/ParkingRC/Parking_RC_config.ini")
        try: variable_config_HighCO = self._variable_config_HighCO_config.getfloat("BPF", "High_CO")
        except: variable_config_HighCO = 300e3
        self.variable_config_HighCO = variable_config_HighCO
        self.samp_rate = samp_rate = 2000000
        self.omega = omega = 250
        self.gain_coeff = gain_coeff = 1
        self.fft_size_slider = fft_size_slider = 1024
        self.fft_size1 = fft_size1 = 1024
        self.decimation_coeff = decimation_coeff = 4
        self.center_freq = center_freq = 433.5E6
        self.Low_CO = Low_CO = variable_config_LowCO
        self.High_CO = High_CO = variable_config_HighCO

        ##################################################
        # Blocks
        ##################################################
        self.nb = self.nb = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "RF")
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "filtered")
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "BB")
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "Auto Corr")
        self.Add(self.nb)
        _omega_sizer = wx.BoxSizer(wx.VERTICAL)
        self._omega_text_box = forms.text_box(
        	parent=self.nb.GetPage(2).GetWin(),
        	sizer=_omega_sizer,
        	value=self.omega,
        	callback=self.set_omega,
        	label="omega",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._omega_slider = forms.slider(
        	parent=self.nb.GetPage(2).GetWin(),
        	sizer=_omega_sizer,
        	value=self.omega,
        	callback=self.set_omega,
        	minimum=0,
        	maximum=1000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.nb.GetPage(2).Add(_omega_sizer)
        _center_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._center_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_center_freq_sizer,
        	value=self.center_freq,
        	callback=self.set_center_freq,
        	label="Center frequency",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._center_freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_center_freq_sizer,
        	value=self.center_freq,
        	callback=self.set_center_freq,
        	minimum=433E6,
        	maximum=435E6,
        	num_steps=200,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_center_freq_sizer)
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
        self.wxgui_scopesink2_0_0_0_0 = scopesink2.scope_sink_f(
        	self.nb.GetPage(2).GetWin(),
        	title="BB",
        	sample_rate=samp_rate*gain_coeff/decimation_coeff,
        	v_scale=0,
        	v_offset=0,
        	t_scale=1,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.nb.GetPage(2).GridAdd(self.wxgui_scopesink2_0_0_0_0.win, 0, 1, 1, 1)
        self.wxgui_scopesink2_0_0_0 = scopesink2.scope_sink_f(
        	self.nb.GetPage(2).GetWin(),
        	title="After MM",
        	sample_rate=samp_rate/decimation_coeff,
        	v_scale=0,
        	v_offset=0,
        	t_scale=1,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.nb.GetPage(2).GridAdd(self.wxgui_scopesink2_0_0_0.win, 0, 0, 1, 1)
        self.wxgui_fftsink2_0_0 = fftsink2.fft_sink_c(
        	self.nb.GetPage(0).GetWin(),
        	baseband_freq=center_freq,
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
        )
        self.nb.GetPage(0).Add(self.wxgui_fftsink2_0_0.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.nb.GetPage(1).GetWin(),
        	baseband_freq=center_freq,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate*gain_coeff/decimation_coeff,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="Filtered",
        	peak_hold=False,
        )
        self.nb.GetPage(1).Add(self.wxgui_fftsink2_0.win)
        self.low_pass_filter_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate*gain_coeff/decimation_coeff, 5000, 3500, firdes.WIN_HAMMING, 6.76))
        _fft_size_slider_sizer = wx.BoxSizer(wx.VERTICAL)
        self._fft_size_slider_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_fft_size_slider_sizer,
        	value=self.fft_size_slider,
        	callback=self.set_fft_size_slider,
        	label="fft_size_1",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._fft_size_slider_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_fft_size_slider_sizer,
        	value=self.fft_size_slider,
        	callback=self.set_fft_size_slider,
        	minimum=24,
        	maximum=1024,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_fft_size_slider_sizer)
        self.digital_correlate_access_code_bb_0 = digital.correlate_access_code_bb("11111", 0)
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(omega*(1+0.0), 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.digital_binary_slicer_fb_1 = digital.binary_slicer_fb()
        self.blocks_wavfile_sink_0_0 = blocks.wavfile_sink("/home/maayan4/ParkingRC/baseband_mm.wav", 1, samp_rate/8, 8)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink("/home/maayan4/ParkingRC/baseband.wav", 1, samp_rate*gain_coeff/decimation_coeff, 8)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((100, ))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/maayan4/ParkingRC/ParkingRC-f4.335000e+08-s2.000000e+06-t20160513215032.cfile", False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, "/home/maayan4/ParkingRC/parkRC_bytes", False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_add_const_vxx_0_0 = blocks.add_const_vff((-0.3, ))
        self.band_pass_filter_0 = filter.fir_filter_ccc(decimation_coeff, firdes.complex_band_pass(
        	gain_coeff, samp_rate, Low_CO, High_CO, High_CO-Low_CO, firdes.WIN_HAMMING, 6.76))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0, 0), (self.blocks_complex_to_mag_0, 0))    
        self.connect((self.band_pass_filter_0, 0), (self.wxgui_fftsink2_0, 0))    
        self.connect((self.blocks_add_const_vxx_0_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_const_vxx_0_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.band_pass_filter_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_fftsink2_0_0, 0))    
        self.connect((self.digital_binary_slicer_fb_1, 0), (self.digital_correlate_access_code_bb_0, 0))    
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.blocks_wavfile_sink_0_0, 0))    
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_1, 0))    
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.wxgui_scopesink2_0_0_0, 0))    
        self.connect((self.digital_correlate_access_code_bb_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.blocks_wavfile_sink_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.wxgui_scopesink2_0_0_0_0, 0))    


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
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(self.gain_coeff, self.samp_rate, self.Low_CO, self.High_CO, self.High_CO-self.Low_CO, firdes.WIN_HAMMING, 6.76))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate*self.gain_coeff/self.decimation_coeff, 5000, 3500, firdes.WIN_HAMMING, 6.76))
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate*self.gain_coeff/self.decimation_coeff)
        self.wxgui_fftsink2_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0_0_0.set_sample_rate(self.samp_rate/self.decimation_coeff)
        self.wxgui_scopesink2_0_0_0_0.set_sample_rate(self.samp_rate*self.gain_coeff/self.decimation_coeff)

    def get_omega(self):
        return self.omega

    def set_omega(self, omega):
        self.omega = omega
        self._omega_slider.set_value(self.omega)
        self._omega_text_box.set_value(self.omega)
        self.digital_clock_recovery_mm_xx_0.set_omega(self.omega*(1+0.0))

    def get_gain_coeff(self):
        return self.gain_coeff

    def set_gain_coeff(self, gain_coeff):
        self.gain_coeff = gain_coeff
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(self.gain_coeff, self.samp_rate, self.Low_CO, self.High_CO, self.High_CO-self.Low_CO, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate*self.gain_coeff/self.decimation_coeff, 5000, 3500, firdes.WIN_HAMMING, 6.76))
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate*self.gain_coeff/self.decimation_coeff)
        self.wxgui_scopesink2_0_0_0_0.set_sample_rate(self.samp_rate*self.gain_coeff/self.decimation_coeff)

    def get_fft_size_slider(self):
        return self.fft_size_slider

    def set_fft_size_slider(self, fft_size_slider):
        self.fft_size_slider = fft_size_slider
        self._fft_size_slider_slider.set_value(self.fft_size_slider)
        self._fft_size_slider_text_box.set_value(self.fft_size_slider)

    def get_fft_size1(self):
        return self.fft_size1

    def set_fft_size1(self, fft_size1):
        self.fft_size1 = fft_size1

    def get_decimation_coeff(self):
        return self.decimation_coeff

    def set_decimation_coeff(self, decimation_coeff):
        self.decimation_coeff = decimation_coeff
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate*self.gain_coeff/self.decimation_coeff, 5000, 3500, firdes.WIN_HAMMING, 6.76))
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate*self.gain_coeff/self.decimation_coeff)
        self.wxgui_scopesink2_0_0_0.set_sample_rate(self.samp_rate/self.decimation_coeff)
        self.wxgui_scopesink2_0_0_0_0.set_sample_rate(self.samp_rate*self.gain_coeff/self.decimation_coeff)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self._center_freq_slider.set_value(self.center_freq)
        self._center_freq_text_box.set_value(self.center_freq)
        self.wxgui_fftsink2_0.set_baseband_freq(self.center_freq)
        self.wxgui_fftsink2_0_0.set_baseband_freq(self.center_freq)

    def get_Low_CO(self):
        return self.Low_CO

    def set_Low_CO(self, Low_CO):
        self.Low_CO = Low_CO
        self._Low_CO_slider.set_value(self.Low_CO)
        self._Low_CO_text_box.set_value(self.Low_CO)
        self._variable_config_LowCO_config = ConfigParser.ConfigParser()
        self._variable_config_LowCO_config.read("/home/maayan4/ParkingRC/Parking_RC_config.ini")
        if not self._variable_config_LowCO_config.has_section("BPF"):
        	self._variable_config_LowCO_config.add_section("BPF")
        self._variable_config_LowCO_config.set("BPF", "Low_CO", str(self.Low_CO))
        self._variable_config_LowCO_config.write(open("/home/maayan4/ParkingRC/Parking_RC_config.ini", 'w'))
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(self.gain_coeff, self.samp_rate, self.Low_CO, self.High_CO, self.High_CO-self.Low_CO, firdes.WIN_HAMMING, 6.76))

    def get_High_CO(self):
        return self.High_CO

    def set_High_CO(self, High_CO):
        self.High_CO = High_CO
        self._High_CO_slider.set_value(self.High_CO)
        self._High_CO_text_box.set_value(self.High_CO)
        self._variable_config_HighCO_config = ConfigParser.ConfigParser()
        self._variable_config_HighCO_config.read("/home/maayan4/ParkingRC/Parking_RC_config.ini")
        if not self._variable_config_HighCO_config.has_section("BPF"):
        	self._variable_config_HighCO_config.add_section("BPF")
        self._variable_config_HighCO_config.set("BPF", "High_CO", str(self.High_CO))
        self._variable_config_HighCO_config.write(open("/home/maayan4/ParkingRC/Parking_RC_config.ini", 'w'))
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(self.gain_coeff, self.samp_rate, self.Low_CO, self.High_CO, self.High_CO-self.Low_CO, firdes.WIN_HAMMING, 6.76))


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = top_block()
    tb.Start(True)
    tb.Wait()
