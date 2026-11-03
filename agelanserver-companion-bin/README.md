# agelanserver-companion-bin

luskaner's ageServerLauncherCompanion (AGPL-3.0) DLLs, loaded into Age of
Empires II/III: DE and Age of Mythology: Retold by the Goldberg emulator's
`steam_settings/load_dlls/` (the game packages link the ones they need from
`/usr/lib/agelanserver-companion/`):

- `AgeFakeHostsCerts.dll`: resolves the official hosts to the LAN server and
  trusts its certificate inside the game process (`--overrideHosts` /
  `--overrideCerts`, passed by the ageLANServer launcher). Without those
  arguments it does nothing.
- `Age2FakeOnline.dll`, `Age3FakeOnline.dll`: make AoE II/III believe they
  are online.
- `AgeFakeSignKey.dll`: for the newer community "Age Server" (needs
  `--sigkey-der`); installed but not used by the game packages.
