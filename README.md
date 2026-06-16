# وكيل التعلم والتطوير الذاتي (Self-Evolving AI Agent)

هذا الوكيل مصمم ليعمل بشكل مستقل على GitHub Actions، حيث يقوم بالبحث في الإنترنت، تعلم مفاهيم جديدة، وتحديث الكود الخاص به أو ذاكرته تلقائياً.

## المميزات
*   **عقل ذكي**: يستخدم Groq LLaMA 3 70B لاتخاذ القرارات.
*   **بحث حقيقي**: يستخدم DuckDuckGo للوصول إلى أحدث المعلومات على الإنترنت.
*   **ذاكرة مستمرة**: يخزن ما يتعلمه في ملفات JSON داخل المستودع.
*   **تطوير ذاتي**: يمكنه تعديل الكود الخاص به لتحسين أدائه.
*   **أتمتة كاملة**: يعمل كل 6 ساعات عبر GitHub Actions.

## كيفية الإعداد
1.  قم بإنشاء مستودع (Repository) جديد على GitHub.
2.  ارفع ملفات المجلد `self_evolving_agent` إلى المستودع.
3.  اذهب إلى إعدادات المستودع (Settings) -> Secrets and variables -> Actions.
4.  أضف Secret جديد باسم `GROQ_API_KEY` وضع فيه مفتاح API الخاص بك من [Groq Console](https://console.groq.com/).
5.  تأكد من تفعيل صلاحيات الكتابة لـ GitHub Actions:
    *   Settings -> Actions -> General -> Workflow permissions -> اختر **Read and write permissions**.

## هيكل المشروع
*   `core.py`: المحرك الأساسي للوكيل.
*   `self_improvement.py`: المسؤول عن تحديث كود الوكيل.
*   `workflow.yml`: ملف تعريف GitHub Actions (يجب وضعه في `.github/workflows/`).
*   `memory/`: مجلد تخزين المعلومات المكتسبة.
