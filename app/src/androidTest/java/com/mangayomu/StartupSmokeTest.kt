package com.mangayomu

import android.os.SystemClock
import androidx.lifecycle.Lifecycle
import androidx.test.ext.junit.rules.ActivityScenarioRule
import androidx.test.platform.app.InstrumentationRegistry
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
        InstrumentationRegistry.getInstrumentation().waitForIdleSync()
        assertActivityResumed()

        // Check again after first-render effects and startup network work begin.
        SystemClock.sleep(1500)
        InstrumentationRegistry.getInstrumentation().waitForIdleSync()
        assertActivityResumed()
    }

    private fun assertActivityResumed() {
        activityRule.scenario.onActivity { activity ->
            assertEquals(Lifecycle.State.RESUMED, activity.lifecycle.currentState)
        }
    }
}
