def maybe_schedule(s: int | float | timedelta | BaseSchedule, relative: bool, app: Celery | None) -> float | timedelta | BaseSchedule:
    return f'maybe_schedule result'