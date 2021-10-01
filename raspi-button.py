#!/bin/bash/env python

from settings_reader import get_variable
from pattern_evaluator import compare
from gpiozero import Button
from signal import pause
import time

class ButtonCustomiser:
    # reset the default parameter
    def reset(self):
        self.pressed_since = 0
        self.idle_since = 0
        self.in_progress = False
        self.pattern = []

    # when button is pressed start progress and timer
    def pressed(self):
        self.in_progress = True
        self.pressed_since = time.time()

    # when button is released the idle timer is started and trigger the evaluation
    def released(self):
        self.idle_since = time.time()
        self.evaluate_activation()

    def evaluate_activation(self):
        # get the parameters from the config
        short_press = get_variable("TIMINGS", "short_press", "int")
        long_press = get_variable("TIMINGS", "long_press", "int")
        # calculate the time between button press and release
        time_pressed = (time.time() - self.pressed_since)*1000//1
        # based on the length, either add a _ or a . to the pattern or reset the default parameters
        if time_pressed >= long_press:
            self.pattern.append("_")
        elif time_pressed >= short_press:
            self.pattern.append(".")
        else:
            self.reset()
        # trigger the evaluation of the idle time
        self.evaluate_idle()

    def evaluate_idle(self):
        # get parameter from the config
        idle_time = get_variable("TIMINGS", "idle_time", "int")
        while True:
            # as long as there is no button press
            if not(self.trigger.is_pressed):
                # in case it is currently in progress, and idle time exceeds the parameter
                if (
                    self.in_progress and
                    (time.time() - self.idle_since)*1000//1 >= idle_time
                ):
                    # send the pattern for comparision
                    compare(self.pattern)
                    # reset parameter
                    self.reset()
                    # break out of the loop
                    break
                time.sleep(0.01)
                # continue in the loop
                continue
            # as soon as the button is pressed break out the loop
            else:
                break

    def __init__(self, channel):
        # set-up the trigger
        self.trigger = Button(channel)
        self.reset()


if __name__ == "__main__":
	# get the gpio pin
    gpio_pin = get_variable("SYSTEMVARIABLES","gpio_pin", "int")
    # initialise button
    casebutton = ButtonCustomiser(gpio_pin)
    # create triggers for pressed and released
    casebutton.trigger.when_pressed = casebutton.pressed
    casebutton.trigger.when_released = casebutton.released
    # pause until event is triggered
    pause()
