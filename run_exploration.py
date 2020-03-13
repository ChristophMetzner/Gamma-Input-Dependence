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
# A script to run a series of trials of the model used in the replication study.
#
# ------------------------------------------------------------------------------
import numpy as np
from simple_model_class import simpleModel



s = 2**13
time  = 500 # 2                # simulation stime (in ms)
dt =float(time)/float(s) #0.5
print('time step:', dt)


#Control condition
#tau_inh = 8.0
#g_ie = 0.015
#g_ii = 0.02
#b_inh = -0.01

# Tau Inh condition (representing prolonged IPSC decay times)
#tau_inh = 28.0
#g_ie = 0.015
#g_ii = 0.02
#b_inh = -0.01

# G Inh condition (representing reduced GABA availability)
#tau_inh = 8.0
#g_ie = 0.0075
#g_ii = 0.01
#b_inh = -0.01

# Tau and G Inh condition
tau_inh = 28.0
g_ie = 0.0075
g_ii = 0.01
b_inh = -0.01


drive_frequencies = [40.0, 30.0, 20.0]            # frequency of the periodic drive input
background_rate = 33.3            # average frequency of the Poissonian noise
A = 0.5                    # strength factor of the Poissonian noise



seeds = np.load('Seeds.npy')


g_de = 0.275  # default 0.3

filename = 'drive_0275_g_and_tau_inh'  # 'drive_05_g_and_tau_inh'    # filename, in case data is recorded
directory = 'Exploration/Input_Strength_0275/G_and_Tau_Inh/'  # directory where data will be stored









for f in drive_frequencies:
	print(f)
	for i in seeds:
		print(i)
		model = simpleModel(drive_frequency=f, background_rate=background_rate,
							A=A, dt=dt, tau_inh=tau_inh, g_de=g_de, g_ie=g_ie,
							g_ii=g_ii, b_inh=b_inh, seed=i, filename=filename + "drive_strength_"+str(g_de)+
							"_drive_frequency_"+str(f)+"_seed_" + str(i), directory=directory)
		meg, ex, inh = model.run(time, 1, 0, 0)





