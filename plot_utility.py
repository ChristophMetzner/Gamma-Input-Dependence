# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2017, Christoph Metzner
# Distributed under the (new) BSD License.
#
# Contributor: Christoph Metzner (c.metzner@herts.ac.uk , christoph.metzner@gmail.com )
# -----------------------------------------------------------------------------
# Utility functions for plotting
#
# -----------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

from analysis import calcPowerSpectrum,getSingleSpikeTimes,getSpikeTimes

def plot_MEG_summary(time,meg_data,xlabel,ylabel,annotations,savefig,filename,fontsizes):
    f,((ax1,ax2),(ax3,ax4),(ax5,ax6)) = plt.subplots(3,2,sharex=True,sharey=True,figsize=[25.0,25.0])

    ax1.plot(time,meg_data[0],'k',linewidth=1.5)
    ax1.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax1.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax1.annotate(annotations[0],xy=(0,0.5),xytext=(-ax1.yaxis.labelpad-15,0),
    xycoords=ax1.yaxis.label,textcoords='offset points',size=fontsizes[1],ha='right',va='center')
    ax2.plot(time,meg_data[1],'k',linewidth=1.5)
    ax2.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax2.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax3.plot(time,meg_data[2],'k',linewidth=1.5)
    ax3.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax3.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax3.annotate(annotations[1],xy=(0,0.5),xytext=(-ax3.yaxis.labelpad-15,0),
    xycoords=ax3.yaxis.label,textcoords='offset points',size=fontsizes[1],ha='right',va='center')
    ax4.plot(time,meg_data[3],'k',linewidth=1.5)
    ax4.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax4.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax5.plot(time,meg_data[4],'k',linewidth=1.5)
    ax5.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax5.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax5.annotate(annotations[2],xy=(0,0.5),xytext=(-ax5.yaxis.labelpad-15,0),
    xycoords=ax5.yaxis.label,textcoords='offset points',size=fontsizes[1],ha='right',va='center')
    ax5.annotate(annotations[3],xy=(0.5,0),xytext=(0,-115),xycoords='axes fraction',
    textcoords='offset points',size=fontsizes[1],ha='center',va='bottom')
    ax6.plot(time,meg_data[5],'k',linewidth=1.5)
    ax6.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax6.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax6.annotate(annotations[4],xy=(0.5,0),xytext=(0,-115),xycoords='axes fraction',
    textcoords='offset points',size=35,ha='center',va='bottom')

    plt.setp(ax1.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax2.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax3.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax4.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax5.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax6.get_xticklabels(),visible=True,fontsize=fontsizes[2])

    plt.setp(ax2.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax4.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax6.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax1.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax3.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax5.get_yticklabels(),visible=True,fontsize=fontsizes[2])

    if savefig:
        #plt.savefig(filename+'.png',dpi=600)
        plt.savefig(filename+'.eps',dpi=600)



