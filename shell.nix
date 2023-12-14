with import <nixpkgs> {};
with pkgs;

mkShell {
	buildInputs = [
  		curl

		# Defines a python + set of packages.
		(python3.withPackages (ps: with ps; with python3Packages; [
			jupyter
			ipython
			#torch
			#torchWithCuda
			pytorch
			#pytorchWithCuda
			transformers
			numpy
			io
			biopython
			tqdm
			scipy
		]))
	];

	# Automatically run jupyter when entering the shell.
	shellHook = "jupyter notebook";
}
