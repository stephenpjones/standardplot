"""
Centralized plotting configuration for consistent data visualization
"""
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from pathlib import Path
import json

class PlotConfig:
    """Centralized plotting configuration management"""
    
    def __init__(self, config_path=None):
        # Enhanced configuration with synthesized optimal palette
        # Based on the enhanced_palette_showcase.py synthesized_optimal palette
        self.base_config = {
            'figure': {
                'figsize': (14/2.54, 10.5/2.54),  # Convert cm to inches
                'dpi': 300,
                'facecolor': '#fafafa',  # Warm white background (slightly lighter than original)
                'edgecolor': 'none'
            },
            'font': {
                'family': 'Arial',  # Arial with automatic fallback
                'size': 11,  # Axis label font size
                'weight': 'normal'
            },
            'axes': {
                'titlesize': 0,  # No titles on plots
                'titleweight': 'normal',
                'labelsize': 11,
                'labelweight': 'normal',
                'linewidth': 1.2,
                'spines.top': True,     # Full border
                'spines.right': True,   # Full border
                'spines.bottom': True,  # Full border
                'spines.left': True,    # Full border
                'grid': False,          # Grid off
                'facecolor': '#fafafa',  # Plot area background - warm white
                'edgecolor': '#4a4a4a',  # Border color - dark grey
                'labelcolor': '#4a4a4a'  # Label color - dark grey
            },
            'xtick': {
                'top': False,     # Tick marks on labeled axes only
                'bottom': True,
                'direction': 'in',  # Internal ticks
                'major.size': 6,    # Major tick length
                'minor.size': 3,    # Minor tick length
                'minor.visible': True,  # Show minor ticks
                'color': '#4a4a4a'  # Tick color - dark grey
            },
            'ytick': {
                'left': True,     # Tick marks on labeled axes only  
                'right': False,
                'direction': 'in',  # Internal ticks
                'major.size': 6,    # Major tick length
                'minor.size': 3,    # Minor tick length
                'minor.visible': True,  # Show minor ticks
                'color': '#4a4a4a'  # Tick color - dark grey
            },
            'legend': {
                'fontsize': 9,
                'frameon': False,
                'loc': 'best',
                'labelcolor': '#4a4a4a'  # Legend text color - dark grey
            },
            'colors': {
                # Synthesized Optimal Palette from enhanced_palette_showcase.py
                'background': '#fafafa',     # Warm white background
                'primary': '#2c5aa0',        # Deep Blue - excellent primary, colorblind-safe
                'secondary': '#e17a47',      # Warm Orange - perfect blue complement, high contrast
                'tertiary': '#6ab187',       # Natural Green - universally distinguishable
                'accent': '#f4c842',         # Golden Yellow - high visibility, colorblind-friendly
                'purple': '#9c4f96',         # Rich Purple - fills red-blue gap in color space
                'neutral': '#8b8b8b',        # Neutral Gray - perfect for less important data
                
                # Legacy color names for backward compatibility
                'hilight': '#e17a47',        # Maps to secondary orange
                'dark': '#8b8b8b',          # Maps to neutral gray
                'other': '#f4c842',         # Maps to accent yellow
                
                # Complete synthesized palette for cycling
                'palette': ['#2c5aa0', '#e17a47', '#6ab187', '#f4c842', '#9c4f96', '#8b8b8b']
            },
            'line': {
                'linewidth': 2.5,
                'markersize': 8
            },
            'save': {
                'format': 'png',
                'bbox_inches': 'tight',
                'pad_inches': 0.1,
                'transparent': False
            }
        }
        
        # Load custom config if provided
        if config_path and Path(config_path).exists():
            self.load_config(config_path)
    
    def load_config(self, config_path):
        """Load configuration from JSON file"""
        with open(config_path, 'r') as f:
            custom_config = json.load(f)
        
        # Deep merge custom config with base config
        self._deep_merge(self.base_config, custom_config)
    
    def _deep_merge(self, base_dict, update_dict):
        """Recursively merge dictionaries"""
        for key, value in update_dict.items():
            if key in base_dict and isinstance(base_dict[key], dict) and isinstance(value, dict):
                self._deep_merge(base_dict[key], value)
            else:
                base_dict[key] = value
    
    def apply_global_style(self):
        """Apply configuration to matplotlib rcParams"""
        # Set matplotlib parameters
        plt.rcParams.update({
            'figure.figsize': self.base_config['figure']['figsize'],
            'figure.dpi': self.base_config['figure']['dpi'],
            'figure.facecolor': self.base_config['figure']['facecolor'],
            'figure.edgecolor': self.base_config['figure']['edgecolor'],
            
            'font.family': 'sans-serif',  # Use sans-serif family
            'font.sans-serif': ['Arial', 'Liberation Sans', 'DejaVu Sans', 'Helvetica', 'sans-serif'],  # Arial with fallbacks
            'font.size': self.base_config['font']['size'],
            'font.weight': self.base_config['font']['weight'],
            
            'axes.titlesize': self.base_config['axes']['titlesize'],
            'axes.titleweight': self.base_config['axes']['titleweight'],
            'axes.labelsize': self.base_config['axes']['labelsize'],
            'axes.labelweight': self.base_config['axes']['labelweight'],
            'axes.linewidth': self.base_config['axes']['linewidth'],
            'axes.spines.top': self.base_config['axes']['spines.top'],
            'axes.spines.right': self.base_config['axes']['spines.right'],
            'axes.spines.bottom': self.base_config['axes']['spines.bottom'],
            'axes.spines.left': self.base_config['axes']['spines.left'],
            'axes.grid': self.base_config['axes']['grid'],
            'axes.facecolor': self.base_config['axes']['facecolor'],
            'axes.edgecolor': self.base_config['axes']['edgecolor'],  # Border color
            'axes.labelcolor': self.base_config['axes']['labelcolor'],  # Label color
            
            'xtick.top': self.base_config['xtick']['top'],
            'xtick.bottom': self.base_config['xtick']['bottom'],
            'xtick.direction': self.base_config['xtick']['direction'],
            'xtick.major.size': self.base_config['xtick']['major.size'],
            'xtick.minor.size': self.base_config['xtick']['minor.size'],
            'xtick.minor.visible': self.base_config['xtick']['minor.visible'],
            'xtick.color': self.base_config['xtick']['color'],  # Tick color from config
            
            'ytick.left': self.base_config['ytick']['left'],
            'ytick.right': self.base_config['ytick']['right'],
            'ytick.direction': self.base_config['ytick']['direction'],
            'ytick.major.size': self.base_config['ytick']['major.size'],
            'ytick.minor.size': self.base_config['ytick']['minor.size'],
            'ytick.minor.visible': self.base_config['ytick']['minor.visible'],
            'ytick.color': self.base_config['ytick']['color'],  # Tick color from config
            
            'legend.fontsize': self.base_config['legend']['fontsize'],
            'legend.frameon': self.base_config['legend']['frameon'],
            'legend.labelcolor': self.base_config['legend']['labelcolor'],
            
            'lines.linewidth': self.base_config['line']['linewidth'],
            'lines.markersize': self.base_config['line']['markersize'],
            
            'savefig.format': self.base_config['save']['format'],
            'savefig.bbox': self.base_config['save']['bbox_inches'],
            'savefig.pad_inches': self.base_config['save']['pad_inches'],
            'savefig.transparent': self.base_config['save']['transparent']
        })
        
        # Set default color cycle
        plt.rcParams['axes.prop_cycle'] = plt.cycler(color=self.base_config['colors']['palette'])
    
    def get_color(self, color_name):
        """Get color by name from the palette"""
        return self.base_config['colors'].get(color_name, color_name)
    
    def get_palette(self, n_colors=None):
        """Get color palette"""
        palette = self.base_config['colors']['palette']
        if n_colors:
            return (palette * ((n_colors // len(palette)) + 1))[:n_colors]
        return palette
    
    def get_synthesized_palette_info(self):
        """Get information about the synthesized optimal palette"""
        return {
            'name': 'Synthesized Optimal Palette',
            'description': 'Scientifically optimized synthesis of best color theory principles',
            'colors': {
                'primary': {'hex': '#2c5aa0', 'name': 'Deep Blue', 'use': 'Primary data, colorblind-safe'},
                'secondary': {'hex': '#e17a47', 'name': 'Warm Orange', 'use': 'Complementary, high contrast'},
                'tertiary': {'hex': '#6ab187', 'name': 'Natural Green', 'use': 'Universally distinguishable'},
                'accent': {'hex': '#f4c842', 'name': 'Golden Yellow', 'use': 'High visibility, colorblind-friendly'},
                'purple': {'hex': '#9c4f96', 'name': 'Rich Purple', 'use': 'Fills red-blue gap in color space'},
                'neutral': {'hex': '#8b8b8b', 'name': 'Neutral Gray', 'use': 'Less important data'}
            },
            'background': {'hex': '#fafafa', 'name': 'Warm White', 'use': 'Easy on eyes, works with all colors'},
            'features': [
                'Maximum perceptual separation in LAB color space',
                'Colorblind accessibility (protanopia, deuteranopia, tritanopia)',
                'Balanced warm/cool distribution',
                'Print-safe (works in grayscale)',
                'Even brightness distribution for fair visual weight'
            ]
        }
    
    def switch_to_legacy_palette(self):
        """Switch back to the original blue palette for comparison"""
        legacy_config = {
            'figure': {'facecolor': '#b0d8e3'},
            'axes': {
                'facecolor': '#b0d8e3',
                'edgecolor': '#0e3768',
                'labelcolor': '#0e3768'
            },
            'xtick': {'color': '#0e3768'},
            'ytick': {'color': '#0e3768'},
            'legend': {'labelcolor': '#0e3768'},
            'colors': {
                'background': '#b0d8e3',
                'primary': '#0e3768',
                'hilight': '#f1f2f6', 
                'dark': '#555555',
                'other': '#efe897',
                'palette': ['#0e3768', '#f1f2f6', '#555555', '#efe897', '#0e3768', '#555555']
            }
        }
        
        self._deep_merge(self.base_config, legacy_config)
        self.apply_global_style()
        print("Switched to legacy blue palette")
    
    def switch_to_synthesized_palette(self):
        """Switch to the synthesized optimal palette"""
        synth_config = {
            'figure': {'facecolor': '#fafafa'},
            'axes': {
                'facecolor': '#fafafa',
                'edgecolor': '#4a4a4a',
                'labelcolor': '#4a4a4a'
            },
            'xtick': {'color': '#4a4a4a'},
            'ytick': {'color': '#4a4a4a'},
            'legend': {'labelcolor': '#4a4a4a'},
            'colors': {
                'background': '#fafafa',
                'primary': '#2c5aa0',
                'secondary': '#e17a47',
                'tertiary': '#6ab187',
                'accent': '#f4c842',
                'purple': '#9c4f96',
                'neutral': '#8b8b8b',
                'hilight': '#e17a47',
                'dark': '#8b8b8b',
                'other': '#f4c842',
                'palette': ['#2c5aa0', '#e17a47', '#6ab187', '#f4c842', '#9c4f96', '#8b8b8b']
            }
        }
        
        self._deep_merge(self.base_config, synth_config)
        self.apply_global_style()
        print("Switched to synthesized optimal palette")
    
    def save_config(self, config_path):
        """Save current configuration to JSON file"""
        with open(config_path, 'w') as f:
            json.dump(self.base_config, f, indent=2)

# Initialize global config
plot_config = PlotConfig()
plot_config.apply_global_style()
