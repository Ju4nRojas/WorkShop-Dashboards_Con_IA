# Demo 3 - Verificador de requisitos (SOLO LECTURA: no instala ni modifica nada).
# Uso (PowerShell):   powershell -ExecutionPolicy Bypass -File verificar_requisitos.ps1
$ErrorActionPreference = 'SilentlyContinue'
$raiz = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path))
$res = New-Object System.Collections.Generic.List[object]
function Add-R($nombre, $estado, $detalle, $accion) { $res.Add([pscustomobject]@{ Requisito = $nombre; Estado = $estado; Detalle = $detalle; 'Que hacer' = $accion }) }

# 1) Sistema operativo (el MCP local no soporta macOS)
if ($env:OS -eq 'Windows_NT') { Add-R 'Windows' 'OK' ([System.Environment]::OSVersion.VersionString) '' }
else { Add-R 'Windows' 'FALTA' 'El MCP local solo funciona en Windows' 'Usar el servidor hospedado (requiere Entra ID y administrador de Fabric)' }

# 2) Power BI Desktop
$pkg = Get-AppxPackage -Name '*PowerBI*' | Select-Object -First 1
$exe = @("$env:ProgramFiles\Microsoft Power BI Desktop\bin\PBIDesktop.exe", "${env:ProgramFiles(x86)}\Microsoft Power BI Desktop\bin\PBIDesktop.exe") | Where-Object { Test-Path $_ } | Select-Object -First 1
if ($pkg) { Add-R 'Power BI Desktop' 'OK' "Tienda: $($pkg.Version)" '' }
elseif ($exe) { Add-R 'Power BI Desktop' 'OK' $exe '' }
else { Add-R 'Power BI Desktop' 'FALTA' 'No se encontro' 'Instalar Power BI Desktop (Microsoft Store o descarga oficial)' }

# 3) Node.js (la CLI de reportes pide 20+; el MCP pide 18+)
$nv = (& node --version 2>$null)
if ($nv) {
    $mayor = [int](($nv -replace '^v','').Split('.')[0])
    if ($mayor -ge 20) { Add-R 'Node.js 20+' 'OK' $nv '' } else { Add-R 'Node.js 20+' 'FALTA' "Version $nv" 'Actualizar Node.js (winget install OpenJS.NodeJS.LTS)' }
} else { Add-R 'Node.js 20+' 'FALTA' 'No se encontro' 'Instalar Node.js LTS' }

# 4) CLI powerbi-report-author (la usa el skill de reportes para crear, validar y previsualizar)
$cli = (& powerbi-report-author --version 2>$null)
if ($cli) { Add-R 'CLI powerbi-report-author' 'OK' "$cli" '' }
else { Add-R 'CLI powerbi-report-author' 'FALTA' 'No instalada' 'npm install -g @microsoft/powerbi-report-authoring-cli@latest' }

# 5) Plugin powerbi-authoring en Claude
$plug = Get-ChildItem "$env:USERPROFILE\.claude\plugins\cache\fabric-collection\powerbi-authoring" -Directory | Sort-Object Name | Select-Object -Last 1
if ($plug) { Add-R 'Plugin powerbi-authoring' 'OK' "Version $($plug.Name)" '' }
else { Add-R 'Plugin powerbi-authoring' 'FALTA' 'No esta instalado' '/plugin marketplace add microsoft/skills-for-fabric  y  /plugin install powerbi-authoring@fabric-collection' }

# 6) Paquete del MCP ya descargado por npx (si no, la primera conexion descarga y puede dar timeout)
$mcp = Get-ChildItem "$env:LOCALAPPDATA\npm-cache\_npx" -Directory | ForEach-Object { Join-Path $_.FullName 'node_modules\@microsoft\powerbi-modeling-mcp' } | Where-Object { Test-Path $_ } | Select-Object -First 1
if ($mcp) { Add-R 'Paquete del MCP en cache' 'OK' 'Ya descargado por npx' '' }
else { Add-R 'Paquete del MCP en cache' 'AVISO' 'No esta en cache de npx' 'Calentar: abrir una sesion con el plugin con tiempo y esperar a que conecte; aceptar el EULA' }

# 7) Datos de la demo
$csv = Join-Path $raiz 'datos\despachos_eds_mensual.csv'
if (Test-Path $csv) { Add-R 'CSV de la demo' 'OK' ('{0:N0} KB' -f ((Get-Item $csv).Length/1KB)) '' }
else { Add-R 'CSV de la demo' 'FALTA' $csv 'Regenerar con datos\preparar_datos.py' }

# 8) Ubicacion del proyecto (OneDrive y rutas largas complican Power Query y los archivos PBIP)
if ($raiz -match 'OneDrive') { Add-R 'Ubicacion del proyecto' 'AVISO' 'El proyecto esta dentro de OneDrive' 'Crear el PBIP en una carpeta local fuera de OneDrive, p. ej. C:\Demo3PowerBI, y copiar alli el CSV' }
else { Add-R 'Ubicacion del proyecto' 'OK' $raiz '' }

# 9) Acceso al registro de npm (descarga de CLI y MCP)
$ver = (& npm view '@microsoft/powerbi-report-authoring-cli' version 2>$null)
if ($ver) { Add-R 'Acceso a npm' 'OK' "registry responde; CLI disponible: $ver" '' } else { Add-R 'Acceso a npm' 'AVISO' 'No respondio' 'Revisar red o proxy; sin npm no se descargan la CLI ni el MCP' }

$res | Format-Table -AutoSize -Wrap
$falta = @($res | Where-Object { $_.Estado -eq 'FALTA' }).Count; $aviso = @($res | Where-Object { $_.Estado -eq 'AVISO' }).Count
Write-Host ("Resultado: {0} faltan, {1} avisos, {2} correctos. Este script no probo el MCP ni Power BI Desktop: eso se comprueba en el ensayo." -f $falta, $aviso, ($res.Count - $falta - $aviso))
