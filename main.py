import urllib.request
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from functools import partial

Window.clearcolor = get_color_from_hex("#0d1117")

class ThamerTVApp(App):
    def build(self):
        self.title = "THAMER.ABUMUSTFA TV"
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        header = BoxLayout(orientation='vertical', size_hint_y=0.15, padding=5)
        title_label = Label(text="THAMER.ABUMUSTFA", font_size='28sp', bold=True, color=get_color_from_hex("#58a6ff"))
        subtitle_label = Label(text="نظام البث الرقمي الذكي للموبايل والشاشات السمارت", font_size='14sp', color=get_color_from_hex("#8b949e"))
        header.add_widget(title_label)
        header.add_widget(subtitle_label)
        main_layout.add_widget(header)
        
        self.status_label = Label(text="📺 اختر باقة أو قناة لبدء البث الآمن...", size_hint_y=0.1, font_size='16sp', color=get_color_from_hex("#39d353"))
        main_layout.add_widget(self.status_label)
        
        scroll_view = ScrollView(size_hint_y=0.75)
        grid_layout = GridLayout(cols=1, spacing=15, size_hint_y=None)
        grid_layout.bind(minimum_height=grid_layout.setter('height'))
        
        packages = {
            "⚽ باقة قنوات BEIN SPORT الرياضية": [
                {"name": "beIN Sports HD1", "url": "http://example.com/bein1.m3u8"},
                {"name": "beIN Sports HD2", "url": "http://example.com/bein2.m3u8"},
                {"name": "beIN Sports HD3", "url": "http://example.com/bein3.m3u8"}
            ],
            "🛰️ باقة قنوات قمر نايل سات (NileSat)": [
                {"name": "MBC 1", "url": "http://example.com/mbc1.m3u8"},
                {"name": "Al Arabiya", "url": "http://example.com/arabiya.m3u8"},
                {"name": "القرآن الكريم مباشر", "url": "http://example.com/quran.m3u8"}
            ],
            "🌍 باقة القنوات العربية والدولية": [
                {"name": "القنوات العراقية المباشرة", "url": "http://example.com/iraq.m3u8"},
                {"name": "القنوات الخليجية", "url": "http://example.com/gulf.m3u8"},
                {"name": "قنوات مصرية ومنوعة", "url": "http://example.com/egypt.m3u8"}
            ]
        }
        
        for package_name, channels in packages.items():
            pkg_label = Label(text=package_name, font_size='18sp', bold=True, size_hint_y=None, height=40, color=get_color_from_hex("#ff7b72"))
            grid_layout.add_widget(pkg_label)
            channel_grid = GridLayout(cols=2, spacing=10, size_hint_y=None, height=len(channels)*60)
            
            for chan in channels:
                btn = Button(text=chan["name"], font_size='16sp', background_normal='', background_color=get_color_from_hex("#161b22"), size_hint_y=None, height=50)
                btn.bind(on_press=partial(self.play_channel, chan))
                channel_grid.add_widget(btn)
                
            grid_layout.add_widget(channel_grid)

        scroll_view.add_widget(grid_layout)
        main_layout.add_widget(scroll_view)
        return main_layout

    def play_channel(self, channel_info, instance):
        channel_name = channel_info["name"]
        self.status_label.text = f"⏳ جاري الاتصال بالسيرفر وتشغيل: {channel_name}..."

if __name__ == '__main__':
    ThamerTVApp().run()