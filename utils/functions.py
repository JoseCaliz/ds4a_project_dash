def highlight_current_page(lev_nav, current_page):
    for key in lev_nav.keys():
        if key == current_page:
            lev_nav[key] = True
        else:
            left_nav[key] = False

    return lev_nav
