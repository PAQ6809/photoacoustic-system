"""Tests for photoacoustic signal generation and analysis."""
import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import acquire_signal, analyze_signal


def test_acquire_signal():
    """Test synthetic signal generation."""
    num_points = 1000
    frequency = 100000.0
    
    t, signal = acquire_signal(num_points, frequency)
    
    assert signal is not None
    assert len(signal) == num_points
    assert len(t) == num_points
    assert all(isinstance(x, float) for x in signal)


def test_analyze_signal():
    """Test metrics calculation."""
    test_signal = [0.1, 0.5, 1.0, 0.8, 0.3, 0.1]
    
    peak, energy = analyze_signal([], test_signal)
    
    assert peak == 1.0
    assert isinstance(peak, float)
    assert isinstance(energy, float)


def test_empty_signal():
    """Test handling of empty signal."""
    peak, energy = analyze_signal([], [])
    assert peak == 0.0
    assert energy == 0.0


def test_single_point_signal():
    """Test handling of single point signal."""
    peak, energy = analyze_signal([0.0], [0.5])
    assert peak == 0.5
    assert energy == 0.5


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
