public class Producer implements Runnable {

    private Queue q;
    public Producer(Queue q, String name) {
        this.q = q;
        Thread producer = new Thread(this, name);
        producer.start();
    }
    @Override
    // как реализовано помещение значения в очередь (учитана случайность разов-помещения_значения: от 1 до 3)
    public void run() {
        while (true) {
            try {
                int r = (int) (Math.random() * 3) + 1; //случайное число от 1 до 3 - сколько будет произведено значений
                for (int i = 1; i <= r; i++) {//повторить r раз:
                    int number = (int) (Math.random() * 10) + 1;// создаём случайное число int number от 1 до 10, это как раз производимое значение-приоритет
                    q.insert(number);
                }
                Thread.sleep(200);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
    }
}
