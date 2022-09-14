class ParkingSystem {
public:
    int x, y, z;
    ParkingSystem(int big, int medium, int small) {
        x = big; y = medium; z = small;
    }
    
    bool addCar(int carType) {
        bool val = false;
        switch(carType){
            case 1: if(x){
                x--;
                val = true;
            }
                break;
            case 2: if(y){
                y--;
                val = true;
            }
                break;
            case 3: if(z){
                z--;
                val = true;
            }
                break;
        }
        return val;
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */