message_file = 'result.wav';
[message_signal, message_sample_rate] = audioread(message_file);

% Use the butter filter to enact a low pass filter on the data
% Block out data outside of 8k
[signal,rate] = butter(10,2*8000/message_sample_rate,'low');
voice_filter = filter(signal,rate,message_signal(:,1));

% Resample with new freq
% 2x original sample rate
double_freq = 48000;
upsample = resample(voice_filter,double_freq,message_sample_rate);
upsample = 1/max(abs(upsample)) * upsample;

% Attempt amplitude modulation with carrier frequency that
% ranges from 17k-24k

dt = 1/double_freq;
num_samples = size(upsample,1);
t = (0:dt:(num_samples - 1)*dt)';
carrier = 24000;
final_result = upsample.*cos(2*pi*carrier*t) + 1*cos(2*pi*carrier*t);
%here we use double sideband modulation; instead we can only keep either
final_result = 1/max(abs(final_result)) * final_result;

result_file = 'result_24k.wav';
audiowrite(result_file, final_result,double_freq);