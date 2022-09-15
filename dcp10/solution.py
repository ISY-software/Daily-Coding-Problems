#!/bin/python3
#-*- encoding: utf-8 -*-
import threading
import time

def executer (job,t):
    time.sleep(t)
    job()

def jobScheduler(job, time):
    thr = threading.Thread(target=executer, args=(job,time))
    print('Sheduler', time )
    thr.start()

def testP():
    print('Test P')



jobScheduler(testP,2)
jobScheduler(testP,3)
jobScheduler(testP,4)
