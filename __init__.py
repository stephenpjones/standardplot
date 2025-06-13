"""
StandardPlot - Consistent plotting configuration for data analysis

This package provides standardized plotting functions and configurations
that automatically apply consistent styling across all your plots.
"""

__version__ = "1.0.0"
__author__ = "Your Name"

# Import main components
from .config import PlotConfig, plot_config
from .utils import StandardPlots, PlotSaver, plot_saver

# Auto-apply global configuration on import
plot_config.apply_global_style()

# Make key components available at package level
__all__ = [
    'PlotConfig',
    'plot_config', 
    'StandardPlots',
    'PlotSaver',
    'plot_saver'
]

# Convenience function for quick setup
def setup_custom_config(config_path):
    """Load and apply custom configuration"""
    global plot_config
    plot_config = PlotConfig(config_path)
    plot_config.apply_global_style()
    return plot_config

# Version info
def get_version():
    """Return package version"""
    return __version__
