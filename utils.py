"""
Standardized plotting utilities with consistent styling
"""
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
import pandas as pd
import numpy as np
from pathlib import Path
import os

try:
    from .config import plot_config
except ImportError:
    from config import plot_config

# Create Bitstream Vera font properties
VERA_FONT_PATH = r"C:\Users\steve\AppData\Local\Microsoft\Windows\Fonts\VeraMono.ttf"
if os.path.exists(VERA_FONT_PATH):
    VERA_FONT_PROP = fm.FontProperties(fname=VERA_FONT_PATH)
else:
    VERA_FONT_PROP = None

def apply_vera_font_to_axes(ax):
    """Apply Bitstream Vera font to all text elements in axes"""
    if VERA_FONT_PROP is not None:
        # Apply to axis labels
        ax.xaxis.label.set_fontproperties(VERA_FONT_PROP)
        ax.yaxis.label.set_fontproperties(VERA_FONT_PROP)
        
        # Apply to tick labels
        for label in ax.get_xticklabels() + ax.get_yticklabels():
            label.set_fontproperties(VERA_FONT_PROP)
        
        # Apply to title if it exists
        if ax.get_title():
            ax.title.set_fontproperties(VERA_FONT_PROP)
        
        # Apply to legend if it exists
        legend = ax.get_legend()
        if legend:
            for text in legend.get_texts():
                text.set_fontproperties(VERA_FONT_PROP)
                text.set_color('#4a4a4a')  # Set legend text color

class StandardPlots:
    """Collection of standardized plotting functions"""
    
    @staticmethod
    def line_plot(data, x=None, y=None, hue=None, title=None, 
                  xlabel=None, ylabel=None, figsize=None, **kwargs):
        """Standardized line plot"""
        figsize = figsize or plot_config.base_config['figure']['figsize']
        fig, ax = plt.subplots(figsize=figsize)
        
        if isinstance(data, pd.DataFrame):
            if hue:
                for i, (name, group) in enumerate(data.groupby(hue)):
                    color = plot_config.get_palette()[i % len(plot_config.get_palette())]
                    ax.plot(group[x], group[y], label=name, color=color, **kwargs)
                ax.legend()
            else:
                ax.plot(data[x], data[y], color=plot_config.get_color('primary'), **kwargs)
        else:
            ax.plot(data, color=plot_config.get_color('primary'), **kwargs)
        
        StandardPlots._apply_standard_formatting(ax, title, xlabel, ylabel)
        return fig, ax
    
    @staticmethod
    def bar_plot(data, x=None, y=None, hue=None, title=None,
                 xlabel=None, ylabel=None, figsize=None, **kwargs):
        """Standardized bar plot"""
        figsize = figsize or plot_config.base_config['figure']['figsize']
        fig, ax = plt.subplots(figsize=figsize)
        
        if isinstance(data, pd.DataFrame):
            if hue:
                sns.barplot(data=data, x=x, y=y, hue=hue, ax=ax, 
                           palette=plot_config.get_palette(), **kwargs)
            else:
                ax.bar(data[x], data[y], color=plot_config.get_color('primary'), **kwargs)
        else:
            ax.bar(range(len(data)), data, color=plot_config.get_color('primary'), **kwargs)
        
        StandardPlots._apply_standard_formatting(ax, title, xlabel, ylabel)
        return fig, ax
    
    @staticmethod
    def scatter_plot(data, x=None, y=None, hue=None, size=None, title=None,
                     xlabel=None, ylabel=None, figsize=None, **kwargs):
        """Standardized scatter plot"""
        figsize = figsize or plot_config.base_config['figure']['figsize']
        fig, ax = plt.subplots(figsize=figsize)
        
        if isinstance(data, pd.DataFrame):
            if hue:
                for i, (name, group) in enumerate(data.groupby(hue)):
                    color = plot_config.get_palette()[i % len(plot_config.get_palette())]
                    sizes = group[size] if size else None
                    ax.scatter(group[x], group[y], label=name, color=color, s=sizes, **kwargs)
                ax.legend()
            else:
                sizes = data[size] if size else None
                ax.scatter(data[x], data[y], color=plot_config.get_color('primary'), s=sizes, **kwargs)
        
        StandardPlots._apply_standard_formatting(ax, title, xlabel, ylabel)
        return fig, ax
    
    @staticmethod
    def histogram(data, bins=30, title=None, xlabel=None, ylabel='Frequency',
                  figsize=None, **kwargs):
        """Standardized histogram"""
        figsize = figsize or plot_config.base_config['figure']['figsize']
        fig, ax = plt.subplots(figsize=figsize)
        
        ax.hist(data, bins=bins, color=plot_config.get_color('primary'), 
                alpha=0.7, edgecolor='white', linewidth=0.5, **kwargs)
        
        StandardPlots._apply_standard_formatting(ax, title, xlabel, ylabel)
        return fig, ax
    
    @staticmethod
    def heatmap(data, title=None, figsize=None, **kwargs):
        """Standardized heatmap"""
        figsize = figsize or (8, 6)
        fig, ax = plt.subplots(figsize=figsize)
        
        sns.heatmap(data, ax=ax, cmap='RdYlBu_r', center=0, 
                   square=True, linewidths=.5, **kwargs)
        
        # Titles are disabled - ignore title parameter
        
        return fig, ax
    
    @staticmethod
    def subplot_grid(n_plots, ncols=2, figsize=None, **kwargs):
        """Create standardized subplot grid"""
        nrows = (n_plots + ncols - 1) // ncols
        figsize = figsize or (ncols * 5, nrows * 4)
        
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize, **kwargs)
        
        # Ensure axes is always a list
        if n_plots == 1:
            axes = [axes]
        elif nrows == 1:
            axes = axes.tolist()
        else:
            axes = axes.flatten()
        
        # Hide unused subplots
        for i in range(n_plots, len(axes)):
            axes[i].set_visible(False)
        
        return fig, axes[:n_plots]
    
    @staticmethod
    def _apply_standard_formatting(ax, title=None, xlabel=None, ylabel=None):
        """Apply standard formatting to axes"""
        # Titles are disabled - ignore title parameter
        if xlabel:
            ax.set_xlabel(xlabel, fontsize=plot_config.base_config['axes']['labelsize'],
                         fontweight=plot_config.base_config['axes']['labelweight'])
        if ylabel:
            ax.set_ylabel(ylabel, fontsize=plot_config.base_config['axes']['labelsize'],
                         fontweight=plot_config.base_config['axes']['labelweight'])
        
        # Enable minor ticks
        ax.minorticks_on()
        
        # Apply Bitstream Vera font to all text elements
        apply_vera_font_to_axes(ax)

class PlotSaver:
    """Utility for consistent plot saving"""
    
    def __init__(self, base_path="./figures"):
        self.base_path = Path(base_path)
        self.base_path.mkdir(exist_ok=True)
    
    def save_plot(self, fig, filename, subfolder=None, **kwargs):
        """Save plot with consistent settings"""
        save_path = self.base_path
        if subfolder:
            save_path = save_path / subfolder
            save_path.mkdir(exist_ok=True)
        
        # Merge with default save settings
        save_kwargs = plot_config.base_config['save'].copy()
        save_kwargs.update(kwargs)
        
        full_path = save_path / f"{filename}.{save_kwargs['format']}"
        fig.savefig(full_path, **save_kwargs)
        print(f"Plot saved to: {full_path}")
        
        return full_path

# Initialize global plot saver
plot_saver = PlotSaver()
