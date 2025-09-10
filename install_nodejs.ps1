$nodeInstallerUrl = "https://nodejs.org/dist/v20.10.0/node-v20.10.0-x64.msi"
$installerPath = "$env:TEMP\nodejs_installer.msi"

Write-Host "Downloading Node.js installer..."
Invoke-WebRequest -Uri $nodeInstallerUrl -OutFile $installerPath

Write-Host "Running Node.js installer..."
Start-Process msiexec.exe -ArgumentList "/i $installerPath /quiet /norestart" -Wait

Write-Host "Node.js installation complete. Please restart your terminal."
