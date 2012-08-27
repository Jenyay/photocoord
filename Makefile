all:

win:
	cd src && python setup_win.py build
	copy lib\\*.* build\\photocoord_win
	cd build\\photocoord_win && 7z a ..\\photocoord_win.zip .\\* -aoa

script:
	cd src && 7z a ../build/photocoord_src.zip EXIF.py photocoord.py -aoa