def plot_MEG_summary_overlay(time,meg_data,meg_data_s,xlabel,ylabel,annotations,savefig,filename,fontsizes):
    f,((ax1,ax2),(ax3,ax4),(ax5,ax6)) = plt.subplots(3,2,sharex=True,sharey=True,figsize=[25.0,25.0])

    ax1.plot(time,meg_data[0],'k',linewidth=1.5)
    ax1.plot(time,meg_data_s[0],'r',linewidth=1.5)
    ax1.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax1.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax1.annotate(annotations[0],xy=(0,0.5),xytext=(-ax1.yaxis.labelpad-15,0),
    xycoords=ax1.yaxis.label,textcoords='offset points',size=fontsizes[1],ha='right',va='center')
    ax2.plot(time,meg_data[1],'k',linewidth=1.5)
    ax2.plot(time,meg_data_s[1],'r',linewidth=1.5)
    ax2.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax2.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax3.plot(time,meg_data[2],'k',linewidth=1.5)
    ax3.plot(time,meg_data_s[2],'r',linewidth=1.5)
    ax3.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax3.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax3.annotate(annotations[1],xy=(0,0.5),xytext=(-ax3.yaxis.labelpad-15,0),
    xycoords=ax3.yaxis.label,textcoords='offset points',size=fontsizes[1],ha='right',va='center')
    ax4.plot(time,meg_data[3],'k',linewidth=1.5)
    ax4.plot(time,meg_data_s[3],'r',linewidth=1.5)
    ax4.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax4.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax5.plot(time,meg_data[4],'k',linewidth=1.5)
    ax5.plot(time,meg_data_s[4],'r',linewidth=1.5)
    ax5.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax5.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax5.annotate(annotations[2],xy=(0,0.5),xytext=(-ax5.yaxis.labelpad-15,0),
    xycoords=ax5.yaxis.label,textcoords='offset points',size=fontsizes[1],ha='right',va='center')
    ax5.annotate(annotations[3],xy=(0.5,0),xytext=(0,-115),xycoords='axes fraction',
    textcoords='offset points',size=fontsizes[1],ha='center',va='bottom')
    ax6.plot(time,meg_data[5],'k',linewidth=1.5)
    ax6.plot(time,meg_data_s[5],'r',linewidth=1.5)
    ax6.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax6.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax6.annotate(annotations[4],xy=(0.5,0),xytext=(0,-115),xycoords='axes fraction',
    textcoords='offset points',size=35,ha='center',va='bottom')

    plt.setp(ax1.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax2.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax3.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax4.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax5.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax6.get_xticklabels(),visible=True,fontsize=fontsizes[2])

    plt.setp(ax2.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax4.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax6.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax1.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax3.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax5.get_yticklabels(),visible=True,fontsize=fontsizes[2])

    if savefig:
        #plt.savefig(filename+'.png',dpi=600)
        plt.savefig(filename+'.eps',dpi=600)

