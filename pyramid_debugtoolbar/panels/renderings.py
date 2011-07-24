from pyramid_debugtoolbar.panels import DebugPanel

_ = lambda x: x

class RenderingsDebugPanel(DebugPanel):
    """
    Panel that displays the renderers used during the request.
    """
    name = 'Template'
    has_content = True
    renderings = ()

    def process_beforerender(self, event):
        if not self.renderings:
            self.renderings = []
        name = event['renderer_info'].name
        if name and name.startswith('pyramid_debugtoolbar'):
            return
        system = getattr(event, '_system', 'unknown')
        val = getattr(event, 'rendering_val', 'unknown')
        self.renderings.append(dict(name=name, system=system, val=val))

    def nav_title(self):
        return _('Renderings')

    def nav_subtitle(self):
        num = len(self.renderings)
        return '%d %s' % (num, self.pluralize("rendering", "renderings", num))

    def title(self):
        return _('Renderings')

    def url(self):
        return ''

    def content(self):
        return self.render(
            'pyramid_debugtoolbar.panels:templates/renderings.jinja2', {
            'renderings': self.renderings
        }, request=self.request)

