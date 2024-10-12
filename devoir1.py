import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Définir la plage de fréquences à évaluer
frequencies = np.logspace(0, 3, 500)

# Définir la fonction de transfert
sys = signal.TransferFunction([0, 0.03, 2], [0.0009, 0.06, 1])
w, mag, phase = signal.bode(sys, frequencies)

# Interpolate to find the frequencies where the magnitude is -6 dB and -20 dB
freq_at_minus_6db = np.interp(-6, mag[::-1], w[::-1])
freq_at_minus_20db = np.interp(-20, mag[::-1], w[::-1])

# Interpolate to find the magnitude and phase at 45 rad/s
mag_at_45 = np.interp(45, w, mag)
phase_at_45 = np.interp(45, w, phase)

# Créer le diagramme de Bode
plt.figure()
plt.suptitle('Diagramme de Bode')

# Magnitude
plt.subplot(2, 1, 1)
plt.semilogx(w, mag)
plt.axvline(x=45, color='red', linestyle='--')
plt.scatter([45], [mag_at_45], color='red', zorder=5)
plt.text(45, mag_at_45, f'(45, {mag_at_45:.2f} dB)', fontsize=12, color='black', verticalalignment='top', horizontalalignment='right')
plt.ylabel('Amplitude (dB)')

# Add points at -3 dB and -20 dB
plt.scatter([freq_at_minus_6db], [-6], color='red', zorder=5)
plt.scatter([freq_at_minus_20db], [-20], color='red', zorder=5)

# Annotate the points with their coordinates
plt.text(freq_at_minus_6db, -6, f'({freq_at_minus_6db:.2f}, -6 dB)', fontsize=12, color='black', verticalalignment='bottom', horizontalalignment='left')
plt.text(freq_at_minus_20db, -20, f'({freq_at_minus_20db:.2f}, -20 dB)', fontsize=12, color='black', verticalalignment='bottom', horizontalalignment='left')

# Phase
plt.subplot(2, 1, 2)
plt.semilogx(w, phase)
plt.axvline(x=45, color='red', linestyle='--')
plt.scatter([45], [phase_at_45], color='red', zorder=5)
plt.text(45, phase_at_45, f'(45, {phase_at_45:.2f}°)', fontsize=12, color='black', verticalalignment='top', horizontalalignment='right')


plt.xlabel('Fréquence (rad/s)')
plt.ylabel('Phase (degrés)')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Adjust layout to make room for the suptitle
plt.show()