def plot_MEG_summary_overlay_4in1(time,meg_data,meg_data_s,xlabel,ylabel,annotations,savefig,filename,fontsizes):
    f,((ax1,ax2,ax3,ax4),(ax5,ax6,ax7,ax8),(ax9,ax10,ax11,ax12)) = plt.subplots(3,4,sharex=True,sharey=True,figsize=[30.0,25.0])

    ax1.plot(time,meg_data[0],'k',linewidth=1.5)
    ax1.plot(time,meg_data_s[0],'r',linewidth=1.5)
    ax1.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax1.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax1.annotate(annotations[0],xy=(0,0.5),xytext=(-ax1.yaxis.labelpad-15,0),
    xycoords=ax1.yaxis.label,textcoords='offset points',size=fontsizes[1],ha='right',va='center')
    ax2.plot(time,meg_data[1],'k',linewidth=1.5)
    ax2.plot(time,meg_data_s[1],'r',linewidth=1.5)
    ax2.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax2.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax3.plot(time,meg_data[2],'k',linewidth=1.5)
    ax3.plot(time,meg_data_s[2],'r',linewidth=1.5)
    ax3.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax3.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax4.plot(time,meg_data[3],'k',linewidth=1.5)
    ax4.plot(time,meg_data_s[3],'r',linewidth=1.5)
    ax4.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax4.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax5.plot(time,meg_data[4],'k',linewidth=1.5)
    ax5.plot(time,meg_data_s[4],'r',linewidth=1.5)
    ax5.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax5.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax5.annotate(annotations[1],xy=(0,0.5),xytext=(-ax5.yaxis.labelpad-15,0),
    xycoords=ax5.yaxis.label,textcoords='offset points',size=fontsizes[1],ha='right',va='center')
    ax6.plot(time,meg_data[5],'k',linewidth=1.5)
    ax6.plot(time,meg_data_s[5],'r',linewidth=1.5)
    ax6.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax6.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax7.plot(time,meg_data[6],'k',linewidth=1.5)
    ax7.plot(time,meg_data_s[6],'r',linewidth=1.5)
    ax7.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax7.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax8.plot(time,meg_data[7],'k',linewidth=1.5)
    ax8.plot(time,meg_data_s[7],'r',linewidth=1.5)
    ax8.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax8.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax9.plot(time,meg_data[8],'k',linewidth=1.5)
    ax9.plot(time,meg_data_s[8],'r',linewidth=1.5)
    ax9.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax9.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax9.annotate(annotations[2],xy=(0,0.5),xytext=(-ax9.yaxis.labelpad-15,0),
    xycoords=ax9.yaxis.label,textcoords='offset points',size=fontsizes[1],ha='right',va='center')
    ax9.annotate(annotations[3],xy=(0.5,0),xytext=(0,-115),xycoords='axes fraction',
    textcoords='offset points',size=fontsizes[1],ha='center',va='bottom')
    ax10.plot(time,meg_data[9],'k',linewidth=1.5)
    ax10.plot(time,meg_data_s[9],'r',linewidth=1.5)
    ax10.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax10.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax10.annotate(annotations[4],xy=(0.5,0),xytext=(0,-115),xycoords='axes fraction',
    textcoords='offset points',size=fontsizes[1],ha='center',va='bottom')
    ax11.plot(time,meg_data[10],'k',linewidth=1.5)
    ax11.plot(time,meg_data_s[10],'r',linewidth=1.5)
    ax11.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax11.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax11.annotate(annotations[5],xy=(0.5,0),xytext=(0,-115),xycoords='axes fraction',
    textcoords='offset points',size=fontsizes[1],ha='center',va='bottom')
    ax12.plot(time,meg_data[11],'k',linewidth=1.5)
    ax12.plot(time,meg_data_s[11],'r',linewidth=1.5)
    ax12.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax12.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax12.annotate(annotations[6],xy=(0.5,0),xytext=(0,-115),xycoords='axes fraction',
    textcoords='offset points',size=fontsizes[1],ha='center',va='bottom')

    plt.setp(ax1.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax2.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax3.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax4.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax5.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax6.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax7.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax8.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax9.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax10.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax11.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax12.get_xticklabels(),visible=True,fontsize=fontsizes[2])

    plt.setp(ax2.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax4.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax6.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax1.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax3.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax5.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax8.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax10.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax12.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax7.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax9.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax11.get_yticklabels(),visible=True,fontsize=fontsizes[2])

    if savefig:
        #plt.savefig(filename+'.png',dpi=600)
        plt.savefig(filename+'.eps',dpi=600)




