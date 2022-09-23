


class Elements:

    def getCheckbox(add, names):
        print("checkbox...")
        with add.div(klass="form-check"):
            add.input(klass="form-check-input", type="checkbox", id="sample_check1", name="sample_check1")
            string = ['<label class="form-check-label" for="sample_check1">', names, '</label>']
            # add._doc_elements.append(i)
            for i in string:
                add._doc_elements.append(i)


    def getButton(add, name):
        print("button...")
        add.button(type="button", klass="btn btn-primary px-3", _t=name)


    def getCarousel(add):
        string = ['<div class="container">',
                  '<div id="carousel" class="carousel slide" data-ride="carousel" style="height:150px; width:200px">',
                  '<a class="left carousel-control" href="#carousel" data-slide="prev">',
                  '<span class="glyphicon glyphicon-chevron-left"></span>',
                  '<span class="sr-only">Previous</span>', '</a>',
                  '<a class="right carousel-control" href="#carousel" data-slide="next">',
                  '<span class="glyphicon glyphicon-chevron-right"></span>', '<span class="sr-only">Next</span>', '</a>',
                  '<ol class="carousel-indicators">', '<li data-target="#carousel" data-slide-to="0" class="active"></li>',
                  '<li data-target="#carousel" data-slide-to="1"></li>',
                  '<li data-target="#carousel" data-slide-to="2"></li>', '</ol>',
                  '<div class="carousel-inner" >', '<div class="item active">',
                  '<img src="image.jpg" class="d-block w-100" alt="Any alternative" >',
                  '</div>', '<div class="item">', '<img src="image.jpg" class="d-block w-100" alt="Any alternative" >',
                  '</div>',
                  '<div class="item">', '<img src="image.jpg" class="d-block w-100" alt="Any alternative" >', '</div>',
                  '<a class="left carousel-control" href="#myCarousel" data-slide="prev">',
                  '<span class="glyphicon glyphicon-chevron-left"></span>',
                  '<span class="sr-only">Previous</span>', '</a>',
                  '<a class="right carousel-control" href="#myCarousel" data-slide="next">',
                  '<span class="glyphicon glyphicon-chevron-right"></span>', '<span class="sr-only">Next</span>', '</a>',
                  '</div>', '</div>', '</div>']
        return string


    def getHeading(add, name):
        print("heading...")
        with add.p(klass="h3"):
            add(name)


    def getImage(add):
        print("image...")
        add.img(src="image.png", klass="img-fluid mt-4", alt="Any alternative")


    def getLabel(add, name):
        print("label...")
        with add.label():
            add(name)


    def getLink(add, name):
        print("link...")
        with add.a(href="#", klass="stretched-link"):
            add(name)


    def getPagination(add):
        print("pagination...")
        with add.ul(klass="pagination"):
            with add.li(klass="page-item"):
                add.a(klass="page-item", href="#", _t="Previous")
            with add.li(klass="page-item"):
                add.a(klass="page-item", href="#", _t="1")
            with add.li(klass="page-item"):
                add.a(klass="page-item", href="#", _t="2")
            with add.li(klass="page-item"):
                add.a(klass="page-item", href="#", _t="3")
            with add.li(klass="page-item"):
                add.a(klass="page-item", href="#", _t="Next")


    def getParagraph(add):
        print("paragraph...")
        with add.p(klass="text-black-50"):
            add("Lorem ipsum dolor sit amet, consectetur adipiscing elit \
            <br /> \
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
            <br /> \
            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris")


    def getRadioButton(add, names):
        print("radio_button...")
        with add.div(klass="form-check"):
            add.input(type="radio", klass="form-check-input", name="radio_button1", id="radio_button1")
            string = ['<label class="form-check-label" for="sample_check1">', names, '</label>']
            # add._doc_elements.append(i)
            for i in string:
                add._doc_elements.append(i)


    def getSelect(add):
        print("select...")
        with add.select(klass="form-select"):
            add.option(value="0", _t="Select your choice")
            add.option(value="1", _t="OptionOne")
            add.option(value="2", _t="OptionTwo")
            add.option(value="3", _t="OptionThree")


    def getTable(add):
        print("table...")
        with add.table():
            with add.thead().tr():
                add.th(scope="col", _t="#")
                add.th(scope="col")
                add.th(scope="col")
                add.th(scope="col")
            with add.tbody():
                with add.tr():
                    add.th(scope="row", _t="1")
                    add.td()
                    add.td()
                    add.td()
                    add.th(scope="row", _t="1")
                    add.td()
                    add.td()
                    add.td()
                with add.tr():
                    add.th(scope="row", _t="3")
                    add.td(colspan="2")
                    add.td()


    def getTextarea(add):
        print("textarea...")
        add.textarea(rows="9", cols="40")


    def getTextBox(add):
        print("textbox...")
        add.input(type='text', name="sample_textbox")


def getElements(add, label, name="No value"):

    el = Elements()

    if (label == 1):
        el.getButton(add, name)
    elif (label == 2):
        string = el.getCarousel(add)
        for i in string:
            add._doc_elements.append(i)
    elif (label == 3):
        el.getCheckbox(add, name)
    elif (label == 4):
        el.getHeading(add, name)
    elif (label == 5):
        el.getImage(add)
    elif (label == 6):
        el.getLabel(add, name)
    elif (label == 7):
        el.getLink(add, name)
    elif (label == 8):
        el.getPagination(add)
    elif (label == 9):
        el.getParagraph(add)
    elif (label == 10):
        el.getRadioButton(add, name)
    elif (label == 11):
        el.getSelect(add)
    elif (label == 12):
        el.getTable(add)
    elif (label == 13):
        el.getTextarea(add)
    elif (label == 14):
        el.getTextBox(add)
    else:
        print("Invalid or Null Label occurred", label)
