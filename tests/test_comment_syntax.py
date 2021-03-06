import sys
if sys.version_info < (3, 0):
    import testcase
    from tableofcomments import TableOfComments
else:
    from . import testcase
    from ..tableofcomments import TableOfComments


#
# Tests getting titles within a variety of comment syntaxes
#
class TestCommentSyntax(testcase.TestCase):

    title = "Test Comment Syntax"

    # Using find() to check if result is correct
    def test_javascript_syntax(self):
        # Setup
        self.set_syntax('javascript')
        self.set_settings({'level_char': '>'})
        self.set_text(self.text_javascript())
        # Test
        toc = TableOfComments(self.view, self.edit)
        titles = toc.get_comment_titles('string')
        self.check_titles_match(titles)

    def test_css_syntax(self):
        # Setup
        self.view.set_syntax_file('Packages/CSS/CSS.tmLanguage')
        self.set_syntax('css')
        self.set_settings({'level_char': '#'})
        self.set_text(self.text_css())
        # Test
        toc = TableOfComments(self.view, self.edit)
        titles = toc.get_comment_titles('string', 'test')
        self.check_titles_match(titles)

    def test_python_syntax(self):
        # Setup
        self.set_syntax('python')
        self.set_settings({'level_char': '>'})
        self.set_text(self.text_python())
        # Test
        toc = TableOfComments(self.view, self.edit)
        titles = toc.get_comment_titles('string')
        self.check_titles_match(titles)

    def check_titles_match(self, titles):
        for title in ['Heading 1', '- Heading 2', '-- Heading 3']:
            if title in titles:
                self.ok()
            else:
                self.error('Missing title ' + title)

    def text_javascript(self):
        return """
/*
* > Heading 1
*/
var func = function(x){
    return x > 3;
}
/* >> Heading 2 */

// >>> Heading 3

"""

    def text_css(self):
        return """
/*
* # Heading 1
*/
#id { display:none } /* Should not show */

/* ## Heading 2 */

/* ### Heading 3 */

"""

    def text_python(self):
        return """
# > Heading 1
def function(x):
    return x > 3

    # >> Heading 2

# >>> Heading 3

"""
