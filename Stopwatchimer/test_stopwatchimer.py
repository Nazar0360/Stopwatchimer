def test_stopwatch():
    from Stopwatchimer import Stopwatch
    from time import sleep
    print('The stopwatch test:')
    s = Stopwatch(round_time=0)
    assert s.time == 0
    print('Waiting 1 second')
    sleep(1)
    print('The stopwatch time:', s.pause_stopwatch())
    assert s.time == 1
    print('The stopwatch paused')
    print('Waiting 1 second')
    sleep(1)
    print('The stopwatch time:', s.pause_stopwatch())
    assert s.time == 1
    s.resume_stopwatch()
    print('The stopwatch was resumed')
    print('The stopwatch time:', s.time)
    assert s.time == 1
    print('Waiting 1 second')
    sleep(1)
    print('The stopwatch time:', s.pause_stopwatch())
    assert s.time == 2
    print('The stopwatch paused')
    print('Waiting 1 second')
    sleep(1)
    print('The stopwatch time:', s.pause_stopwatch())
    assert s.time == 2
    s.resume_stopwatch()
    print('The stopwatch was resumed')
    print('The stopwatch time:', s.time)
    assert s.time == 2
    s.start_stopwatch()
    assert s.time == 0
    print('The stopwatch restarted')
    print('Waiting 1 second')
    sleep(1)
    print('The stopwatch time:', s.pause_stopwatch())
    assert s.time == 1
    print('The stopwatch paused')
    print('Waiting 1 second')
    sleep(1)
    print('The stopwatch time:', s.pause_stopwatch())
    assert s.time == 1
    s.resume_stopwatch()
    print('The stopwatch was resumed')
    assert s.time == 1
    print('The stopwatch time:', s.time)
    print('Waiting 1 second')
    sleep(1)
    print('The stopwatch time:', s.pause_stopwatch())
    assert s.time == 2
    print('The stopwatch paused')
    print('Waiting 1 second')
    sleep(1)
    print('The stopwatch time:', s.pause_stopwatch())
    assert s.time == 2
    s.resume_stopwatch()
    print('The stopwatch was resumed')
    print('The stopwatch time:', s.time)
    assert s.time == 2
    s.time = 5
    print('The stopwatch time is set to 5')
    print('The stopwatch time:', s.time)
    assert s.time == 5
    print('Waiting 1 second')
    sleep(1)
    print('The stopwatch time:', s.pause_stopwatch())
    assert s.time == 6
    print('The stopwatch paused')
    print('Waiting 1 second')
    sleep(1)
    print('The stopwatch time:', s.pause_stopwatch())
    assert s.time == 6
    s.resume_stopwatch()
    print('The stopwatch was resumed')
    print('The stopwatch time:', s.time)
    assert s.time == 6
    print('Waiting 1 second')
    sleep(1)
    print('The stopwatch time:', s.pause_stopwatch())
    assert s.time == 7
    print('The stopwatch paused')
    print('Waiting 1 second')
    sleep(1)
    print('The stopwatch time:', s.pause_stopwatch())
    assert s.time == 7
    s.resume_stopwatch()
    print('The stopwatch was resumed')
    print('The stopwatch time:', s.time)
    assert s.time == 7
    assert s.name == 'Stopwatch'
    s.name = 'StW'
    print('The stopwatch name has been set to StW')
    assert s.name == 'StW'
    print('Creating stopwatches with names: None, None, \'s\', \'s\', \'secret\'')
    s1, s2, s3, s4, s5 = Stopwatch(), Stopwatch(), Stopwatch('s'), Stopwatch('s'), Stopwatch('secret')
    print('Stopwatches:', Stopwatch.get_stopwatches())
    assert list(Stopwatch.get_stopwatches().keys()) == ['[0]StW', '[0]Stopwatch', '[1]Stopwatch', '[0]s', '[1]s']
    print('Stopwatches with name "Stopwatch":', Stopwatch.get_stopwatches('Stopwatch'))
    assert Stopwatch.get_stopwatches('Stopwatch') == [s1, s2]
    print('Stopwatches with name "s":', Stopwatch.get_stopwatches('s'))
    assert Stopwatch.get_stopwatches('s') == [s3, s4]
    print('Stopwatches with name index 0:', Stopwatch.get_stopwatches(name_index=0))
    assert Stopwatch.get_stopwatches(name_index=0) == [s, s1, s3]
    print('Stopwatches with name index 1:', Stopwatch.get_stopwatches(name_index=1))
    assert Stopwatch.get_stopwatches(name_index=1) == [s2, s4]
    print('Stopwatches with name "s" name index 1:', Stopwatch.get_stopwatches('s', name_index=1))
    assert Stopwatch.get_stopwatches('s', name_index=1) == s4


