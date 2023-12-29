{ pkgs ? import <nixpkgs> {} }:
(pkgs.buildFHSUserEnv {
  name = "pipzone";
  targetPkgs = pkgs: (with pkgs; [
    gcc
    python310
    python310Packages.pip
    python310Packages.virtualenv
#    cudaPackages.cudatoolkit
  ]);
  runScript = "
  unset SOURCE_DATE_EPOCH
  virtualenv venv/
  source venv/bin/activate
  TMPDIR=~/tmp python -m pip install -r requirements.txt
  jupyter lab
  ";
}).env
