####################################################################
# Implements an extension of the simple model from Vierling-Claassen et al., 
# J Neurophysiol, 2008
# 
# This extension has two populations of inhibitory neurons: FS PV+ basket cells
# and LTS SOM+ cells
#
# @author: Christoph Metzner, 17/01/2019
####################################################################


import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab





class simpleModelFsLts(object):
    
    '''


    Attributes:
        n_ex		: number of excitatory cells
        n_fs		: number of FS cells
        n_som       : number of SOM cells

        eta		    :
        tau_R		: 'synaptic rise time'
        tau_ex		: exc. 'synaptic decay time'
        tau_fs	    : inh. 'synaptic decay time' for FS cells (population B)
        tau_som	    : inh. 'synaptic decay time' for SOM cells (population C)

        g_ee		: E-E weight
        g_eb		: E-B weight
        g_ec		: E-C weight
        g_be		: B-E weight
        g_ce		: C-E weight
        g_bb		: B-B weight
        g_cc		: C-C weight
        g_bc		: B-C weight
        g_cb        : C-B weight
        g_de		: Drive-E weight
        g_db		: Drive-B weight
        g_dc		: Drive-C weight

        dt		: time step

        b_ex		: applied current to excitatory cells
        b_fs		: applied current to FS cells
        b_som		: applied current to SOM cells
        drive_frequency : drive frequency


        background_rate : rate of the background noise spike trains
        A		: scaling factor for the background noise strength

        seed		: seed for the random generator
    '''

    def __init__(self,n_ex=20,n_fs=10,n_som=10,eta=5.0,tau_R=0.1,tau_ex=2.0,tau_fs=8.0,tau_som=50.0,g_ee=0.015,
                 g_eb=0.025, g_ec=0.025,g_be=0.015,g_ce=0.015,g_bb=0.02,g_cb=0.02,g_bc=0.02,g_de=0.3,g_db=0.08,
                 dt=0.05,b_ex=-0.01,b_fs=-0.01,b_som=-0.05,drive_frequency=0.0,background_rate=33.3,
                 A=0.65,seed=12345,filename='default',directory='/'):
        self.n_ex = n_ex
        self.n_fs = n_fs
        self.n_som = n_som
        self.eta = eta
        self.tau_R = tau_R
        self.tau_ex = tau_ex
        self.tau_fs = tau_fs
        self.tau_som = tau_som
        self.g_ee = g_ee
        self.g_eb = g_eb
        self.g_ec = g_ec
        self.g_be = g_be
        self.g_ce = g_ce
        self.g_bb = g_bb
        self.g_cb = g_cb
        self.g_bc = g_bc
        self.g_de = g_de
        self.g_db = g_db
        self.dt = dt
        self.b_ex = b_ex
        self.b_fs = b_fs
        self.b_som = b_som
        self.drive_frequency = drive_frequency
        self.background_rate = background_rate
        self.A = A
        self.seed = seed
        self.filename = filename
        self.directory = directory
    
    def run(self,time=100.0,saveMEG=0,saveEX=0,saveFS=0,saveSOM=0):
        '''
        Runs the model and returns (and stores) the results
               
        Parameters:
        time : the length of the simulation (in ms)
        saveMEG: flag that signalises whether the MEG signal should be stored
        saveEX: flag that signalises whether the exc. population activity should be stored
        saveFS: flag that signalises whether the FS cell population activity should be stored
        saveSOM: flag that signalises whether the SOM cell population activity should be stored
        '''
            
        time_points = np.linspace(0,time,int(time/self.dt)+1) # number of time steps (in ms) 
    
        # Initialisations
        drive_cell  =   np.zeros((len(time_points),))	# the pacemaking drive cell
    
    
        theta_ex = np.zeros((self.n_ex,len(time_points)))		# exc. neurons
        theta_fs = np.zeros((self.n_fs,len(time_points)))		# FS cells
        theta_som = np.zeros((self.n_som,len(time_points)))		# SOM cells
    
        s_ee = np.zeros((self.n_ex,self.n_ex,len(time_points))) 	# E-E snyaptic gating variables
        s_eb = np.zeros((self.n_ex,self.n_fs,len(time_points)))	# E-B snyaptic gating variables
        s_ec = np.zeros((self.n_ex,self.n_som,len(time_points)))	# E-C snyaptic gating variables
        s_be = np.zeros((self.n_fs,self.n_ex,len(time_points)))	# B-E snyaptic gating variables
        s_ce = np.zeros((self.n_som,self.n_ex,len(time_points)))	# C-E snyaptic gating variables
        s_bb = np.zeros((self.n_fs,self.n_fs,len(time_points)))	# B-B snyaptic gating variables
        s_cb = np.zeros((self.n_som,self.n_fs,len(time_points)))	# C-B snyaptic gating variables
        s_bc = np.zeros((self.n_fs,self.n_som,len(time_points)))	# B-C snyaptic gating variables
        s_de = np.zeros((self.n_ex,len(time_points)))			# Drive-E snyaptic gating variables
        s_db = np.zeros((self.n_fs,len(time_points)))			# Drive-B snyaptic gating variables
        #s_dc = np.zeros((self.n_som,len(time_points)))			# Drive-C snyaptic gating variables; no drive for SOM cells
        
        N_ex = np.zeros((self.n_ex,len(time_points)))			# Noise to exc. cells
        N_fs = np.zeros((self.n_fs,len(time_points)))			# Noise to fs cells
        N_som = np.zeros((self.n_som,len(time_points)))			# Noise to som cells
        
        S_ex = np.zeros((self.n_ex,len(time_points)))			# Synaptic inputs for exc. cells
        S_fs = np.zeros((self.n_fs,len(time_points)))		# Synaptic inputs for FS cells
        S_som = np.zeros((self.n_som,len(time_points)))	# Synaptic inputs for som cells
        
        meg = np.zeros((self.n_ex,len(time_points)))			# MEG component for each cell (only E-E EPSCs)
        
        # applied currents
        B_ex    = self.b_ex * np.ones((self.n_ex,))				# applied current for exc. cells
        B_fs   = self.b_fs * np.ones((self.n_fs,))			# applied current for FS cells
        B_som   = self.b_som * np.ones((self.n_som,))			# applied current for SOM cells
        
        # Frequency = 1000/period(in ms) and b= pi**2 / period**2 (because period = pi* sqrt(1/b); see Boergers and Kopell 2003) 
        period  = 1000.0/self.drive_frequency
        b_drive = np.pi**2/period**2			# applied current for drive cell 
        
        # Seed the random generator
        random.seed( self.seed )
        
        # Noise spike trains
        ST_ex = [None]*self.n_ex
        ST_fs = [None]*self.n_fs
        ST_som = [None]*self.n_som
        
        rate_parameter = 1000*(1.0/self.background_rate)
        rate_parameter = 1.0/rate_parameter
        for i in range(self.n_ex):
            template_spike_array = []
            # Produce Poissonian spike train
            total_time = 0.0
            while total_time < time:
                next_time = random.expovariate(rate_parameter)
                total_time = total_time + next_time 
                if total_time < time:
                    template_spike_array.append(total_time)
                    
            ST_ex[i] = template_spike_array
                
        
        for i in range(self.n_fs):
            template_spike_array = []
            # Produce Poissonian spike train
            total_time = 0.0
            while total_time < time:
                next_time = random.expovariate(rate_parameter)
                total_time = total_time + next_time 
                if total_time < time:
                    template_spike_array.append(total_time)
                    
            ST_fs[i] = template_spike_array

        for i in range(self.n_som):
            template_spike_array = []
            # Produce Poissonian spike train
            total_time = 0.0
            while total_time < time:
                next_time = random.expovariate(rate_parameter)
                total_time = total_time + next_time 
                if total_time < time:
                    template_spike_array.append(total_time)
                    
            ST_som[i] = template_spike_array
         

               
        a = np.zeros((self.n_ex,1))    
        b = np.zeros((self.n_fs,1))
        c = np.zeros((self.n_som,1))
        # Simulation
        for t in range(1,len(time_points)):
            # calculate noise (not done in a very efficient way!)
            for i in range(self.n_ex):
                for tn in ST_ex[i]:
                    N_ex[i,t] = N_ex[i,t] + self._noise(t,tn) 
        
            # calculate noise (not done in a very efficient way!)
            for i in range(self.n_fs):
                for tn in ST_fs[i]:
                    N_fs[i,t] = N_fs[i,t] + self._noise(t,tn)
            
            # calculate noise (not done in a very efficient way!)
            for i in range(self.n_som):
                for tn in ST_som[i]:
                    N_som[i,t] = N_som[i,t] + self._noise(t,tn)
                    
            # evolve gating variables
            s_ee[:,:,t] 	= s_ee[:,:,t-1] + self.dt*(-1.0*(s_ee[:,:,t-1]/self.tau_ex) + np.exp(-1.0*self.eta*(1+np.cos(theta_ex[:,t-1])))*((1.0-s_ee[:,:,t-1])/self.tau_R))
            # this seems awfully complicated            
            for k in range(self.n_ex):
                a[k,0]=theta_ex[k,t-1]
            s_eb[:,:,t] 	= s_eb[:,:,t-1] + self.dt*(-1.0*(s_eb[:,:,t-1]/self.tau_ex) + np.exp(-1.0*self.eta*(1+np.cos(a)))*((1.0-s_eb[:,:,t-1])/self.tau_R))
            s_ec[:,:,t] 	= s_ec[:,:,t-1] + self.dt*(-1.0*(s_ec[:,:,t-1]/self.tau_ex) + np.exp(-1.0*self.eta*(1+np.cos(a)))*((1.0-s_ec[:,:,t-1])/self.tau_R))
            # this seems awfully complicated            
            for l in range(self.n_fs):
                b[l,0]=theta_fs[l,t-1]
            s_be[:,:,t] 	= s_be[:,:,t-1] + self.dt*(-1.0*(s_be[:,:,t-1]/self.tau_fs) + np.exp(-1.0*self.eta*(1+np.cos(b)))*((1.0-s_be[:,:,t-1])/self.tau_R))
            s_bb[:,:,t] 	= s_bb[:,:,t-1] + self.dt*(-1.0*(s_bb[:,:,t-1]/self.tau_fs) + np.exp(-1.0*self.eta*(1+np.cos(theta_fs[:,t-1])))*((1.0-s_bb[:,:,t-1])/self.tau_R))
            s_bc[:,:,t] 	= s_bc[:,:,t-1] + self.dt*(-1.0*(s_bc[:,:,t-1]/self.tau_fs) + np.exp(-1.0*self.eta*(1+np.cos(b)))*((1.0-s_bc[:,:,t-1])/self.tau_R))
            for m in range(self.n_som):
                c[m,0]=theta_som[m,t-1]
            s_ce[:,:,t] 	= s_ce[:,:,t-1] + self.dt*(-1.0*(s_ce[:,:,t-1]/self.tau_som) + np.exp(-1.0*self.eta*(1+np.cos(c)))*((1.0-s_ce[:,:,t-1])/self.tau_R))
            s_cb[:,:,t] 	= s_cb[:,:,t-1] + self.dt*(-1.0*(s_cb[:,:,t-1]/self.tau_som) + np.exp(-1.0*self.eta*(1+np.cos(c)))*((1.0-s_cb[:,:,t-1])/self.tau_R))


            s_de[:,t]    	= s_de[:,t-1]   + self.dt*(-1.0*(s_de[:,t-1]/self.tau_ex) + np.exp(-1.0*self.eta*(1+np.cos(drive_cell[t-1])))*((1.0-s_de[:,t-1])/self.tau_R))
            s_db[:,t]   	= s_db[:,t-1]   + self.dt*(-1.0*(s_db[:,t-1]/self.tau_ex) + np.exp(-1.0*self.eta*(1+np.cos(drive_cell[t-1])))*((1.0-s_db[:,t-1])/self.tau_R))
            #s_dc[:,t]   	= s_dc[:,t-1]   + self.dt*(-1.0*(s_dc[:,t-1]/self.tau_ex) + np.exp(-1.0*self.eta*(1+np.cos(drive_cell[t-1])))*((1.0-s_dc[:,t-1])/self.tau_R))
             
            # calculate total synaptic input
            S_ex[:,t]	= self.g_ee*np.sum(s_ee[:,:,t-1],axis=0) - self.g_be*np.sum(s_be[:,:,t-1],axis=0) - self.g_ce*np.sum(s_ce[:,:,t-1],axis=0) + self.g_de*s_de[:,t-1]
            S_fs[:,t] = self.g_eb*np.sum(s_eb[:,:,t-1],axis=0) - self.g_bb*np.sum(s_bb[:,:,t-1],axis=0) - self.g_cb*np.sum(s_cb[:,:,t-1],axis=0) + self.g_db*s_db[:,t-1]
            S_som[:,t] = self.g_ec*np.sum(s_ec[:,:,t-1],axis=0)  - self.g_bc*np.sum(s_bc[:,:,t-1],axis=0) #+ self.g_dc*s_dc[:,t-1]
            
            meg[:,t]	= self.g_ee*np.sum(s_ee[:,:,t-1],axis=0)  #+ self.g_de*s_de[:,t-1]

            
            # evolve drive cell
            drive_cell[t]  	= drive_cell[t-1]  + self.dt*((1 - np.cos(drive_cell[t-1])) + b_drive*(1 + np.cos(drive_cell[t-1])))
             
            # evolve theta
            theta_ex[:,t]  	= theta_ex[:,t-1]  + self.dt*( (1 - np.cos(theta_ex[:,t-1])) + (B_ex + S_ex[:,t] + N_ex[:,t])*(1 + np.cos(theta_ex[:,t-1])))
            theta_fs[:,t] 	= theta_fs[:,t-1] + self.dt*( (1 - np.cos(theta_fs[:,t-1])) + (B_fs + S_fs[:,t] + N_fs[:,t])*(1 + np.cos(theta_fs[:,t-1])))
            theta_som[:,t] 	= theta_som[:,t-1] + self.dt*( (1 - np.cos(theta_som[:,t-1])) + (B_som + S_som[:,t] + N_som[:,t])*(1 + np.cos(theta_som[:,t-1])))
    
    
    
        # Sum EPSCs of excitatory cells
        MEG = np.sum(meg,axis=0)

     
           
        if saveMEG:
            filenameMEG = self.directory  + self.filename + '-MEG.npy'
            np.save(filenameMEG,MEG)

          
          
        if saveEX:
            filenameEX = self.directory  + self.filename + '-Ex.npy'
            np.save(filenameEX,theta_ex)
          
          
        if saveFS:
           filenameFS = self.directory  + self.filename + '-Bask.npy'
           np.save(filenameFS,theta_fs)
           
        if saveSOM:
           filenameSOM = self.directory  + self.filename + '-Chand.npy'
           np.save(filenameSOM,theta_som)
              
        return MEG,theta_ex,theta_fs,theta_som
    
    
    def plotTrace(self,trace,sim_time,save):
        '''
           Plots a trace signal versus time
           Parameters:
           trace: the trace signal to plot
           sim_time: the duration of the simulation
        '''
        fig = plt.figure()
        ax = fig.add_subplot(111)
        time = np.linspace(0,sim_time,int(sim_time/self.dt)+1)
        ax.plot(time,trace,'k')
        
        #plt.show()
    
    def plotMEG(self,MEG,sim_time,save):
        '''
           Plots a simulated MEG signal versus time
           Parameters:
           MEG: the simulated MEG signal to plot
           sim_time: the duration of the simulation
        '''
        fig = plt.figure()
        ax = fig.add_subplot(111)
        time = np.linspace(0,sim_time,int(sim_time/self.dt)+1)
        ax.plot(time,MEG,'k')
        
        if save:
            filenamepng = self.directory+self.filename+'-MEG.png'
            #print filenamepng
            plt.savefig(filenamepng,dpi=600)
        
        
        #plt.show()
    
    def rasterPlot(self,data,sim_time,save,name):
        '''
           Plots a raster plot for an array of spike trains
           Parameters:
           data: array of spike trains
           sim_time: duration of the simulation
        '''
        spiketrains = self._getSpikeTimes(data)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for i,times in enumerate(spiketrains):
            y = [i]*len(times)
            ax.plot(times,y,linestyle='None',color='k',marker='|',markersize=10)
            ax.axis([0,sim_time,-0.5,len(spiketrains)])
    
        if save:
            filenamepng = self.directory+self.filename+'-'+name+'-raster.png'
            #print filenamepng
            plt.savefig(filenamepng,dpi=600)
        #plt.show()
    
    def calculatePSD(self,meg,sim_time):
        '''
           Calculates the power spectral density of a simulated MEG signal
           Parameters:
           meg: the simulated MEG signal
           sim_time: the duration of the simulation
        '''
        # fourier sample rate
        fs = 1. / self.dt	
        
        tn = np.linspace(0,sim_time,int(sim_time/self.dt)+1)
        
        npts = len(meg)
        startpt = int(0.2*fs)
        
        if (npts - startpt)%2!=0:
            startpt = startpt + 1
        
        meg = meg[startpt:]
        tn = tn[startpt:]
        nfft = len(tn)    
        
        pxx,freqs=mlab.psd(meg,NFFT=nfft,Fs=fs,noverlap=0,window=mlab.window_none)
        pxx[0] = 0.0

        return pxx,freqs
    
           
           
    def plotPSD(self,freqs,psd,fmax,save):
        '''
            Plots the power spectral density of a simulated MEG signal
            Parameters:
            freqs: frequency vector
            psd: power spectral density vector
            fmax: maximum frequency to display
        '''
        fig = plt.figure()
        ax = fig.add_subplot(111)
    
    
        ax.plot(freqs,psd)
        ax.axis(xmin=0, xmax=fmax)
            
        if save:
            filenamepng = self.directory+self.filename+'-PSD.png'
            #print filenamepng
            plt.savefig(filenamepng,dpi=600)
            
        
        return ax
    

    def _getSingleSpikeTimes(self,neuron):
        '''
           Calculates the spike times from the trace of a single theta neuron
           Parameters:
           neuron: the single neuron trace
        '''
        spike_times = []
        old = 0.0
        for i,n in enumerate(neuron):

          # if theta passes (2l-1)*pi, l integer, with dtheta/dt>0 then the neuron spikes (see Boergers and Kopell, 2003)
          if (n%(2*np.pi))>np.pi and (old%(2*np.pi))<np.pi:
              spike_time = i*self.dt
              spike_times.append(spike_time)
          old = n
        
        return spike_times
        
    def _getSpikeTimes(self,data):
        '''
           Calculates the spike times from an array of theta neuron traces
           Parameters:
           data: the traces array
        '''
        nx,ny = data.shape
        spike_times_array = [None]*nx
        for i in range(nx):
            spike_times_array[i] = self._getSingleSpikeTimes(data[i,:])
        
        return spike_times_array
    
    def _noise(self,t,tn):
        t  = t * self.dt
        if t-tn>0:
            value = (self.A*(np.exp(-(t-tn)/self.tau_ex)-np.exp(-(t-tn)/self.tau_R)))/(self.tau_ex-self.tau_R)
        else:
            value = 0
    
        return value









