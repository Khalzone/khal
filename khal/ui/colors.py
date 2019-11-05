# Copyright (c) 2013-2017 Christian Geier et al.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# ikhal screen
# +header-----------------------------------------
# |    dayname
# |mon
# |
# |      td           date header focused/selected
# |th
# |
# |
# |name
# |
# |
# |
# +footer------------------------------------------

# new event screen
# +header--------------------
# |
# |Title:  edit
# |< calendars >
# |
# |Location:  edit/edit focused
# |Categories:  edit/edit focused
# |Description:  edit/edit focused
# |[ ] Alldays
# |From: edit/edit focused/edition validated
# |To: edit/edit focused/edition validated
# |[ ] Repeat: < weekly > every:1
# |             <list>
# |
# ---------------------------
# line header = text to edit

dark = [
    ('header', 'white', 'black'),
    ('footer', 'white', 'black'),
    ('line header', 'black', 'white', 'bold'),
    ('bright', 'dark blue', 'white', ('bold', 'standout')),
    ('list', 'black', 'white'),
    ('list focused', 'white', 'light blue', 'bold'),
    ('edit', 'black', 'white'),
    ('edit focused', 'white', 'light blue', 'bold'),
    ('button', 'black', 'dark cyan'),
    ('button focused', 'white', 'light blue', 'bold'),

    ('reveal focus', 'black', 'light gray'),
    ('today focus', 'white', 'dark magenta'),
    ('today', 'dark gray', 'dark green',),

    ('date header', 'light gray', 'black'),
    ('date header focused', 'black', 'white'),
    ('date header selected', 'dark gray', 'light gray'),

    ('dayname', 'light gray', ''),
    ('monthname', 'light gray', ''),
    ('weeknumber_right', 'light gray', ''),
    ('edit', 'white', 'dark blue'),
    ('alert', 'white', 'dark red'),
    ('mark', 'white', 'dark green'),
    ('frame', 'white', 'black'),
    ('frame focus', 'light red', 'black'),
    ('frame focus color', 'dark blue', 'black'),
    ('frame focus top', 'dark magenta', 'black'),

    ('editfc', 'white', 'dark blue', 'bold'),
    ('editbx', 'light gray', 'dark blue'),
    ('editcp', 'black', 'light gray', 'standout'),
    ('popupbg', 'white', 'black', 'bold'),
]
light = [
    ('header', 'black', 'white'),
    ('footer', 'black', 'white'),
    ('line header', 'black', 'white', 'bold'),
    ('bright', 'dark blue', 'white', ('bold', 'standout')),
    ('list', 'black', 'white'),
    ('list focused', 'white', 'light blue', 'bold'),
    ('edit', 'black', 'white'),
    ('edit focused', 'white', 'light blue', 'bold'),
    ('button', 'black', 'dark cyan'),
    ('button focused', 'white', 'light blue', 'bold'),

    ('reveal focus', 'black', 'dark cyan', 'standout'),
    ('today focus', 'white', 'dark cyan', 'standout'),
    ('today', 'black', 'light gray', 'dark cyan'),

    ('date header', '', 'white'),
    ('date header focused', 'white', 'dark gray', ('bold', 'standout')),
    ('date header selected', 'dark gray', 'light cyan'),

    ('dayname', 'dark gray', 'white'),
    ('monthname', 'dark gray', 'white'),
    ('weeknumber_right', 'dark gray', 'white'),
    ('edit', 'white', 'dark blue'),
    ('alert', 'white', 'dark red'),
    ('mark', 'white', 'dark green'),
    ('frame', 'dark gray', 'white'),
    ('frame focus', 'light red', 'white'),
    ('frame focus color', 'dark blue', 'white'),
    ('frame focus top', 'dark magenta', 'white'),

    ('editfc', 'white', 'dark blue', 'bold'),
    ('editbx', 'light gray', 'dark blue'),
    ('editcp', 'black', 'light gray', 'standout'),
    ('popupbg', 'white', 'black', 'bold'),
]
"""256 colors theme"""
backgcolor = 'h0'
themecolor = 'h2'
activecolor = 'h11'
visiblecolor = 'h9'
colors256 = [
    #fixed elements
    ('header', '', '', '', themecolor, backgcolor, ),
    ('footer', '', '','', themecolor, backgcolor, ),
    ('dayname', '', '','', themecolor, backgcolor, ),
    ('monthname', '', '','', themecolor, backgcolor, ),
    ('today', '', '', '', activecolor, backgcolor, ),
    ('date header', '', '', '', themecolor, backgcolor, ),

    #selected elements
    ('date header focused', '', '', '', backgcolor, activecolor, ),
    ('date header selected', '', '','', activecolor, backgcolor, ),
    ('reveal focus', '', '', '', backgcolor, activecolor, ),
    ('today focus', '', '', '', backgcolor, activecolor, ),

    # ikhal editor panel
    ('edit', '', '', '', activecolor, backgcolor, ),
    ('edit focused', '', '', '', backgcolor, activecolor, ),
    ('popupbg', '', '', '', themecolor, backgcolor ),
    ('list', '', '', '', activecolor, backgcolor, ),
    ('edition validated', '', '', '', themecolor, backgcolor, ),


    ('list focused', '', '', '', visiblecolor, backgcolor, ),
    ('frame', '', '', '', visiblecolor, visiblecolor, ),
    ('frame focus color', '', '', '', visiblecolor, visiblecolor, ),
    ('frame focus top', 'dark magenta', 'black'),

    # Unknown impact
    ('alert', 'light red', 'light red', 'light red', visiblecolor, backgcolor, ),
    ('line header', '', '', '', visiblecolor, visiblecolor, ),
    ('weeknumber_right', 'light red', '', ),
    ('weeknumber_left', 'yellow', '', ),
    ('mark', 'light green', 'light green', ),
    ('bright', 'light green', 'light red', ('bold', 'standout', )),

    # Never called elements
    ('frame focus', 'light red', 'black', ),
    ('editfc', 'white', 'light red', 'bold'),
    ('editbx', '', '', '', visiblecolor, visiblecolor, ),
    ('editcp', 'black', 'light red', 'standout'),
    ('button', 'black', 'light blue', ),
    ('button focused', 'yellow', 'dark green', 'bold', ),
]
