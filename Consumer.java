public class Consumer implements Runnable {

    private Queue q;

    public Consumer(Queue q, int max_value) {
        this.q = q;
        Thread consumer = new Thread(this);
        consumer.setName((max_value <= 5)? "Потребитель 1-5": "Потребитель 6-10");
        consumer.start();
    }
    @Override
    // как реализовано удаление из массива значения
    public void run() {
        while (true) {
            try {
                q.deleteMax();
                Thread.sleep(200);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