def plot_PSD_summary(freqs,psd_data,xlabel,ylabel,annotations,savefig,filename,fontsizes):
    f2,((ax1,ax2),(ax3,ax4),(ax5,ax6)) = plt.subplots(3,2,sharex=True,
    sharey=True,figsize=[25.0,25.0])

    ax1.plot(freqs,psd_data[0],'k',linewidth=2)
    ax1.axis(xmin=0, xmax=55)
    ax1.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax1.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax1.annotate(annotations[0],xy=(0,0.5),xytext=(-ax1.yaxis.labelpad-15,0),
    xycoords=ax1.yaxis.label,textcoords='offset points',size=35,ha='right',va='center')
    #xticks=ax1.xaxis.get_ticklabels()
    #xticks[2].set_weight('bold')
    #xticks[3].set_weight('bold')
    #xticks[4].set_weight('bold')

    ax2.plot(freqs,psd_data[1],'k',linewidth=2)
    ax2.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax2.set_ylabel(ylabel,fontsize=fontsizes[0])
    #xticks=ax2.xaxis.get_ticklabels()
    #xticks[2].set_weight('bold')
    #xticks[3].set_weight('bold')
    #xticks[4].set_weight('bold')

    ax3.plot(freqs,psd_data[2],'k',linewidth=2)
    ax3.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax3.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax3.annotate(annotations[1],xy=(0,0.5),xytext=(-ax3.yaxis.labelpad-15,0),
    xycoords=ax3.yaxis.label,textcoords='offset points',size=fontsizes[1],ha='right',va='center')
    #xticks=ax3.xaxis.get_ticklabels()
    #xticks[2].set_weight('bold')
    #xticks[3].set_weight('bold')
    #xticks[4].set_weight('bold')

    ax4.plot(freqs,psd_data[3],'k',linewidth=2)
    ax4.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax4.set_ylabel(ylabel,fontsize=fontsizes[0])
    #xticks=ax4.xaxis.get_ticklabels()
    #xticks[2].set_weight('bold')
    #xticks[3].set_weight('bold')
    #xticks[4].set_weight('bold')

    ax5.plot(freqs,psd_data[4],'k',linewidth=2)
    ax5.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax5.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax5.annotate(annotations[2],xy=(0,0.5),xytext=(-ax5.yaxis.labelpad-15,0),
    xycoords=ax5.yaxis.label,textcoords='offset points',size=fontsizes[1],ha='right',va='center')
    ax5.annotate(annotations[3],xy=(0.5,0),xytext=(0,-115),xycoords='axes fraction',
    textcoords='offset points',size=fontsizes[1],ha='center',va='bottom')
    xticks=ax5.xaxis.get_ticklabels()
    xticks[2].set_weight('bold')
    xticks[3].set_weight('bold')
    xticks[4].set_weight('bold')

    ax6.plot(freqs,psd_data[5],'k',linewidth=2)
    ax6.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax6.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax6.annotate(annotations[4],xy=(0.5,0),xytext=(0,-115),xycoords='axes fraction',
    textcoords='offset points',size=fontsizes[1],ha='center',va='bottom')
    xticks=ax6.xaxis.get_ticklabels()
    xticks[2].set_weight('bold')
    xticks[3].set_weight('bold')
    xticks[4].set_weight('bold')


    plt.setp(ax1.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax2.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax3.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax4.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax5.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax6.get_xticklabels(),visible=True,fontsize=fontsizes[2])

    plt.setp(ax2.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax4.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax6.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax1.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax3.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax5.get_yticklabels(),visible=True,fontsize=fontsizes[2])

    if savefig:
        #plt.savefig(filename+'.png',dpi=600)
        plt.savefig(filename+'.eps',dpi=600)


