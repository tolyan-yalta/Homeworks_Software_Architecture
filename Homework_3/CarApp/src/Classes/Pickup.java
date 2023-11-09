package CarApp.src.Classes;

import CarApp.src.Enumerators.TypeCar;
import CarApp.src.Enumerators.TypeFuel;
import CarApp.src.Enumerators.TypeGearBox;
import CarApp.src.Interfaces.ICarWash;
import CarApp.src.Interfaces.IFuelStation;

import java.awt.*;

public class Pickup extends Car implements IFuelStation, ICarWash {
    
    private int loadCap;

    public Pickup(String make, String model,
                  int numberWheels, TypeFuel fuelType, TypeGearBox gearBoxType,
                  Color bodyColor, int engineCap, int loadCap) {

        super(make, model, TypeCar.PICKUP, numberWheels, fuelType, gearBoxType, bodyColor, engineCap);

        this.loadCap = loadCap;

    }

    @Override
    public void fuel() {

    }

    @Override
    public void wipWindshield() {

    }

    @Override
    public void wipHeadlights() {

    }

    @Override
    public void wipMirrors() {

    }
}
