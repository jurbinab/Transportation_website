from django.shortcuts import HttpResponse
from Transport.models import vehicle, vehicle_live

def index(request,vehi,lat,lon):
    try :
        temp_veh = vehicle.objects.get(vehicle_name=vehi)
        #temp_veh = get_object_or_404(vehicle,vehicle_name=vehicle)
        temp_veh_liv = vehicle_live()
        temp_veh_liv.vehicle = temp_veh
        temp_veh_liv.lon_pos = lon
        temp_veh_liv.lat_pos = lat
        temp_veh_liv.save()

        return HttpResponse("<h3>"+vehi+" @</br>lat: "+lat+"</br>lon: "+lon+"</h3>")
    except :
        return HttpResponse("<h1>Bloody Fool...first,know how many buses you have in total!!</h1>")