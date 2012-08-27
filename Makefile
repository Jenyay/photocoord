all:

win:
	cd src && python setup_win.py build
	copy lib\\*.* build\\photocoord_win
	cd build\\photocoord_win && 7z a ..\\photocoord.zip .\\* -aoa
