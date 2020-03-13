# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Copyright (c) 2020, Christoph Metzner
# Distributed under the (new) BSD License.
#
# Contributors: Christoph Metzner (cmetzner@ni.tu-berlin.de)
# ------------------------------------------------------------------------------
# References:
#
# * Vierling-Claassen, D., Siekmeier, P., Stufflebeam, S., & Kopell, N. (2008).
#   Modeling GABA alterations in schizophrenia: a link between impaired
#   inhibition and altered gamma and beta range auditory entrainment.
#   Journal of neurophysiology, 99(5), 2656-2671.
# ------------------------------------------------------------------------------
# A script to caclulate the average MEG signal and, subsequently, its PSD from
# a series of trials of the model used in the replication study.
# ----------------------------------------------------------------------------


import numpy as np
import matplotlib.mlab as mlab


def calc_power_spectrum(meg, dt, sim_time):
    # fourier sample rate
    fs = 1. / dt

    tn = np.linspace(0, sim_time, int(sim_time / dt) + 1)

    npts = len(meg)
    startpt = int(0.2 * fs)

    if (npts - startpt) % 2 != 0:
        startpt = startpt + 1

    meg = meg[startpt:]
    tn = tn[startpt:]
    nfft = len(tn)

    pxx, freqs = mlab.psd(meg, NFFT=nfft, Fs=fs, noverlap=0, window=mlab.window_none)
    pxx[0] = 0.0

    return pxx, freqs


s = 2**13
time = 500  # simulation time (in ms)
dt = float(time)/float(s)

seeds = np.load('Seeds.npy')

g_de = 0.275
filename = 'drive_0275_g_and_tau_inh'  # 'drive_0225_control'
directory = 'Exploration/Input_Strength_0275/G_and_Tau_Inh/'  # directory where data is stored
frequencies = [40.0, 30.0, 20.0]

megs = np.zeros((len(seeds), s))

for f in frequencies:
    print(f)
    for i, ss in enumerate(seeds):
        print(i)
        filename2 = filename + "drive_strength_" + str(g_de) +"_drive_frequency_" + str(f) + "_seed_" + \
                    str(ss)+'-MEG.npy'
        megs[i, :] = np.load(directory+filename2)

    avg_meg = np.mean(megs, axis=0)
    avg_psd, freqs = calc_power_spectrum(avg_meg, dt, time)

    np.save('Exploration/Input_Strength_0275/'+filename+'_drive_frequency_' + str(f) +'-MEG.npy', avg_meg)
    np.save('Exploration/Input_Strength_0275/'+filename+'_drive_frequency_' + str(f) +'-PSD.npy', avg_psd)
    np.save('Exploration/freqs.npy', freqs)