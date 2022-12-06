fs=96000; % samplig frequency (should be at least x2.2 of f0 )

[sb, fd]=audioread('weather.wav'); % signal in audio domain
if fd ~= fs                  % change sampling prequency to target
    sb = resample(sb, fs, fd);
end    
sb=sb./max(sb); % normalization

A = 1; % amplitude of carrier tone 
T = length(sb) / fs; % length of signal
f0 = 40000; % carrier frequency
Fi0 = pi/2; % initial phase
N = T * fs;  % number of samples
t = (0 : N-1) / fs;  % time stamps

sa = A * sin(2 * pi * f0 * t + Fi0); % samples of carrier tone

% first method
% s = sb .* sa + imag(hilbert(sb)) .* imag(hilbert(sa));
% to have upper sideband use
% s = sb .* sa - imag(hilbert(sb)) .* imag(hilbert(sa));

% second method
s = ssbmod(sb, f0, fs);

s=s./(max(s)); % normalization of modulated signal
%write the attack signal into an audio file; fill in the path
ultrasound_file = 'weather_attack_second.wav';
audiowrite(ultrasound_file, s, fs);