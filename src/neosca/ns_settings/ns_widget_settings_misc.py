#!/usr/bin/env python3


from PySide6.QtWidgets import QCheckBox, QGridLayout, QGroupBox, QSizePolicy, QSpacerItem

from neosca.ns_settings.ns_settings import Ns_Settings
from neosca.ns_settings.ns_widget_settings_abstract import Ns_Widget_Settings_Abstract


class Ns_Widget_Settings_Misc(Ns_Widget_Settings_Abstract):
    name: str = "Miscellaneous"

    def __init__(self, main=None):
        super().__init__(main)
        self.setup_cache()
        self.setup_confirmation()

        self.gridlayout.addWidget(self.groupbox_cache, 0, 0)
        self.gridlayout.addWidget(self.groupbox_confirmation, 1, 0)
        self.gridlayout.addItem(QSpacerItem(0, 0, vData=QSizePolicy.Policy.Expanding))

    def setup_cache(self) -> None:
        self.checkbox_cache_for_future_runs = QCheckBox("Cache for future runs")
        self.checkbox_use_past_cache = QCheckBox("Use past cache if available")

        gridlayout_cache = QGridLayout()
        gridlayout_cache.addWidget(self.checkbox_cache_for_future_runs, 0, 0)
        gridlayout_cache.addWidget(self.checkbox_use_past_cache, 1, 0)
        self.groupbox_cache = QGroupBox("Cache")
        self.groupbox_cache.setLayout(gridlayout_cache)

    def setup_confirmation(self) -> None:
        self.checkbox_dont_confirm_on_exit = QCheckBox("Don't confirm on exit")
        self.checkbox_dont_confirm_on_cache_deletion = QCheckBox("Don't confirm on cache deletion")

        gridlayout_confirmation = QGridLayout()
        gridlayout_confirmation.addWidget(self.checkbox_dont_confirm_on_exit, 0, 0)
        gridlayout_confirmation.addWidget(self.checkbox_dont_confirm_on_cache_deletion, 1, 0)
        self.groupbox_confirmation = QGroupBox("Confirmation")
        self.groupbox_confirmation.setLayout(gridlayout_confirmation)

    def load_settings(self) -> None:
        self.load_settings_cache()
        self.load_settings_confirmation()

    def load_settings_cache(self) -> None:
        self.checkbox_cache_for_future_runs.setChecked(
            Ns_Settings.value(f"{self.name}/cache-for-future-runs", type=bool)
        )
        self.checkbox_use_past_cache.setChecked(Ns_Settings.value(f"{self.name}/use-past-cache", type=bool))

    def load_settings_confirmation(self) -> None:
        self.checkbox_dont_confirm_on_exit.setChecked(
            Ns_Settings.value(f"{self.name}/dont-confirm-on-exit", type=bool)
        )
        self.checkbox_dont_confirm_on_cache_deletion.setChecked(
            Ns_Settings.value(f"{self.name}/dont-confirm-on-cache-deletion", type=bool)
        )

    def verify_settings(self) -> bool:
        return True

    def apply_settings(self) -> None:
        self.apply_settings_cache()
        self.apply_settings_confirmation()

    def apply_settings_cache(self) -> None:
        Ns_Settings.setValue(
            f"{self.name}/cache-for-future-runs", self.checkbox_cache_for_future_runs.isChecked()
        )
        Ns_Settings.setValue(f"{self.name}/use-past-cache", self.checkbox_use_past_cache.isChecked())

    def apply_settings_confirmation(self) -> None:
        Ns_Settings.setValue(
            f"{self.name}/dont-confirm-on-exit", self.checkbox_dont_confirm_on_exit.isChecked()
        )
        Ns_Settings.setValue(
            f"{self.name}/dont-confirm-on-cache-deletion",
            self.checkbox_dont_confirm_on_cache_deletion.isChecked(),
        )
