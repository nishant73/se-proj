DT = """QToolTip
{
     border: 1px solid black;
     background-color: #D1DBCB;
     padding: 1px;
     border-radius: 3px;
     opacity: 100;
}

QWidget
{
    color: #b1b1b1;
    background-color: #323232;
    selection-background-color:#323232;
    selection-color: black;
    background-clip: border;
    border-image: none;
    border: 0px transparent black;
    outline: 0;
}

QWidget:item:hover
{
    background-color: #D1DBCB;
    color: black;
}

QWidget:item:selected
{
    background-color: #D1DBCB;
    border: 0px
}

QRadioButton
{
    spacing: 5px;
    outline: none;
    color: #eff0f1;
    margin-bottom: 2px;
}

QRadioButton:disabled
{
    color: #76797C;
}
QRadioButton::indicator
{
    width: 21px;
    height: 21px;
}

QRadioButton::indicator:unchecked
{
    image: url(:/qss_icons/rc/radio_unchecked.png);
}


QRadioButton::indicator:unchecked:hover,
QRadioButton::indicator:unchecked:focus,
QRadioButton::indicator:unchecked:pressed
{
    border: none;
    outline: none;
    image: url(:/qss_icons/rc/radio_unchecked_focus.png);
}

QRadioButton::indicator:checked
{
    border: none;
    outline: none;
    image: url(:/qss_icons/rc/radio_checked.png);
}

QRadioButton::indicator:checked:hover,
QRadioButton::indicator:checked:focus,
QRadioButton::indicator:checked:pressed
{
    border: none;
    outline: none;
    image: url(:/qss_icons/rc/radio_checked_focus.png);
}

QRadioButton::indicator:checked:disabled
{
    outline: none;
    image: url(:/qss_icons/rc/radio_checked_disabled.png);
}

QRadioButton::indicator:unchecked:disabled
{
    image: url(:/qss_icons/rc/radio_unchecked_disabled.png);
}


QMenuBar
{
    background-color: #323232;
    color: #D1DBCB;
}

QMenuBar::item
{
    background-color: #323232;
    background: transparent;
    /* padding: 2px 20px 2px 20px; */
}

QMenuBar::item:selected
{
    background: transparent;
    /* border: 1px solid #76797C; */
}

QMenuBar::item:pressed
{
    border: 0px solid #76797C;
    background-color: #D1DBCB;
    color: #000;
    margin-bottom:-1px;
    padding-bottom:1px;
}

QMenu
{
    background-color: #323232;
    /* border: 1px solid #76797C; */
    color: #eff0f1;
    /*margin: 2px; */
}

QMenu::icon
{
    /*margin: 5px;*/
}

QMenu::item
{
    padding: 2px 30px 2px 30px;
    /*margin-left: 5px;*/
    border: 1px solid transparent; /* reserve space for selection border */
}

QMenu::item:selected
{
    color: #000000;
}

QMenu::separator {
    height: 2px;
    background: #D1DBCB;
    margin-left: 10px;
    margin-right: 5px;
}

QMenu::indicator {
    width: 18px;
    height: 18px;
}

/* non-exclusive indicator = check box style indicator
   (see QActionGroup::setExclusive) */
QMenu::indicator:non-exclusive:unchecked {
    image: url(:/qss_icons/rc/checkbox_unchecked.png);
}

QMenu::indicator:non-exclusive:unchecked:selected {
    image: url(:/qss_icons/rc/checkbox_unchecked_disabled.png);
}

QMenu::indicator:non-exclusive:checked {
    image: url(:/qss_icons/rc/checkbox_checked.png);
}

QMenu::indicator:non-exclusive:checked:selected {
    image: url(:/qss_icons/rc/checkbox_checked_disabled.png);
}

/* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */
QMenu::indicator:exclusive:unchecked {
    image: url(:/qss_icons/rc/radio_unchecked.png);
}

QMenu::indicator:exclusive:unchecked:selected {
    image: url(:/qss_icons/rc/radio_unchecked_disabled.png);
}

QMenu::indicator:exclusive:checked {
    image: url(:/qss_icons/rc/radio_checked.png);
}

QMenu::indicator:exclusive:checked:selected {
    image: url(:/qss_icons/rc/radio_checked_disabled.png);
}

QMenu::right-arrow {
    margin: 5px;
    image: url(:/qss_icons/rc/right_arrow.png)
}


QWidget:disabled
{
    color: #454545;
    background-color: #323232;
}

QAbstractItemView
{
    alternate-background-color: #323232;
    color: #eff0f1;
    border: 1px solid 3A3939;
    border-radius: 2px;
}

QWidget:focus, QMenuBar:focus,QToolBar:focus,QScrollAreaViewer:focus
{
    /* border: 2px solid #D1DBCB; */
}

QTabWidget:focus, QCheckBox:focus, QRadioButton:focus, QSlider:focus
{
    border: none;
}

QLineEdit
{
    background-color: #1e1e1e;
    selection-background-color: #D1DBCB;
    selection-color: black;
    padding: 5px;
    border-style: solid;
    border: 1px solid #76797C;
    border-radius: 2px;
    color: #eff0f1;
}

QGroupBox {
    border:1px solid #76797C;
    border-radius: 2px;
    margin-top: 20px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 10px;
}

QAbstractScrollArea
{
    border-radius: 0px;
    border: 0px solid #76797C;
    background-color: transparent;
}

QTextEdit
{
    background-color: #1e1e1e;
    color: #eff0f1;
    border: 1px solid #76797C;
}

QPlainTextEdit
{
    background-color: #1e1e1e;;
    color: #eff0f1;
    border-radius: 2px;
    border: 1px solid #76797C;
}

QHeaderView::section
{
    background-color: #76797C;
    color: #eff0f1;
    padding: 5px;
    border: 1px solid #76797C;
}

QSizeGrip {
    image: url(:/qss_icons/rc/sizegrip.png);
    width: 12px;
    height: 12px;
}


QMainWindow::separator
{
    background-color: #323232;
    color: white;
    padding-left: 4px;
    spacing: 2px;
    border: 1px dashed #76797C;
}

QMainWindow::separator:hover
{

    background-color: #787876;
    color: white;
    padding-left: 4px;
    border: 1px solid #76797C;
    spacing: 2px;
}


QMenu::separator
{
    height: 1px;
    background-color: #76797C;
    color: white;
    padding-left: 4px;
    margin-left: 10px;
    margin-right: 5px;
}

QFrame
{
    border-radius: 0px;
    /*border: 1px solid #76797C;*/
}


QFrame[frameShape="0"]
{
    border-radius: 0px;
    border: 0px transparent #76797C;
}

QStackedWidget
{
    border: 1px transparent black;
}

QToolBar {
    border: 0px transparent #393838;
    background: 0px solid #323232;
    font-weight: bold;
}

QToolBar::handle:horizontal {
    image: url(:/qss_icons/rc/Hmovetoolbar.png);
}
QToolBar::handle:vertical {
    image: url(:/qss_icons/rc/Vmovetoolbar.png);
}
QToolBar::separator:horizontal {
    image: url(:/qss_icons/rc/Hsepartoolbar.png);
}
QToolBar::separator:vertical {
    image: url(:/qss_icons/rc/Vsepartoolbar.png);
}
QToolButton#qt_toolbar_ext_button {
    background: #58595a
}

QPushButton
{
    color: #eff0f1;
    background-color: #323232;
    border-width: 1px;
    border-color: #76797C;
    border-style: solid;
    padding: 5px;
    border-radius: 0px;
    outline: none;
}

QPushButton:disabled
{
    background-color: #323232;
    border-width: 1px;
    border-color: #454545;
    border-style: solid;
    padding-top: 5px;
    padding-bottom: 5px;
    padding-left: 10px;
    padding-right: 10px;
    border-radius: 2px;
    color: #454545;
}

QPushButton:focus {
    background-color: #D1DBCB;
    color: black;
}

QPushButton:pressed
{
    color: black;
    background-color: #D1DBCB;
    padding-top: -15px;
    padding-bottom: -17px;
}

QComboBox
{
    selection-background-color: #D1DBCB;
    background-color: #31363B;
    border-style: solid;
    border: 1px solid #76797C;
    border-radius: 2px;
    padding: 5px;
    min-width: 75px;
}

QPushButton:checked{
    background-color: #76797C;
    border-color: #6A6969;
}

QComboBox:hover,QPushButton:hover,QAbstractSpinBox:hover,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QAbstractView:hover,QTreeView:hover
{
    border: 1px solid #D1DBCB;
}

QComboBox:on
{
    padding-top: 0px;
    padding-left: 4px;
    selection-background-color: #4a4a4a;
}

QComboBox QAbstractItemView
{
    background-color: #1e1e1e;
    border-radius: 2px;
    border: 1px solid #76797C;
    selection-background-color: #D1DBCB;
}

QComboBox::drop-down
{
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;

    border-left-width: 0px;
    border-left-color: darkgray;
    border-left-style: solid;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
}

QComboBox::down-arrow
{
    image: url(:/qss_icons/rc/down_arrow_disabled.png);
}

QComboBox::down-arrow:on, QComboBox::down-arrow:hover,
QComboBox::down-arrow:focus
{
    image: url(:/qss_icons/rc/down_arrow.png);
}

QAbstractSpinBox {
    padding: 2px;
    margin: 2px;
    background-color: #1e1e1e;
    color: #eff0f1;
    border-radius: 0px;
    min-width: 75px;
    selection-background-color: #D1DBCB;
    selection-color: black;
}

QAbstractSpinBox:up-button
{
    background-color: transparent;
    subcontrol-origin: border;
    subcontrol-position: center right;
}

QAbstractSpinBox:down-button
{
    background-color: transparent;
    subcontrol-origin: border;
    subcontrol-position: center left;
}

QAbstractSpinBox::up-arrow,QAbstractSpinBox::up-arrow:disabled,QAbstractSpinBox::up-arrow:off {
    image: url(:/qss_icons/rc/up_arrow_disabled.png);
    width: 10px;
    height: 10px;
}
QAbstractSpinBox::up-arrow:hover
{
    image: url(:/qss_icons/rc/up_arrow.png);
}


QAbstractSpinBox::down-arrow,QAbstractSpinBox::down-arrow:disabled,QAbstractSpinBox::down-arrow:off
{
    image: url(:/qss_icons/rc/down_arrow_disabled.png);
    width: 10px;
    height: 10px;
}
QAbstractSpinBox::down-arrow:hover
{
    image: url(:/qss_icons/rc/down_arrow.png);
}


QLabel
{
    border: 0px solid black;
    margin-left: 2px;
    margin-right: 2px;
    color: #D1DBCB;
}

QTabWidget{
    border: 0px transparent black;
}

QTabWidget::pane {
    border: 1px solid #76797C;
    padding: 5px;
    margin: 0px;
}

QTabWidget::tab-bar {
    left: 5px; /* move to the right by 5px */
}

QTabBar
{
    qproperty-drawBase: 0;
    border-radius: 3px;
}

QTabBar::focus
{
    border: 0px transparent black;
    color: black;
}

QTabBar::hover
{
    border: 0px transparent black;
    color: black;
}

QTabBar::close-button  {
    image: url(:/qss_icons/rc/close.png);
    background: transparent;
}

QTabBar::close-button:hover
{
    image: url(:/qss_icons/rc/close-hover.png);
    background: transparent;
}

QTabBar::close-button:pressed {
    image: url(:/qss_icons/rc/close-pressed.png);
    background: transparent;
}

/* TOP TABS */
QTabBar::tab:top {
    color: #eff0f1;
    border: 1px solid #76797C;
    border-bottom: 1px transparent black;
    background-color: #323232;
    padding: 5px;
    min-width: 50px;
    border-top-left-radius: 2px;
    border-top-right-radius: 2px;
}

QTabBar::tab:top:!selected
{
    color: #eff0f1;
    background-color: #54575B;
    border: 1px solid #76797C;
    border-bottom: 1px transparent black;
    border-top-left-radius: 2px;
    border-top-right-radius: 2px;
}

QTabBar::tab:top:!selected:hover {
    background-color: #D1DBCB;
    color: black;
}

/* BOTTOM TABS */
QTabBar::tab:bottom {
    color: #eff0f1;
    border: 1px solid #76797C;
    border-top: 1px transparent black;
    background-color: #323232;
    padding: 5px;
    border-bottom-left-radius: 2px;
    border-bottom-right-radius: 2px;
    min-width: 50px;
}

QTabBar::tab:bottom:!selected
{
    color: #eff0f1;
    background-color: #54575B;
    border: 1px solid #76797C;
    border-top: 1px transparent black;
    border-bottom-left-radius: 2px;
    border-bottom-right-radius: 2px;
}

QTabBar::tab:bottom:!selected:hover {
    background-color: #D1DBCB;
    color: black;
}

/* LEFT TABS */
QTabBar::tab:left {
    color: #eff0f1;
    border: 1px solid #76797C;
    border-left: 1px transparent black;
    background-color: #323232;
    padding: 5px;
    border-top-right-radius: 2px;
    border-bottom-right-radius: 2px;
    min-height: 50px;
}

QTabBar::tab:left:!selected
{
    color: #eff0f1;
    background-color: #54575B;
    border: 1px solid #76797C;
    border-left: 1px transparent black;
    border-top-right-radius: 2px;
    border-bottom-right-radius: 2px;
}

QTabBar::tab:left:!selected:hover {
    background-color: #D1DBCB;
    color: black;
}


/* RIGHT TABS */
QTabBar::tab:right {
    color: #eff0f1;
    border: 1px solid #76797C;
    border-right: 1px transparent black;
    background-color: #323232;
    padding: 5px;
    border-top-left-radius: 2px;
    border-bottom-left-radius: 2px;
    min-height: 50px;
}

QTabBar::tab:right:!selected
{
    color: #eff0f1;
    background-color: #54575B;
    border: 1px solid #76797C;
    border-right: 1px transparent black;
    border-top-left-radius: 2px;
    border-bottom-left-radius: 2px;
}

QTabBar::tab:right:!selected:hover {
    background-color: #D1DBCB;
    color: black;
}

QTabBar QToolButton::right-arrow:enabled {
     image: url(:/qss_icons/rc/right_arrow.png);
 }

 QTabBar QToolButton::left-arrow:enabled {
     image: url(:/qss_icons/rc/left_arrow.png);
 }

QTabBar QToolButton::right-arrow:disabled {
     image: url(:/qss_icons/rc/right_arrow_disabled.png);
 }

 QTabBar QToolButton::left-arrow:disabled {
     image: url(:/qss_icons/rc/left_arrow_disabled.png);
 }

QTableCornerButton::section {
    background-color: #323232;
    border: 1px transparent #76797C;
    border-radius: 0px;
}

QToolBox  {
    padding: 5px;
    border: 1px transparent black;
}

QToolBox::tab {
    color: #eff0f1;
    background-color: #323232;
    border: 1px solid #76797C;
    border-bottom: 1px transparent #323232;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
}

QToolBox::tab:selected { /* italicize selected tabs */
    font: italic;
    background-color: #323232;
    border-color: #D1DBCB;
 }

QStatusBar::item {
    border: 0px transparent dark;
    margin: 0px;
    border: 0px;
 }


QFrame[height="3"], QFrame[width="3"] {
    background-color: #76797C;
}


QSplitter::handle {
    border: 1px dashed #76797C;
}

QSplitter::handle:hover {
    background-color: #787876;
    border: 1px solid #76797C;
}

QSplitter::handle:horizontal {
    width: 1px;
}

QSplitter::handle:vertical {
    height: 1px;
}

 """
def styling():
    return DTuuu