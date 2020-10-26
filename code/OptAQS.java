import java.util.Iterator;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.AtomicReference;
import java.util.concurrent.locks.LockSupport;

public abstract class OptAQS {

    protected volatile AtomicReference<Thread> owner = new AtomicReference<>();

    protected volatile LinkedBlockingQueue<Thread> waiters = new LinkedBlockingQueue<>();

    protected volatile AtomicInteger state = new AtomicInteger(0);

    public AtomicInteger getState(){
        return state;
    }

    public void setState(AtomicInteger state){
        this.state = state;
    }

    public abstract boolean tryAcquire();

    public abstract boolean tryRelease();

    public void acquire() {
        boolean addQ = true;

        while (!tryAcquire()) {
            if (addQ) {
                waiters.offer(Thread.currentThread());
                addQ = false;
            } else {
                LockSupport.park();
            }
        }

        waiters.remove(Thread.currentThread());
    }

    public void release() {
        if (tryRelease()) {
            Iterator<Thread> iterator = waiters.iterator();

            while (iterator.hasNext()) {
                LockSupport.unpark(iterator.next());
            }
        }
    }

    // 返回资源的占用情况
    public abstract int tryAcquireShared();

    public abstract boolean tryReleaseShared();

    public void acquireShared() {
        boolean addQ = true;
        while (tryAcquireShared() < 0) {
            if (addQ) {
                waiters.offer(Thread.currentThread());
                addQ = false;
            } else {
                LockSupport.park();
            }
        }

        waiters.remove(Thread.currentThread());
    }

    public void releaseShared() {
        if (tryReleaseShared()) {
            Iterator<Thread> iterator = waiters.iterator();
            while (iterator.hasNext()){
                LockSupport.unpark(iterator.next());
            }
        }
    }
}
