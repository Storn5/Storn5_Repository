import numpy as np
import matplotlib.pyplot as plt

from astropy import units as u
from astropy.coordinates import SkyCoord

artemis2_data = np.loadtxt('Artemis_II_OEM_2026_04_02_to_EI_v3.asc', dtype='str', delimiter=' ', skiprows=20)

artemis2_t = artemis2_data[:, 0].astype(np.datetime64)
artemis2_coords = artemis2_data[:, 1:4].astype(np.float64)
artemis2_speeds = artemis2_data[:, 4:].astype(np.float64)
artemis2_abs_speeds = np.linalg.norm(artemis2_speeds, axis=1).reshape(-1, 1)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
trajectory_scatter = ax.scatter(
    artemis2_coords[:, 0],
    artemis2_coords[:, 1],
    artemis2_coords[:, 2],
    c=artemis2_abs_speeds,
    cmap='twilight',
)
fig.colorbar(trajectory_scatter, orientation='vertical').set_label('Velocity, km/s')
ax.scatter(0, 0, 0, c='green', s=50)
ax.set_title('Artemis 2 trajectory')
plt.show()
