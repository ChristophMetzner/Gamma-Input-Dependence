import numpy as np

drive_frequencies = [40.0, 30.0, 20.0]

freqs = np.load('Exploration/freqs.npy')

meg_d01_ctrl = np.zeros((3, 8192))
meg_d02_ctrl = np.zeros((3, 8192))
meg_d03_ctrl = np.zeros((3, 8192))
meg_d04_ctrl = np.zeros((3, 8192))
meg_d05_ctrl = np.zeros((3, 8192))

psd_d01_ctrl = np.zeros((3, 4095))
psd_d02_ctrl = np.zeros((3, 4095))
psd_d03_ctrl = np.zeros((3, 4095))
psd_d04_ctrl = np.zeros((3, 4095))
psd_d05_ctrl = np.zeros((3, 4095))

for i, f in enumerate(drive_frequencies):
    meg_d01_ctrl[i] = np.load('Exploration/Input_Strength_01/drive_01_control_drive_frequency_'+str(f)+'-MEG.npy')
    meg_d02_ctrl[i] = np.load('Exploration/Input_Strength_02/drive_02_control_drive_frequency_'+str(f)+'-MEG.npy')
    meg_d03_ctrl[i] = np.load('Exploration/Input_Strength_03/drive_03_control_drive_frequency_'+str(f)+'-MEG.npy')
    meg_d04_ctrl[i] = np.load('Exploration/Input_Strength_04/drive_04_control_drive_frequency_'+str(f)+'-MEG.npy')
    meg_d05_ctrl[i] = np.load('Exploration/Input_Strength_05/drive_05_control_drive_frequency_'+str(f)+'-MEG.npy')

    psd_d01_ctrl[i] = np.load('Exploration/Input_Strength_01/drive_01_control_drive_frequency_'+str(f)+'-PSD.npy')
    psd_d02_ctrl[i] = np.load('Exploration/Input_Strength_02/drive_02_control_drive_frequency_'+str(f)+'-PSD.npy')
    psd_d03_ctrl[i] = np.load('Exploration/Input_Strength_03/drive_03_control_drive_frequency_'+str(f)+'-PSD.npy')
    psd_d04_ctrl[i] = np.load('Exploration/Input_Strength_04/drive_04_control_drive_frequency_'+str(f)+'-PSD.npy')
    psd_d05_ctrl[i] = np.load('Exploration/Input_Strength_05/drive_05_control_drive_frequency_'+str(f)+'-PSD.npy')







