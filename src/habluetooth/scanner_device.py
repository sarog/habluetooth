"""Base classes for HA Bluetooth scanners for bluetooth."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData

if TYPE_CHECKING:
    from .base_scanner import BaseHaScanner


@dataclass(slots=True)
class BluetoothScannerDevice:
    """Data for a bluetooth device from a given scanner."""

    scanner: BaseHaScanner
    ble_device: BLEDevice
    advertisement: AdvertisementData

    def score_connection_path(self, rssi_diff: int) -> float:
        """Return a score for the connection path to this device."""
        return self.scanner._score_connection_paths(rssi_diff, self)
