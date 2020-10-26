import java.lang.System;
import java.lang.reflect.Field;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.DoubleAdder;
import java.util.concurrent.atomic.LongAdder;
import java.util.concurrent.locks.Lock;

import sun.misc.Unsafe;

public class Demo {

    // // volatile int i = 0;
    // // AtomicInteger i = new AtomicInteger(0);
    // private LongAdder longAdder = new LongAdder();
    // volatile long i = 0;

    // static Unsafe unsafe;

    // // private static long valueOffset;

    // // static {
    // // try {
    // // Field field = Unsafe.class.getDeclaredField("theUnsafe");
    // // field.setAccessible(true);
    // // unsafe = (Unsafe) field.get(null);

    // // // 偏移量 offset 用于定位内存地址
    // // valueOffset = unsafe.objectFieldOffset(Demo.class.getDeclaredField("i"));
    // // } catch (Exception ex) {

    // // }
    // // }

    // public void add() {

    // // int current;
    // // do {
    // // // 根据偏移量获得要更改的值, 这部分逻辑可以被更复杂的业务替换
    // // current = unsafe.getIntVolatile(this, valueOffset);
    // // } while (!unsafe.compareAndSwapInt(this, valueOffset, current, current +
    // 1)); // 更新失败说明被其他线程影响了, 需要重做业务

    // // synchronized (this) {

    // // this.i++;
    // // }

    // // longAdder.add(i);
    // longAdder.increment();

    // // i.incrementAndGet();
    // }

    // public static void main(String[] args) throws InterruptedException {

    // Demo demo = new Demo();

    // for (int k = 0; k < 2; k++) {
    // new Thread(() -> {
    // for (int j = 0; j < 10000; j++) {
    // demo.add();

    // }
    // }).start();
    // }

    // Thread.sleep(2000L);

    // demo.i = demo.longAdder.sum();

    // System.out.println(demo.i);
    // }

    // int i = 0;
    // Lock lock = new OptLock();

    // public void add() {
    // lock.lock();
    // try {
    // i++;
    // } finally {
    // lock.unlock();
    // }
    // }

    // public static void main(String[] args) throws InterruptedException {
    // Demo demo = new Demo();
    // for (int k = 0; k < 4; k++) {
    // new Thread(() -> {
    // for (int j = 0; j < 10000; j++)
    // demo.add();
    // }).start();
    // }

    // Thread.sleep(2000L);

    // System.out.println(demo.i);
    // }

    public static void main(String[] args) throws InterruptedException {
        int N = 5;
        OptCDL cdl = new OptCDL(N);

        for (int i = 0; i < N - 1; i++) {

            new Thread(() -> {
                System.out.println("start");
                cdl.countDown();
                cdl.await();
                System.out.println(Thread.currentThread());
            }).start();

        }

        Thread.sleep(2000L);

        new Thread(() -> {
            System.out.println("Last one start");
            cdl.countDown();
            System.out.println("Last one end");
        }).start();
    }

}