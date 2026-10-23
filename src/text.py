WELCOME = f"""
    <h1 align="right">سلام به RichFormatterBot خوش آمدید! 👋</h1>

    <p align="right">متن یا کدهای HTML خود را ارسال کنید تا بلافاصله آن را به یک <b>Rich Message</b> کامل و زیبا تبدیل کنم.</p>

    <h3 align="right">📌 راهنمای سریع:</h3>
    <p align="right">
    1. متن یا کد HTML خود را بفرستید.<br>
    2. از تگ‌های پشتیبانی‌شده مثل <code>&lt;h1&gt;</code>، <code>&lt;table&gt;</code> و... استفاده کنید.<br>
    3. خروجی نهایی را پیش‌نمایش بگیرید یا فوروارد کنید!
    </p>

    <h3>🚀 از دکمه‌های پایین شروع کن</h3>
        
        <tg-button-row>
            <tg-button type="url" style="success" url="https://t.me/SI_KSH">پشتیبانی ربات</tg-button>
        </tg-button-row>
    """

HTML = """
    <h1>🌐 راهنمای قالب HTML در Rich Message</h1>
    <p>با HTML می‌تونی پیام‌هات رو بخش‌بندی و قالب‌بندی کنی. تگ‌ها رو داخل فیلد <code>html</code> بفرست و حتماً هر تگ بازشده رو ببند.</p>
    <blockquote>نکته: برای دیدن خودِ کد، تگ‌ها رو داخل <code>&lt;pre&gt;&lt;code&gt;</code> بگذار؛ برای دیدن نتیجه، همان تگ‌ها را بیرون از کد بنویس.</blockquote>

    <hr/>
    <h3>✨ قالب‌بندی متن</h3>
    <pre><code>&lt;b&gt;پر رنگ&lt;/b&gt;
&lt;i&gt;کج&lt;/i&gt;
&lt;u&gt;زیرخط&lt;/u&gt;
&lt;s&gt;خط‌خورده&lt;/s&gt;
&lt;code&gt;کد کوتاه&lt;/code&gt;
&lt;mark&gt;هایلایت&lt;/mark&gt;
&lt;tg-spoiler&gt;متن مخفی&lt;/tg-spoiler&gt;
&lt;sup&gt;بالانویس&lt;/sup&gt; و &lt;sub&gt;زیرنویس&lt;/sub&gt;</code></pre>
    <p>نتیجه: <b>پر رنگ</b>، <i>کج</i>، <u>زیرخط</u>، <s>خط‌خورده</s>، <code>کد کوتاه</code>، <mark>هایلایت</mark>، <tg-spoiler>متن مخفی</tg-spoiler>، x<sup>2</sup> و H<sub>2</sub>O</p>

    <hr/>
    <h3>🔠 عنوان‌ها</h3>
    <pre><code>&lt;h1&gt;عنوان بزرگ&lt;/h1&gt;
&lt;h2&gt;عنوان&lt;/h2&gt;
&lt;h3&gt;زیرعنوان&lt;/h3&gt;</code></pre>
    <p>عنوان‌ها برای جداکردن بخش‌های پیام استفاده می‌شن:</p>
    <h1>عنوان بزرگ</h1>
    <h2>عنوان</h2>
    <h3>زیرعنوان</h3>

    <hr/>
    <h3>🧾 فهرست‌ها</h3>
    <pre><code>&lt;ul&gt;&lt;li&gt;مورد اول&lt;/li&gt;&lt;li&gt;مورد دوم&lt;/li&gt;&lt;/ul&gt;
&lt;ol&gt;&lt;li&gt;مرحله اول&lt;/li&gt;&lt;li&gt;مرحله دوم&lt;/li&gt;&lt;/ol&gt;
&lt;ul&gt;&lt;li&gt;&lt;input type="checkbox" checked/&gt; انجام‌شده&lt;/li&gt;
&lt;li&gt;&lt;input type="checkbox"/&gt; در انتظار&lt;/li&gt;&lt;/ul&gt;</code></pre>
    <p>فهرست نامرتب:</p>
    <ul><li>مورد اول</li><li>مورد دوم</li></ul>
    <p>فهرست مرحله‌ای:</p>
    <ol><li>مرحله اول</li><li>مرحله دوم</li></ol>
    <ul><li><input type="checkbox" checked/> انجام‌شده</li><li><input type="checkbox"/> در انتظار</li></ul>

    <hr/>
    <h3>🔗 لینک و نقل‌قول</h3>
    <pre><code>&lt;a href="https://telegram.org"&gt;وب‌سایت تلگرام&lt;/a&gt;
&lt;blockquote&gt;متن نقل‌قول&lt;cite&gt;نام نویسنده&lt;/cite&gt;&lt;/blockquote&gt;
&lt;aside&gt;این بخش برای برجسته‌کردن یک نکته است.&lt;cite&gt;نکته&lt;/cite&gt;&lt;/aside&gt;</code></pre>
    <p><a href="https://telegram.org">وب‌سایت تلگرام</a></p>
    <blockquote>متن نقل‌قول<cite>نویسنده</cite></blockquote>
    <aside>این بخش برای برجسته‌کردن یک نکته است.<cite>نکته</cite></aside>

    <hr/>
    <h3>📝 ارجاع و پانوشت</h3>
    <p>برای ساخت پانوشت، به متن یک لینک داخلی بده و مقصد را با یک anchor مشخص کن:</p>
    <pre><code>متن با ارجاع &lt;a href="#note-1"&gt;[۱]&lt;/a&gt;
&lt;a name="note-1"&gt;&lt;/a&gt;
&lt;p&gt;&lt;sup&gt;۱&lt;/sup&gt; توضیح پانوشت&lt;/p&gt;</code></pre>
    <p>در این نمونه، ارجاع <a href="#note-1">[۱]</a> به توضیح پایین می‌ره.</p>
    <a name="note-1"></a><p><sup>۱</sup> این متن، نمونه‌ی پانوشت است.</p>

    <hr/>
    <h3>💻 کد</h3>
    <p>برای نمایش کد چندخطی از <code>pre</code> و <code>code</code> استفاده کن:</p>
    <pre><code>&lt;pre&gt;&lt;code class="language-python"&gt;print("سلام دنیا")&lt;/code&gt;&lt;/pre&gt;</code></pre>
    <pre><code class="language-python">print("سلام دنیا")</code></pre>

    <hr/>
    <h3>📊 جدول</h3>
    <p>هر ردیف را با <code>tr</code> و هر خانه را با <code>th</code> یا <code>td</code> بساز:</p>
                <pre><code>&lt;table bordered striped compact&gt;
    &lt;tr&gt;&lt;th&gt;زبان&lt;/th&gt;&lt;th&gt;ویژگی&lt;/th&gt;&lt;/tr&gt;
    &lt;tr&gt;&lt;td&gt;Python&lt;/td&gt;&lt;td&gt;خوانا&lt;/td&gt;&lt;/tr&gt;
&lt;/table&gt;</code></pre>
    <table bordered striped compact>
        <tr><th>کاربرد</th><th>مقادیر داخل table</th></tr>
        <tr><td>خط کشی دور جدول</td><td>bordered</td></tr>
        <tr><td>راه راه شدن هر ردیف</td><td>striped</td></tr>
        <tr><td>جدول فشرده با فاصله کمتر</td><td>compact</td></tr>
        <tr><td>هدر جدول همیشه بالای صفحه می‌ماند.</td><td>sticky-headers</td></tr>
        <tr><td>ردیف انتخاب شده برجسته می‌شود.</td><td>highlight</td></tr>
    </table>
    <p>همه مقادیر را میتوانید داخل&lt;table <mark>bordered striped compact highlight</mark>&gt; پشت سر هم دیگه بزارید تا اعمال شود.</p>

    <hr/>
    <h3>🔘 مدیریت دکمه‌ها و لینک‌ها</h3>
    <p>برای ساخت ردیف دکمه‌های شیشه‌ای و تعاملی از ساختار زیر استفاده کنید:</p>

    <pre><code>&lt;tg-button-row&gt;
        &lt;tg-button type="url" style="success" url="https://google.com"&gt;🌐 سایت گوگل&lt;/tg-button&gt;
        &lt;tg-button type="copy_text" text="متن نمونه برای کپی"&gt;📋 کپی متن&lt;/tg-button&gt;
    &lt;/tg-button-row&gt;</code></pre>

    <tg-button-row>
        <tg-button type="url" style="success" url="https://google.com">🌐 سایت گوگل</tg-button>
        <tg-button type="copy_text" text="متن نمونه برای کپی">📋 کپی متن</tg-button>
    </tg-button-row>

    <p>مقادیر ویژگی <strong>Type</strong> را به همراه کاربرد آن مشاهده کنید:</p>
    <table bordered striped compact>
        <tr><th>کاربرد</th><th>Type</th></tr>
        <tr><td>🔗 باز کردن لینک خارجی یا وب‌سایت</td><td><code>url</code></td></tr>
        <tr><td>📋 کپی کردن متن در کلیپ‌بورد</td><td><code>copy_text</code></td></tr>
    </table>

    <p>مقادیر رنگ‌بندی و <strong>Style</strong> دکمه‌ها:</p>
    <table bordered striped compact>
        <tr><th>توضیح ظاهر دکمه</th><th>Style</th></tr>
        <tr><td>🔵 دکمه آبی (اطلاعات / لینک اصلی)</td><td><code>primary</code></td></tr>
        <tr><td>🟢 دکمه سبز (تایید / موفقیت / وب‌سایت)</td><td><code>success</code></td></tr>
        <tr><td>🔴 دکمه قرمز (هشدار / حذف / خطا)</td><td><code>danger</code></td></tr>
        <tr><td>🔗 نمایش دکمه به‌شکل لینک (فقط callback)</td><td><code>link</code></td></tr>
    </table>

    <hr/>
    <h3>➗ فرمول ریاضی</h3>
    <pre><code>&lt;tg-math&gt;x^2 + y^2&lt;/tg-math&gt;
&lt;tg-math-block&gt;E = mc^2&lt;/tg-math-block&gt;</code></pre>
    <p>فرمول درون‌خطی: <tg-math>x^2 + y^2</tg-math></p>
    <tg-math-block>E = mc^2</tg-math-block>

    <hr/>
    <h3>🔽 بخش بازشونده</h3>
        <pre><code>&lt;details open&gt;
        &lt;summary&gt;عنوان بخش&lt;/summary&gt;
  متن داخل بخش
&lt;/details&gt;</code></pre>
    <details open><summary>برای دیدن نمونه باز شو</summary><p>محتوای بخش بازشونده اینجاست.</p></details>

    <hr/>
    <p>✨ حالا یکی از نمونه‌ها رو تغییر بده و در ربات امتحانش کن.</p>
"""