def plot_PSD_summary_overlay(freqs,psd_data,psd_data_s,xlabel,ylabel,annotations,savefig,filename,fontsizes):
    f2,((ax1,ax2),(ax3,ax4),(ax5,ax6)) = plt.subplots(3,2,sharex=True,
    sharey=True,figsize=[25.0,25.0])

    ax1.plot(freqs,psd_data[0],'k',linewidth=2)
    ax1.plot(freqs,psd_data_s[0],'r',linewidth=2)
    ax1.axis(xmin=0, xmax=55)
    ax1.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax1.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax1.annotate(annotations[0],xy=(0,0.5),xytext=(-ax1.yaxis.labelpad-15,0),
    xycoords=ax1.yaxis.label,textcoords='offset points',size=35,ha='right',va='center')
    xticks=ax1.xaxis.get_ticklabels()
    xticks[2].set_weight('bold')
    xticks[3].set_weight('bold')
    xticks[4].set_weight('bold')

    ax2.plot(freqs,psd_data[1],'k',linewidth=2)
    ax2.plot(freqs,psd_data_s[1],'r',linewidth=2)
    ax2.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax2.set_ylabel(ylabel,fontsize=fontsizes[0])
    xticks=ax2.xaxis.get_ticklabels()
    xticks[2].set_weight('bold')
    xticks[3].set_weight('bold')
    xticks[4].set_weight('bold')

    ax3.plot(freqs,psd_data[2],'k',linewidth=2)
    ax3.plot(freqs,psd_data_s[2],'r',linewidth=2)
    ax3.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax3.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax3.annotate(annotations[1],xy=(0,0.5),xytext=(-ax3.yaxis.labelpad-15,0),
    xycoords=ax3.yaxis.label,textcoords='offset points',size=fontsizes[1],ha='right',va='center')
    xticks=ax3.xaxis.get_ticklabels()
    xticks[2].set_weight('bold')
    xticks[3].set_weight('bold')
    xticks[4].set_weight('bold')

    ax4.plot(freqs,psd_data[3],'k',linewidth=2)
    ax4.plot(freqs,psd_data_s[3],'r',linewidth=2)
    ax4.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax4.set_ylabel(ylabel,fontsize=fontsizes[0])
    xticks=ax4.xaxis.get_ticklabels()
    xticks[2].set_weight('bold')
    xticks[3].set_weight('bold')
    xticks[4].set_weight('bold')

    ax5.plot(freqs,psd_data[4],'k',linewidth=2)
    ax5.plot(freqs,psd_data_s[4],'r',linewidth=2)
    ax5.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax5.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax5.annotate(annotations[2],xy=(0,0.5),xytext=(-ax5.yaxis.labelpad-15,0),
    xycoords=ax5.yaxis.label,textcoords='offset points',size=fontsizes[1],ha='right',va='center')
    ax5.annotate(annotations[3],xy=(0.5,0),xytext=(0,-115),xycoords='axes fraction',
    textcoords='offset points',size=fontsizes[1],ha='center',va='bottom')
    xticks=ax5.xaxis.get_ticklabels()
    xticks[2].set_weight('bold')
    xticks[3].set_weight('bold')
    xticks[4].set_weight('bold')

    ax6.plot(freqs,psd_data[5],'k',linewidth=2)
    ax6.plot(freqs,psd_data_s[5],'r',linewidth=2)
    ax6.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax6.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax6.annotate(annotations[4],xy=(0.5,0),xytext=(0,-115),xycoords='axes fraction',
    textcoords='offset points',size=fontsizes[1],ha='center',va='bottom')
    xticks=ax6.xaxis.get_ticklabels()
    xticks[2].set_weight('bold')
    xticks[3].set_weight('bold')
    xticks[4].set_weight('bold')


    plt.setp(ax1.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax2.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax3.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax4.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax5.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax6.get_xticklabels(),visible=True,fontsize=fontsizes[2])

    plt.setp(ax2.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax4.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax6.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax1.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax3.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax5.get_yticklabels(),visible=True,fontsize=fontsizes[2])

    if savefig:
        #plt.savefig(filename+'.png',dpi=600)
        plt.savefig(filename+'.eps',dpi=600)



