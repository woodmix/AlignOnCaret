import sublime
import sublime_plugin

from Default.indentation import line_and_normed_pt as normed_rowcol

class AlignOnCaretCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        view = self.view
        sel = view.sel()

        # キャレットが一つしかない場合はステータスバーにメッセージを残して終了
        if len(sel) == 1:
            view.window().status_message("Multi-select, please.")

        else:

            # 最も後ろにあるキャレットのカラム位置を取得。
            max_col = max([normed_rowcol(view, region.b)[1] for region in sel])

            # 処理後、キャレットを動かすための Region を格納する配列を初期化。
            afters = []

            # キャレットを一つずつ走査して、一揃えと新しいキャレット位置を表す Region を作成する。
            for region in sel:
                length = max_col - normed_rowcol(view, region.b)[1]
                view.insert(edit, region.b, ' ' * length)
                afters.append( sublime.Region(region.b + length, region.b + length) )

            # すべてのキャレットを移動。
            sel.clear()
            sel.add_all(afters)