MEDIA = """
    <h1>🖼 راهنمای افزودن مدیا به Rich Message</h1>
    <p>برای نمایش مدیا از تگ HTML متناسب با نوع فایل استفاده کن. آدرس باید مستقیم و برای تلگرام قابل‌دسترسی باشد.</p>
    <blockquote>آدرس‌های <code>telegram.org/example</code> در این راهنما نمونه‌اند؛ برای استفاده‌ی واقعی، آن‌ها را با لینک فایل خودت عوض کن.</blockquote>

    <hr/>
    <h3>🗺️ نقشه</h3>
    <pre><code>&lt;tg-map lat="41.9" long="12.5" zoom="14"/&gt;</code></pre>
    <tg-map lat="41.9" long="12.5" zoom="14"/>

    <hr/>
    <h3>📷 عکس</h3>
    <p>از تگ <code>img</code> استفاده کن:</p>
    <pre><code>&lt;img src="https://telegram.org/example/photo.jpg"/&gt;</code></pre>
    <img src="https://telegram.org/example/photo.jpg"/>

    <hr/>
    <h3>🎬 ویدیو</h3>
    <pre><code>&lt;video src="https://telegram.org/example/video.mp4"&gt;&lt;/video&gt;</code></pre>
    <video src="https://telegram.org/example/video.mp4"></video>

    <hr/>
    <h3>🎵 فایل صوتی</h3>
    <pre><code>&lt;audio src="https://telegram.org/example/audio.mp3"&gt;&lt;/audio&gt;</code></pre>
    <audio src="https://telegram.org/example/audio.mp3"></audio>

    <hr/>
    <h3>🎙️ پیام صوتی</h3>
    <p>برای فایل OGG از تگ صوتی استفاده کن:</p>
    <pre><code>&lt;audio src="https://telegram.org/example/audio.ogg"&gt;&lt;/audio&gt;</code></pre>
    <audio src="https://telegram.org/example/audio.ogg"></audio>

    <hr/>
    <h3>🎞️ انیمیشن GIF</h3>
    <p>انیمیشن را با تگ ویدیو بفرست:</p>
    <pre><code>&lt;video src="https://telegram.org/example/animation.gif"&gt;&lt;/video&gt;</code></pre>
    <video src="https://telegram.org/example/animation.gif"></video>

    <hr/>
    <h3>📝 مدیا همراه کپشن</h3>
    <p>برای افزودن توضیح، مدیا را داخل <code>figure</code> بگذار و کپشن را در <code>figcaption</code> بنویس:</p>
        <pre><code>&lt;figure&gt;&lt;img src="https://telegram.org/example/photo.jpg"/&gt;&lt;figcaption&gt;کپشن عکس&lt;/figcaption&gt;&lt;/figure&gt;
    &lt;figure&gt;&lt;video src="https://telegram.org/example/video.mp4"&gt;&lt;/video&gt;&lt;figcaption&gt;کپشن ویدیو&lt;/figcaption&gt;&lt;/figure&gt;
    &lt;figure&gt;&lt;audio src="https://telegram.org/example/audio.mp3"&gt;&lt;/audio&gt;&lt;figcaption&gt;کپشن فایل صوتی&lt;/figcaption&gt;&lt;/figure&gt;
    &lt;figure&gt;&lt;audio src="https://telegram.org/example/audio.ogg"&gt;&lt;/audio&gt;&lt;figcaption&gt;کپشن پیام صوتی&lt;/figcaption&gt;&lt;/figure&gt;
    &lt;figure&gt;&lt;video src="https://telegram.org/example/animation.gif"&gt;&lt;/video&gt;&lt;figcaption&gt;کپشن انیمیشن&lt;/figcaption&gt;&lt;/figure&gt;</code></pre>
    <figure><img src="https://telegram.org/example/photo.jpg"/><figcaption>نمونه کپشن عکس<cite>منبع تصویر</cite></figcaption></figure>

    <hr/>
    <h3>🎞️ اسلایدشو</h3>
    <p>چند فایل را داخل <code>tg-slideshow</code> قرار بده:</p>
        <pre><code>&lt;tg-slideshow&gt;
    &lt;img src="https://telegram.org/example/photo.jpg"/&gt;
    &lt;video src="https://telegram.org/example/video.mp4"&gt;&lt;/video&gt;
    &lt;figcaption&gt;توضیح اسلایدشو&lt;/figcaption&gt;
&lt;/tg-slideshow&gt;</code></pre>
    <tg-slideshow>
      <img src="https://telegram.org/example/photo.jpg"/>
      <video src="https://telegram.org/example/video.mp4"></video>
      <figcaption>نمونه اسلایدشو<cite>راهنمای Rich Message</cite></figcaption>
    </tg-slideshow>

    <hr/>
    <p>✨ تگ را انتخاب کن، لینک فایل خودت را جایگزین کن و نتیجه را در ربات ببین.</p>
"""
