#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Taurus-1 decoder
# Author: Daniel Estevez
# Description: Taurus-1 decoder
# Generated: Sun Oct  6 13:36:41 2019
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from ccsds_viterbi import ccsds_viterbi  # grc-generated hier_block
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
from rms_agc import rms_agc  # grc-generated hier_block
import lilacsat
import satellites
import sip
from gnuradio import qtgui


class taurus1(gr.top_block, Qt.QWidget):

    def __init__(self, bfo=12000, ip='127.0.0.1', port=7355, recstart=''):
        gr.top_block.__init__(self, "Taurus-1 decoder")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Taurus-1 decoder")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "taurus1")
        self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))


        ##################################################
        # Parameters
        ##################################################
        self.bfo = bfo
        self.ip = ip
        self.port = port
        self.recstart = recstart

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 5
        self.samp_per_sym = samp_per_sym = 5
        self.nfilts = nfilts = 16
        self.alpha = alpha = 0.35

        self.variable_constellation_0 = variable_constellation_0 = digital.constellation_calcdist(([-1, 1]), ([0, 1]), 2, 1).base()

        self.threshold = threshold = 3
        self.samp_rate = samp_rate = 48000
        self.rrc_taps_0 = rrc_taps_0 = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(samp_per_sym), 0.35, 11*samp_per_sym*nfilts)
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), alpha, 11*sps*nfilts)
        self.nfilts_0 = nfilts_0 = 16
        self.equalizer_gain = equalizer_gain = 0.05
        self.af_gain = af_gain = 0

        ##################################################
        # Blocks
        ##################################################
        self._equalizer_gain_range = Range(0.0, 0.2, 0.01, 0.05, 200)
        self._equalizer_gain_win = RangeWidget(self._equalizer_gain_range, self.set_equalizer_gain, 'Equalizer: Gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._equalizer_gain_win)
        self._af_gain_tool_bar = Qt.QToolBar(self)
        self._af_gain_tool_bar.addWidget(Qt.QLabel('AF Gain'+": "))
        self._af_gain_line_edit = Qt.QLineEdit(str(self.af_gain))
        self._af_gain_tool_bar.addWidget(self._af_gain_line_edit)
        self._af_gain_line_edit.returnPressed.connect(
        	lambda: self.set_af_gain(eng_notation.str_to_num(str(self._af_gain_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._af_gain_tool_bar)
        self.satellites_taurus1_telemetry_parser_0 = satellites.taurus1_telemetry_parser()
        self.satellites_submit_0 = satellites.submit('https://db.satnogs.org/api/telemetry/', 44530, 'AD7NP', -122.2084, 47.6458, recstart)
        self.satellites_print_timestamp_0 = satellites.print_timestamp('%Y-%m-%d %H:%M:%S', True)
        self.satellites_lilacsat1_demux_0_0 = satellites.lilacsat1_demux("syncword")
        self.satellites_lilacsat1_demux_0 = satellites.lilacsat1_demux("syncword")
        self.satellites_kiss_to_pdu_1 = satellites.kiss_to_pdu(False)
        self.rms_agc_0 = rms_agc(
            alpha=1e-2,
            reference=0.5,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=6,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1000, #size
        	8000, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.125)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['A', 'B', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 1, 0, 1, 2)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 6000, 500, firdes.WIN_HAMMING, 6.76))
        self.lilacsat_vitfilt27_fb_0_0 = lilacsat.vitfilt27_fb()
        self.lilacsat_vitfilt27_fb_0 = lilacsat.vitfilt27_fb()
        self.lilacsat_sync_det_b_0_0 = lilacsat.sync_det_b(0x1ACFFC1D, 116, True, True)
        self.lilacsat_sync_det_b_0 = lilacsat.sync_det_b(0x1ACFFC1D, 116, True, True)
        self.lilacsat_lilacsat1_frame_depack_0 = lilacsat.lilacsat1_frame_depack()
        (self.lilacsat_lilacsat1_frame_depack_0).set_max_output_buffer(512)
        self.lilacsat_codec2_decode_bf_0 = lilacsat.codec2_decode_bf(0)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_fcf(1, (firdes.low_pass(1, samp_rate, 10000, 1000)), bfo, samp_rate)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, 0.05, (rrc_taps), nfilts, nfilts/2, 0.01, 1)
        self.digital_lms_dd_equalizer_cc_0_0 = digital.lms_dd_equalizer_cc(2, equalizer_gain, 2, variable_constellation_0)
        self.digital_fll_band_edge_cc_0 = digital.fll_band_edge_cc(sps, 0.350, 100, 0.01)
        self.digital_diff_decoder_bb_0_0 = digital.diff_decoder_bb(2)
        self.digital_diff_decoder_bb_0 = digital.diff_decoder_bb(2)
        self.digital_costas_loop_cc_0_0 = digital.costas_loop_cc(0.1, 2, False)
        self.digital_correlate_access_code_tag_bb_0_0_0_0_0 = digital.correlate_access_code_tag_bb("00011010110011111111110000011101", threshold, "syncword")
        self.digital_correlate_access_code_tag_bb_0_0_0_0 = digital.correlate_access_code_tag_bb("00011010110011111111110000011101", threshold, "syncword")
        self.digital_additive_scrambler_bb_0_0_0_0 = digital.additive_scrambler_bb(0xA9, 0xFF, 7, count=0, bits_per_byte=1, reset_tag_key="syncword")
        self.digital_additive_scrambler_bb_0_0_0 = digital.additive_scrambler_bb(0xA9, 0xFF, 7, count=0, bits_per_byte=1, reset_tag_key="syncword")
        self.ccsds_viterbi_0_0 = ccsds_viterbi()
        self.ccsds_viterbi_0 = ccsds_viterbi()
        self.blocks_unpacked_to_packed_xx_0_0_0_0_0 = blocks.unpacked_to_packed_bb(1, gr.GR_MSB_FIRST)
        self.blocks_unpacked_to_packed_xx_0_0_0_0 = blocks.unpacked_to_packed_bb(1, gr.GR_MSB_FIRST)
        self.blocks_unpack_k_bits_bb_0_0_0_1 = blocks.unpack_k_bits_bb(8)
        self.blocks_unpack_k_bits_bb_0_0_0 = blocks.unpack_k_bits_bb(8)
        self.blocks_udp_source_0 = blocks.udp_source(gr.sizeof_short*1, ip, port, 1472, False)
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_char*1, '127.0.0.1', 7000, 7, False)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, 8000,True)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 32767)
        self.blocks_pdu_to_tagged_stream_1_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_pdu_to_tagged_stream_1 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((10.0**(af_gain/20.0), ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((0, ))
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, 1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 1)
        self.blocks_complex_to_real_0_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.audio_source_0 = audio.source(8000, '', True)
        self.audio_sink_0 = audio.sink(48000, '', True)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.lilacsat_lilacsat1_frame_depack_0, 'out'), (self.blocks_message_debug_0, 'store'))
        self.msg_connect((self.lilacsat_sync_det_b_0, 'out'), (self.lilacsat_lilacsat1_frame_depack_0, 'in'))
        self.msg_connect((self.lilacsat_sync_det_b_0_0, 'out'), (self.lilacsat_lilacsat1_frame_depack_0, 'in'))
        self.msg_connect((self.satellites_kiss_to_pdu_1, 'out'), (self.satellites_print_timestamp_0, 'in'))
        self.msg_connect((self.satellites_kiss_to_pdu_1, 'out'), (self.satellites_submit_0, 'in'))
        self.msg_connect((self.satellites_lilacsat1_demux_0, 'kiss'), (self.blocks_pdu_to_tagged_stream_1, 'pdus'))
        self.msg_connect((self.satellites_lilacsat1_demux_0, 'codec2'), (self.blocks_pdu_to_tagged_stream_1_0, 'pdus'))
        self.msg_connect((self.satellites_lilacsat1_demux_0_0, 'kiss'), (self.blocks_pdu_to_tagged_stream_1, 'pdus'))
        self.msg_connect((self.satellites_lilacsat1_demux_0_0, 'codec2'), (self.blocks_pdu_to_tagged_stream_1_0, 'pdus'))
        self.msg_connect((self.satellites_print_timestamp_0, 'out'), (self.blocks_message_debug_0, 'print_pdu'))
        self.msg_connect((self.satellites_print_timestamp_0, 'out'), (self.satellites_taurus1_telemetry_parser_0, 'in'))
        self.connect((self.audio_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.ccsds_viterbi_0, 0))
        self.connect((self.blocks_complex_to_real_0_0, 0), (self.blocks_delay_0_0, 0))
        self.connect((self.blocks_complex_to_real_0_0, 0), (self.lilacsat_vitfilt27_fb_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.ccsds_viterbi_0_0, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.lilacsat_vitfilt27_fb_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_pdu_to_tagged_stream_1, 0), (self.blocks_unpacked_to_packed_xx_0_0_0_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_1_0, 0), (self.blocks_unpacked_to_packed_xx_0_0_0_0_0, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_udp_source_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0_0_0, 0), (self.lilacsat_sync_det_b_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0_0_0_1, 0), (self.lilacsat_sync_det_b_0_0, 0))
        self.connect((self.blocks_unpacked_to_packed_xx_0_0_0_0, 0), (self.satellites_kiss_to_pdu_1, 0))
        self.connect((self.blocks_unpacked_to_packed_xx_0_0_0_0_0, 0), (self.blocks_udp_sink_0, 0))
        self.connect((self.ccsds_viterbi_0, 0), (self.digital_diff_decoder_bb_0, 0))
        self.connect((self.ccsds_viterbi_0_0, 0), (self.digital_diff_decoder_bb_0_0, 0))
        self.connect((self.digital_additive_scrambler_bb_0_0_0, 0), (self.satellites_lilacsat1_demux_0, 0))
        self.connect((self.digital_additive_scrambler_bb_0_0_0_0, 0), (self.satellites_lilacsat1_demux_0_0, 0))
        self.connect((self.digital_correlate_access_code_tag_bb_0_0_0_0, 0), (self.digital_additive_scrambler_bb_0_0_0, 0))
        self.connect((self.digital_correlate_access_code_tag_bb_0_0_0_0_0, 0), (self.digital_additive_scrambler_bb_0_0_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0, 0), (self.blocks_complex_to_real_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0, 0), (self.digital_lms_dd_equalizer_cc_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0, 0), (self.digital_correlate_access_code_tag_bb_0_0_0_0, 0))
        self.connect((self.digital_diff_decoder_bb_0_0, 0), (self.digital_correlate_access_code_tag_bb_0_0_0_0_0, 0))
        self.connect((self.digital_fll_band_edge_cc_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.digital_lms_dd_equalizer_cc_0_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_costas_loop_cc_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.rms_agc_0, 0))
        self.connect((self.lilacsat_codec2_decode_bf_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.lilacsat_codec2_decode_bf_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.lilacsat_lilacsat1_frame_depack_0, 0), (self.lilacsat_codec2_decode_bf_0, 0))
        self.connect((self.lilacsat_vitfilt27_fb_0, 0), (self.blocks_unpack_k_bits_bb_0_0_0, 0))
        self.connect((self.lilacsat_vitfilt27_fb_0_0, 0), (self.blocks_unpack_k_bits_bb_0_0_0_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.rms_agc_0, 0), (self.digital_fll_band_edge_cc_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "taurus1")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_bfo(self):
        return self.bfo

    def set_bfo(self, bfo):
        self.bfo = bfo
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.bfo)

    def get_ip(self):
        return self.ip

    def set_ip(self, ip):
        self.ip = ip

    def get_port(self):
        return self.port

    def set_port(self, port):
        self.port = port

    def get_recstart(self):
        return self.recstart

    def set_recstart(self, recstart):
        self.recstart = recstart

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.alpha, 11*self.sps*self.nfilts))

    def get_samp_per_sym(self):
        return self.samp_per_sym

    def set_samp_per_sym(self, samp_per_sym):
        self.samp_per_sym = samp_per_sym
        self.set_rrc_taps_0(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.samp_per_sym), 0.35, 11*self.samp_per_sym*self.nfilts))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.alpha, 11*self.sps*self.nfilts))
        self.set_rrc_taps_0(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.samp_per_sym), 0.35, 11*self.samp_per_sym*self.nfilts))

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), self.alpha, 11*self.sps*self.nfilts))

    def get_variable_constellation_0(self):
        return self.variable_constellation_0

    def set_variable_constellation_0(self, variable_constellation_0):
        self.variable_constellation_0 = variable_constellation_0

    def get_threshold(self):
        return self.threshold

    def set_threshold(self, threshold):
        self.threshold = threshold
        self.digital_correlate_access_code_tag_bb_0_0_0_0_0.set_threshold(self.threshold)
        self.digital_correlate_access_code_tag_bb_0_0_0_0.set_threshold(self.threshold)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 6000, 500, firdes.WIN_HAMMING, 6.76))
        self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.low_pass(1, self.samp_rate, 10000, 1000)))

    def get_rrc_taps_0(self):
        return self.rrc_taps_0

    def set_rrc_taps_0(self, rrc_taps_0):
        self.rrc_taps_0 = rrc_taps_0

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rrc_taps))

    def get_nfilts_0(self):
        return self.nfilts_0

    def set_nfilts_0(self, nfilts_0):
        self.nfilts_0 = nfilts_0

    def get_equalizer_gain(self):
        return self.equalizer_gain

    def set_equalizer_gain(self, equalizer_gain):
        self.equalizer_gain = equalizer_gain
        self.digital_lms_dd_equalizer_cc_0_0.set_gain(self.equalizer_gain)

    def get_af_gain(self):
        return self.af_gain

    def set_af_gain(self, af_gain):
        self.af_gain = af_gain
        Qt.QMetaObject.invokeMethod(self._af_gain_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.af_gain)))
        self.blocks_multiply_const_vxx_1.set_k((10.0**(self.af_gain/20.0), ))


def argument_parser():
    description = 'Taurus-1 decoder'
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option, description=description)
    parser.add_option(
        "", "--bfo", dest="bfo", type="eng_float", default=eng_notation.num_to_str(12000),
        help="Set carrier frequency of the BPSK signal [default=%default]")
    parser.add_option(
        "", "--ip", dest="ip", type="string", default='127.0.0.1',
        help="Set UDP listen IP [default=%default]")
    parser.add_option(
        "", "--port", dest="port", type="intx", default=7355,
        help="Set UDP port [default=%default]")
    parser.add_option(
        "", "--recstart", dest="recstart", type="string", default='',
        help="Set start of recording, if processing a recording (format YYYY-MM-DD HH:MM:SS) [default=%default]")
    return parser


def main(top_block_cls=taurus1, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(bfo=options.bfo, ip=options.ip, port=options.port, recstart=options.recstart)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
