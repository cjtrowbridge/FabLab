param(
  [string]$Command = "doctor"
)

if ($Command -eq "doctor") {
  python3 --version | Out-Null
  git --version | Out-Null
  python3 scripts/classify_third_party.py check | Out-Null
  python3 scripts/provider_tool.py validate | Out-Null
  Write-Output "FabLab bootstrap doctor passed"
  exit 0
}

Write-Error "Only doctor is implemented in the Phase 4 PowerShell skeleton."
exit 2
