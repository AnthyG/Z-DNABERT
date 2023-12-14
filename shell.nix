{ pkgs ? import <nixpkgs> {} }:
(pkgs.buildFHSUserEnv {
  name = "pipzone";
  targetPkgs = pkgs: (with pkgs; [
    python310
    python310Packages.pip
    python310Packages.virtualenv
    cudaPackages.cudatoolkit
  ]);
  runScript = "
  virtualenv venv/
  source venv/bin/activate
  pip install -r requirements.txt
  jupyter lab
  ";
}).env
