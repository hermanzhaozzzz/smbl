import smbl
import snakemake
import os

import __program

GEM_INDEXER = __program.get_bin_file_path("gem-indexer")
GEM_MAPPER  = __program.get_bin_file_path("gem-mapper")
GEM_2_SAM   = __program.get_bin_file_path("gem-2-sam")


##########################################
##########################################


class Gem(__program.Program):
	@classmethod
	def get_installation_files(cls):
		return [
			GEM_INDEXER,
			GEM_MAPPER,
			GEM_2_SAM,
		]

	@classmethod
	def install(cls):
		if smbl.is_linux() and smbl.is_os_64bit():
			fn=cls.download_file("http://sourceforge.net/projects/gemlibrary/files/gem-library/Binary%20pre-release%203/GEM-binaries-Linux-x86_64-core_i3-20130406-045632.tbz2/download","gem.tbz2")
		else:
			raise NotImplementedError("Unsupported OS")

		dir=cls.extract_tar(fn,strip=2)


		cls.install_file("gem-indexer",GEM_INDEXER)
		cls.install_file("gem-mapper",GEM_MAPPER)
		cls.install_file("gem-2-sam",GEM_2_SAM)

	@classmethod
	def supported_platforms(cls):
		return ["linux"]
