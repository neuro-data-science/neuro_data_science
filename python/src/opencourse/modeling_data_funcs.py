import numpy as np


def evaluate_score_ExpCos(params, spikes, angle):
    predictedF = np.exp(params[0] + params[1] * np.cos(angle - params[2]))
    logP = spikes * np.log(predictedF) - predictedF
    spikes_factorial = np.array([np.math.factorial(ii) for ii in spikes])
    logP -= np.log(spikes_factorial)
    score = -1. * np.sum(logP)
    return score

def format_plot(ax, y_max=6):
    ax.set_xlabel('angle (rad)')
    ax.set_ylabel('spike counts')
    ax.set_ylim(0, y_max)
    ax.set_xticks(np.linspace(-np.pi, np.pi, 5))
    ax.set_xticklabels([r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$', r'$\pi$'])
    ax.set_xlim(-np.pi, np.pi)
