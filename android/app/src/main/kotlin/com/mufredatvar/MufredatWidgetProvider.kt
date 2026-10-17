package com.mufredatvar

import android.app.PendingIntent
import android.appwidget.AppWidgetManager
import android.content.Context
import android.content.Intent
import android.content.SharedPreferences
import android.util.Log
import android.widget.RemoteViews
import es.antonborri.home_widget.HomeWidgetProvider

class MufredatWidgetProvider : HomeWidgetProvider() {
    override fun onUpdate(
        context: Context,
        appWidgetManager: AppWidgetManager,
        appWidgetIds: IntArray,
        widgetData: SharedPreferences
    ) {
        try {
            appWidgetIds.forEach { widgetId ->
                val views = RemoteViews(context.packageName, R.layout.widget_layout).apply {
                    val teacherName = widgetData.getString("teacher_name", "") ?: ""
                    val gradeTitle = widgetData.getString("grade_title", "7. SINIF MATEMATİK") ?: "7. SINIF MATEMATİK"
                    val weekInfo = widgetData.getString("week_info", "6. Hafta • 13-17 Ekim") ?: "6. Hafta • 13-17 Ekim"
                    val theme = widgetData.getString("theme_name", "Tema: Sayılar ve Nicelikler") ?: "Tema: Sayılar ve Nicelikler"
                    val outcomeCode = widgetData.getString("outcome_code", "MAT.7.1.3") ?: "MAT.7.1.3"
                    val outcomeDesc = widgetData.getString("outcome_desc", "Rasyonel sayıları sıralar ve karşılaştırır.") ?: "Rasyonel sayıları sıralar ve karşılaştırır."
                    val subtopic = widgetData.getString("subtopic", "Payda eşitleme, yarıma ve bütüne yakınlık stratejileriyle rasyonel sayıları sıralama.") ?: "Payda eşitleme, yarıma ve bütüne yakınlık stratejileriyle rasyonel sayıları sıralama."

                    val displayTag = if (teacherName.isNotBlank() && teacherName != "KEMAL ÖĞRETMEN") {
                        "$teacherName • $gradeTitle"
                    } else {
                        gradeTitle
                    }

                    setTextViewText(R.id.widget_grade_tag, displayTag)
                    setTextViewText(R.id.widget_week_info, weekInfo)
                    setTextViewText(R.id.widget_theme, theme)
                    setTextViewText(R.id.widget_outcome_code, outcomeCode)
                    setTextViewText(R.id.widget_outcome_desc, outcomeDesc)
                    setTextViewText(R.id.widget_subtopic, subtopic)

                    val intent = Intent(context, MainActivity::class.java).apply {
                        flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TOP
                    }
                    val pendingIntent = PendingIntent.getActivity(
                        context,
                        0,
                        intent,
                        PendingIntent.FLAG_UPDATE_CURRENT or PendingIntent.FLAG_IMMUTABLE
                    )
                    setOnClickPendingIntent(R.id.widget_root, pendingIntent)
                }
                appWidgetManager.updateAppWidget(widgetId, views)
            }
        } catch (e: Exception) {
            Log.e("MufredatWidget", "Error updating widget: ${e.message}", e)
        }
    }
}
