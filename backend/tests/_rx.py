import reactivex as rx
from reactivex.scheduler.scheduler import Scheduler
from typing import Optional


class GetLojas:
    def __call__(self, observer: rx.Observer, scheduler: Optional[Scheduler]):
        observer.on_next([1, 2, 3, 4, 5])

        observer.on_completed()


class GetValue:
    def __call__(self, value):
        print("Received {0}".format(value))


class ErrorOnGetValue:
    def __call__(self, value):
        print("Error Occurred: {0}".format(value))


class CompletedOnGetValue:
    def __call__(self):
        print("Done!")


class Main:
    def __init__(self):
        self.get_value = GetValue()
        self.error_on_get_value = ErrorOnGetValue()
        self.completed_on_get_value = CompletedOnGetValue()

    def handle(self):
        observable = GetLojas()
        rx.create(observable).subscribe(  # type: ignore
            on_next=self.get_value,
            on_error=self.error_on_get_value,
            on_completed=self.completed_on_get_value,
        )


main = Main()

main.handle()
