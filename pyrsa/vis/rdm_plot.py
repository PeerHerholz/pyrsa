#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 16:21:53 2020

@author: heiko
"""

import numpy as np
import matplotlib.pyplot as plt
from pyrsa.rdm import rank_transform
from pyrsa.vis.colors import rdm_colormap

def show_rdm(rdm, do_rank_transform=False, pattern_descriptor=None,
             cmap=None):
    """shows an rdm object

    Parameters
    ----------
    rdm : pyrsa.rdm.RDMs
        RDMs object to be plotted
    do_rank_transform : bool
        whether we should do a rank transform before plotting
    pattern_descriptor : String
        name of a pattern descriptor which will be used as an axis label
    cmap : color map
        colormap or identifier for a colormap to be used
        conventions as for matplotlib colormaps

    """
    if cmap is None:
        cmap = rdm_colormap() 
    if do_rank_transform:
        rdm = rank_transform(rdm)
    rdm_mat = rdm.get_matrices()
    if rdm.n_rdm  > 1:
        m = np.ceil(np.sqrt(rdm.n_rdm+1))
        n = np.ceil((1 + rdm.n_rdm) / m)
        for idx in range(rdm.n_rdm):
            plt.subplot(n, m, idx + 1)
            plt.imshow(rdm_mat[idx], cmap=cmap)
            _add_descriptor_labels(rdm, pattern_descriptor)
        plt.subplot(n, m, n * m)
        plt.imshow(np.mean(rdm_mat, axis=0), cmap=cmap)
        _add_descriptor_labels(rdm, pattern_descriptor)
    elif rdm.n_rdm == 1:
        plt.imshow(rdm_mat[0], cmap=cmap)
        _add_descriptor_labels(rdm, pattern_descriptor)
    plt.show()


def _add_descriptor_labels(rdm, descriptor, ax=None):
    """ adds a descriptor as ticklabels """
    if ax is None:
        ax = plt.gca()
    if descriptor is not None:
        desc = rdm.pattern_descriptors[descriptor]
        ax.set_xticks(np.arange(rdm.n_cond))
        ax.set_xticklabels(desc)
        ax.set_yticks(np.arange(rdm.n_cond))
        ax.set_yticklabels(desc)
        plt.ylim(rdm.n_cond - 0.5, -0.5)
        plt.xlim(-0.5, rdm.n_cond - 0.5)
    else:
        ax.set_xticks([])
        ax.set_yticks([])