def plot_PSD_summary_overlay_4in1(freqs,psd_data,psd_data_s,xlabel,ylabel,annotations,savefig,filename,fontsizes):
    f2,((ax1,ax2,ax3,ax4),(ax5,ax6,ax7,ax8),(ax9,ax10,ax11,ax12)) = plt.subplots(3,4,sharex=True,
    sharey=True,figsize=[40.0,25.0])

    ax1.plot(freqs,psd_data[0],'k',linewidth=2)
    ax1.plot(freqs,psd_data_s[0],'r',linewidth=2)
    ax1.axis(xmin=0, xmax=55)
    ax1.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax1.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax1.annotate(annotations[0],xy=(0,0.5),xytext=(-ax1.yaxis.labelpad-15,0),
    xycoords=ax1.yaxis.label,textcoords='offset points',size=35,ha='right',va='center')

    ax2.plot(freqs,psd_data[1],'k',linewidth=2)
    ax2.plot(freqs,psd_data_s[1],'r',linewidth=2)
    ax2.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax2.set_ylabel(ylabel,fontsize=fontsizes[0])

    ax3.plot(freqs,psd_data[2],'k',linewidth=2)
    ax3.plot(freqs,psd_data_s[2],'r',linewidth=2)
    ax3.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax3.set_ylabel(ylabel,fontsize=fontsizes[0])

    ax4.plot(freqs,psd_data[3],'k',linewidth=2)
    ax4.plot(freqs,psd_data_s[3],'r',linewidth=2)
    ax4.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax4.set_ylabel(ylabel,fontsize=fontsizes[0])

    ax5.plot(freqs,psd_data[4],'k',linewidth=2)
    ax5.plot(freqs,psd_data_s[4],'r',linewidth=2)
    ax5.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax5.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax5.annotate(annotations[1],xy=(0,0.5),xytext=(-ax5.yaxis.labelpad-15,0),
    xycoords=ax5.yaxis.label,textcoords='offset points',size=fontsizes[1],ha='right',va='center')

    ax6.plot(freqs,psd_data[5],'k',linewidth=2)
    ax6.plot(freqs,psd_data_s[5],'r',linewidth=2)
    ax6.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax6.set_ylabel(ylabel,fontsize=fontsizes[0])

    ax7.plot(freqs,psd_data[6],'k',linewidth=2)
    ax7.plot(freqs,psd_data_s[6],'r',linewidth=2)
    ax7.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax7.set_ylabel(ylabel,fontsize=fontsizes[0])

    ax8.plot(freqs,psd_data[7],'k',linewidth=2)
    ax8.plot(freqs,psd_data_s[7],'r',linewidth=2)
    ax8.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax8.set_ylabel(ylabel,fontsize=fontsizes[0])

    ax9.plot(freqs,psd_data[8],'k',linewidth=2)
    ax9.plot(freqs,psd_data_s[8],'r',linewidth=2)
    ax9.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax9.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax9.annotate(annotations[2],xy=(0,0.5),xytext=(-ax9.yaxis.labelpad-15,0),
    xycoords=ax9.yaxis.label,textcoords='offset points',size=fontsizes[1],ha='right',va='center')
    ax9.annotate(annotations[3],xy=(0.5,0),xytext=(0,-115),xycoords='axes fraction',
    textcoords='offset points',size=fontsizes[1],ha='center',va='bottom')
    xticks=ax9.xaxis.get_ticklabels()
    xticks[2].set_weight('bold')
    xticks[3].set_weight('bold')
    xticks[4].set_weight('bold')

    ax10.plot(freqs,psd_data[9],'k',linewidth=2)
    ax10.plot(freqs,psd_data_s[9],'r',linewidth=2)
    ax10.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax10.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax10.annotate(annotations[4],xy=(0.5,0),xytext=(0,-115),xycoords='axes fraction',
    textcoords='offset points',size=fontsizes[1],ha='center',va='bottom')
    xticks=ax10.xaxis.get_ticklabels()
    xticks[2].set_weight('bold')
    xticks[3].set_weight('bold')
    xticks[4].set_weight('bold')

    ax11.plot(freqs,psd_data[10],'k',linewidth=2)
    ax11.plot(freqs,psd_data_s[10],'r',linewidth=2)
    ax11.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax11.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax11.annotate(annotations[5],xy=(0.5,0),xytext=(0,-115),xycoords='axes fraction',
    textcoords='offset points',size=fontsizes[1],ha='center',va='bottom')
    xticks=ax11.xaxis.get_ticklabels()
    xticks[2].set_weight('bold')
    xticks[3].set_weight('bold')
    xticks[4].set_weight('bold')

    ax12.plot(freqs,psd_data[11],'k',linewidth=2)
    ax12.plot(freqs,psd_data_s[11],'r',linewidth=2)
    ax12.set_xlabel(xlabel,fontsize=fontsizes[0])
    ax12.set_ylabel(ylabel,fontsize=fontsizes[0])
    ax12.annotate(annotations[6],xy=(0.5,0),xytext=(0,-115),xycoords='axes fraction',
    textcoords='offset points',size=fontsizes[1],ha='center',va='bottom')
    xticks=ax12.xaxis.get_ticklabels()
    xticks[2].set_weight('bold')
    xticks[3].set_weight('bold')
    xticks[4].set_weight('bold')


    plt.setp(ax1.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax2.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax3.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax4.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax5.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax6.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax7.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax8.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax9.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax10.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax11.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax12.get_xticklabels(),visible=True,fontsize=fontsizes[2])

    plt.setp(ax2.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax4.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax6.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax1.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax3.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax5.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax8.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax10.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax12.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax7.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax9.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax11.get_yticklabels(),visible=True,fontsize=fontsizes[2])

    if savefig:
        #plt.savefig(filename+'.png',dpi=600)
        plt.savefig(filename+'.eps',dpi=600)


