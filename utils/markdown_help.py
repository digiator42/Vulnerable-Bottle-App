from markdown_it import MarkdownIt
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from mdit_py_plugins.front_matter import front_matter_plugin
from mdit_py_plugins.footnote import footnote_plugin

def highlight_code(code, lang):
    try:
        lexer = get_lexer_by_name(lang, stripall=True)
    except:
        lexer = get_lexer_by_name("text", stripall=True)

    formatter = HtmlFormatter()
    return highlight(code, lexer, formatter)

def plugin(md):
    def render_fence(tokens, idx, options, env):
        token = tokens[idx]
        code = token.content
        lang = token.info.strip() if token.info else None
        return highlight_code(code, lang)
    
    md.renderer.rules["fence"] = render_fence

md = (MarkdownIt().use(plugin=plugin)
.use(front_matter_plugin)
.use(footnote_plugin)
.enable('table')
)