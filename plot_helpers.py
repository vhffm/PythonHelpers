"""
Helper Functions for Plotting.
"""

import matplotlib.pyplot as plt


def scatter_matrix(data_array, data_tags, 
                   data_array_lo, data_array_hi, \
                   data_array_ticks):
    """
    Plot Scatter Matrix.
    """
    
    N = len(data_array)
    fig, axarr = plt.subplots(N-1,N-1)
    #fig.set_size_inches(8.27,8.27*(6./8.)*2./3.)
    fig.set_size_inches(8.27,8.27*(6./8.))
    
    # Remove Lower Left Half
    for irow in range(N-1):
        for icol in range(irow):
            ax = axarr[irow,icol]
            #ax.scatter(0,0,c='b')
            #plt.setp(ax.get_xticklabels(), visible=False)
            fig.delaxes(ax)
            
    # Plot Data
    for irow in range(N-1):
        for icol in range(irow,N-1):
            # Extract Axis
            ax = axarr[irow,icol]
            
            # Debug
            # ax.scatter(1,1,c='r')
            
            # Extract Data
            xdata = data_array[icol+1]
            ydata = data_array[irow]
            
            # Extract Axis Labels
            xlabel = data_tags[icol+1]
            ylabel = data_tags[irow]
            
            # Extract Data Limits
            xlo = data_array_lo[icol+1]
            xhi = data_array_hi[icol+1]
            ylo = data_array_lo[irow]
            yhi = data_array_hi[irow]
            
            # Extract Ticks
            xticks = data_array_ticks[icol+1]
            yticks = data_array_ticks[irow]
            
            # Plot Data
            ax.scatter(xdata, ydata, s=2**2, c='k', edgecolor='none')
            
            # Plot Axis Label
            if icol == irow:
                ax.set_ylabel(ylabel)
                ax.set_xlabel(xlabel)
            # Remove Tick Marks
            else:
                plt.setp(ax.get_xticklabels(), visible=False)
                plt.setp(ax.get_yticklabels(), visible=False)
                
            # Set Axis Limits
            ax.set_xlim([xlo, xhi])
            ax.set_ylim([ylo, yhi])
            
            # Set Axis Ticks
            ax.set_xticks(xticks)
            ax.set_yticks(yticks)
        
    # Tighten
    fig.subplots_adjust(hspace=0, wspace=0)