def plot_single_trial(sim_time,spike_times,freqs,data_psd,time,data_meg,xlabels,ylabels,annotations,savefig,filename,fontsizes):
    plt.figure(3,figsize=[20.0,15.0])
    ax1 = plt.subplot2grid((2,2),(0,0), rowspan=2)
    ax2 = plt.subplot2grid((2,2),(0,1))
    ax3 = plt.subplot2grid((2,2),(1,1))

    # Raster plot
    for i,times in enumerate(spike_times[0]):
        y = [i+10]*len(times)
        ax2.plot(times,y,linestyle='None',color='k',marker='|',markersize=10)


    for i,times in enumerate(spike_times[1]):
        y = [i]*len(times)
        ax2.plot(times,y,linestyle='None',color='b',marker='|',markersize=10)
        ax2.axis([0,sim_time,-0.5,30])
    ax2.set_xlabel(xlabels[0],fontsize=fontsizes[0])
    ax2.set_yticks([])
    ax2.annotate(annotations[0],xy=(0,0.5),xytext=(-ax2.yaxis.labelpad,-75),
    xycoords=ax2.yaxis.label,textcoords='offset points',size=fontsizes[1],ha='right',va='top')
    ax2.annotate(annotations[1],xy=(0,0.5),xytext=(-ax2.yaxis.labelpad,75),
    xycoords=ax2.yaxis.label,textcoords='offset points',size=fontsizes[1],ha='right',va='bottom')
    plt.setp(ax2.get_xticklabels(),fontsize=fontsizes[2])

    # MEG plot
    ax3.plot(time,data_meg,'k',linewidth=1.5)
    ax3.set_xlabel(xlabels[0],fontsize=fontsizes[0])
    ax3.set_ylabel(ylabels[0],fontsize=fontsizes[0])
    plt.setp(ax3.get_xticklabels(),fontsize=fontsizes[2])
    plt.setp(ax3.get_yticklabels(),fontsize=fontsizes[2])

    # Power spectrum plot
    ax1.plot(freqs*1000,data_psd,'k',linewidth=2)
    ax1.axis(xmin=0, xmax=55)
    ax1.set_xlabel(xlabels[1],fontsize=fontsizes[0])
    ax1.set_ylabel(ylabels[1],fontsize=fontsizes[0])
    plt.setp(ax1.get_xticklabels(),fontsize=fontsizes[2])
    plt.setp(ax1.get_yticklabels(),fontsize=fontsizes[2])

    if savefig:
        #plt.savefig(filename+'.png',dpi=600)
        plt.savefig(filename+'.eps',dpi=600)


