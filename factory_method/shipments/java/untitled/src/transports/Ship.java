package transports;

import interfaces.Transport;

public class Ship implements Transport {
    @Override
    public String delivery() {
        return "Se ha realizado el envio por medio de un barco";
    }
}
