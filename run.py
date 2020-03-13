# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# Copyright (c) 2017, Christoph Metzner
# Distributed under the (new) BSD License.
#
# Contributors: Christoph Metzner (c.metzner@herts.ac.uk)
# ------------------------------------------------------------------------------
# References:
#
# * Vierling-Claassen, D., Siekmeier, P., Stufflebeam, S., & Kopell, N. (2008). 
#   Modeling GABA alterations in schizophrenia: a link between impaired 
#   inhibition and altered gamma and beta range auditory entrainment. 
#   Journal of neurophysiology, 99(5), 2656-2671.
# ------------------------------------------------------------------------------
# A script to run a single trial of the model used in the replication study.
#
# ------------------------------------------------------------------------------

from simple_model_class import simpleModel
import matplotlib.pyplot as plt
import numpy as np

s=2**13
time = 500                # simulation time (in ms)
dt=float(time)/float(s)
print('time step:',dt)



tau_inh = 28.0
g_de = 0.3


drive_frequency = 40.0            # frequency of the periodic drive input
background_rate = 33.3            # average frequency of the Poissonian noise
A = 0.5                    # strength factor of the Poissonian noise
seed = 123456                # seed for the random generator


filename = 'test'            # filename, in case data is recorded
directory = ''                # directory where data will be stored

model = simpleModel(drive_frequency=drive_frequency, background_rate=background_rate, g_de = g_de,  A=A, tau_inh=tau_inh, seed=seed,
                    dt=dt, filename=filename, directory=directory)

meg, ex, inh = model.run(time, 0, 0, 0)

pxx, freqs = model.calculatePSD(meg, time)
model.plotPSD(freqs, pxx, 50.0, 0)

model.rasterPlot(ex, time, 0, 'Ex')
model.rasterPlot(inh, time, 0, 'Inh')
model.plotMEG(meg, time, 0)
plt.show()