def plot_MEG_PSD_combination(time,freqs,meg_data,meg_data_s,psd_data,psd_data_s,xlabel1,ylabel1,xlabel2,ylabel2,annotations,savefig,filename,fontsizes):
    f,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,sharex=False,sharey=False,figsize=[30.0,25.0])

    ax1.plot(time,meg_data[0],'k',linewidth=2.5)
    ax1.plot(time,meg_data_s[0],'r',linewidth=2.5)
    ax1.axis(ymin=0, ymax=17.5)
    ax1.set_xlabel(xlabel1,fontsize=fontsizes[0])
    ax1.set_ylabel(ylabel1,fontsize=fontsizes[0])
    ax1.annotate(annotations[0],xy=(0,0.5),xytext=(-ax1.yaxis.labelpad-15,0),
    xycoords=ax1.yaxis.label,textcoords='offset points',size=fontsizes[1],ha='right',va='center')
    ax2.plot(freqs,psd_data[0],'k',linewidth=4)
    ax2.plot(freqs,psd_data_s[0],'r',linewidth=4)
    ax2.axis(xmin=0, xmax=55)
    ax2.set_xlabel(xlabel2,fontsize=fontsizes[0])
    ax2.set_ylabel(ylabel2,fontsize=fontsizes[0])
    xticks=ax2.xaxis.get_ticklabels()
    xticks[2].set_weight('bold')
    xticks[3].set_weight('bold')
    xticks[4].set_weight('bold')
    ax3.plot(time,meg_data[1],'k',linewidth=2.5)
    ax3.plot(time,meg_data_s[1],'r',linewidth=2.5)
    ax3.axis(ymin=0, ymax=17.5)
    ax3.set_xlabel(xlabel1,fontsize=fontsizes[0])
    ax3.set_ylabel(ylabel1,fontsize=fontsizes[0])
    ax3.annotate(annotations[1],xy=(0,0.5),xytext=(-ax3.yaxis.labelpad-15,0),
    xycoords=ax3.yaxis.label,textcoords='offset points',size=fontsizes[1],ha='right',va='center')
    ax4.plot(freqs,psd_data[1],'k',linewidth=4)
    ax4.plot(freqs,psd_data_s[1],'r',linewidth=4)
    ax4.axis(xmin=0, xmax=55)
    ax4.set_xlabel(xlabel2,fontsize=fontsizes[0])
    ax4.set_ylabel(ylabel2,fontsize=fontsizes[0])
    xticks=ax4.xaxis.get_ticklabels()
    xticks[2].set_weight('bold')
    xticks[3].set_weight('bold')
    xticks[4].set_weight('bold')

    plt.setp(ax1.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax2.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax3.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax4.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    
    plt.setp(ax1.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax2.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax3.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax4.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    

    if savefig:
        #plt.savefig(filename+'.png',dpi=600)
        plt.savefig(filename+'.eps',dpi=600)

def plot_barplot(x,ctrl,schiz,xlabel,ylabel,annotations,colours,savefig,filename,fontsizes,tick_label):
    plt.figure(5,figsize=[30.0,7.5])
    ax1 = plt.subplot2grid((1,5),(0,0))
    ax2 = plt.subplot2grid((1,5),(0,1))
    ax3 = plt.subplot2grid((1,5),(0,2))
    ax4 = plt.subplot2grid((1,5),(0,3))
    ax5 = plt.subplot2grid((1,5),(0,4))

    ax1.bar(x,[ctrl[0][0],schiz[0][0],ctrl[0][1],schiz[0][1]],width=0.5,color=colours,tick_label=tick_label)
    ax1.set_xlabel(xlabel[0],fontsize=fontsizes[0])
    ax1.set_ylabel(ylabel,fontsize=fontsizes[0])    
    ax2.bar(x,[ctrl[1][0],schiz[1][0],ctrl[1][1],schiz[1][1]],width=0.5,color=colours,tick_label=tick_label)  
    ax2.set_xlabel(xlabel[1],fontsize=fontsizes[0])
    ax3.bar(x,[ctrl[2][0],schiz[2][0],ctrl[2][1],schiz[2][1]],width=0.5,color=colours,tick_label=tick_label)
    ax3.set_xlabel(xlabel[2],fontsize=fontsizes[0])
    ax4.bar(x,[ctrl[3][0],schiz[3][0],ctrl[3][1],schiz[3][1]],width=0.5,color=colours,tick_label=tick_label)
    ax4.set_xlabel(xlabel[3],fontsize=fontsizes[0])
    ax5.bar(x,[ctrl[4][0],schiz[4][0],ctrl[4][1],schiz[4][1]],width=0.5,color=colours,tick_label=tick_label)
    ax5.set_xlabel(xlabel[4],fontsize=fontsizes[0])

    plt.setp(ax1.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax2.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax3.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax4.get_xticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax5.get_xticklabels(),visible=True,fontsize=fontsizes[2])    

    plt.setp(ax1.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax2.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax3.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax4.get_yticklabels(),visible=True,fontsize=fontsizes[2])
    plt.setp(ax5.get_yticklabels(),visible=True,fontsize=fontsizes[2])   
    

    if savefig:
        #plt.savefig(filename+'.png',dpi=600)
        plt.savefig(filename+'.eps',dpi=600)


