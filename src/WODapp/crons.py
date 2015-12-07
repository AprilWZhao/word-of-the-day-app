from django_cron import CronJobBase, Schedule

class WordOfTheDayJob(CronJobBase):
    RUN_EVERY_MINS = 120*12 # every day

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'WODapp.word_job'    # a unique id

    def do(self):
        pass    # do your thing here