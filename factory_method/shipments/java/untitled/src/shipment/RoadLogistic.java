package shipment;

import interfaces.Transport;
import transports.Truck;

public class RoadLogistic extends Logistic{
    @Override
    public Transport createTransport() {
        return new Truck();
    }
}
