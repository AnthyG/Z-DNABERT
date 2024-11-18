{ pkgs ? import <nixpkgs> {} }:
(pkgs.buildFHSUserEnv {
  name = "pipzone";
  targetPkgs = pkgs: (with pkgs; [
    gcc
    python311
    python311Packages.pip
    python311Packages.virtualenv
#    cudaPackages.cudatoolkit
  ]);
  runScript = "
  bash ./run.sh
  ";
}).env
