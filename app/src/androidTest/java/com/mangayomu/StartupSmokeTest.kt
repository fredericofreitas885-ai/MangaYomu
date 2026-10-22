package com.mangayomu

import android.os.SystemClock
import androidx.lifecycle.Lifecycle
import androidx.test.ext.junit.rules.ActivityScenarioRule
import org.junit.Assert.assertEquals
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith
import androidx.test.ext.junit.runners.AndroidJUnit4

@RunWith(AndroidJUnit4::class)
class StartupSmokeTest {
    @get:Rule
    val activityRule = ActivityScenarioRule(MainActivity::class.java)

    @Test
    fun mainActivityStaysResumedAfterStartup() {
        assertActivityResumed()

        // Check again after the first-render effects and startup work begin.
        SystemClock.sleep(1500)
        assertActivityResumed()
    }

    private fun assertActivityResumed() {
        activityRule.scenario.onActivity { activity ->
            assertEquals(Lifecycle.State.RESUMED, activity.lifecycle.currentState)
        }
    }
}
