python .\\modifySpeedLimit.py
python .\\randomTrips.py -n custom.net.xml -r custom.routes.xml -l --begin 0 --end 800 --period 2 --min-distance 380
cp custom.routes.xml .\\20\\custom_20.routes.xml
cp custom.routes.xml .\\30\\custom_30.routes.xml
cp custom.routes.xml .\\40\\custom_40.routes.xml
cp custom.routes.xml .\\50\\custom_50.routes.xml
cp custom.routes.xml .\\60\\custom_60.routes.xml
cp custom.routes.xml .\\70\\custom_70.routes.xml