from .adherence import Adherence


class AdherenceStageOne(Adherence):
    """Adherence CRF completed at baseline (in-person)."""

    class Meta:
        proxy = True
        verbose_name = "Adherence (Baseline)"
        verbose_name_plural = "Adherence (Baseline)"


class AdherenceStageTwo(Adherence):
    """Adherence CRF completed at d3 and d9 (telephone)."""

    class Meta:
        proxy = True
        verbose_name = "Adherence (Day 3 & Day 9)"
        verbose_name_plural = "Adherence (Day 3 & Day 9)"


class AdherenceStageThree(Adherence):
    """Adherence CRF completed at d14 (in-person)."""

    class Meta:
        proxy = True
        verbose_name = "Adherence (Day 14)"
        verbose_name_plural = "Adherence (Day 14)"


class AdherenceStageFour(Adherence):
    """Adherence CRF completed on or after w4 (telephone)."""

    class Meta:
        proxy = True
        verbose_name = "Adherence (Week 4+)"
        verbose_name_plural = "Adherence (Week 4+)"
