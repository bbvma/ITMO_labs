public class Main {

    public static void main(String[] args) {
        Queue q = new Queue(10); // создали объект очереди
        //Создаём 4 потока и запускаем их (т.к. запуск прописан в конструкторе)
        Producer p1 = new Producer(q, "Производитель 1");
        Producer p2 = new Producer(q, "Производитель 2");
        Consumer c1 = new Consumer(q, 5);
        Consumer c2 = new Consumer(q, 10);
    }

}
