import java.util.Iterator;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;
import java.util.concurrent.locks.LockSupport;

public class OptFutureTask<T> implements Runnable, Future {

    Callable<T> callable;
    T result = null;
    volatile String state = "NEW";
    volatile LinkedBlockingQueue<Thread> waiters = new LinkedBlockingQueue<>();

    public OptFutureTask(Callable<T> callable) {
        this.callable = callable;
    }

    @Override
    public boolean cancel(boolean mayInterruptIfRunning) {
        // TODO Auto-generated method stub
        return false;
    }

    @Override
    public boolean isCancelled() {
        // TODO Auto-generated method stub
        return false;
    }

    @Override
    public boolean isDone() {
        // TODO Auto-generated method stub
        return false;
    }

    @Override
    public T get() throws InterruptedException, ExecutionException {
        while(!"END".equals(state)){
            waiters.offer(Thread.currentThread());
            LockSupport.park();
        }
        waiters.remove(Thread.currentThread());
        return result;
    }

    @Override
    public Object get(long timeout, TimeUnit unit) throws InterruptedException, ExecutionException, TimeoutException {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public void run() {
        try {
            result = callable.call();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            state = "END";
        }

        Iterator<Thread> iterator = waiters.iterator();

        while(iterator.hasNext()){
            LockSupport.unpark(iterator.next());
        }
    }

}
