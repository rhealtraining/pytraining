from page_objects import PageObject, PageElement

class MainPage (PageObject):
    def check_page(self):
        return "Welcome" in self.w.title