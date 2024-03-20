import shipment.Logistic;
import shipment.RoadLogistic;
import shipment.SeaLogistic;

public class Main {
    public static void main(String[] args) {
        Logistic logistic = new RoadLogistic();
        logistic.planDelivery();

        logistic = new SeaLogistic();
        logistic.planDelivery();
    }
}