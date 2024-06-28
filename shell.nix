let
  pkgs = import <nixpkgs> {};
in pkgs.mkShell {
  packages = [
    (pkgs.python311.withPackages (python-pkgs: [
      python-pkgs.python-dotenv
      python-pkgs.spotipy
    ]))
  ];
}
