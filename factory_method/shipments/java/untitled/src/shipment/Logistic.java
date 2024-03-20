package shipment;

import interfaces.Transport;

public abstract class Logistic {

    public void planDelivery() {
        Transport transport = this.createTransport();
        System.out.println(transport.delivery());
    }

    public abstract Transport createTransport();
}
