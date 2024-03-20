package shipment;

import interfaces.Transport;
import transports.Ship;

public class SeaLogistic extends Logistic{
    @Override
    public Transport createTransport() {
        return new Ship();
    }
}
