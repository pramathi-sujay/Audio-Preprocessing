"""
config.py

Configuration settings for the duration standardization module.
"""

# Maximum duration of each output clip (seconds)
WINDOW_DURATION = 60.0

# Overlap between consecutive clips (seconds)
OVERLAP_DURATION = 10.0

# Minimum duration required to keep the final clip (seconds)
MIN_CLIP_DURATION = 10.0

# Audio longer than this will be flagged for manual review (seconds)
VERY_LONG_DURATION = 300.0