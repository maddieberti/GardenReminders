# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.building.build_main import Analysis, PYZ, EXE, BUNDLE

a = Analysis(
    ['main.py'],
    pathex=['/Users/maddieberti/PycharmProjects/GardenReminders'],
    binaries=[],
    datas=[
        ('/Users/maddieberti/PycharmProjects/GardenReminders/sounds', 'sounds'),
    ],
    hiddenimports=[
        'plyer', 'plyer._platforms', 'plyer.platforms', 'plyer.platforms.macosx',
        'plyer.platforms.macosx.notification', 'playsound3'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='GardenReminders',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='/Users/maddieberti/PycharmProjects/GardenReminders/icon/plant.icns',
)

app = BUNDLE(
    exe,
    name='GardenReminders.app',
    icon='/Users/maddieberti/PycharmProjects/GardenReminders/icon/plant.icns',
    bundle_identifier=None,
)

