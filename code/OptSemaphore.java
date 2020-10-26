import java.util.concurrent.Semaphore;

public class OptSemaphore {

    OptAQS aqs = new OptAQS() {

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

            int count = getState().get();
            int n = count - 1;


            // int n =  
            return 0;
        }

        @Override
        public boolean tryReleaseShared() {
            return getState().incrementAndGet() >= 0;
        }

    };

    public OptSemaphore(int permits){
        aqs.getState().set(permits);
    }

    public void acquire() {
        aqs.acquireShared();
    }

    public void release() {
        aqs.releaseShared();
    }

}
