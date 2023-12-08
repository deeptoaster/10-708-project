import os
import numpy as np
import scipy


exp1 = os.listdir("SharedData_TrainingEffect42HumanSubjectsNoninvasiveBCI/Exp1")
exp2 = os.listdir("SharedData_TrainingEffect42HumanSubjectsNoninvasiveBCI/Exp2")

experiments = []
labels = []
for exp in exp1:
    mat = scipy.io.loadmat("SharedData_TrainingEffect42HumanSubjectsNoninvasiveBCI/Exp1/"+exp)

    exp_states = dict()
    for _ in mat['Experimental_states']:
        for wrapper in _:
            fieldnames = wrapper.dtype.names
            for idx, val in enumerate(wrapper):
                exp_states[f'{fieldnames[idx]}'] = val.flatten()

    # Maybe we can use the dict that Robin prepared to extract the targets?
    targets = exp_states['TargetCode']
    results = exp_states['ResultCode']
    # cursor = exp_states['CursorPosX']

    raw_eeg = mat['output_data']

    # Get indices for the start/end of  each trial
    trial_start_index = np.nonzero(np.diff(targets))[0][::2]+1
    trial_start_end_index = np.nonzero(np.diff(targets))[0]+1

    # labels to ConvNet in one data file
    targets = targets[trial_start_index]
    results = results[trial_start_index]
    print("labels: ")
    print(targets.shape)
    print(targets)
    print('-----------------------------------------------')
    print("minimum trial duration: ", np.amin(np.diff(trial_start_end_index)[::2]))

    raw_eeg = np.split(raw_eeg,trial_start_end_index)[1::2]
    input = []

    for eeg in raw_eeg:
    # index 210 to 310 (1s) because the motor imgination starts 2s after the target shows up. 210 is 2s (200) plus 0.1s (10) reaction time. 
    # The target will freeze on the screen for 1s and the shortest trial only lasts for 4.3 seconds so the upper bound needs to be <330, 4.32 (432) minus 1s (100).
    # 310 is taken to round to 100
        input.append(eeg[210:310,:])

    # inputs to ConvNet in one data file
    input = np.array(input)


    exp_states = dict()
    for _ in mat['Experiment_Parm']:
        for wrapper in _:
            fieldnames = wrapper.dtype.names
            for idx, val in enumerate(wrapper):
                exp_states[f'{fieldnames[idx]}'] = val.flatten()

    channels = exp_states['Channels']

    montage = 'FP1-F7;F7-T7;T7-P7;P7-O1;FP2-F8;F8-T8;T8-P8;P8-O2;T7-C3;C3-CZ;CZ-C4;C4-T8;FP1-F3;F3-C3;C3-P3;P3-O1;FP2-F4;F4-C4;C4-P4;P4-O2'

    electrode_pairs = montage.split(";")

    new_data = np.zeros((125,100,20))
    for i in range(len(electrode_pairs)):

        pair = electrode_pairs[i]
        electrode_1 = pair.split("-")[0]
        electrode_2 = pair.split("-")[1]
        for j in range(len(channels)):
            if channels[j][0] == electrode_1:
                index_1 = j
            if channels[j][0] == electrode_2:
                index_2 = j

        new_data[:,:,i] = input[:,:,index_1] - input[:,:,index_2]

    print(new_data.shape)



    fft_signal = np.fft.rfft(new_data, axis=1)
    print(fft_signal[:120,:,:].shape)
    experiments.append(fft_signal[:120,:,:])
    labels.append(targets[:120])

for exp in exp2:
    mat = scipy.io.loadmat("SharedData_TrainingEffect42HumanSubjectsNoninvasiveBCI/Exp2/"+exp)

    exp_states = dict()
    for _ in mat['Experimental_states']:
        for wrapper in _:
            fieldnames = wrapper.dtype.names
            for idx, val in enumerate(wrapper):
                exp_states[f'{fieldnames[idx]}'] = val.flatten()

    # Maybe we can use the dict that Robin prepared to extract the targets?
    targets = exp_states['TargetCode']
    results = exp_states['ResultCode']
    # cursor = exp_states['CursorPosX']

    raw_eeg = mat['output_data']

    # Get indices for the start/end of  each trial
    trial_start_index = np.nonzero(np.diff(targets))[0][::2]+1
    trial_start_end_index = np.nonzero(np.diff(targets))[0]+1

    # labels to ConvNet in one data file
    targets = targets[trial_start_index]
    results = results[trial_start_index]
    print("labels: ")
    print(targets)
    print('-----------------------------------------------')
    print("minimum trial duration: ", np.amin(np.diff(trial_start_end_index)[::2]))

    raw_eeg = np.split(raw_eeg,trial_start_end_index)[1::2]
    input = []

    for eeg in raw_eeg:
    # index 210 to 310 (1s) because the motor imgination starts 2s after the target shows up. 210 is 2s (200) plus 0.1s (10) reaction time. 
    # The target will freeze on the screen for 1s and the shortest trial only lasts for 4.3 seconds so the upper bound needs to be <330, 4.32 (432) minus 1s (100).
    # 310 is taken to round to 100
        input.append(eeg[210:310,:])

    # inputs to ConvNet in one data file
    input = np.array(input)




    exp_states = dict()
    for _ in mat['Experiment_Parm']:
        for wrapper in _:
            fieldnames = wrapper.dtype.names
            for idx, val in enumerate(wrapper):
                exp_states[f'{fieldnames[idx]}'] = val.flatten()

    channels = exp_states['Channels']

    montage = 'FP1-F7;F7-T7;T7-P7;P7-O1;FP2-F8;F8-T8;T8-P8;P8-O2;T7-C3;C3-CZ;CZ-C4;C4-T8;FP1-F3;F3-C3;C3-P3;P3-O1;FP2-F4;F4-C4;C4-P4;P4-O2'

    electrode_pairs = montage.split(";")

    new_data = np.zeros((120,100,20))
    for i in range(len(electrode_pairs)):

        pair = electrode_pairs[i]
        electrode_1 = pair.split("-")[0]
        electrode_2 = pair.split("-")[1]
        for j in range(len(channels)):
            if channels[j][0] == electrode_1:
                index_1 = j
            if channels[j][0] == electrode_2:
                index_2 = j

        new_data[:,:,i] = input[:,:,index_1] - input[:,:,index_2]

    print(new_data.shape)

    fft_signal = np.fft.rfft(new_data, axis=1)
    print(fft_signal.shape)
    experiments.append(fft_signal)
    labels.append(targets)


dataset = np.array(experiments)
print(dataset.shape)
dataset = np.reshape(dataset,(84*120,51,20))
print(dataset.shape)
np.save('bci_x', dataset)


labels = np.array(labels)
print(labels.shape)
labels = np.reshape(labels,(84*120,-1))
print(labels.shape)
np.save('bci_y', labels)

