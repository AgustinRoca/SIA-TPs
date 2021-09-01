package criteria;

public class TimeStopCriteria implements StopCriteria{
    private final long maxTime;

    public TimeStopCriteria(long maxTime) {
        this.maxTime = maxTime;
    }

    @Override
    public boolean shouldStop(StopCriteriaData data) {
        return System.currentTimeMillis() - data.getStartTime() > maxTime;
    }
}
