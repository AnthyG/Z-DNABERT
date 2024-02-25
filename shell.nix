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
  bash ./run.sh
  ";
}).env
