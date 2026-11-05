[Setup]
AppName=الوحدة التنفيذية للمشاريع
AppVersion=1.0
DefaultDirName={pf}\YemenTelecomApp
DefaultGroupName=YemenTelecomApp
OutputDir=.\Output
OutputBaseFilename=YemenTelecom_Setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Files]
Source: "dist\windows_app.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "*.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "*.jpg"; DestDir: "{app}"; Flags: ignoreversion
Source: "*.ttf"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\الوحدة التنفيذية للمشاريع"; Filename: "{app}\windows_app.exe"
Name: "{commondesktop}\الوحدة التنفيذية للمشاريع"; Filename: "{app}\windows_app.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked