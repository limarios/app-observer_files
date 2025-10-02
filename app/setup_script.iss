[Setup]
AppName=Monitor de Cópia
AppVersion=1.0
DefaultDirName={userappdata}\MonitorCopias
DefaultGroupName=MonitorCopias
OutputDir=.
OutputBaseFilename=MonitorCopias_Installer
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\MonitorCopias.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{commondesktop}\Monitor de Cópia"; Filename: "{app}\MonitorCopias.exe"

[Run]
Filename: "{app}\MonitorCopias.exe"; Description: "Executar após a instalação"; Flags: nowait postinstall
