import java.util.concurrent.atomic.AtomicInteger;

public class OptCDL {
    OptAQS aqs = new OptAQS(){

        @Override
        public boolean tryAcquire() {
            // TODO Auto-generated method stub
            return false;
        }

        @Override
        public boolean tryRelease() {
            // TODO Auto-generated method stub
            return false;
        }

        @Override
        public int tryAcquireShared() {
            return this.getState().get() == 0 ? 1 : -1;
        }

        @Override
        public boolean tryReleaseShared() {
            return this.getState().decrementAndGet() == 0;
        }
        
    };

    public OptCDL(int count) {
        aqs.setState(new AtomicInteger(count));        
    }

    public void await(){
        aqs.acquireShared();
    }

    public void countDown(){
        aqs.releaseShared();
    }
}