def test_timer():
    from Stopwatchimer import Timer
    from time import sleep
    print('The timer test:')
    t = Timer(3)
    assert t.timer_time == 3
    print('Timer is set to 3 seconds')
    print('Waiting 1 second')
    sleep(1)
    print('The timer is over:', t.is_over)
    assert not t.is_over
    print('The rest of the timer time:', t.rest_time)
    assert round(t.rest_time) == 3
    t.start_timer()
    print('The timer has started')
    print('Waiting 1 second')
    sleep(1)
    print('The timer is over:', t.is_over)
    assert not t.is_over
    print('The rest of the timer time:', t.rest_time)
    assert round(t.rest_time) == 2
    print('Waiting 1 second')
    sleep(1)
    print('The timer is over:', t.is_over)
    assert not t.is_over
    print('The rest of the timer time:', t.rest_time)
    assert round(t.rest_time) == 1
    print('Waiting 1 second')
    sleep(1)
    print('The timer is over:', t.is_over)
    assert t.is_over
    print('The rest of the timer time:', t.rest_time)
    assert round(t.rest_time) == 0
    t.start_timer()
    assert round(t.rest_time) == 3
    assert not t.is_over
    print('The timer has restarted')
    print('Waiting 1 second')
    sleep(1)
    print('The timer is over:', t.is_over)
    assert not t.is_over
    print('The rest of the timer time:', t.rest_time)
    assert round(t.rest_time) == 2
    t.pause_timer()
    print('The timer has paused')
    print('Waiting 1 second')
    sleep(1)
    print('The timer is over:', t.is_over)
    assert not t.is_over
    print('The rest of the timer time:', t.rest_time)
    assert round(t.rest_time) == 2
    t.resume_timer()
    print('The timer has resumed')
    print('Waiting 1 second')
    sleep(1)
    print('The timer is over:', t.is_over)
    assert not t.is_over
    print('The rest of the timer time:', t.rest_time)
    assert round(t.rest_time) == 1
    print('Waiting 1 second')
    sleep(1)
    print('The timer is over:', t.is_over)
    assert t.is_over
    print('The rest of the timer time:', t.rest_time)
    assert round(t.rest_time) == 0
    print('The timer time:', t.timer_time)
    t.modify_timer_time(2)
    print('The timer time has modified by 2')
    print('The timer time:', t.timer_time)
    assert round(t.timer_time) == 5
    print('Waiting 1 second')
    sleep(1)
    print('The timer is over:', t.is_over)
    assert not t.is_over
    print('The rest of the timer time:', t.rest_time)
    assert round(t.rest_time) == 1
    print('Waiting 1 second')
    sleep(1)
    print('The timer is over:', t.is_over)
    assert t.is_over
    print('The rest of the timer time:', t.rest_time)
    assert round(t.rest_time) == 0
    t.timer_time = 8
    print('The timer time has been set to 8')
    assert round(t.timer_time) == 8
    print('The timer time:', t.timer_time)
    assert round(t.rest_time) == 3
    print('Waiting 1 second')
    sleep(1)
    print('The timer is over:', t.is_over)
    assert not t.is_over
    print('The rest of the timer time:', t.rest_time)
    assert round(t.rest_time) == 2
    print('Waiting 1 second')
    sleep(1)
    print('The timer is over:', t.is_over)
    assert not t.is_over
    print('The rest of the timer time:', t.rest_time)
    assert round(t.rest_time) == 1
    print('Waiting 1 second')
    sleep(1)
    print('The timer is over:', t.is_over)
    assert t.is_over
    print('The rest of the timer time:', t.rest_time)
    assert round(t.rest_time) == 0
    assert t.name == 'Timer'
    t.name = 'T'
    print('The timer name has been set to T')
    assert t.name == 'T'
    print('Creating timers with names: None, None, \'t\', \'t\', \'secret\'')
    t1, t2, t3, t4, t5 = Timer(1), Timer(1), Timer(1, 't'), Timer(1, 't'), Timer(1, 'secret')
    print('Timers:', Timer.get_timers())
    assert list(Timer.get_timers().keys()) == ['[0]T', '[0]Timer', '[1]Timer', '[0]t', '[1]t']
    print('Timers with name "Timer":', Timer.get_timers('Timer'))
    assert Timer.get_timers('Timer') == [t1, t2]
    print('Timers with name "t":', Timer.get_timers('t'))
    assert Timer.get_timers('t') == [t3, t4]
    print('Timers with name index 0:', Timer.get_timers(name_index=0))
    assert Timer.get_timers(name_index=0) == [t, t1, t3]
    print('Timers with name index 1:', Timer.get_timers(name_index=1))
    assert Timer.get_timers(name_index=1) == [t2, t4]
    print('Timers with name "t" name index 1:', Timer.get_timers('t', name_index=1))
    assert Timer.get_timers('t', name_index=1) == t4
