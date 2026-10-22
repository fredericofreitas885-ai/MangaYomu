package com.mangayomu

import android.os.SystemClock
import androidx.compose.ui.test.assertIsDisplayed
import androidx.compose.ui.test.junit4.createAndroidComposeRule
import androidx.compose.ui.test.onNodeWithText
import androidx.test.ext.junit.runners.AndroidJUnit4
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith

@RunWith(AndroidJUnit4::class)
class StartupSmokeTest {
    @get:Rule
    val composeRule = createAndroidComposeRule<MainActivity>()

    @Test
    fun appLaunchesAndShowsExploreScreen() {
        composeRule.waitForIdle()
        composeRule.onNodeWithText("MangaYomu").assertIsDisplayed()

        // Keep the process alive briefly so startup effects can run too.
        SystemClock.sleep(1500)
        composeRule.waitForIdle()
        composeRule.onNodeWithText("MangaYomu").assertIsDisplayed()
    }
}
