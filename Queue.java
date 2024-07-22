import java.util.concurrent.locks.ReentrantLock;
import java.util.concurrent.locks.Condition;

public class Queue implements PriorityQueue{
    int [] array; //массив, хранящий значения-приоритеты
    ReentrantLock locker;
    Condition not_full, not_empty, condition_1_5, condition_6_10; //4 условия
    int cnt = 0; // количество значений в очереди, которое будет иногда играть роль индекса в массиве

    public Queue(int n) {
        array = new int[n];// при создании объекта очереди, мы инициализируем массив, хранящий значения-приоритеты
        locker = new ReentrantLock(); // создаем блокировку
        not_full = locker.newCondition(); // получаем условия, связанные с блокировкой
        not_empty = locker.newCondition();
        condition_1_5 = locker.newCondition();
        condition_6_10 = locker.newCondition();
    }

    public void insert(int val) throws InterruptedException {
        locker.lock(); //синхронизация
        try{
            while (full())
                not_full.await(); // пока очередь заполнена, производить и помещать значения нельзя, ожидаем
            //помещаем значение в очередь:
            int index = cnt;
            array[cnt++] = val;
            while (index > 0 && array[index] > array[(index - 1)/2]) {
                int parent = (index - 1)/2;
                change(index,parent);
                index = parent;
            }
            System.out.println(Thread.currentThread().getName() + " добавил " + val);
            print_queue();

            condition_1_5.signalAll();
            condition_6_10.signalAll();
            not_empty.signalAll(); // возобновляем все потоки: когда добавилось значение, говорим остановленным потокам, что теперь можно удалять значения
        } finally {
            locker.unlock();
        }
    }

    public void change(int index, int parent) {
        int temp = array[index];
        array[index] = array[parent];
        array[parent] = temp;
    }

    public int deleteMax() throws InterruptedException {
        locker.lock(); //синхронизация
        try{
            while (empty())
                not_empty.await(); //очередь пуста, не можем потреблять значения
            if (Thread.currentThread().getName().equals("Потребитель 1-5")) { //если поток потребляет значения 1-5
                while (array[0] > 5) { //а максимальное значение этот поток потребить не может
                    condition_1_5.signalAll();
                    condition_6_10.await();
                }
            }
            else {   	  //если поток потребляет значения 6-10
                while (array[0] <= 5) { //а максимальное значение этот поток потребить не может
                    condition_6_10.signalAll(); //то тормозим этот поток
                    condition_1_5.await();
                }
            }
            int maximum = array[0];
            //сохраняем максимальное значение, помещаем в верхушку дерева самое нижнее правое значение
            cnt--; // переместили последнее значение наверх => кол-во значений уменьшилось на 1
            array[0] = array[cnt];

            int index = 0;
            while (index < (cnt - 1)/2) {
                int left_son = index*2 + 1;
                int right_son = index*2 + 2;
                int biggest_son = left_son;
                if (right_son < cnt && array[right_son] > array[left_son])
                    biggest_son = right_son;
                if (array[index] < array[biggest_son]) {
                    change(index,biggest_son);
                    index = biggest_son;
                }
                else
                    break;
            }
            System.out.println(Thread.currentThread().getName() + " удалил " + maximum);
            print_queue();
            not_full.signalAll(); //после всех действий значение точно удалено, значит потоки, которые были остановлены вследствие заполненной очереди, могут работать дальше
            return maximum;
        } finally {
            locker.unlock();
        }
    }

    private void print_queue(){
        System.out.print("Очередь: ");
        for(int i = 0; i < cnt; ++i)
            System.out.print(array[i] + " ");
        System.out.println();
        System.out.println();
    }

    public boolean full() { //метод проверки полноты очереди
        return cnt == 10;
    }
    public boolean empty() { //метод проверки пустоты очереди
        return cnt == 0;
    }
}
