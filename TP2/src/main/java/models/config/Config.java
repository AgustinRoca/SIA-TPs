package models.config;

public final class Config {
    private static final Config instance = new Config();

    public static Config getInstance() {
        return instance;
    }

    private String outputPath;
    private PlayerConfig playerConfig;
    private EquipmentConfig equipmentConfig;
    private MutationConfig mutationConfig;
    private CrossoverConfig crossoverConfig;
    private FillMethod fillMethod;
    private StopCriteriaConfig stopCriteriaConfig;
    private SelectionReplacementConfig selectionConfig;
    private SelectionReplacementConfig replacementConfig;
    private ProbabilisticTournamentConfig probabilisticTournamentConfig;
    private DeterministicTournamentConfig deterministicTournamentConfig;

    private BoltzmannConfig boltzmannConfig;

    public String getOutputPath() {
        return this.outputPath;
    }

    public void setOutputPath(String outputPath) {
        this.outputPath = outputPath;
    }

    public PlayerConfig getPlayerConfig() {
        return this.playerConfig;
    }

    public void setPlayerConfig(PlayerConfig playerConfig) {
        this.playerConfig = playerConfig;
    }

    public EquipmentConfig getEquipmentConfig() {
        return this.equipmentConfig;
    }

    public void setEquipmentConfig(EquipmentConfig equipmentConfig) {
        this.equipmentConfig = equipmentConfig;
    }

    public MutationConfig getMutationConfig() {
        return this.mutationConfig;
    }

    public void setMutationConfig(MutationConfig mutationConfig) {
        this.mutationConfig = mutationConfig;
    }

    public CrossoverConfig getCrossoverConfig() {
        return this.crossoverConfig;
    }

    public void setCrossoverConfig(CrossoverConfig crossoverConfig) {
        this.crossoverConfig = crossoverConfig;
    }

    public FillMethod getFillMethod() {
        return this.fillMethod;
    }

    public void setFillMethod(FillMethod fillMethod) {
        this.fillMethod = fillMethod;
    }

    public StopCriteriaConfig getStopCriteriaConfig() {
        return this.stopCriteriaConfig;
    }

    public void setStopCriteriaConfig(StopCriteriaConfig stopCriteriaConfig) {
        this.stopCriteriaConfig = stopCriteriaConfig;
    }

    public SelectionReplacementConfig getSelectionConfig() {
        return this.selectionConfig;
    }

    public void setSelectionConfig(SelectionReplacementConfig selectionConfig) {
        this.selectionConfig = selectionConfig;
    }

    public SelectionReplacementConfig getReplacementConfig() {
        return this.replacementConfig;
    }

    public void setReplacementConfig(SelectionReplacementConfig replacementConfig) {
        this.replacementConfig = replacementConfig;
    }

    public ProbabilisticTournamentConfig getProbabilisticTournamentConfig() {
        return this.probabilisticTournamentConfig;
    }

    public void setProbabilisticTournamentConfig(ProbabilisticTournamentConfig tournamentConfig) {
        this.probabilisticTournamentConfig = tournamentConfig;
    }

    public DeterministicTournamentConfig getDeterministicTournamentConfig() {
        return this.deterministicTournamentConfig;
    }

    public void setDeterministicTournamentConfig(DeterministicTournamentConfig tournamentConfig) {
        this.deterministicTournamentConfig = tournamentConfig;
    }

    public BoltzmannConfig getBoltzmannConfig() {
        return this.boltzmannConfig;
    }

    public void setBoltzmannConfig(BoltzmannConfig boltzmannConfig) {
        this.boltzmannConfig = boltzmannConfig;
    }
}
